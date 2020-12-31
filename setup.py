#!/usr/bin/env python3

# ------------------------------------------------------------------------------
"""
  Setup file of basilic. 

  Author: Rémi Mignot, 2020.
"""

from setuptools import setup

# Load requirements: 
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

# ------------------------------------------------------------------------------
# Setup configuration
setup(
  name        = 'basilic', 
  version     = '0.1.0', 
  author      = 'Rémi Mignot', 
  # author_email = 'no@email.com', 
  packages    = [ 'basilic' ], 
  # scripts   = [ 'basilic/bin/no_script' ], 
  url         = 'https://github.com/remignot/basilic', 
  license     = 'LICENSE.txt', 
  keywords    = [ 'tools' ], 
  description = 'A good package for divers things !', 
  long_description = open( 'README.md' ).read(), 
  
  include_package_data = True,
  package_data = { 'basilic_ipy': [ 'data/*' ] },
  
  python_requires   = '>=3',
  install_requires  = requirements, 
  # dependency_links  = [ 'http://not_yet.com' ], 
)
