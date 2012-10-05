# -*- coding: utf-8 -*-

class Config( object ):
  instance = None
  class __Config: pass

  def __new__( cls ):
    if not Config.instance:
      Config.instance = Config.__Config( )
    return Config.instance

  def __getattr__( self, key ):
      return getattr( self.instance, key )

  def __setattr__( self, key, value ):
      return setattr( self.instance, key, value )
