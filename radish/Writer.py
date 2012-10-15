# -*- coding: utf-8 -*-

import sys

from radish.Colorful import colorful
from radish.Config import Config
from radish.FeatureParser import FeatureParser
from radish.HookRegistry import after, before
from radish.FileSystemHelper import FileSystemHelper as fsh

@before.each_feature
def print_before_feature( feature ):
  if not feature.DryRun:
    print( colorful.bold_white( "  " + feature.Sentence + " " * (FeatureParser.longest_feature_text - len( feature.Sentence ))) + " " * 10 + colorful.bold_black( "# " + fsh.filename( feature.filename )))
    for l in feature.description.splitlines( ):
      colorful.out.white( "    " + l )
    print( "" )

@before.each_scenario
def print_before_scenario( scenario ):
  if not scenario.DryRun:
    colorful.out.bold_white( "    " + scenario.Sentence )

@after.each_scenario
def print_after_scenario( scenario ):
  if not scenario.DryRun:
    print( "" )

@before.each_step
def print_before_step( step ):
  if not step.DryRun:
    colorful.out.bold_brown( "      %*d. %s"%( len( str( FeatureParser.highest_step_id )), step.Id, step.Sentence ))

@after.each_step
def print_after_step( step ):
  if not step.DryRun:
    sys.stdout.write( "\033[A" )
    if step.passed:
      color_fn = colorful.out.bold_green
    elif step.passed == False:
      color_fn = colorful.out.bold_red
    elif step.passed == None:
      color_fn = colorful.out.cyan
    color_fn( "      %*d. %s"%( len( str( FeatureParser.highest_step_id )), step.Id, step.Sentence ))

    if step.passed == False:
      for l in step.fail_reason.traceback.splitlines( ):
        colorful.out.red( "      " + l )

@after.all
def print_after_all( endResult ):
  if not Config( ).dry_run:
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

    colorful.out.bold_white( str( endResult.total_features ) + " features (%s"%( feature_text ) + white( ")" ))
    colorful.out.bold_white( str( endResult.total_scenarios ) + " scenarios (%s"%( scenario_text ) + white( ")" ))
    colorful.out.bold_white( str( endResult.total_steps ) + " steps (%s"%( step_text ) + white( ")" ))
