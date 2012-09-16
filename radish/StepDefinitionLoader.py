# -*- coding: utf-8 -*-

from radish.StepRegistry import StepRegistry
from radish.FileSystemHelper import FileSystemHelper as fsh

class StepDefinitionLoader( object ):
  def __init__( self, basedir, features ):
    # FIXME: check if basedir exists
    self.basedir  = basedir
    self.features = features

  def load_steps( self ):
    fsh.import_module( self.basedir, "steps.py" )

  def merge_steps_with_defintions( self ):
    sr = StepRegistry( )
    for feature in self.features:
      for scenario in feature.Scenarios:
        for step in scenario.Steps:
          match, func = sr.find( step.Sentence )
          if match and func:
            step.func = func
            step.match = match
          else:
            return False # FIXME: raise StepDefinitionNotFoundException
