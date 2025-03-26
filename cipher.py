# to get the fancy text
import pyfiglet
# getting to main()
def main():
    # getting the fancy text
    print_large_text("Caesar Cypher")
    # infinite loop to get the mode
    while True:
        # getting the mode
        mode = input('What operation do you want to perform (encrpytion or decryption): ').strip().lower()
        # checking mode
        if mode in ['encryption', 'decryption']:
            break
        else:
            print("There are only two modes available")
            continue
    # getting the key
    while True:
        key = input("Enter the cypher key: ")
        if key.lstrip('-').isdigit() and int(key) < 25:
            key = int(key)
            break
        else:
            print("key can only be a numeric which is not more than 25")
            continue
    # getting the text
    text = input("Enter the text to be cipher: ")
    # cipher text
    cipher = "" 
    # going through the text char by char
    for ch in text:
        if ch.isalpha(): # if char is alpha
            # having a specific set of instruction to run in encryption mode
            ch = cipher_alpha(key, ch, mode)
            cipher = cipher + ch # stored the altered character in new string
        # if char is a numeric
        if ch.isdigit():
            ch = cipher_digi(key, ch, mode)
            cipher = cipher + ch
        # if it's not any alpha numeric character
        if ch.isalnum() == False:
                cipher = cipher + ch
    # printing the cipher and cipher texts
    print(f"The cipher text is \033[32m{cipher}\033[0m")

def print_large_text(text): # taken through AI
    ascii_art = pyfiglet.figlet_format(text, font = 'slant') # figlet_format takes input as a normal text and makes it's ASCII art
    print(ascii_art)

def cipher_alpha(key, ch, mode):
    if key == 0: return ch # if key is zero it messes up the below calculations and i don't want what complication
    if mode == 'encryption': ascii = ord(ch) + key # taking the ascii value
    elif mode == 'decryption': ascii = ord(ch) - key
    if ch.isupper(): # knwoing if the ascii value will lie close the capital words or not
        if ascii not in range(65, 91): # checking if it's in the capital ascii alpha list or not
            if key > 0: ascii = (ascii - 90) + 64 # making the ascii value rotate again in the capiatal alphas list
            elif key < 0: ascii = (ascii + 90) - 64 # for negative key
            return chr(ascii)
        else: # if ascii in 65 to 90 range then just get the rigt char
            return chr(ascii)
    else: # ch is lower
        if ascii not in range(97, 123): # checking if char is close the small case alphas ascii values
            if key > 0: ascii = (ascii + 122) - 96 # getting the right ascii by rotating through the list
            elif key < 0: ascii = (ascii - 122) + 96
            return chr(ascii) # getting the right char
        else:
            return chr(ascii)

def cipher_digi(key, ch, mode):
    if key == 0: return ch # return if key is zero
    if mode == 'encryption': ascii = ord(ch) + key # taking the ascii value
    elif mode == 'decryption': ascii = ord(ch) - key
    if ascii not in range(48, 58):
        if key > 0: ascii = (ascii + 57) - 47 # again rotating it in the ascii list
        elif key < 0: ascii = (ascii - 57) + 47
        return chr(ascii)
    else: 
        return chr(ascii)

if __name__ == "__main__":
    main()
