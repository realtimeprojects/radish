# -*- coding: utf-8 -*-

from radish.Config import Config
from radish.StepRegistry import StepRegistry
from radish.FileSystemHelper import FileSystemHelper as fsh
from radish.Exceptions import StepDefinitionFileNotFoundError, StepDefinitionNotFoundError


class Loader(object):
    def __init__(self, features):
        self.features = features

    def load(self):
        self.load_terrain()
        self.load_step_definitions()

    def load_terrain(self):
        fsh.import_module(Config().basedir, "terrain.py")

    def load_step_definitions(self):
        if len(fsh.locate(Config().basedir, "steps.py")) == 0:
            raise StepDefinitionFileNotFoundError(Config().basedir, "steps.py")

        fsh.import_module(Config().basedir, "steps.py")
        self.merge_steps_with_definitions()

    def merge_steps_with_definitions(self):
        sr = StepRegistry()
        for feature in self.features:
            for scenario in feature.Scenarios:
                for step in scenario.Steps:
                    match, func = sr.find(step.Sentence)
                    if match and func:
                        step.func = func
                        step.match = match
                    else:
                        raise StepDefinitionNotFoundError(step.Sentence)
