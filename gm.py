import time #Doing this from some SO answer, beacuse I want to pause my script.

# Setting up the story.
print (""" Let me tell you a story.

Do you want to hear about

1. A gist from one of the chapters of the 11th century treatise
“Liber Abaci”
or
2. A story about the Golden Mean?
""")

user_choice = input("Pick 1 or 2 > ")

while True:
    if user_choice == '1':
        print("\nSucker! It’s the same story. :) ")
        input("\nPress the Enter/Return key to go back in time! > ")
        break
    elif user_choice == '2':
        break
    else:
        user_choice = input('Pick 1 or 2? >')


# Explaining the concept, with data and a small demo
print ('*'*80)
print ("\n""""Liber Abaci (1202, also spelled as Liber Abbaci) is a historic
book on arithmetic by Leonardo of Pisa""")
time.sleep(1.5)
print ("also known as Fibonacci!")
time.sleep(1.5)
print ("""Another example in this chapter, describing the growth of a population of
rabbits, was the origin of the Fibonacci sequence for which the author is most
famous today.""")
time.sleep(1.5)
print ('*'*80)
input("Press the Enter/Return key to continue")
print ('*'*80)
print("\n""""You know Fibonacci numbers""")
time.sleep(1.5)
print("""while there are lots of other numbers that can be summed in a series,
only the Fibonacci series, (i.e the sequence that starts with 0 & 1) approaches
what we call the Golden Ratio (symbolised \u03C6 or phi)""")
time.sleep(1.5)
print("""So just what is the Golden Ratio?""")
time.sleep(1.5)
print("""The golden ratio is a special number approximately equal to
1.6180339887498948482. """)
time.sleep(1.5)
print("""or more accurately,  1 + sqrt\{5}
                     ------------
                           2""")
time.sleep(1.5)
print("""To illustrate:
-----------------------------------
A            B                    C

The ratio of the long segment (BC) to the short segment (AC) is the *same* as
the ratio of the total segment (AC) to the long segment (BC)
""")
print ('*'*80)
input("Press the Enter/Return key to continue")

print("""
Let’s do this to actually get it""")

get_1 = int(input("Give me a 1: "))
while True:
    if get_1 == 1:
        break
    else:
        get_1 = int(input("Give me a 1: "))

get_2 = int(input("Give me a 2: "))
while True:
    if get_2 == 2:
        break
    else:
        get_2 = int(input("Give me a 2: "))

get_3 = int(input(f"""Adding {get_1} & {get_2} would get you? : """))
while True:
    if get_3 == 3:
        break
    else:
        get_3 = int(input("Give me the sum of 1+2: "))

get_5 = int(input(f"""Add that to {get_2} would get you? : """))
while True:
    if get_5 == 5:
        break
    else:
        get_5 = int(input("Give me the sum of 3+2: "))

print ("""Let’s fast forward this a bit """)
time.sleep(1.5)
num_1, num_2 = get_3, get_5
while num_2 < 150:
    print(num_2, end=' ')
    num_1, num_2 = num_2, num_1 + num_2

print ("""and so on and so forth…

""")
print ('*'*80)
input("Press the Enter/Return key to continue")

# Conclusion - Telling the user about the golden mean across domains

print("""
Let’s see this across domains …""")
print("What do you want to know about? : ")
domain=input("name, place, animal, thing … or type quit to quit? > ")
while True:

    if domain == "name":
        print ("""

You obviously can’t do names for people, so let’s do music.
An octave is the interval between a note and the next instance of that
same note name on the piano.
An octave spans 13 notes (C,C#,D,D#,E,F,F#,G,G#,A,A#,B,C)
There are 8 normal notes (the *white* keys)
The remaining 5 sharps are arranged in groups of 2 & 3
A C “chord” consists of C, E, & G (3 notes in the 1, 3, & 5 positions)
You’ll find evidence of the Golden Mean, even in compositions

""")
        domain=input("name, place, animal, thing … or type quit to quit? > ")

    if domain == "place":
        print ("""

Speaking of places, let’s go big!
Spiral galaxies follow the familiar Fibonacci pattern.
The Milky Way has several spiral arms (5 actually), each of them a
logarithmic spiral (Our solar system is in one of them, called Orion)
Another galaxy that looks like ours is Messier 74

""")
        domain=input("name, place, animal, thing … or type quit to quit? > ")

    if domain == "animal":
        print ("""

The simplest, most beautiful thing, you could see is a Nautilus shell.
Or the horns on an elephant!
The eyes, beak, wing and key body markings of the penguin all fall
at golden sections of its height.
All the key facial features of the tiger fall at golden sections of the lines
defining the length and width of its face.
The body sections of an ant are defined by the golden sections of its length.
Its leg sections are also golden sections of its length.

""")
        domain=input("name, place, animal, thing … or type quit to quit? > ")

    if domain == "thing":
        print ("""

Let’s stick with nature; specifically flowers and seeds.
The number of petals in a flower consistently follows the Fibonacci sequence.
Famous examples include the lily, which has three petals,
buttercups, which have five,
the chicory’s 21,
the daisy’s 34, and so on.
Phi appears in petals on account of the ideal packing arrangement as selected
by Darwinian processes; each petal is placed at 0.618034 per turn
(out of a 360° circle) allowing for the best possible exposure to sunlight
and other factors.

Similarly Seed heads
Typically, seeds are produced at the center, and then migrate towards
the outside to fill all the space.
Sunflowers provide a great example of these spiraling patterns.

""")
        domain=input("name, place, animal, thing … or type quit to quit? > ")

    elif domain == "quit":
        break

    else:
        domain=input("name, place, animal, thing … or type quit to quit? > ")



print("""



A cosmic constant, the ‘golden ratio’ is found in the shapes of
hurricanes, elephant tusks and even in galaxies.
It truly is Nature’s wonder!

To hear it told even more beautifully, watch this video
https://www.youtube.com/watch?v=O2wU-HT7FiM

Goodbye!


""")
