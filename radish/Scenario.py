# -*- coding: utf-8 -*-

from radish.Step import Step

class Scenario( object ):
  def __init__( self, id, sentence, filename ):
    self.id = id
    self.sentence = sentence
    self.filename = filename
    self.steps = []

  @property
  def Id( self ):
    return self.id

  @property
  def Sentence( self ):
    return self.sentence

  @property
  def Steps( self ):
    return self.steps

  @property
  def Passed( self ):
    for s in self.steps:
      if not s.Passed: return False
    return True

  def AppendStep( self, step ):
    if isinstance( step, Step ):
      self.steps.append( step )
