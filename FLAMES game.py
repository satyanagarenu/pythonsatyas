import random

def play_hangman():
    word_list = ["python", "javascript", "computer", "programming", "algorithm"]
    word = random.choice(word_list)
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    word_guessed = set()
    tries = 6
    print("Let's play Hangman!")
    while len(word_letters) > 0 and tries > 0:
        print("You have", tries, "tries left.")
        print("Used letters:", " ".join(used_letters))
        print("Word:", " ".join(letter if letter in word_guessed else "_" for letter in word))
        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_guessed.add(user_letter)
                word_letters.remove(user_letter)
            else:
                tries -= 1
        else:
            print("You have already used that letter. Try again.")
    if len(word_letters) == 0:
        print("Congratulations! You guessed the word", word, "!")
    else:
        print("Sorry, you ran out of tries. The word was", word + ".")

play_hangman()'''



'''name1 = input('Enter your name: ')
name2 = input('Enter your name: ')

name1 = list(name1.lower())
name2 = list(name2.lower())

for l in name1:
    if l in name2:
        idx = name1.index(l)
        name1[idx] = '_'
        idx = name2.index(l)
        name2[idx] = '_'
print(name1)
print(name2)

name3 = name1+name2
count = 0
for i in name3:
    if (i != '_' and i != " "):
        count += 1
print(count)
f = list('FLAMES')
index = 0
while len(f) > 1:  
    for j in range(count):
        index += 1
        if index > len(f):
            index = 1
    f.remove(f[index-1])
    index -= 1
print(f)'''


'''import random

print('Welcome to the Game!')

dice = [1,2,3,4,5,6]


rules = "The rules of the game are: \n1. The game has to be started if the number on the dice when rolled is 1 or 6. \n2. The positions of the snakes are: [11,13,17,25,36,53,62,79,87,95] \n3. The positions of the ladders are: [6,18,27,48,57,69,78,84] \n3. The player who reaches the position 100 will win."
print(rules)

snakes =  [11,13,17,25,36,53,62,79,87,95]
ladders = [6,18,27,48,57,69,78,84]

position1 = 0
position2 = 0

while True:
    a = random.choice(dice)
    if position1 == 0:
        player1 = input("Player - 1, enter 'roll' to roll the dice: ").lower()
        if player1 == 'roll':
            print("The dice is rolled.")
            print("The number is: ",a)
            if a == 1 or a == 6:
                print("Congratulations, you can start your game.")
                print("Player - 1 position is: 1")
                position1 = 1
                a = random.choice(dice)
            else:
                print("Better luck next time.")
        else:
            print("The code is incorrect.")
    a = random.choice(dice)
    if position2 == 0:
        player2 = input("Player - 2, enter 'roll' to roll the dice: ")
        if player2 == 'roll':
            print("The dice is rolled.")
            print("The number is: ",a)
            if a == 1 or a == 6:
                print("Congratulations, you can start your game.")
                print("Player - 2 position is: 1")
                position2 = 1
            else:
                print("Better luck next time.")
        else:
            print("The code is incorrect.")
    a = random.choice(dice)
    if position1 >= 1 and position1 <= 100:
        player1 = input("Player - 1, enter 'roll' to roll the dice: ")
        if player1 == 'roll':
            print("The dice is rolled.")
            print("The number is: ",a)
            position1 += a
            if position1 == 11:
                position1 = 4
                print("Snake bit you, player - 1 position is: ",position1)
            elif position1 == 17:
                position1 = 8
                print("Snake bit you, player - 1 position is: ",position1)
            elif position1 == 36:
                position1 = 14
                print("Snake bit you, player - 1 position is: ",position1)
            elif position1 == 53:
                position1 = 34
                print("Snake bit you, player - 1 position is: ",position1)
            elif position1 == 79:
                position1 = 57
                print("Snake bit you, player - 1 position is: ",position1)
            elif position1 == 87: 
                position1 = 38
                print("Snake bit you, player - 1 position is: ",position1)
            elif position1 == 96:
                position1 = 12
                print("Snake bit you, player - 1 position is: ",position1)
            elif position1 == 6:
                position1 = 26
                print("You took ladder, player - 1 position is: ",position1)
            elif position1 == 27:
                position1 = 43
                print("You took ladder, player - 1 position is: ",position1)
            elif position1 == 48:
                position1 = 62
                print("You took ladder, player - 1 position is: ",position1)
            elif position1 == 69:
                position1 = 85
                print("You took ladder, player - 1 position is: ",position1)
            elif position1 == 84:
                position1 = 93
                print("You took ladder, player - 1 position is: ",position1)
            elif position1 > 100:
                position1 = position1 - a
                print("Player - 1 position is: ",position1)
            elif position1 == 100:
                print('Player- 1 position is: 100')
                print("Congratulations player - 1")
                print("You won the match.")
                break
            else:
                print("Player - 1 position is: ",position1)
        else:
            print("The code is invalid.")
    a = random.choice(dice)
    if position2 >= 1 and position2 <= 100:
        player2 = input("Player - 2, enter 'roll' to roll the dice: ")
        if player2 == 'roll':
            print("The dice is rolled.")
            print("The number is: ",a)
            position2 += a
            if position2 == 11:
                position2 = 4
                print("Snake bit you, player - 2 position is: ",position2)
            elif position2 == 17:
                position2 = 8
                print("Snake bit you, player - 2 position is: ",position2)
            elif position2 == 36:
                position2 = 14
                print("Snake bit you, player - 2 position is: ",position2)
            elif position2 == 53:
                position2 = 34
                print("Snake bit you, player - 2 position is: ",position2)
            elif position2 == 79:
                position2 = 57
                print("Snake bit you, player - 2 position is: ",position2)
            elif position2 == 87: 
                position2 = 38
                print("Snake bit you, player - 2 position is: ",position2)
            elif position2 == 96:
                position2 = 12
                print("Snake bit you, player - 2 position is: ",position2)
            elif position2 == 6:
                position2 = 26
                print("You took ladder, player - 2 position is: ",position2)
            elif position2 == 27:
                position2 = 43
                print("You took ladder, player - 2 position is: ",position2)
            elif position2 == 48:
                position2 = 62
                print("You took ladder, player - 2 position is: ",position2)
            elif position2 == 69:
                position2 = 85
                print("You took ladder, player - 2 position is: ",position2)
            elif position2 == 84:
                position2 = 93
                print("You took ladder, player - 2 position is: ",position2)
            elif position2 > 100:
                position2 = position2 - a
                print("Player - 2 position is: ",position2)
            elif position2 == 100:
                print("Player - 2 position is: 100")
                print("Congratulations player - 2")
                print("You won the match.")
                break
            else:
                print("Player - 2 position is: ",position2)
        else:
            print("The code is invalid.")
    
