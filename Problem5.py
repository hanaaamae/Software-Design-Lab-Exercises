import random

history = []

hedges = ("Please tell me more.",
"Many of my patients tell me the same thing.",
"Please continue.")

qualifiers = ("Why do you say that ",
"You seem to think that ",
"Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your",
"we":"you", "us":"you", "mine":"yours",
"you":"I", "your":"my", "yours":"mine"}

class Doctor:
    def __init__(self):
        pass
  
    def greeting(self):
        return "Good morning, I hope you are well today.\nWhat can I do for you?"
  
    def farewell(self):
        return "Have a nice day!"

    def reply(self,sentence):
        """Implements three different reply strategies."""
        probability = random.randint(1, 5)
        if probability in (1, 2):
        # Just hedge
            answer = random.choice(hedges)
        elif probability == 3 and len(history) > 3:
        # Go back to an earlier topic
            answer = "Earlier you said that " + \
            changePerson(random.choice(history))
        else:
        # Transform the current input
            answer = random.choice(qualifiers) + changePerson(sentence)
        # Always add the current sentence to the history list
        history.append(sentence)
        return answer

def changePerson(sentence):
    """Replaces first person pronouns with second person
    pronouns."""
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)

def main():
    """Handles the interaction between patient and doctor."""
    doctor=Doctor()
    print(doctor.greeting())
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print(doctor.farewell())
            break
        print(doctor.reply(sentence))

# The entry point for program execution
if __name__ == "__main__":
    main()