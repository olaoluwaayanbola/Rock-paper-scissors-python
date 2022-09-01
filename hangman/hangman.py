import random
import string
from words import words

def get_word():
    index = random.randint(0,len(words))  
    word = words[index] 
    while '-' in words[index] or " " in words[index] :
        word = words[index] 
    return words[index].upper() 

def diagrams(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 1): 
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif(wrong == 5):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(wrong == 6):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("   ===")
Attempts = 0
def hangman():
    global Attempts
    valid_words = get_word()
    letters = set(valid_words)
    guessed_letters = set()
    alphabet_in_english = set(string.ascii_uppercase)
    alphabet_in_english.add('HINT')
    
    while len(letters) > 0:
        if Attempts <= 7:
            print('you have used these letters','=> ',''.join(guessed_letters))
            print(f'Number of Attempts {Attempts}')
            user_input = str(input('Guess a letter: ').upper())
            
            # Hidden feature 
            if user_input == 'HINT':
                hint = random.choice(valid_words)
                print(f'{hint} is in the word')
            
            if user_input in alphabet_in_english - guessed_letters:
                guessed_letters.add(user_input)
                if user_input in letters:
                    letters.remove(user_input)   
            elif user_input in guessed_letters:
                print(f'letter{user_input} has been used') 
            elif user_input in guessed_letters:
                print(f'Hint has been used')  
            else:
                print(f'{user_input} is not a valid input!!')
                
            diagrams(Attempts)
            word_list = [letter if letter in guessed_letters else '_' for letter in valid_words]
            print("".join(word_list))
            Attempts = Attempts + 1
            
        if Attempts >= 7:
            word_return = f'The word was {valid_words}' 
            print(word_return)
            return
        
hangman()

###### By olaoluwa ######
    