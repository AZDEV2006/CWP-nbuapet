#!/usr/bin/env python3

def main () :
      numeric = int(input("Enter a number\n"))

      for i in range (10) :
            print(f"{i} x {numeric} = {i * numeric}")

if __name__ == "__main__" :
      main()