def replace():
    url = 'www.my_site.com#about'
    print(url.replace("#", "/"))
#replace()

def ing():
    word = input("Enter your word: ")
    print(word + 'ing')
#ing()

def name_switch():
    name = 'Ivanou Ivan'
    arr = name.split( )
    arr_inverted = (arr[1], arr[0])
    print(' '.join(arr_inverted))
name_switch()

def remove_spaces():
    text = input("Enter some text with spaces: ")
    print(text.strip())
remove_spaces()

def capitalize():
    proper_name = 'pARiS'
    print(proper_name.capitalize())
capitalize()

def split_string():
    str1 = 'Robin Singh'
    print(str1.split())
    str2 = 'I love arrays they are my favorite'
    print(str2.split())
split_string()


def welcome_message():
    arr = ['Robin', 'Singh']
    str1 = 'Welcome'
    str2 = 'airport'
    print (f"Hello, {' '.join(arr)}! {str1} to {str2}")
welcome_message()



def arr_to_string():
    arr = ["I", "love", "arrays", "they", "are", "my", "favorite"]
    print(" ".join(arr))
arr_to_string()


def list_formatting():
    list = input(('Enter 10 characters separated by spaces: ').strip()).split()
    list[2] = input('Enter new value for the 3rd character: ').strip()
    del list[6]
    print(list)
list_formatting()