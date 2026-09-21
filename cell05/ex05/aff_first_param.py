#!/usr/bin/env python3

import sys

def main () :
      params = len(sys.argv)

      if (params < 2) :
            print(None)
      else :
            print(f"{sys.argv[1]}")
if __name__ == "__main__" :
      main()