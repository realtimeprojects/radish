# -*- coding: utf-8 -*-

class UtilRegistry( object ):
  def __new__( type, *args ):
    if not "instance" in type.__dict__:
      type.instance = object.__new__( type )
    return type.instance

  def __init__( self ):
    if not "utils" in dir( self ):
      self.utils = {}

  def register( self, util, func ):
    self.utils[util] = func

  def has_util( self, util ):
    return self.utils.has_key( util )

  def call_util( self, util, *args, **kw ):
    if self.utils.has_key( util ):
      return self.utils[util]( *args, **kw )
    return None

def utils( util ):
  def wrapper( func ):
    UtilRegistry( ).register( util, func )
    return func
  return wrapper
