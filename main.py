from datetime import datetime
from time import sleep
from os import system
from playsound import playsound


def get_x():
    while True:
        x = int(input('How long after do you want the your pc to shut down? :'))
        if x <= 0: #checking is there any negative input or zero
            print('If you want to shut down your pc now do it with manuel :D')
        else:
            break
    return x


def main():
    while True:
        try: 
             x = get_x()
        except ValueError: # checking is x an integer
            print("Please enter an integer.")
        else:
            get_date_n_print(x)
            playsound("goodnight.mp3") #You can create your goodnight message with createmessage.py.
            start_timer(x)
            break



def start_timer(x): #the function who makes starts timer for shutting down and then shuts down your pc
    timer = x * (60 * 60)
    sleep(timer)
    print("Your pc will shutdown in 30seconds. Good night.")
    sleep(30)
    system("shutdown /s")


def get_date_n_print(x):
    now = datetime.now()
    h = now.hour
    d = now.minute
    hp = x + h
    if hp > 24:
        hp = hp-24
    print(f"Your pc will shutdown at {int(hp)}  {int(d)}. Good night :) ")


if __name__ == "__main__":
    main()
