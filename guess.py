import random
import pyinputplus as pyip

def guess(x):
    number=random.randint(1,x)
    print(number)
    guess = 0
    while guess != number:
        guess = pyip.inputInt('Enter num: ', max=x)
        
        if guess > number :
            print(f"Too High !")
        elif guess < number : 
            print(f"Too Low !")
    print(f"you guessed the correct number {number}")           

guess(30)