# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:11:05 2020

@author: Sophia
"""

import pandas as pd


def menu():
    choice = -1
    while choice not in (0,1,2,3,4,5,6,7,8,9):
        choice = int(input('''
1. Get Movie Rating Based on Title
2. Get Movie Plot Summary 
3. Get Movie Box Office Statistics 
4. Movie Recs (KNN)
5. Get N Top Movies 
6. Get Random Movies 
7. Get Movies by Genre
8. Get Top N Cast Members
9. Get Movie Poster
0. Quit

Please select a choice from the number options above: ''').strip())
        if choice not in (0,1,2,3,4,5,6):
            print("\nOption not valid! Please select a valid option (0-6).")
    return choice

def main ():
    choice = -1
    while choice != 0:
        choice = menu()
        if choice == 1:
            print()
        elif choice == 2:
            print ()
        elif choice == 3:
            print()
        elif choice == 4:
            print()
        elif choice == 5:
            print()
        elif choice == 6:
            print() # have to figure out how to do a replace printy loop thing
        elif choice == 7:
            print()
        elif choice == 8:
            print()
        elif choice == 9:
            print()
    return ''

if __name__=='__main__':
    main()
