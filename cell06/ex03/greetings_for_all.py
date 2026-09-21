#!/usr/bin/env python3
import sys

def greetings (params: str | int ="noble stranger") :
      if str(params).isnumeric() :
            print("Error! It was not a name.")
      else :
            print(f"Hello, {params}")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)