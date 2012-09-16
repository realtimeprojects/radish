#!/usr/bin/python
# -*- coding: utf-8 -*-

import radish

def main( ):
  fp = radish.FeatureParser( "~/Work/radish/testfiles/features/001-feature.feature" )
  fp.parse( )

if __name__ == "__main__":
  main( )
