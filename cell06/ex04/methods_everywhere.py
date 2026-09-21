#!/usr/bin/env python3
import sys

def shrink (param) :
      return print(param[0:8:1])

def enlarge (param) :
      while len(param) < 8 :
            param += "Z"

      return print(param)

if len(sys.argv) < 2 :
      print("none")
else :
      for i in sys.argv[::1] :
            if len(i) < 8 :
                  enlarge(i)
            else :
                  shrink(i)