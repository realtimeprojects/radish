# -*- coding: utf-8 -*-

import os
import re

from radish.Config import Config
from radish.Feature import Feature
from radish.Scenario import Scenario
from radish.Step import Step
from radish.FileSystemHelper import FileSystemHelper as fsh
from radish.Exceptions import FeatureFileNotFoundException


class FeatureParser(object):
    def __init__(self):
        self.features = []
        self.feature_files = []
        for f in Config().feature_files:
            if os.path.isdir(f):
                self.feature_files.extend(fsh.locate(f, "*.feature"))
            else:
                self.feature_files.append(f)

    @property
    def Features(self):
        return self.features

    def parse(self):
        conf = Config()
        conf.highest_feature_id = 0
        conf.highest_scenario_id = 0
        conf.highest_step_id = 0
        conf.longest_feature_text = 0
        self.feature_id = 0
        for f in self.feature_files:
            self.features.extend(self.parse_feature(f))
        conf.highest_feature_id = self.feature_id

    def parse_feature(self, feature_file):
        if not os.path.exists(feature_file):
            print FeatureFileNotFoundException(feature_file)
            raise SystemExit(-2)

        features = []
        in_feature = False
        scenario_id = 0
        step_id = 0
        line_no = 0

        # FIXME: compile regex patterns
        f = open(feature_file, "r")
        for l in f.readlines():
            line_no += 1
            if not l.strip() or re.search("^[ ]*?#", l):
                continue

            feature_match = re.search("Feature: ?(.*)$", l)
            scenario_match = re.search("Scenario: ?(.*)$", l)

            if feature_match:  # create new feature
                in_feature = True
                self.feature_id += 1
                scenario_id = 0
                features.append(Feature(self.feature_id, feature_match.group(1), feature_file, line_no))
                if len(feature_match.group(1)) > Config().longest_feature_text:
                    Config().longest_feature_text = len(feature_match.group(1))
            elif scenario_match:  # create new scenario
                in_feature = False
                scenario_id += 1
                step_id = 0
                features[-1].AppendScenario(Scenario(scenario_id, scenario_match.group(1), feature_file, line_no))
                if scenario_id > Config().highest_scenario_id:
                    Config().highest_scenario_id = scenario_id
            else:  # create new step or append feature description line
                line = l.rstrip(os.linesep).strip()
                if not in_feature:
                    step_id += 1
                    features[-1].Scenarios[-1].AppendStep(Step(step_id, line, feature_file, line_no))
                    if step_id > Config().highest_step_id:
                        Config().highest_step_id = step_id
                else:
                    features[-1].AppendDescriptionLine(line)
                    if len(line) + 2 > Config().longest_feature_text:
                        Config().longest_feature_text = len(line) + 2

        f.close()
        return features
