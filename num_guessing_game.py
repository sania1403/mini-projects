# get guess
import random
def get_guess():
    return input("What is your guess ")
# generate coputer code

def generate_code():
    digits=[str(num) for num in range(10)]

    #shuffle the digits
    random.shuffle(digits)
    #then grab the first three
    return digits[:3]

# generate the clues

def generate_clues(code,user_guess):

    if user_guess==code:
        return "CODE CRACKED!"
    
    clues=[]

    
    for ind,num in enumerate(user_guess):
        if num==code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    if clues ==[]:
        return ["Nope"]
    else:
        return clues


# run game logic  
print("Welcome code breaker!")

secret_code=generate_code()

clue_report=[]

while clue_report!="CODE  CRACKED!":
    guess=get_guess()
    clue_report=generate_clues(guess,secret_code)
    print("here is the result if your guess: ")
    for clue in clue_report:
        print(clue)