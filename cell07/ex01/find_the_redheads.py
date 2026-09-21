#!/usr/bin/env python3

def find_the_redheads (dupont_family) :
      return [key for key, value in dupont_family.items() if value == "red"]

dupont_family = {
      "florian": "red",
      "marie": "blond",
      "virginie": "brunette",
      "david": "red",
      "franck": "red"
}
print(find_the_redheads(dupont_family))