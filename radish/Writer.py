# -*- coding: utf-8 -*-

from radish.Colorful import colorful
from radish.HookRegistry import after, before

@after.all
def print_after_all( ):
  print( "Here goes the result" )

@before.each_feature
def print_before_feature( feature ):
  colorful.out.bold_white( "  " + feature.sentence )
  for l in feature.description.splitlines( ): colorful.out.white( "    " + l )
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
  colorful.out.bold_green( "\033[A      " + str( step.id ) + ". " + step.sentence )
