import random
import pickle


class Doctor():

    QUALIFIERS = ['Why do you say that ', 'You seem to think that ',
                  'Did I just hear you say that ', 'Why do you believe that ']

    REPLACEMENTS = {'I': 'you', 'me': 'you', 'my': 'your',
                    'we': 'you', 'us': 'you', 'am': 'are',
                    'you': 'I', 'You': 'I'}

    HEDGES = ['Go on.', 'I would like to hear more about that.',
              'And what do you think about this?', 'Please continue.']

    def __init__(self):
        self.history = []
        self.person = None
        self.firstTalk = True

    def greeting(self, client):

        return 'Hello, please state your name <>'

    def farewell(self):
        return 'Have a nice day!'

    def reply(self, sentence):
        answer = ''
        if self.firstTalk:
            self.person = str(sentence)
            # print(self.person)
            try:
                with open(self.person+'.dat', 'rb') as f:
                    self.history = pickle.load(f)
                    answer = 'Welcome Back ' +  \
                        self.person + \
                        ', Last Discussion: ' \
                        + str(self.history[-1])

            except Exception:
                # create one
                file = open(self.person+'.dat', 'wb')
                file.close()
                answer = 'Greetings! ' + self.person

            finally:
                self.firstTalk = False
            return answer
        else:
            choice = random.randint(1, 10)
            if choice == 1:
                if len(self.history) > 3:
                    answer = 'Earlier you said that ' + \
                        self.change_person(random.choice(self.history))
                else:
                    answer = random.choice(Doctor.HEDGES)
            elif choice in (2, 3, 4, 5):
                answer = random.choice(Doctor.QUALIFIERS) + \
                    self.change_person(sentence)
            else:
                answer = random.choice(Doctor.HEDGES)
        self.history.append(answer)
        return answer

    def updateFile(self):
        with open(self.person+'.dat', 'wb') as f:
            pickle.dump(self.history, f)

    def change_person(self, sentence):
        oldlist = sentence.split()
        newlist = []
        for word in oldlist:
            if word in Doctor.REPLACEMENTS:
                newlist.append(Doctor.REPLACEMENTS[word])
            else:
                newlist.append(word)
        return " ".join(newlist)
