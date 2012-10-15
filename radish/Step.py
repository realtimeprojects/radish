# -*- coding: utf-8 -*-

import traceback
import inspect

from radish.Colorful import colorful
from radish.Config import Config
from radish.UtilRegistry import UtilRegistry
from radish.Exceptions import ValidationException

class Step( object ):
  CHARS_PER_LINE = 80

  def __init__( self, id, sentence, filename ):
    self.id = id
    self.sentence = sentence
    self.filename = filename
    self.func = None
    self.match = None
    self.passed = None
    self.fail_reason = None

  @property
  def Id( self ):
    return self.id

  @property
  def Sentence( self ):
    return self.sentence

  @property
  def SplittedSentence( self ):
    ur = UtilRegistry( )
    if ur.has_util( "split_sentence" ):
      return ur.call_util( "split_sentence", self.sentence )
    else:
      splitted = [self.sentence[i:i+Step.CHARS_PER_LINE] for i in range( 0, len( self.sentence ), Step.CHARS_PER_LINE )]
      return len( splitted ), ( "\n          " ).join( splitted )

  @property
  def DryRun( self ):
    return Config( ).dry_run

  @property
  def Func( self ):
    return self.func

  @property
  def Match( self ):
    return self.match

  @property
  def Passed( self ):
    return self.passed

  class FailReason( object ):
    def __init__( self, e ):
      self.exception = e
      self.reason = unicode( e )
      self.traceback = traceback.format_exc( e )

  def run( self ):
    kw = self.match.groupdict( )
    try:
      if kw:
        self.func( self, **kw )
      else:
        self.func( self, *self.match.groups( ))
      self.passed = True
    except Exception, e:
      self.passed = False
      self.fail_reason = Step.FailReason( e )
      if self.DryRun:
        caller = inspect.trace( )[-1]
        print( "%s:%d: error: %s"%( caller[1], caller[2], unicode( e )))
    return self.passed

  def ValidationError( self, msg ):
    if self.DryRun:
      caller = inspect.getouterframes( inspect.currentframe( ))[1]
      print( "%s:%d: error: %s"%( caller[1], caller[2], msg ))
    else:
      raise ValidationException( msg )
