#string concatenation (aka how to put strings together)
#suppose we want to create a string that says "I want ______"
thing = "apples"

# a few ways to do this
#print("I want " + thing)
#print("I want {}".format(thing))
#print(f"I want {thing}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated amd {verb2} like you are {famous_person}!"

print(madlib)