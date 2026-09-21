#!/usr/bin/env python3

def main () :
      try :
            word = str(input("Give me a word : "))
            print(word.upper())
      except ValueError :
            pass

if __name__ == "__main__" :
      main()