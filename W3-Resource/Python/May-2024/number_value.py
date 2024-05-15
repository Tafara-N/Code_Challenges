#!/usr/bin/env python3

# Program that accepts an integer (n) and computes the value of n+nn+nnn

n = int(input("Enter a number : "))

n = int(f"{n}")
n2 = int(f"{n}{n}")
n3 = int(f"{n}{n}{n}")

print("Expected Result : ", n + n2 + n3)
