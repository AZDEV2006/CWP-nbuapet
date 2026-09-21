#!/usr/bin/env python3

def main () :
      n = 10
      i = 0
      j = 0

      while i <= 10 :
            row = f"Table de : {i}:"
            j = 0
            while j <= 10 :
                  row += f" {i * j}"
                  j = j + 1
            print(row)
            i += 1

if __name__ == "__main__" :
      main()