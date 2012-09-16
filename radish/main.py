#!/usr/bin/python
# -*- coding: utf-8 -*-

import radish

def main( ):
  basedir = "~/Work/radish/testfiles/steps/"
  fp = radish.FeatureParser( "~/Work/radish/testfiles/features/001-feature.feature" )
  fp.parse( )

  sl = radish.StepLoader( basedir, fp.Features )
  sl.load_steps( )
  sl.merge_steps_with_defintions( )

if __name__ == "__main__":
  main( )
