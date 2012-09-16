# -*- coding: utf-8 -*-

from radish.FileSystemHelper import FileSystemHelper as fsh

class TerrainLoader( object ):
  def __init__( self, basedir ):
    # FIXME: check if basedir exists
    self.basedir  = basedir

  def load_terrain( self ):
    fsh.import_module( self.basedir, "terrain.py" )
