# -*- coding: utf-8 -*-

class Runner( object ):
  def __init__( self, features ):
    self.features = features

  def run( self ):
    for f in self.features:
      f.write( )

      for s in f.Scenarios:
        s.write( )
        for step in s.Steps:
          step.write( )
          step.run( )
        print
