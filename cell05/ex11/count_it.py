#!/usr/bin/env python3

import sys
import re

def main () :
      params = len(sys.argv)
      if (params < 2) :
            print(None)
      else :
            params_arr = sys.argv[1::]
            print(f"parameters: {len(params_arr)}")
            for v in params_arr :
                  print(f"{v}: {len(v)}")
if __name__ == "__main__" :
      main()