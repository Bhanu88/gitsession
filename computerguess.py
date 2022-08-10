import random
import pyinputplus as pyip

def comguess(x):
    low = 1
    high = x
    feedback =''
    while feedback != 'correct':
        if low != high:
            guess = random.randint(low,high)
        else: 
            guess =low    
        print(f'The guess is {guess}')
        feedback = pyip.inputMenu(['low', 'high', 'correct'])
        if feedback == 'high':
            high= guess - 1
        elif feedback == 'low':
            low = guess + 1 
    print(f'you guessed the number correctly {guess}')

comguess(200)

