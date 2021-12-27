#Today we learn how to experiment with randomness!
#Randomness is important in a lot of games!
#Who doesn't love the cosmic dice!

#Let's look at my code. This one is a game of Minecraft!

import random
ore = ['diamonds','emeralds','gold','iron']
enemy = ['zombie','skeleton','creeper','villager'] 
print(f'you went mining and got {random.randint(2,25)} {random.choice(ore)}.')
print(f'you hit a {random.choice(enemy)} and dealed {random.randint(1,100)} damage.')

#Let me explain it!
#First we import the random module!

#Then we make a 2d list.
#A 2d list are made like this:
#cheese = ['parmesan','gouda']

#then we make an f string.
#which is like a regular string ('')
#but is written like (f'')

#then we do the randomizations.
#{random.randint(13,37)} would cause Python to print a random number between 13 and 37.
#{random.choice(cheese)} would cause Python to print either parmesan or gouda.

#That wasn't too hard, wasn't it?
#Fun fact: randomness isn't random.
#And it never was.
#Dice were never truly random, neither was the RNG.
