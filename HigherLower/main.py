from art import logo, vs
from gamedata import data
import random

print(logo)

def get_celebrity():
    return random.choice(data)

def Play_game():
    score = 0
    a = get_celebrity()
    user_invincible = True
    streak = 0

    while user_invincible:
        while True:
            b = get_celebrity()
            if b != a:
                break


        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

        user_choice = input("who has more followers? Type 'A' or 'B' ").capitalize()

        if compare_followers(a, b, user_choice):  
            score += 1
            streak += 1
            print(f"You're right! current score {score}.")
        else:
            print(f"Sorry, thats wrong. Final score: {score}")    
            user_invincible = False
        
        if streak == 2:
            # Reset consecutive correct count and change celeb A
            streak = 0
            a = b
        else:
            # Keep celeb A for the next round
            a = b

def compare_followers(first_celeb, second_celeb, guess):
    if guess == 'A':
        return first_celeb['follower_count'] > second_celeb['follower_count']
    else:
        return second_celeb['follower_count'] > first_celeb['follower_count']
        

    


# while True:
Play_game()
    # print("Thanks for playing! Goodbye! 👋")
    # break