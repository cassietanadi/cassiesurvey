class Question:
    def __init__(self, questionNumber, responses, questionText, answerOptions):
        self.questionNumber = questionNumber 
        self.responses = responses
        self.questionText = questionText
        self.answerOptions = answerOptions

    def ask(self):
        print(self.questionText, self.answerOptions)
        print('Your Answer: ')
        responseSingular= input()
        self.responses.append(responseSingular) 
        print(self.responses)
        # self.nextQuestion
