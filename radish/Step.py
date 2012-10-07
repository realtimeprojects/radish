# -*- coding: utf-8 -*-

import traceback

from radish.Colorful import colorful

class Step( object ):
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
    return self.passed
