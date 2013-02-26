# -*- coding: utf-8 -*-

import re

from radish.singleton import singleton


@singleton()
class StepRegistry(object):
    def __init__(self):
        self.steps = {}

    def register(self, regex, func):
        self.steps[regex] = func

    def find(self, sentence):
        for regex, func in self.steps.items():
            match = re.search(regex, sentence)
            if match:
                return match, func
        return None, None
