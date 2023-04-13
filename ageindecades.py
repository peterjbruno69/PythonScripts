#!/usr/bin/env python3

age = int(input("What is your age?\n"))

ageindecades = age // 10
years = age % 10

print("You are " + str(ageindecades) + " decades and " + str(years) + " years old.")

