#!/usr/bin/env python3

import sys
import re

def main () :
      params = len(sys.argv)

      if (params < 2) :
            print(None)
      else :
            params = sys.argv[1::]
            for k in params :
                  if k.endswith("ism") :
                        pass
                  else :
                        print(f"{k}ism")
if __name__ == "__main__" :
      main()