from utils.trivia import QuestionAnswer, QuestionList

ballresponse = [
    'Yes', 'No', 'Take a wild guess...', 'Very doubtful',
    'Sure', 'Without a doubt', 'Most likely', 'Might be possible',
    "You'll be the judge", 'no... (╯°□°）╯︵ ┻━┻', 'no... baka',
    'senpai, pls no ;-;'
]
i = 0
answers = []
questions = []

## @story{9} The bot reads in a list of questions to choose from.
with open ("trivia_questions_answers.txt") as fp:
    count = 0
    a_count = 0
    q_count = 0
    
    for line in fp:
        count +=1
        if count % 2 == 0: # answer
            answers.append(line)
            a_count+=1
        else: # question
            questions.append(line)
            q_count+=1


_all_questions = []
for i in range(q_count):
     _all_questions.append(QuestionAnswer(questions[i], answers[i]))

## @story{9} The list of questions needs to be packed into the designed
#  data structure.
trivia_questions = QuestionList(_all_questions)
