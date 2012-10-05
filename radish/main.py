#!/usr/bin/python
# -*- coding: utf-8 -*-

import radish

import argparse

def main( ):
  parser = argparse.ArgumentParser( description = "radish is a smart 'Test-Driven Developement'-Tool", epilog = "(C) Copyright 2012 by Timo Furrer <tuxtimo@gmail.com>" )
  parser.add_argument( "-b", "--basedir",    help = "The basedir is used to locate the steps.py and terrain.py", nargs = 1, default = "features" )
  parser.add_argument( "-a", "--abort-fail", help = "If one feature file fails this option will stop the execution", action = "store_true" )
  parser.add_argument( "-v", "--verbosity",  help = "The verbosity level for the output", default = 1 )
  parser.add_argument( "feature_files",      help = "The feature files", nargs = "+" )

  args = parser.parse_args( )

  # initialize config object
  cf = radish.Config( )
  cf.SetBasedir( radish.FileSystemHelper.expand( args.basedir[0] ))
  cf.feature_files = args.feature_files
  cf.abort_fail = args.abort_fail
  cf.verbosity = args.verbosity

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
