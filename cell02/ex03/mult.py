#!/usr/bin/env python3

def main () :
      try :
            first_n = int(input("Enter the first number: \n").strip())
            sec_n = int(input("Enter the second number: \n").strip())

            multi = first_n * sec_n

            print(f"{first_n} X {sec_n} = {multi}")

            if (multi >= 0) :
                  print("This result is positive.\n")
            else :
                  print("This result is negative.\n")
            
      except ValueError :
            pass

if __name__ == "__main__" :
      main() 