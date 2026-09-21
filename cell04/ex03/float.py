#!/usr/bin/env python3

def main () :
      try :
            inp = input("Give me a number: ")
            toFloat = float(inp)

            if toFloat.is_integer() :
                  print("This number is an integer.")
            else :
                  print("This number is a decimal.")

      except ValueError:
            pass

if __name__ == "__main__" :
      main()