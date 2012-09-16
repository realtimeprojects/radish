# -*- coding: utf-8 -*-

import os
import fnmatch

class FileSystemHelper( object ):
  @classmethod
  def expand( cls, path ):
    """Expand the environment variables and the user's home directory in a given path"""
    return os.path.expanduser( os.path.expandvars( path ))

  @classmethod
  def abspath( cls, path ):
    """Return the absolut path of the given path"""
    return os.path.abspath( cls.expand( path ))

  @classmethod
  def dirname( cls, path ):
    """Return the directory name for the given path"""
    return cls.abspath( os.path.dirname( path ))

  @classmethod
  def filename( cls, path, with_extension = True ):
    """Return the filename of the given path"""
    f = os.path.split( path )[1]
    if not with_extension:
      f = os.path.splitext( f )[0]
    return f

  @classmethod
  def locate( cls, root, pattern ):
    """Locate files in a directory recursively if it fits with the given pattern"""
    root = cls.abspath( root )
    files = []
    for p, d, f in os.walk( root ):
      for filename in fnmatch.filter( f, pattern ):
        files.append( os.path.join( p, filename ))
    files.sort( )
    return files
