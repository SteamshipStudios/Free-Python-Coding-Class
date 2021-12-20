#This lesson will teach you the basics of printing text!
#Let's look at my code.

zalgo = "zalgo text" 
zalga = "he" 
print(f'{zalga.upper()} COMES') 
print("the text below is called " + zalgo)
print ("z̵̈̉aľ̥͆g̙͛̓o ͈̮̓t͊e͏̪̫x͚̺̫t")
print("If it does not show up,")
print("Don't worry!")
print("Average " + zalgo + " has a ton of strange characters which may not load on some devices!")
print(zalgo + "is named after Zalgo comics.")

#Let me explain it now.

#If I say X = 'dog'
#And then I say print('All ' + X + 's go to heaven')
#In the console it will say: All dogs go to heaven
#The reason it says this instead of 'Alldogs go to heaven'
#Is because we included a space after the all which was recognized by Python and included in the print.
#Also X becomes dog because we said so beforehand with X = 'dog'

#And if I then say to the console: print(f'{X.upper()} IS CUTE')
#The console will say: DOG IS CUTE
#The reason it says this is because we appended an upper.
#Let me give you a diagram because this is pretty complex for Lesson 1.

#(f'
# Beginning of an f string which makes this possible

#{} 
# Helps contain the variable

#X
# Helps tell Python that we're using the variable named X

#.upper
# Optional, tells Python to make it uppercase (.title = Dog) (.lower = dog)

#()
# For some reason this is essential, I'm too dumb to know why.

#Also put '#' before something to make it a comment.
#Now leave, I hope you learned something, I know somebody didn't. I'm looking at you, Hunter.
