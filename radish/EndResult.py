# -*- coding: utf-8 -*-

class EndResult( object ):
  def __init__( self, features ):
    self.features = features
    self.total_features = 0
    self.total_scenarios = 0
    self.total_steps = 0

    self.passed_features = 0
    self.failed_features = 0
    self.passed_scenarios = 0
    self.failed_scenarios = 0
    self.passed_steps = 0
    self.failed_steps = 0
    self.skipped_steps = 0

    self.total_features = len( features )
    for f in features:
      if f.Passed:
        self.passed_features += 1

      self.total_scenarios += len( f.Scenarios )

      for s in f.Scenarios:
        if s.Passed:
          self.passed_scenarios += 1

        self.total_steps += len( s.Steps )

        for step in s.Steps:
          if step.Passed:
            self.passed_steps += 1
          elif step.Passed == False:
            self.failed_steps += 1
          elif step.Passed == None:
            self.skipped_steps += 1

    self.failed_features = self.total_features- self.passed_features
    self.failed_scenarios = self.total_scenarios - self.passed_scenarios

  @property
  def Features( self ):
    return self.features
