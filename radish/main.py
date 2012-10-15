#!/usr/bin/python
# -*- coding: utf-8 -*-

import radish

import os
import time
#import argparse
import optparse

def main( ):
  parser = optparse.OptionParser( description = "radish is a smart 'Test-Driven Developement'-Tool", epilog = "(C) Copyright 2012 by Timo Furrer <tuxtimo@gmail.com>" )
  parser.add_option( "-b", "--basedir",
                    dest = "basedir",
                    default = os.path.join( os.getcwd( ), "radish" ),
                    help = "The basedir is used to locate the steps.py and terrain.py"
                  )
  parser.add_option( "-a", "--abort-fail",
                     dest = "abort_fail",
                     action = "store_true",
                     help = "If one feature file fails this option will stop the execution"
                   )
  parser.add_option( "-v", "--verbosity",
                     dest = "verbosity",
                     default = 1,
                     help    = "The verbosity level for the output"
                   )
  parser.add_option( "-m", "--marker",
                     default = int( time.time( )),
                     help    = "A specific marker for the step loggings"
                   )
  #parser = argparse.ArgumentParser( description = "radish is a smart 'Test-Driven Developement'-Tool", epilog = "(C) Copyright 2012 by Timo Furrer <tuxtimo@gmail.com>" )
  #parser.add_argument( "-b", "--basedir",
                       #nargs   = 1,
                       #default = [ os.path.join( os.getcwd( ), "radish" ) ],
                       #help    = "The basedir is used to locate the steps.py and terrain.py"
                     #)
  #parser.add_argument( "-a", "--abort-fail",
                       #action = "store_true",
                       #help   = "If one feature file fails this option will stop the execution"
                     #)
  #parser.add_argument( "-v", "--verbosity",
                       #default = 1,
                       #help    = "The verbosity level for the output"
                     #)
  #parser.add_argument( "-m", "--marker",
                       #default = int( time.time( )),
                       #help    = "A specific marker for the step loggings"
                     #)
  #parser.add_argument( "feature_files",
                       #nargs = "+",
                       #help  = "The feature files"
                     #)

  #args = parser.parse_args( )
  options, args = parser.parse_args( )

  # initialize config object
  cf = radish.Config( )
  #cf.SetBasedir( radish.FileSystemHelper.expand( options.basedir[0] ))
  cf.SetBasedir( radish.FileSystemHelper.expand( options.basedir ))
  #cf.feature_files = options.feature_files
  cf.feature_files = args
  cf.abort_fail    = options.abort_fail
  cf.verbosity     = options.verbosity
  cf.marker        = options.marker

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
