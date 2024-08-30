

reference_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "w","y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "w","y", "z"]

def encode(text, cypher_number, list_of_letters):
    if cypher_number > 26:
        cypher_number = cypher_number % 26

    #creating a encoded_text using for loop and saving it in a variable

    encoded_text = ""

    for i in text:
        index_i = reference_list.index(i)
        encoded_text += reference_list[index_i + cypher_number]

    print(encoded_text)
    return encoded_text


def decode(text, cypher_number, list_of_letters):
    if cypher_number > 26:
        cypher_number = cypher_number % 26

    decoded_text = ""

    for i in text:
        index_i = reference_list.index(i) + 26
        decoded_text += reference_list[index_i - cypher_number]

    print(decoded_text)
    return decoded_text



while True:
    chosen_func = input("Choose decode or encode").lower()

    word = input("Enter You Text: ")
    number = int(input("Input Your Cypher Number: "))

    if chosen_func == "encode":
        encode(word, number, reference_list)
    elif chosen_func == 'decode':
        decode(word, number, reference_list)
    else :
        print("Input error, restarting.")
        continue

    start_again = input("Would you like to use the program again? y/n").lower()
    if start_again == 'y':
        continue
    else:
        print("Thank you for using the program.")
        break

