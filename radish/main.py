#!/usr/bin/python
# -*- coding: utf-8 -*-

import radish

def main( ):
  basedir = "~/Work/radish/testfiles/steps/"
  fp = radish.FeatureParser( "~/Work/radish/testfiles/features/001-feature.feature" )
  fp.parse( )

  loader = radish.Loader( basedir, fp.Features )
  loader.load_terrain( )
  loader.load_step_definitions( )

  runner = radish.Runner( fp.Features )
  runner.run( )

if __name__ == "__main__":
  main( )
