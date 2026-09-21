#!/usr/bin/env python3

import sys
import re

def main () :
      params = len(sys.argv)

      if (params < 2) :
            print(None)
      else :
            find = 'z'
            senten = sys.argv[1]
            findAll = re.findall(find, senten, flags=0)
            if len(findAll) != 0 :
                  print("".join(findAll))
            else :
                  print(None)
if __name__ == "__main__" :
      main()