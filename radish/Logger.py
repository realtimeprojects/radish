# -*- coding: utf-8 -*-

import syslog

from radish.HookRegistry import after, before

class Logger( object ):
  @staticmethod
  def init( ):
    syslog.openlog( "radish", facility = syslog.LOG_USER )

  @staticmethod
  def free( ):
    syslog.closelog( )

  @staticmethod
  def log( message ):
    syslog.syslog( syslog.LOG_INFO, message )

@before.all
def log_before_all( ):
  Logger.init( )
  Logger.log( "start to run features" )

@after.all
def log_after_all( endResult ):
  Logger.log( "finished features" )
  Logger.free( )

@before.each_feature
def log_before_feature( feature ):
  Logger.log( "start feature %d: '%s'"%( feature.id, feature.Sentence ))

@after.each_feature
def log_after_feature( feature ):
  Logger.log( "terminated feature %d: '%s'"%( feature.id, feature.Sentence ))

@before.each_scenario
def log_before_scenario( scenario ):
  Logger.log( "start scenario %d: '%s'"%( scenario.id, scenario.Sentence ))

@after.each_scenario
def log_after_scenario( scenario ):
  Logger.log( "terminated scenario %d: '%s'"%( scenario.id, scenario.Sentence ))

@before.each_step
def log_before_step( step ):
  Logger.log( "start step %d: '%s'"%( step.id, step.Sentence ))

@after.each_step
def log_after_step( step ):
  Logger.log( "terminated step %d: '%s'"%( step.id, step.Sentence ))
