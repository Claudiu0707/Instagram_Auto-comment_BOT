from instagrapi import Client
from instagrapi.exceptions import TwoFactorRequired
import configparser
from random import randrange
import time

def main():
    #Create a new configparser object to read from the config.ini file containing the user credentials and post information
    config = configparser.ConfigParser()
    config.read('config.ini')

    username = config['credentials']['username']
    password = config['credentials']['password']
    #Create a new client
    cl = Client()

    #Account login
    #Note: 2FA not working
    try:
        cl.login(username, password)
        print("Login Successful")
    except TwoFactorRequired as e:
        code = input("Please enter your two-factor code: ")
        cl.login(username, password, verification_code=code)
        print("Login Successful")


    post_url = config['post_info']['post_link']
    post_comment = config['post_info']['post_comment']

    #Post 30 comments with random intervals of time between comments
    #Take a break for about 2.5 -> 3 minutes
    #Repeat for 6000 times
    for j in range(6000):
        for i in range(30):
            media_id = cl.media_pk_from_url(post_url)
            cl.media_comment(media_id, post_comment)
            pause_time = randrange(1, 6)
            time.sleep(pause_time)
        wait_time = randrange(150, 180)
        time.sleep(wait_time)

if __name__ == "__main__":
    main()