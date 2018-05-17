import time


# source http://www.woojr.com/wp-content/uploads/2010/05/princess-mad-libs.gif

print("Write an adjective")
adjective1 = input()

print("Write a name")
name1 = input().title()

print("Write a number")
number1 = input()

print("Write a relative")
relative1 = input()

print("Write a place")
place1 = input().title()

print("Name another place")
place2 = input().title()

print("Write a verb ending in -ing")
verb1 = input()

print("Write a plural noun")
noun2 = input()

print("Write another adjective")
adj2 = input()

print("Write another adjective")
adj3 = input()

print("Name a person")
person1 = input().title()

print("Write an adjective ending in -ly")
adj4 = input()

### MAD LIB ###

print("A new and " + adjective1 + " fairy princess movie is coming ot soon! It will be about Snow "
     + name1 + " and the " + number1 + " dwarfs. Snow " + name1 +
      " is a princess whose beauty threatens her " + relative1 + " the queen. Snow "
     + name1 + " is forced to flee from " + place1 + " and hides in nearby " + place2
     + ". There, she discovers the dwarfs " + verb1 + " in their " + noun2
     + ". But the queen finds her and casts a " + adj2 + " spell on her. The dwarfs take care of her until the "
     + adj3 + person1 + " comes to rescue her, and they live " + adj4 + " ever after! ")

time.sleep(100)
