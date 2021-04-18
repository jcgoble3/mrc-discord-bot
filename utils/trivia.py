from dataclasses import dataclass
import random
import enum

from typing import Iterable, List


@dataclass
class QuestionAnswer:
    """Hold a single trivia question with its answer."""
    question: str
    answer: str

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class QuestionList:
    """Hold trivia questions and serve random ones on demand."""

    _questions: List[QuestionAnswer]

    def __init__(self, questions: Iterable[QuestionAnswer]):
        self._questions = list(questions)

    def add_question(self, question: QuestionAnswer) -> None:
        """Add a question to the list."""
        self._questions.append(question)

    def add_questions(self, questions: Iterable[QuestionAnswer]) -> None:
        """Add an iterable of questions to the list."""
        self._questions.extend(questions)

    def get_random_question(self) -> QuestionAnswer:
        """Return a random question."""
        return random.choice(self._questions)

    @property
    def count(self) -> int:
        """Get the number of questions currently known."""
        return len(self._questions)

    def __len__(self) -> int:
        return self.count


# Trivia game object
# The purpose of this object is to hold trivia game data and
# maintain game state.
class Trivia:

    # Object for holding the list of questions
    qlist: QuestionList
    
    # Object for holding the question currently in use by an instance of Trivia
    qAsked: QuestionAnswer
    
    # The inProgress variable is used to keep track of
    # whether a trivia game is in progress or not.
    inProgress: bool

    def __init__(self):
        self.qlist = QuestionList([QuestionAnswer("Question 1", "Answer 1")])
        self.inProgress = False

    # This function is responsible for starting the trivia game.
    def start(self) -> int:
        # Return non-zero value to indicate failure
        # Return 0 to indicate success
        return 0

    # This function is responsible for ending the trivia game.
    def end(self) -> int:
        # Return non-zero value to indicate failure
        # Return 0 to indicate success
        return 0

    def check(self, answer) -> int:
        # Return non-zero value to indicate failure
        # Return 0 to indicate success
        if (self.qAsked.answer == answer)
            return 0
        else
            return -1
        

    # This function is responsible for returning the status of the
    # trivia game.
    def status(self) -> str:
        return "Trivia Status!"
