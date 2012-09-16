# -*- coding: utf-8 -*-

from radish.Step import Step

class Scenario( object ):
  def __init__( self, id, sentence, filename ):
    self.id = id
    self.sentence = sentence
    self.filename = filename
    self.steps = []

  @property
  def Steps( self ):
    return self.steps

  def AppendStep( self, step ):
    if isinstance( step, Step ):
      self.steps.append( step )
