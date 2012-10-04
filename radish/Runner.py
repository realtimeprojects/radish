# -*- coding: utf-8 -*-

from radish.HookRegistry import HookRegistry
from radish.EndResult import EndResult

class Runner( object ):
  def __init__( self, features ):
    self.features = features

  def run( self ):
    hr = HookRegistry( )
    hr.call_hook( "before", "all" )

    for f in self.features:
      hr.call_hook( "before", "feature", f )

      for s in f.Scenarios:
        hr.call_hook( "before", "scenario", s )
        skip_remaining_steps = False

        for step in s.Steps:
          hr.call_hook( "before", "step", step )

          if not skip_remaining_steps:
            passed = step.run( )
            if not passed:
              skip_remaining_steps = True

          hr.call_hook( "after", "step", step )
        hr.call_hook( "after", "scenario", s )
      hr.call_hook( "after", "feature", f )

    hr.call_hook( "after", "all", EndResult( self.features ))
