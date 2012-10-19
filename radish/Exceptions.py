# -*- coding: utf-8 -*-

from radish.Colorful import colorful


class StepLoadingException(Exception):
    """Raised when a step decorator regex is not valid to compile"""
    def __init__(self, regex):
        self.regex = regex

    def __str__(self):
        return colorful.bold_red("The step decorator regex '%s' is not valid to compile" % (self.regex))


class StepDefinitionNotFoundException(Exception):
    """Raised when a step definition could not be found"""
    def __init__(self, step_sentence):
        self.step_sentence = step_sentence

    def __str__(self):
        return colorful.bold_red("The step definition for the step '%s' could not be found" % (self.step_sentence))


class FeatureFileNotFoundException(Exception):
    """Raised when a feature file could not be found"""
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return colorful.bold_red("The feature file '%s' could not be found" % (self.path))


class BasedirNotFoundException(Exception):
    """Raised when the basedir could not be found"""
    def __init__(self, basedir):
        self.basedir = basedir

    def __str__(self):
        return colorful.bold_red("The basedir '%s' could not be found" % (self.basedir))


class StepDefinitionFileNotFoundException(Exception):
    """Raised when the step definition file could not be found"""
    def __init__(self, root, pattern):
        self.root = root
        self.pattern = pattern

    def __str__(self):
        return colorful.bold_red("The step definition file '%s' could not be found in the directory '%s'" % (self.pattern, self.root))


class ValidationException(Exception):
    """Raised when a validation error occured during run"""
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return colorful.bold_red(self.msg)
