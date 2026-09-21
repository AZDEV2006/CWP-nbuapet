#!/usr/bin/env python3

import sys
import re

def main () :
      params = len(sys.argv)

      if (params < 2) :
            print(None)
      else :
            init = sys.argv[1]
            inp = input("What was the parameter? ")

            if inp == init :
                  print("Good job!")
            else :
                  print("Nope, sorry...")
if __name__ == "__main__" :
      main()