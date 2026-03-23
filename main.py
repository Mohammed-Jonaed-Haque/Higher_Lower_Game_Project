import random
import game_data
import art


def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f" {account_name},a {account_description}, from {account_country}"


def compare_data(user_guess, person1, person2):
    if person1 > person2:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(art.logo)
game_continue = True
score = 0
b_question = random.choice(game_data.data)


while game_continue:
    a_question = b_question
    b_question = random.choice(game_data.data)


    if a_question == b_question:
        b_question = random.choice(game_data.data)

    print(f"Compare A: {format_data(a_question)}")
    print (art.vs)
    print(f"Compare B: {format_data(b_question)}")


    a_follower_count = a_question['follower_count']
    b_follower_count = b_question['follower_count']



    user_choice = input("Who has more followers? a/b").lower()


    check_answer = compare_data(user_choice, a_follower_count, b_follower_count)


    if check_answer:
        score += 1
        print("\n" * 100)
        print(art.logo)
        print(f"Well done!! Your current score is: {score}")
    else:
        print(f"Wrong answer!! Your current score is: {score}")
        game_continue = False