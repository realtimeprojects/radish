# -*- coding: utf-8 -*-

import sys

from radish.Colorful import colorful
from radish.FeatureParser import FeatureParser
from radish.HookRegistry import after, before

@before.each_feature
def print_before_feature( feature ):
  print( colorful.bold_white( "  " + feature.sentence + " " * (FeatureParser.longest_feature_text - len( feature.sentence ))) + " " * 10 + colorful.bold_black( "# " + feature.filename ))
  for l in feature.description.splitlines( ):
    colorful.out.white( "    " + l )
  print( "" )

@before.each_scenario
def print_before_scenario( scenario ):
  colorful.out.bold_white( "    " + scenario.sentence )

@after.each_scenario
def print_after_scenario( scenario ):
  print( "" )

@before.each_step
def print_before_step( step ):
  colorful.out.bold_black( "      "  + str( step.id ) + ". " + step.sentence )

@after.each_step
def print_after_step( step ):
  sys.stdout.write( "\033[A" )
  if step.passed:
    fn = colorful.out.bold_green
  elif step.passed == False:
    fn = colorful.out.bold_red
  elif step.passed == None:
    fn = colorful.out.cyan
  fn( "      " + str( step.id ) + ". " + step.sentence )

  if step.passed == False:
    for l in step.fail_reason.traceback.splitlines( ):
      colorful.out.red( "      " + l )

@after.all
def print_after_all( endResult ):
  white = colorful.bold_white
  green = colorful.bold_green
  red = colorful.bold_red
  cyan = colorful.cyan

  feature_text = green( str( endResult.passed_features ) + " passed" )
  if endResult.failed_features > 0:
    feature_text += white( ", " ) + red( str( endResult.failed_features ) + " failed" )

  scenario_text = green( str( endResult.passed_scenarios ) + " passed" )
  if endResult.failed_scenarios > 0:
    scenario_text += white( ", " ) + red( str( endResult.failed_scenarios ) + " failed" )

  step_text = green( str( endResult.passed_steps ) + " passed" )
  if endResult.failed_steps > 0:
    step_text += white( ", " ) + red( str( endResult.failed_steps ) + " failed" )
  if endResult.skipped_steps > 0:
    step_text += white( ", " ) + cyan( str( endResult.skipped_steps ) + " skipped" )

  colorful.out.bold_white( str( endResult.total_features ) + " features (%s)"%( feature_text ))
  colorful.out.bold_white( str( endResult.total_scenarios ) + " scenarios (%s)"%( scenario_text ))
  colorful.out.bold_white( str( endResult.total_steps ) + " steps (%s)"%( step_text ))
