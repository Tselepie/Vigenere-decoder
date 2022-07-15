import re

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z']

def letter_to_number(letter):
    if(letter.isspace()):
        return -1

    j = 0

    while(letter != alphabet[j]):
        j += 1
    
    return j

def decoder(key_number, letter_number):
    if (key_number == -1):
        return letter_number

    return (letter_number-key_number)%26

cmessage = open("EncryptedMessage_2.txt", "r")

i = 0
message = ""
data = cmessage.read()

key = input("Enter keyword: ")
key_to_numbers = []

for letter in key:
    key_to_numbers.append(letter_to_number(letter))

for letter in data:
    message += alphabet[decoder(key_to_numbers[i%len(key)], letter_to_number(letter))]
    i += 1

print(message)

cmessage.close()
