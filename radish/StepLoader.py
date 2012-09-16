# -*- coding: utf-8 -*-

import sys

from radish.StepRegistry import StepRegistry
from radish.FileSystemHelper import FileSystemHelper as fsh

class StepLoader( object ):
  def __init__( self, basedir, features ):
    # FIXME: check if basedir exists
    self.basedir  = basedir
    self.features = features

  def load_steps( self ):
    files = fsh.locate( self.basedir, "steps.py" )
    for f in files:
      root = fsh.dirname( f )
      sys.path.insert( 0, root )
      module_name = fsh.filename( f, False )
      try:
        module = __import__( module_name )
        sys.path.remove( root )
      except ValueError, e:
        import traceback
        if "empty module name" in traceback.format_exc( e ).lower( ):
          continue
        else:
          raise e

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
