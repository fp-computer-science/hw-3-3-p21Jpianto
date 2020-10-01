# Author: JAP (amdg) 10/1/20

a = 1
b = 2
c = 3

f_throw = input("How many free throws?")
i_throw = input("How many 2 pointers?")
o_throw = input("How many 3 pointers?")

f_throw = int(f_throw)
i_throw = int(i_throw)
o_throw = int(o_throw)

one_pts = (f_throw * a)
two_pts = (i_throw * b)
three_pts = (o_throw * c)

total_points = one_pts + two_pts + three_pts

print("The player score" + (" ") + str(total_points) + (" ") + "points in the game")
