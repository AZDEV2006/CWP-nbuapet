#!/usr/bin/env python3

def famous_births(data):

      sort = sorted(data.values(), key=lambda figure : int(figure["date_of_birth"]))

      for k in sort :
            print(f"{k['name']} is a great scientist born in {k['date_of_birth']}.")

women_scientists = {
      "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
      "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
      "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
      "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)