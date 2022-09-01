import random

count = 0

def rock_paper_scissors():
    global count
    print('------>Welcome and may the force be with you<------')
    Times_to_run = int(input("How many times do you want to play r->p->s(e.g 5): "))
    Won = 0
    Lost = 0 
    Tied = 0
    
    while count < Times_to_run:
        computer = random.choice(['r','p','s'])
        user = input('r:rock p:paper s:scissors: ')
        if whowon(user,computer) == 'tie':
            print("you tied")
            Tied += 1
        if whowon(user,computer) and whowon(user,computer) != 'tie':
            Won += 1
            print("you won")
        elif whowon(user,computer) == False:
            Lost += 1
            print("you lost")
        count = count + 1
    print(f"won => {Won} ,tied => {Tied} ,lost => {Lost}")
    
def whowon(u,c):
    if (u == 'r' and c == 'r') or (u == 'p' and c == 'p') or u == 's' and c == 's':
        return "tie"  
    if (u == 'r' and c == 's') or (u == 'p' and c == 'r') or u == 's' and c == 'p':
        return True
    return False  

rock_paper_scissors()

# by olaoluwa
    


