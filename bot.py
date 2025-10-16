import sys

from instagrapi import Client
import configparser
import getpass
import time
import random

def two_factor_auth_callback():
    return input("Enter the 2FA code: ")

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    cl = Client()
    try:
        cl.login(config['credentials']['username'], config['credentials']['password'])
    except Exception as e:
        error_string = str(e).lower()
        if "challenge" in error_string or "two-factor" in error_string:
            print("Waiting for approval")
            for i in range(60):
                time.sleep(5)
                try:
                    cl.login(config['credentials']['username'], config['credentials']['password'])
                    break
                finally:
                    break
            else:
                sys.exit(1)
        else:
            sys.exit(1)

main()