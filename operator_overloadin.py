#operator overloading
class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self,o):
        if (self.a<o.a):
          return "obj_1 is less than obj_2"
        else:
          return "obj_1 is greater than obj_2"

    def __eq__(self,o):
        if (self.a==o.a):
          return "both are equal"
        else:
          return "not equal"

obj_1 = A(11)
obj_2 = A(12)
print(obj_1<obj_2)

obj_3 = A(13)
obj_4 = A(14)
print(obj_3==obj_4)



#flashcard
class Flashcard():
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word + " : " + self.meaning

flash = []
print("Welcome to Flashcard application")
while(True):
    word = input("Enter word: ")
    meaning = input("Enter meaning: ")
    flash.append(Flashcard(word, meaning))
    option = int(input("Enter 0, If you want to add another Flashcard enter 1"))
    if(option == 1):
        break

print("Your Flashcards are: ")
for i in flash:
    print(i)




import random

class FruitQuiz:

  def __init__(self):
    self.fruits = {'apple': 'red',
                   'banana': 'yellow',
                   'grape': 'purple',
                   'orange': 'orange'}

  def quiz(self):
    while (True):
      fruit,color = random.choice(list(self.fruits.items()))
      print("What is the color of {}".format(fruit))
      user_answer = input()
      if user_answer.lower() == color:
        print("Correct Answer!")

      option = int(input("Enter 0, If you want to play again enter 1"))
      if(option == 1):
          print("Thank you for playing")
          break
print("Welcome to the Fruit Quiz!")
fq = FruitQuiz()
fq.quiz()