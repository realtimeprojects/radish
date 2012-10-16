# -*- coding: utf-8 -*-

import syslog

from radish.HookRegistry import after, before
from radish.Config import Config

class Logger( object ):
  @staticmethod
  def init( ):
    syslog.openlog( "radish" )

  @staticmethod
  def free( ):
    syslog.closelog( )

  @staticmethod
  def log( message ):
    syslog.syslog( syslog.LOG_INFO, message )

@before.all
def log_before_all( ):
  Logger.init( )
  Logger.log( "starting test %s"%( unicode( Config( ).marker )))

@after.all
def log_after_all( endResult ):
  Logger.log( "test %s terminated"%( unicode( Config( ).marker )))
  Logger.free( )

@before.each_feature
def log_before_feature( feature ):
  Logger.log( "testing feature %d"%( feature.Id ))

@after.each_feature
def log_after_feature( feature ):
  Logger.log( "feature %d terminated"%( feature.Id ))

@before.each_scenario
def log_before_scenario( scenario ):
  Logger.log( "testing scenario %d"%( scenario.Id ))

@after.each_scenario
def log_after_scenario( scenario ):
  Logger.log( "scenario %d terminated"%( scenario.Id ))

@before.each_step
def log_before_step( step ):
  Logger.log( "testing step %d"%( step.Id ))

@after.each_step
def log_after_step( step ):
  if step.passed == False:
    Logger.log( "step %d FAILED"%( step.Id ))
  else:
    Logger.log( "step %d terminated"%( step.Id ))
