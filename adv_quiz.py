# It's a quiz which ask 10 random questions and scores how much you scored
import random
def get_que():
   
    with open("Quiz.txt", "r") as file:
        
        questions = [line.strip() for line in file if line.strip()]
        
    return random.choice(questions)


wins = {
    "paris":"what is the capital of france?",
    "william shakespeare":"who wrote the play romeo and juliet",
    "jupiter":"what is the largest planet in our solar system?",
    "7":"how many continents are there on earth?",
    "c":"what is the chemical symbol for carbon?",
    "charles babbage":"who is known as the father of computers?",
    "china":"which country is famous for the great wall?",
    "2":"what is the smallest prime number?",
    "heart":"which organ pumps blood through the body?",
    "leonardo da vinci":"who painted the mona lisa?",
    "baseball":"in which sport is the term 'home run' used?",
    "yen":"what is the national currency of japan?",
    "oxygen":"what gas do humans breathe in to survive?",
    "0":"what is the freezing point of water in celsius?",
    "alexander graham Bell":"who invented the telephone?",
    "mars":"which planet is known as the red planet?",
    "new delhi":"what is the capital city of india?",
    "11":"how many players are there in a soccer (football) team?",
    "diamond":"what is the hardest natural substance on earth?",
    "isaac newton":"who discovered gravity when an apple fell on his head (legend)?",
    "mount Everest":"What is the tallest mountain in the world?",
    "lion":"which animal is known as the king of the jungle?",
    "100":"what is the boiling point of water in Celsius?",
    "cheetah":"which is the fastest land animal?",
    "milky way":"in which galaxy do we live?"
}
score=0
l=["a","b","c","d","e","f","g","h","i","j"]
for i in range(1,11):
    l[i]=get_que()
    print(f"Que {i}= {l[i]}")
    z=str(input(f"answer que.{i} ").lower())
    if z in wins:
        wins[z]==l[i]
        score+=1
        print("correct your current score is= ",score)
    else:
        print("incorrect your current score is= ",score)


print("Your final score is ",score)
