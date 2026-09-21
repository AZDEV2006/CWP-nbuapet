#!/usr/bin/env python3
import sys

def downCase (params) :
      return params.lower()

if (len(sys.argv) < 2) :
      print("none")
else :
      for k in sys.argv[1::] :
            print(downCase(k)) 