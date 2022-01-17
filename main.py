# Matrix-Style "Raining Code" screen saver written with python for use on the command line
# Created by Brenton O'Brien, https://github.com/brenton-obrien

import shutil, random, time, sys, os

width = shutil.get_terminal_size()[0] - 1  # Gets the width of terminal window, -1 is used to prevent potential windows bug
row = [0] * width  # Creates a list of zeros which match the width of the terminal screen (this is used in the backend of the program)
printed_row = []  # This is what the user will see printed on the screen, it copies from the 'row list' and formats it to look more like the matrix code

density = 0.007  # How often new streams of characters appear
min_stream_length = 6  # Minimum length for a stream of characters
max_stream_length = 35  # Maximum length for a stream of characters
delay = 0.1  # Time delay inbetween each new line being printed

# List of all the symbols used in the raining code, symbols will be selected at random
symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMабвгдежзиклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
          'αβγδεζηθικλμνξοπρστυφχψωςΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ12345678901234567890-=*_+|:<>"-=*_+|:<>"-=*_+|:<>"-=*_+|:<>"1234567890'

# Allows text to be printed as though it is being typed real time, you input your string and then the speed which you want it to be typed
def print_slow(string, speed):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)


# Title sequence which shows creator and basic instructions
print_slow("Matrix-Style 'Raining Code' screen saver written with python for use on the command line\n"
           "Created by Brenton O'Brien, https://github.com/brenton-obrien\n\nFor best results change the cmd font colour to green", 0.05)
input('Press <Enter> to begin.')  # This pauses the program so that the user can read the above, they must hit enter to continue

os.system('cls')  # Clears the title and instructions

# INTRODUCTION SEQUENCE (this sequence mimics the text at the beginning of the movie)
print_slow('Call trans opt: received. 2-19-98 13:24:18 REC:Log>', 0.05)  # Types out the messages
time.sleep(2)  # Pauses to allow the user to read the message
os.system('cls')  # clears the terminal for the next message

print_slow('Trace program: running', 0.05)
time.sleep(2)
os.system('cls')

print_slow('Wake up, Neo', 0.1)
time.sleep(0.01)
print_slow('...', 0.5)  # Separating the print_slow() statements allows the period ... to be printed slower than the text (just like the movie)
time.sleep(2)
os.system('cls')

print_slow('The Matrix has you', 0.1)
time.sleep(0.01)
print_slow('...', 0.5)
time.sleep(2)
os.system('cls')

print_slow('Follow the white rabbit.', 0.05)
time.sleep(2)
os.system('cls')
print_slow('Knock, knock, Neo.', 0.05)
time.sleep(2)
os.system('cls')


# Main program loop
while True:
    printed_row = []  # Resets the printed row each iteration of the loop

    for i in range(width):  # Creates a for loop which runs for each '0' in the 'row list'
        if row[i] == 0:  # For every zero that the for loop loops over, there is a chance that it can be change into a random interger between min and max stream length
            if random.random() <= density:  # Density is a variable that can alter how often the zeros change into a different number
                row[i] = random.randint(min_stream_length, max_stream_length)
                printed_row.append(random.choice(symbols))  # Adds a random symbol to the printed row list while row[i] is not equal to zero

            else:
                printed_row.append(' ')  # If the chance is unsuccessful then just append an empty space instead of a zero

        elif row[i] > 0:  # If the number in 'row list' is larger than zero, append another symbol to the list, then minus 1 from the row list value
            row[i] -= 1
            printed_row.append(random.choice(symbols))

    time.sleep(delay)  # Sets the delay between printing each line

    print(''.join(printed_row))  # Joins all the spaces and symbols created from this loop into one long string which is then printed to the screen,
                                 # Before being reset on the next loop
