#!/usr/bin/env python3

import sys
def main () :
      params = len(sys.argv)

      if (params < 2) :
            print(None)
      else :
            first = int(sys.argv[1])
            sec = int(sys.argv[2])
            result = [i for i in range(first, sec + 1)]

            print(result)
if __name__ == "__main__" :
      main()