print('=================  She Codes Survey ================= ')
print('This survey will ask 3 qualifying questions and each qualifying question will direct you to the appropiate section')
print('Please answer questions using A, B, C as it is case sensitive')
print('=================  Start Survey ================= ')

from Survey import Survey
from Question import Question
from Answer import Answer
from Section import Section 


qualQuestion1 = Question(1, [], 'Are you a part of the She Codes Program?\n [A] yes \n [B] no', ['A', 'B'])
qualQuestion2 = Question(2, [], 'Did you attend the Wednesday Evening class?\n [A] yes \n [B] no', ['A', 'B'])
qualQuestion3 = Question(3, [], 'Did you attend the Saturday Morning class?\n [A] yes \n [B] no', ['A', 'B'])

question1 = Question(1, [], 'How did you find out about this program?\n [A] Social Media \n [B] Word of Mouth \n [C] Other\n', ['A', 'B','C'])

question2 = Question(2, [], 'Do you work for BHP?\n [A] Yes \n [B] No \n', ['A','B'])

question3 = Question(3, [], 'What time would you prefer the class to start?\n [A] 4:30PM \n [B] 5:00PM \n [C] 5:30PM\n', ['A', 'B','C'])

question4 = Question(4, [], 'How are your energy levels in the evening class?\n [A] Dozing off, I want to go to bed \n [B] Super pumped! \n [C] Ill be okay as long as I have food\n', ['A', 'B','C'])

question5 = Question(5, [], 'What time would you prefer the class to start?\n [A] 8:30AM \n [B] 9:00AM \n [C] 9:30AM\n', ['A', 'B', 'C'])

question6 = Question(6, [], 'How are your energy levels in the morning class?\n [A] I want to go back to bed \n [B] Super pumped! \n [C] Give me food and Ill be okay \n', ['A', 'B','C'])


section1 = Section(qualQuestion1,[question1, question2],'=================  SECTION 1: She Codes =================\n This section is about the She Codes Program \n')

section2 = Section(qualQuestion2,[question3, question4],'=================  SECTION 2. Wednesday Class ================= \n This section relates to the Wednesday Session \n')

section3 = Section(qualQuestion3,[question5, question6],'=================  SECTION 3: Friday Class ================= \n This session relates to the Saturday Session \n')

sheCodesSurvey = Survey([section1 ,section2 ,section3])
sheCodesSurvey.startSurvey()

print('=================  Survey Ends: Thank You for Participating ================= ')