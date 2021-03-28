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
    QuestionAnswer("When did the website “Facebook” launch?", "2004"),
    QuestionAnswer("T/F: The scientific name for the Southern Lights is Aurora Australis?", "T"),
    QuestionAnswer("On average, Americans consume 100 pounds of what per second?", "Chocolate"),
    QuestionAnswer("How many bones are there in the human body?", "206"),
    QuestionAnswer("What does Na stand for on the periodic table?", "Sodium"),
    QuestionAnswer("Which fictional city is the home of Batman?", "Gotham"),
    QuestionAnswer("Which planet is closest to Earth?", "Venus"),
    QuestionAnswer("In the US version of The Office, what is the name of the city they live in?", "Scranton"),
    QuestionAnswer("Which U.S. State is the largest?", "Alaska"),
    QuestionAnswer("Which U.S. State is known as the “Sunflower State”?", "Kansas"),
    QuestionAnswer("Who founded Microsoft?", "Bill Gates"),
    QuestionAnswer("What plant is known to help heal a sunburn?", "Aloe"),
    QuestionAnswer("What is the #1 cookie in the United States?", "Oreo"),
    QuestionAnswer("How many planets are in our solar system? (Including Pluto!)", "9"),    

]

trivia_questions = QuestionList(_all_questions)
