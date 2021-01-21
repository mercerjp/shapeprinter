# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:40:35 2021

@author: James
"""

def stPrinter(n, shape, character, filled, fillCharacter= '*'):
    if shape == 0 and filled == True: #define filled square
        print(str(character)*n) #top of square length print
        for i in range(0, n-2): #middle of square (n-2 because accounting for either side)
            print(str(character)+str(fillCharacter)*(n-2)+str(character)) #fill middle, starting and ending with the characters
        print(str(character)*n) #bottom line
    elif shape == 0 and filled == False: #empty square
        print(str(character)*n) #top square line
        for i in range(0, n-2): #middle of the square
            print(str(character)+" "*(n-2)+str(character)) #fill middle with space, start and end with character
        print(str(character)*n)
        
    elif shape == 1 and filled == True: #filled triangle
        for i in range(n): #for every row
            for j in range(n): #and every column
                if j == 0 or i == (n-1) or i==j: #define the coordinates of the right angle we want to draw
                    print(str(character), end="") #print what we want, end to stop
                elif i == 0 or j == (n-1) or j>i: #prevent outside of triangle being filled
                    print(" ", end="")
                else:
                    print(end=str(fillCharacter)) #everywhere else, fill with character
            print()
    elif shape == 1 and filled == False: #empty triangle
        for i in range(n): #for every row
            for j in range(n): #and every column
                if j == 0 or i == (n-1) or i==j: #define the coordinates we want to draw
                    print(str(character), end="") #print what we want
                else: #everywhere else
                    print(end=" ") #fill with blank space, doesn't matter if its outside the triangle either
            print()

stPrinter(30, 1, "J", True, "M")

