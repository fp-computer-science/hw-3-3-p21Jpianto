# Author: JAP (amdg) 10/1/20

r = input("Radius of cylinder")
h = input("Height of cylinder")

r = int(r)
h = int(h)

π = 3.14159265359

volume = π * (r) ** 2 * h

s_a = 2 * π * r * (h + r)

print(volume, s_a)
