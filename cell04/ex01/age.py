#!/usr/bin/env python3

def main () :
      try :
            i = 10
            inp = int(input("Please tell me your age : "))
            print(f"You are currently {inp} years old.")

            while i <= 30 :
                  sum_age = inp + i
                  print(f"In {i} years, you'll be {sum_age} years old.")
                  i = i + 10

      except ValueError:
            pass
if __name__ == "__main__" :
      main()