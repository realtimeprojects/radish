# -*- coding: utf-8 -*-

import sys

from radish.Config import Config
from radish.HookRegistry import after, before
from radish.FileSystemHelper import FileSystemHelper as fsh


@before.each_feature
def print_before_feature(feature):
    if not feature.DryRun:
        print(feature.Indentation + "%*d. " % (len(str(Config().highest_feature_id)), feature.Id) + feature.Sentence + " " * (Config().longest_feature_text - len(feature.Sentence)) + " " * 10 + "# " + fsh.filename(feature.filename))
        for l in feature.description.splitlines():
            print(feature.Indentation + " " * len(str(Config().highest_feature_id)) + "  " + l)
        print("")


@before.each_scenario
def print_before_scenario(scenario):
    if not scenario.DryRun:
        print(scenario.Indentation + "%*d. %s" % (len(str(Config().highest_scenario_id)), scenario.Id, scenario.Sentence))


@after.each_scenario
def print_after_scenario(scenario):
    if not scenario.DryRun:
        print("")


@before.each_step
def print_before_step(step):
    if not step.DryRun:
        print(step.Indentation + "%*d. %s" % (len(str(Config().highest_step_id)), step.Id, step.SplittedSentence[1]))


@after.each_step
def print_after_step(step):
    if not step.DryRun:
        splitted = step.SplittedSentence
        sys.stdout.write("\033[A" * splitted[0])
        print(step.Indentation + "%*d. %s" % (len(str(Config().highest_step_id)), step.Id, splitted[1]))

        if step.passed is False:
            for l in step.fail_reason.traceback.splitlines():
                print(step.SentenceIndentation + l)


@after.all
def print_after_all(endResult):
    if not Config().dry_run:
        feature_text = str(endResult.passed_features) + " passed"
        if endResult.failed_features > 0:
            feature_text += ", " + str(endResult.failed_features) + " failed"

        scenario_text = str(endResult.passed_scenarios) + " passed"
        if endResult.failed_scenarios > 0:
            scenario_text += ", " + str(endResult.failed_scenarios) + " failed"

        step_text = str(endResult.passed_steps) + " passed"
        if endResult.failed_steps > 0:
            step_text += ", " + str(endResult.failed_steps) + " failed"
        if endResult.skipped_steps > 0:
            step_text += ", " + str(endResult.skipped_steps) + " skipped"

        print(str(endResult.total_features) + " features (%s" % (feature_text) + ")")
        print(str(endResult.total_scenarios) + " scenarios (%s" % (scenario_text) + ")")
        print(str(endResult.total_steps) + " steps (%s" % (step_text) + ")")
