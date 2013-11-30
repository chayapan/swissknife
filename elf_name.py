'''
Created on Nov 30, 2013

@author: chayapan
'''
"""
Idea from facebook post: What is Your Elf Name?
https://www.facebook.com/photo.php?fbid=10152116585856264&set=a.10150492721206264.428470.24530951263&type=1&theater

YEAST application scenarios: 
1. A function that yields an Elf name, given a birthday.
        elf_name(birthday="YYYY-MM-DD")

2. A function that gives an Elf name, given a first name, and birth month.
        elf_name(firstname=FIRST_NAME,birth_month=MM)

3. A function that gives random Elf name.
        elf_name()

"""

from time import strptime
import random

# First letter of your first name:
"""
A - Sweetie            N - Cookie
B - Jolly            O - Sparkle
C - Bubbles            P - Cheerful
D - Tootsie            Q - Delightful
E - Joyful            R - Spunky
F - Sugarplum        S - Candy
G - Twinkle         T - Sprinkles
H - Candy            U - Cupcake
I - Merry            V - Perky
J - Flirty            W - Frosty
K - Chipper            X - Precious
L - Angelic            Y - Sunny
M - Happy            Z - Pinky
"""
letter_map = {
    "A":"Sweetie",        "N":"Cookie",
    "B":"Jolly",        "O":"Sparkle",
    "C":"Bubbles",        "P":"Cheerful",
    "D":"Tootsie",        "Q":"Delightful",
    "E":"Joyful",        "R":"Spunky",
    "F":"Sugarplum",    "S":"Candy",
    "G":"Twinkle",        "T":"Sprinkles",
    "H":"Candy",        "U":"Cupcake",
    "I":"Merry",        "V":"Perky",
    "J":"Flirty",        "W":"Frosty",
    "K":"Chipper",        "X":"Precious",
    "L":"Angelic",        "Y":"Sunny",
    "M":"Happy",        "Z":"Pinky"
}


# Your Birth Month:
"""
January - TwinkleToes
Febuary - Sugarplum
March - McJingles
April - SparklePants
May - PeppermintBuns
June - SugarSocks
July - SprinklePants
August - AngleEars
September - SugarBells
October - PointyToes
November - McSprinkles
December - JollyToes
"""
month_map = {                # 1-12
    1:"TwinkleToes",
    2:"Sugarplum",
    3:"McJingles",
    4:"SparklePants",
    5:"PeppermintBuns",
    6:"SugarSocks",
    7:"SprinklePants",
    8:"AngleEars",
    9:"SugarBells",
    10:"PointyToes",
    11:"McSprinkles",
    12:"JollyToes"
}

# YEAST application scenarios: 
# 1. A function that yields an Elf name, given a birthday.
#         elf_name(birthday="YYYY-MM-DD")
# 2. A function that gives an Elf name, given a first name, and birth month.
#        elf_name(firstname=FIRST_NAME,birth_month=MM)
# 3. A function that gives random Elf name.
#        elf_name()

def elf_name_random():
    """ Randomly generate Elf name """
    return letter_map[random.choice(letter_map.keys())] + " " + month_map[random.choice(month_map.keys())]

def elf_name(firstname,birthday):
    """ Given firstname and birthday, return Elf name. 
        firstname =    string A-Z
        birthday  =    string YYYY-MM-DD  """
    birth_month = strptime(birthday,"%Y-%m-%d").tm_mon
    return "%s %s" % (letter_map[firstname[0].upper()], month_map[birth_month])

if __name__ == '__main__':
    print "1. Test - scenario 1 - "
    print elf_name_random()
    print elf_name_random()
    print "1. Test - scenario 2 - "
    print elf_name("Chayapan","1986-03-08")