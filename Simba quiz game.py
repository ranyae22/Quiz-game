print ("Welcome to the Simba quiz game!")

playing = input("Would you like to play? ")

if playing != "yes":
    quit()

print("epic! let's play. we'll start easy 0_0 type your answer in lowercase letters.")
score = 0

answer = input("what color is Simba's fur? ")
if answer == "orange":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("where does Simba sleep at night? ")
if answer == "ranya's room":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("where did we get simba from? ")
if answer == "avis":    
    print("correct! lets step it up a notch :D" ) 
    score += 1
else:
    print("incorrect, but the questions are getting harder!")
answer = input ("does simba eat avacados? ")
if answer == "yes":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what is simba's favorite toy? ")
if answer == "mouse toy":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input ("does simba eat lettuce? ")
if answer == "yes":
    print("correct! Tricky questions incoming! Get ready!")  
    score += 1
else:
    print("incorrect, but tricky questions are coming! Get ready!")

answer = input("where is Simba's freckle located? ")
if answer == "left side of his nose":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("how old is Simba? ")
if answer == "3":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("when Simba uses the litter box, does he stick his head out? ")
if answer == "yes":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("last question! when is simba's birthday? ")
if answer == "april 30th":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score/10) * 100) + "%.")