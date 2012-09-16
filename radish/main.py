#!/usr/bin/python
# -*- coding: utf-8 -*-

import radish

def main( ):
  basedir = "~/Work/radish/testfiles/steps/"
  fp = radish.FeatureParser( "~/Work/radish/testfiles/features/001-feature.feature" )
  fp.parse( )

  tl = radish.TerrainLoader( basedir )
  tl.load_terrain( )

  sdl = radish.StepDefinitionLoader( basedir, fp.Features )
  sdl.load_steps( )
  sdl.merge_steps_with_defintions( )

if __name__ == "__main__":
  main( )
