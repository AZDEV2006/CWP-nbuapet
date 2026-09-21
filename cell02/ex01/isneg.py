#!/usr/bin/env python3

def main() :
      try :
            num = float(input())

            if (num >= 0) :
                  print("This number is positive.")
            else :
                  print("This number is negative.")
      except ValueError :
            pass

if __name__ == '__main__' :
      main()