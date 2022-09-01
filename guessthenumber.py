import random

def guess_the_number(marg):  
    hold = random.randint(1,marg)
    val = 0 
    while val != hold:
        val = int(input(f"the random number is between 1 and {marg}: "))
        if val > hold:
            print("too high")
        elif val < hold:
            print("too low")         
    print(f'Correct!! the number was {val}')  
value = 10
def Computer_guess(val):
    low = 1
    high = val
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = high
        feedback = input(f'is {guess} too high ?h or too low l or correct c ? ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print('correct i am the man')
    
# Computer_guess(10)
# guess_the_number(20)
