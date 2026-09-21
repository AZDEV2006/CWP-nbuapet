#!/usr/bin/env python3

def add_one(param):
    param += 1


if __name__ == "__main__":
    my_var = 42
    print(f"Before add_one: {my_var}")
    add_one(my_var)
    print(f"After add_one: {my_var}")