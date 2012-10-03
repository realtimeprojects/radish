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
    self.rewrite( )

  # FIXME: better names for self.write and self.rewrite ... e.g. writeSentence, writeResult ;)
  def write( self ):
    colorful.out.bold_black( "      "  + str( self.id ) + ". " + self.sentence )

  def rewrite( self ):
    colorful.out.bold_green( "\033[A      " + str( self.id ) + ". " + self.sentence )
