# -*- coding: utf-8 -*-


from radish.pysingleton.singleton import singleton


@singleton()
class UtilRegistry(object):
    def __init__(self):
        self.utils = {}

    def register(self, util, func):
        self.utils[util] = func

    def has_util(self, util):
        return util in self.utils

    def call_util(self, util, *args, **kw):
        if self.has_util(util):
            return self.utils[util](*args, **kw)
        return None


def utils(util):
    def wrapper(func):
        UtilRegistry().register(util, func)
        return func
    return wrapper
