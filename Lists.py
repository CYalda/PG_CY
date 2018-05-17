name = " Christian"

subjects = {"English","Math","History","Chinese","Comp Sci"}

print("Hello" +  name)

for i in subjects:
    print ("One of my Classes is " +i)


movies = ("The Hangover","Superbad","Pineapple Express","Black Panther")

for i in movies:
    if i == "The Hangover":
        print(i + "is my favorite movie out of all of them.")
    elif i == "Superbad":
        print(i + " is the funniest.")
    elif i == "Black Panther":
        print(i + " has the most action.")

animals = {}

while True:
    print("What is your favorite Animal? Type 'end' to quit")
    answer = input()

    if answer == "end":
        break
    else:
        animals.append(answer)

for i in movies:
    print("One of your favorites is" + i)
