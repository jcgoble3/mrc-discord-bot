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
    QuestionAnswer("Stockholm is the capital and largest city of what country?", "Sweden"),
    QuestionAnswer("What year did the website Facebook launch?", "2004"),
    QuestionAnswer("What is the scientific name for the Southern Lights?", "Aurora Australis"),
    QuestionAnswer("On average, Americans consume 100 pounds of what per second?", "Chocolate"),
    QuestionAnswer("How many bones are there in the human body?", "206"),
    QuestionAnswer("What does Na stand for on the periodic table?", "Sodium"),
    QuestionAnswer("Which fictional city is the home of Batman?", "Gotham"),
    QuestionAnswer("Which planet is closest to Earth?", "Venus"),
    QuestionAnswer("In the US version of The Office, what is the name of the city they live in?", "Scranton"),
    QuestionAnswer("Which U.S. State is the largest (in terms of land area)?", "Alaska"),
    QuestionAnswer("Which U.S. State is known as the Sunflower State?", "Kansas"),
    QuestionAnswer("Who founded Microsoft?", "Bill Gates"),
    QuestionAnswer("What plant is known to help heal a sunburn?", "Aloe"),
    QuestionAnswer("How many planets are in our solar system? (Including Pluto!)", "9"),
    QuestionAnswer("What is your body’s largest organ?", "Skin"),
    QuestionAnswer("What year did the Titanic movie come out?", "1997"),
    QuestionAnswer("Who played Neo in The Matrix?", "Keanu Reeves"),
    QuestionAnswer("What year was the first IPhone released?", "2007"),
    QuestionAnswer("Which bone are babies born without?", "Knee Cap"),
    QuestionAnswer("What is Hawkeye's real Name?", "Clint Barton"),
    QuestionAnswer("Mexico’s Dia de los Muertos, means what in English?", "Day of the Dead"),

]

trivia_questions = QuestionList(_all_questions)
