# -*- coding: utf-8 -*-

import traceback
import inspect
import sys
import datetime

from radish.Config import Config
from radish.UtilRegistry import UtilRegistry
from radish.Exceptions import ValidationError


class Step(object):
    CHARS_PER_LINE = 100

    def __init__(self, id, scenario_id, feature_id, sentence, filename, line_no):
        self.id = id
        self.scenario_id = scenario_id
        self.feature_id = feature_id
        self.sentence = sentence
        self.filename = filename
        self.line_no = line_no
        self.func = None
        self.match = None
        self.passed = None
        self.fail_reason = None
        self.starttime = None
        self.endtime = None
        self.validation_error = False

    @property
    def Id(self):
        return self.id

    @property
    def ScenarioId(self):
        return self.scenario_id

    @property
    def FeatureId(self):
        return self.feature_id

    @property
    def LineNo(self):
        return self.line_no

    @property
    def Sentence(self):
        return self.sentence

    @property
    def SplittedSentence(self):
        ur = UtilRegistry()
        if ur.has_util("split_sentence"):
            try:
                return ur.call_util("split_sentence", self)
            except KeyboardInterrupt:
                pass
        splitted = [self.sentence[i:i + Step.CHARS_PER_LINE] for i in range(0, len(self.sentence), Step.CHARS_PER_LINE)]
        return len(splitted), ("\n" + self.SentenceIndentation).join(splitted)

    @property
    def Indentation(self):
        return "  " + " " * (len(str(Config().highest_feature_id)) + len(str(Config().highest_scenario_id))) + "    "

    @property
    def SentenceIndentation(self):
        return self.Indentation + " " * len(str(Config().highest_step_id)) + "  "

    @property
    def DryRun(self):
        return Config().dry_run

    @property
    def Func(self):
        return self.func

    @property
    def Match(self):
        return self.match

    @property
    def Passed(self):
        return self.passed

    @property
    def Duration(self):
        if self.Passed is True or self.Passed is False:
            td = self.endtime - self.starttime
            return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 1e6) / 1e6
        return -1

    class FailReason(object):
        def __init__(self, e):
            self.exception = e
            self.reason = unicode(e)
            self.traceback = traceback.format_exc(e)
            self.name = e.__class__.__name__

        @property
        def Reason(self):
            return self.reason

        @property
        def Traceback(self):
            return self.traceback

        @property
        def Name(self):
            return self.name

    def run(self):
        kw = self.match.groupdict()
        try:
            self.starttime = datetime.datetime.now()
            if kw:
                self.func(self, **kw)
            else:
                self.func(self, *self.match.groups())
            self.passed = not self.validation_error
        except KeyboardInterrupt:
            raise
        except Exception, e:
            self.passed = False
            self.fail_reason = Step.FailReason(e)
            if self.DryRun:
                caller = inspect.trace()[-1]
                sys.stderr.write("%s:%d: error: %s\n" % (caller[1], caller[2], unicode(e)))
        self.endtime = datetime.datetime.now()
        return self.passed

    def ValidationError(self, msg):
        self.validation_error = True
        if self.DryRun:
            sys.stderr.write("%s:%d: error: %s\n" % (self.filename, self.line_no, msg))
        else:
            raise ValidationError(msg)
