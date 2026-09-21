#!/usr/bin/env python3

import sys

def main () :
      params = len(sys.argv)

      if (params < 3) :
            print(None)
      else :
            params = sys.argv[1:]

            for i in params[::-1] :
                  print(i)
if __name__ == "__main__" :
      main()