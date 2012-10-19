# -*- coding: utf-8 -*-

from radish.Config import Config
from radish.Step import Step


class Scenario(object):
    def __init__(self, id, sentence, filename, line_no):
        self.id = id
        self.sentence = sentence
        self.filename = filename
        self.line_no = line_no
        self.steps = []

    @property
    def Id(self):
        return self.id

    @property
    def LineNo(self):
        return self.line_no

    @property
    def Sentence(self):
        return self.sentence

    @property
    def Indentation(self):
        return "  " + " " * len(str(Config().highest_feature_id)) + "  "

    @property
    def DryRun(self):
        return Config().dry_run

    @property
    def Steps(self):
        return self.steps

    @property
    def Passed(self):
        for s in self.steps:
            if not s.Passed:
                return False
        return True

    def AppendStep(self, step):
        if isinstance(step, Step):
            self.steps.append(step)
