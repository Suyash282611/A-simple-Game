import random as r
import time
A=list()
print('\t\tWELCOME TO THE GAME\t\t')
time.sleep(7)
n=int(input('Enter the number of players:'))
for i in range (0,n):
    name=input('Enter the name:')
    A.append(name)
r.shuffle(A)
print('The game is really simple, all the names of the players that have been entered have been shuffled\nAny 1 of them would be selected eho have to do the desired tasks that have been set up by us which would also be shuffled.')
b=['DANCE','SING A SONG','DO A BACKFLIP','Jump 5 times','DO A CARTWHEEL','SAY A TONGUE TWISTER','TELL A JOKE','DO A HANDSTAND','ACT LIKE A COW','MAKE A FUNNY FACE']
r.shuffle(b)
time.sleep(2)
print('The person selected is',A[0])
time.sleep(3)
print('-'*50)
print('The task is to',b[0])
