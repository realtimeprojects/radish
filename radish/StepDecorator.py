# -*- coding: utf-8 -*-

import re

from radish.StepRegistry import StepRegistry

def step( regex ):
  def wrapper( func ):
    try:
      re.compile( regex )
    except re.error, e:
      return False # FIXME: raise StepLoadingException
    StepRegistry( ).register( regex, func )
    return func
  return wrapper

