class Section:
    def __init__(self, qualifyingQuestion, questionList, description):
        self.qualifyingQuestion = qualifyingQuestion
        self.questionList = questionList
        self.description = description

    def startSection(self):
        print(self.qualifyingQuestion.questionText)
        print('Your Answer: ')
        response= input()
        if response == 'A':
            print(self.description)
            for i in self.questionList:
                i.ask()