from utils.trivia_data import QuestionAnswer, QuestionList

ballresponse = [
    'Yes', 'No', 'Take a wild guess...', 'Very doubtful',
    'Sure', 'Without a doubt', 'Most likely', 'Might be possible',
    "You'll be the judge", 'no... (╯°□°）╯︵ ┻━┻', 'no... baka',
    'senpai, pls no ;-;'
]

_all_questions = [
    QuestionAnswer("What is the capital city of Spain?", "Madrid"),
    QuestionAnswer("What is arachnophobia the fear of?", "Spiders"),
    QuestionAnswer("What is your body’s largest organ?", "Skin"),
    QuestionAnswer("What year did the Titanic movie come out?", "1997"),
    QuestionAnswer("Who played Neo in The Matrix?", "Keanu Reeves"),
    QuestionAnswer("What year was the first IPhone released?", "2007"),
    QuestionAnswer("Which bone are babies born without?", "Knee Cap"),
    QuestionAnswer("What is Hawkeye's real Name?", "Clint Barton"),
    QuestionAnswer("Mexico’s Dia de los Muertos, means what in English?", "Day of the Dead"),
]

trivia_questions = QuestionList(_all_questions)
