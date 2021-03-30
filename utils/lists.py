from utils.trivia import QuestionAnswer, QuestionList

ballresponse = [
    'Yes', 'No', 'Take a wild guess...', 'Very doubtful',
    'Sure', 'Without a doubt', 'Most likely', 'Might be possible',
    "You'll be the judge", 'no... (╯°□°）╯︵ ┻━┻', 'no... baka',
    'senpai, pls no ;-;'
]

_all_questions = [
    QuestionAnswer("What is the capital city of Spain?", "Madrid"),
    QuestionAnswer("What is arachnophobia the fear of?", "Spiders"),
]

trivia_questions = QuestionList(_all_questions)
