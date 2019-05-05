

#
# Name: Yuta Kihara
#
# Program Description, Interfaces, and Functionality
# We will write two functions. The first will be called print opposite case (sentence)
# that accepts one formal parameter sentence and prints a string with all the original
# upper case characters changed to lower-case and the original lower-case characters
# to upper-case. The second function we will write is called get changed case(ch) that
# accepts a single character ch and returns the opposite case of the character.



def print_opposite_case(str):
    newstr = []        # char storage list after changing each case
    for char in list(str):
        newstr.append(get_changed_case(char)) # appending each char into the storage

    print(''.join(newstr)) # join the char list to make one sentence



def get_changed_case(char):
    if 97 <= ord(char) <= 122: # the range of lower case (ASCII)
        return chr(ord(char) - 32)
    elif 65 <= ord(char) <= 90: # the range of upper case (ASCII)
        return chr(ord(char) + 32)
    else:
        return char



while True:
    s = input("Enter a string to convert case to upper or lower \ (press ’q’ to exit):\n")
    if (s == 'q'):
        break

    print_opposite_case(s)
    print("\n")
print("Goodbye")
