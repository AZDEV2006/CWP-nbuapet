#!/usr/bin/env python3

def main () :
      try :
            first = int(input("Give me the first number : "))
            sec = int(input("Give me the second number : "))
            print("Thank you!")
            print(f"{first} + {sec} = {first+sec}")
            print(f"{first} - {sec} = {first-sec}")
            print(f"{first} / {sec} = {first/sec}")
            print(f"{first} * {sec} = {first*sec}")
      except ValueError :
            pass
if __name__ == "__main__" :
      main()