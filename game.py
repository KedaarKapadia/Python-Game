import webbrowser
import random
name = input("What is your name\n")
print(f"Hi, {name}")
mood = input("How is your day so far?\n")
if mood == "Sad" or "sad" or "angry" or "Angry" or "Gloomy" or "gloomy" or "mad" or "Mad":
    mood_angry_res = input("Can I tell you a joke to make your day better?\n")
    if mood_angry_res == "Yes" or "yes" or "YES" or "YES!":
        print("""
        I was wondering
        why the ball kept getting
        bigger and bigger,
        Then it hit me!""")
    else:
        print("Ok, I won't")
        webbrowser.open("https://www.calm.com/?pid=googlesem&af_channel=googlesem&af_c_id=14668023573&af_adset_id=129858268760&af_ad_id=553564592540&af_sub_siteid=&af_keyword=calm&af_sub3=e&af_sub4=Cj0KCQiA9OiPBhCOARIsAI0y71AHzTTH8c7Kl2PxMnJdHZe3edUgaXYjh_PXn9oLAIlEwLGLF0U74soaAr2oEALw_wcB&af_sub5=xx&utm_medium=paid&utm_source=googlesem&utm_campaign=gsa_b2c_us_web_desktop_brand_core_tcpa&utm_content=homepage&utm_term=calm&gclid=Cj0KCQiA9OiPBhCOARIsAI0y71AHzTTH8c7Kl2PxMnJdHZe3edUgaXYjh_PXn9oLAIlEwLGLF0U74soaAr2oEALw_wcB")
        raise SystemExit
elif mood == "Happy" or "happy" or "Awesome" or "AWESOME" or "AWESOME!":
    print("Let's play a game!")
    print("First, Pick a number")
    starting_number = input("Number:\n")
    second_number = random.randint(0, starting_number)
    print(f"Try and guess a number between 1 and {second_number} ")
    guess = input("Guess:\n")
    if guess == second_number:
        if 150 < starting_number:
            print("Correct!! That was just a lucky guess though. ;)\n")
        elif 1000 < starting_number:
            print("There's no way. Your Hacking")
    else:
        print("INCORRECT")
        retry = input("Would you like to try again?\n")
        if retry == "Yes" or "yes" or "y" or "Y":
            guess = input("Guess:\n")
        else:
            raise SystemExit
        

