
class Survey:
    def __init__(self, sectionList):
        self.sectionList = sectionList

    def startSurvey(self):
        for i in self.sectionList:
            i.startSection()
        
    def ask_qualifying_questions(self):
        print('Asking Question')

    def start_survey_questions(self):
        pass

    def ask_question(self):
        pass
    
    def show_answers(self):
        pass

    def answer_question(self):
        pass

    def go_to_next_question(self):
        pass
    