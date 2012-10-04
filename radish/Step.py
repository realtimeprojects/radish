# -*- coding: utf-8 -*-

from radish.Colorful import colorful

class Step( object ):
  def __init__( self, id, sentence, filename ):
    self.id = id
    self.sentence = sentence
    self.filename = filename
    self.func = None
    self.match = None

  @property
  def Sentence( self ):
    return self.sentence

  @property
  def Func( self ):
    return self.func

  @property
  def Match( self ):
    return self.match

  def run( self ):
    kw = self.match.groupdict( )
    if kw:
      self.func( self, **kw )
    else:
      self.func( self, *self.match.groups( ))
