from datetime import datetime
import random
import secrets
import string

def get_current_time():
    """returns the current date and time"""
    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")


def roll_dice():
    """returns a random integer between 1 and 6"""
    return random.randint(1,6)

def generate_password(length=12):
    """generates a secure random password]"""
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""
    for _ in range(length):
        password += secrets.choice(characters)
    return password

def read_text_files(fileName):
  try:
    with open(fileName,"r") as file:
        content = file.read()
    return content
  except FileNotFoundError:
     return "Error: File not found"