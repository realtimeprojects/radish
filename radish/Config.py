# -*- coding: utf-8 -*-

import os

from radish.Exceptions import BasedirNotFoundException


class Config(object):
    instance = None

    class __Config(object):
        def SetBasedir(self, basedir):
            if not os.path.exists(basedir) or not os.path.isdir(basedir):
                print BasedirNotFoundException(basedir)
                raise SystemExit(-2)
            self.basedir = basedir

    def __new__(cls):
        if not Config.instance:
            Config.instance = Config.__Config()
        return Config.instance

    def __getattr__(self, key):
        return getattr(self.instance, key)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)
