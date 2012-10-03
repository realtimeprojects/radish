# -*- coding: utf-8 -*-

from radish.StepRegistry import StepRegistry
from radish.FileSystemHelper import FileSystemHelper as fsh

class Loader( object ):
  def __init__( self, basedir, features ):
    self.basedir = basedir
    self.features = features

  def load( self ):
    self.load_terrain( )
    self.load_step_definitions( )

  def load_terrain( self ):
    fsh.import_module( self.basedir, "terrain.py" )

  def load_step_definitions( self ):
    fsh.import_module( self.basedir, "steps.py" )
    self.merge_steps_with_definitions( )

  def merge_steps_with_definitions( self ):
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
