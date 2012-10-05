# -*- coding: utf-8 -*-

import os
import re

from radish.Feature import Feature
from radish.Scenario import Scenario
from radish.Step import Step
from radish.FileSystemHelper import FileSystemHelper as fsh
from radish.Exceptions import FeatureFileNotFoundException

class FeatureParser( object ):
  longest_feature_text = 0

  def __init__( self, feature_files ):
    self.features = []
    self.feature_files = []
    feature_files = feature_files if isinstance( feature_files, list ) else [feature_files]
    for f in feature_files:
      self.feature_files.append( fsh.expand( f ))

  @property
  def Features( self ):
    return self.features

  def parse( self ):
    self.feature_id = 1
    for f in self.feature_files:
      self.features.extend( self.parse_feature( f ))

  def parse_feature( self, feature_file ):
    if not os.path.exists( feature_file ):
      print FeatureFileNotFoundException( feature_file )
      raise SystemExit( 1 )

    features    = []
    in_feature  = False
    scenario_id = 1
    step_id     = 1

    # FIXME: compile regex patterns
    f = open( feature_file, "r" )
    for l in f.readlines( ):
      if not l.strip( ) or re.search( "^[ ]*?#", l ):
        continue;

      feature_match = re.search( "Feature: ?(.*)$", l )
      scenario_match = re.search( "Scenario: ?(.*)$", l )

      if feature_match: # create new feature
        in_feature = True
        features.append( Feature( self.feature_id, feature_match.group( 1 ), feature_file ))
        self.feature_id += 1
        scenario_id = 1
        if len( feature_match.group( 1 )) > FeatureParser.longest_feature_text:
          FeatureParser.longest_feature_text = len( feature_match.group( 1 ))
      elif scenario_match: # create new scenario
        in_feature = False
        features[-1].AppendScenario( Scenario( scenario_id, scenario_match.group( 1 ), feature_file ))
        scenario_id += 1
        step_id = 1
      else: # create new step or append feature description line
        line = l.rstrip( os.linesep ).strip( )
        if not in_feature:
          features[-1].Scenarios[-1].AppendStep( Step( step_id, line, feature_file ))
          step_id += 1
        else:
          features[-1].AppendDescriptionLine( line )
          if len( line ) + 2 > FeatureParser.longest_feature_text:
            FeatureParser.longest_feature_text = len( line ) + 2

    f.close( )
    return features
