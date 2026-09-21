#!/usr/bin/env python3

def main () :
      my_array = [2, 8, 9, 48, 8, 22, -12, 2]
      sum = [x+2 for x in my_array if x > 5]
      print(sum)

if __name__ == "__main__" :
      main()