#!/usr/bin/env python3

import sys

def main () :
      params = len(sys.argv)

      if (params < 2) :
            print(None)
      else :
            first_params = sys.argv[1]
            
            print(first_params.upper())
if __name__ == "__main__" :
      main()