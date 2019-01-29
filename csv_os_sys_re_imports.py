import csv
with open('users.csv', 'w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['id', 'email', 'name'])
  writer.writerow[('6', 'alexrpereyra@gmail.com', 'Arther Fonz, AKA "The Fonz"')]
cat users.cvs

import os
os.getenv('USER')
os.path.abspath('.')

import sys
sys.argv
['/usr/local/bin/ipython3']
sys.platform
'darwin'
sys.version
'3.7.0 (default, Jul 23 2018, 20:22:55) \n[Clang 9.1.0 (clang-902.0.39.2)]'

#pattern matching
import re
if re.search('string', 'morestrings'): print ('string')
