# -*- coding: utf-8 -*-

import os

from radish.config import Config
from radish.stepregistry import StepRegistry
from radish.filesystemhelper import FileSystemHelper as fsh
from radish.exceptions import StepDefinitionFileNotFoundError, StepDefinitionNotFoundError, WriterNotFoundError


class Loader(object):
    def __init__(self, features):
        self.features = features

    def load(self):
        self.load_terrain()
        self.load_step_definitions()
        self.load_writer()
        self.load_logger()

    def load_terrain(self):
        fsh.import_module(Config().basedir, "terrain.py")

    def load_step_definitions(self):
        if not fsh.locate(Config().basedir, "steps.py"):
            raise StepDefinitionFileNotFoundError(Config().basedir, "steps.py")

        fsh.import_module(Config().basedir, "steps.py")
        self.merge_steps_with_definitions()

    def load_writer(self):
        if not fsh.locate(Config().basedir, "writer.py"):
            level = int(Config().verbosity)
            try:
                fsh.import_module(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Writers"), "level_%d.py" % level, no_modules_error=True)
            except ImportError:
                raise WriterNotFoundError(level)
        else:
            fsh.import_module(Config().basedir, "writer.py")

    def load_logger(self):
        if fsh.locate(Config().basedir, "logger.py"):
            fsh.import_module(Config().basedir, "logger.py")

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
