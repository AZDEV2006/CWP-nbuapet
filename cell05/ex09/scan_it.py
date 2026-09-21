#!/usr/bin/env python3

import sys
import re

def main () :
      params = len(sys.argv)

      if (params < 2) :
            print(None)
      else :
            find = sys.argv[1]
            senten = sys.argv[2]
            findAll = re.findall(find, senten, flags=0)
            count = len(findAll)
            
            print(count)
if __name__ == "__main__" :
      main()