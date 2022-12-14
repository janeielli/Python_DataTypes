# -*- coding: utf-8- -*-

import math

def general_formula(a, b, c):
    determinant = b**2 - 4*a*c

    if(determinant >= 0):
        sol1 = (-b + math.sqrt(determinant))/2*a
        sol2 = (-b - math.sqrt(determinant))/2*a
        print("The solution has two real solutions {0:.3} and {1:.3} \n".format(sol1, sol2))
    else:
        print("The equation has non real solution \n")

if __name__== "__main__":   
    answer_quest = "yes"
    while(answer_quest == "yes"):

        a, b, c = input("Please type the coefficients of the quadratic equation:").split()
        a = float(a)
        b = float(b)
        c = float(c)
        general_formula(a, b, c)

        
        answer_quest = input("\nDo you want to keep using the application? ") 