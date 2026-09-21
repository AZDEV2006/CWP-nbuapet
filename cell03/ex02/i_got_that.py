#!/usr/bin/env python3

def main () :
      inp = input("What you gotta say? : ").strip()

      while True :
            inp2 = input("I got that! Anything else? : ").strip()

            if (inp2 == "STOP"):
                  break
            else :
                  pass
if __name__ == "__main__" :
      main()