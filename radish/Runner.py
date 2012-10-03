# -*- coding: utf-8 -*-

from radish.HookRegistry import HookRegistry

class Runner( object ):
  def __init__( self, features ):
    self.features = features

  def run( self ):
    hr = HookRegistry( )
    hr.call_hook( "before", "all" )
    for f in self.features:
      hr.call_hook( "before", "feature", f )
      f.write( )

      for s in f.Scenarios:
        hr.call_hook( "before", "scenario", s )
        s.write( )
        for step in s.Steps:
          hr.call_hook( "before", "step", step )
          step.write( )
          step.run( )
          hr.call_hook( "after", "step", step )
        print
        hr.call_hook( "after", "scenario", s )
      hr.call_hook( "after", "feature", f )
    hr.call_hook( "after", "all" )
