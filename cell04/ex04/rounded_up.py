#!/usr/bin/env python3
import math

def main () :
      try :
            inp = float(input("Give me a number: "))

            print(math.ceil(inp))
      except ValueError:
            pass

if __name__ == "__main__" :
      main()