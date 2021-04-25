from utils.trivia import QuestionAnswer, QuestionList
import os

ballresponse = [
    'Yes', 'No', 'Take a wild guess...', 'Very doubtful',
    'Sure', 'Without a doubt', 'Most likely', 'Might be possible',
    "You'll be the judge", 'no... (╯°□°）╯︵ ┻━┻', 'no... baka',
    'senpai, pls no ;-;'
]


## @story{9} The bot needs a list of questions to choose from.
# @param filename name of file to load the questions and answers from
def load_trivia_questions(filename: str):
    answers = []
    questions = []

    with open(filename) as fp:
        count = 0

        for line in fp:
            count += 1
            if count % 2 == 0:  # answer
                answers.append(line.rstrip())
            else:  # question
                questions.append(line.rstrip())

    all_questions = []
    for i in range(len(questions)):
        all_questions.append(QuestionAnswer(questions[i], answers[i]))
    return all_questions

## @story{9} The list of questions needs to be packed into the designed
#  data structure.
trivia_questions = QuestionList(
    load_trivia_questions("trivia_questions_answers.txt"))

#List for holding file names from meme directory
all_memes = []
for filename in os.listdir("memes"):
    all_memes.append(filename)
