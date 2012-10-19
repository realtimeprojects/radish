# -*- coding: utf-8 -*-

import re


class StepRegistry(object):
    def __new__(type, *args):
        if not "instance" in type.__dict__:
            type.instance = object.__new__(type)
        return type.instance

    def __init__(self):
        if not "steps" in dir(self):
            self.steps = {}

    def register(self, regex, func):
        self.steps[regex] = func

    def find(self, sentence):
        for regex, func in self.steps.items():
            match = re.search(regex, sentence)
            if match:
                return match, func
        return None, None
