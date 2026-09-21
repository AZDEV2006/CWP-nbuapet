#!/usr/bin/env python3
import math

def main () :
      try :
            inp = str(input())

            sum_text = ""

            for char in inp :
                  if char.isupper() :
                        sum_text += char.lower()
                  else :
                        sum_text += char.upper()

            print(sum_text)

      except ValueError:
            pass

if __name__ == "__main__" :
      main()