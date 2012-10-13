#!/usr/bin/python
# -*- coding: utf-8 -*-

import radish

import os
import time
import argparse

def main( ):
  parser = argparse.ArgumentParser( description = "radish is a smart 'Test-Driven Developement'-Tool", epilog = "(C) Copyright 2012 by Timo Furrer <tuxtimo@gmail.com>" )
  parser.add_argument( "-b", "--basedir",
                       nargs   = 1,
                       default = [ os.path.join( os.getcwd( ), "features" ) ],
                       help    = "The basedir is used to locate the steps.py and terrain.py"
                     )
  parser.add_argument( "-a", "--abort-fail",
                       action = "store_true",
                       help   = "If one feature file fails this option will stop the execution"
                     )
  parser.add_argument( "-v", "--verbosity",
                       default = 1,
                       help    = "The verbosity level for the output"
                     )
  parser.add_argument( "-m", "--marker",
                       default = int( time.time( )),
                       help    = "A specific marker for the step loggings"
                     )
  parser.add_argument( "feature_files",
                       nargs = "+",
                       help  = "The feature files"
                     )

  args = parser.parse_args( )

  # initialize config object
  cf = radish.Config( )
  cf.SetBasedir( radish.FileSystemHelper.expand( args.basedir[0] ))
  cf.feature_files = args.feature_files
  cf.abort_fail    = args.abort_fail
  cf.verbosity     = args.verbosity
  cf.marker        = args.marker

  # parse feature files
  fp = radish.FeatureParser( )
  fp.parse( )

  # load terrain and steps
  loader = radish.Loader( fp.Features )
  loader.load( )

  # run the features
  runner = radish.Runner( fp.Features )
  runner.run( )

if __name__ == "__main__":
  main( )
