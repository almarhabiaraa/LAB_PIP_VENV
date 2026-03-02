#Importing the libraries
from art import text2art
from colorama import Fore, Back, Style


# Task1 
print(text2art("BELIEVE AND ACHIEVE", font="block"))
print(text2art("HELLO", font="sub-zero"))



# Bouns 
Text = text2art("python",font='block',chr_ignore=True)
print(Text)

#Colorama
print(Fore.RED + 'i like red color' + Style.RESET_ALL)

print(Back.MAGENTA + 'i like purple background' + Style.RESET_ALL)

print(Style.BRIGHT + 'i like bright texts')

print(Fore.BLUE + Back.YELLOW +'i like python ' + Style.RESET_ALL)

print(Style.BRIGHT + Fore.MAGENTA +'i like magenta and bright text' + Style.RESET_ALL)


