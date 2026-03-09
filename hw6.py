"""
Homework 6
"""


def replace():
    """Changes symbol # to / in strings."""
    url = 'www.my_site.com#about'
    print(url.replace("#", "/"))


def ing():
    """Adds -ing to words."""
    word = input("Enter your word: ")
    print(word + 'ing')


def name_switch():
    """Switches places of name and surname."""
    name = 'Ivanou Ivan'
    arr = name.split()
    arr_inverted = (arr[1], arr[0])
    print(' '.join(arr_inverted))


def remove_spaces():
    """Removes spaces before and after the user's input."""
    text = input("Enter some text with spaces: ")
    print(text.strip())


def capitalize():
    """Capitalizing the word."""
    proper_name = 'pARiS'
    print(proper_name.capitalize())


def split_string():
    """Splits strings into words."""
    str1 = 'Robin Singh'
    print(str1.split())
    str2 = 'I love arrays they are my favorite'
    print(str2.split())


def welcome_message():
    """Prints welcome message."""
    arr = ['Robin', 'Singh']
    str1 = 'Welcome'
    str2 = 'airport'
    print(f"Hello, {' '.join(arr)}! {str1} to {str2}")


def arr_to_string():
    """Converts a list to string."""
    arr = ["I", "love", "arrays", "they", "are", "my", "favorite"]
    print(" ".join(arr))


def list_formatting():
    """Formats the 3rd symbol of the user's input, and deletes the user's symbol of index [6]"""
    users_list = input('Enter 10 characters separated by spaces: ').strip().split()
    users_list[2] = input('Enter new value for the 3rd character: ').strip()
    del users_list[6]
    print(users_list)

replace()
ing()
name_switch()
remove_spaces()
capitalize()
split_string()
welcome_message()
arr_to_string()
list_formatting()
