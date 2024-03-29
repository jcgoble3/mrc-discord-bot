from dataclasses import dataclass
import random

from typing import Iterable, List

## @story{9} In order to do trivia, the bot must be able to link a question
#  to its corresponding answer. Additionally, standard conventions of the
#  language such as usage of dataclasses should be adhered to.
@dataclass
class QuestionAnswer:
    """Hold a single trivia question with its answer."""
    question: str
    answer: str

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

## @story{9} In order to do trivia, the bot must be able to have multiple
#  questions available and select one at random.
class QuestionList:
    """Hold trivia questions and serve random ones on demand."""

    _questions: List[QuestionAnswer]

    ## @story{9} Enables the list to be pre-populated with an existing
    #  list of questions
    #  @param questions questions to populate list
    def __init__(self, questions: Iterable[QuestionAnswer]):
        self._questions = list(questions)

    ## @story{9} Enables a question to be added to the list
    #  @param question question to add to list
    def add_question(self, question: QuestionAnswer) -> None:
        """Add a question to the list."""
        self._questions.append(question)

    ## @story{9} Enables questions to be added to the list
    #  @param questions questions to add to list
    def add_questions(self, questions: Iterable[QuestionAnswer]) -> None:
        """Add an iterable of questions to the list."""
        self._questions.extend(questions)

    ## @story{9} Enables the bot to select a random question to ask
    def get_random_question(self) -> QuestionAnswer:
        """Return a random question."""
        return random.choice(self._questions)

    ## @story{9} A way to get the current number of questions for
    #  use in informational messages, implemented with the property
    #  decorator to follow standard Python convention for a getter.
    @property
    def count(self) -> int:
        """Get the number of questions currently known."""
        return len(self._questions)

    ## @story{9} Another way, following Python conventions for lengths,
    #  to get the current number of questions for use in informational
    #  messages
    def __len__(self) -> int:
        return self.count


## @story{9} The purpose of this object is to hold trivia game data and
# maintain game state.
class Trivia:

    ## @story{9} Object for holding the list of questions
    qlist: QuestionList

    ## @story{9} Object for holding the question currently in use by an instance of Trivia
    qAsked: QuestionAnswer

    ## @story{9} Used to keep track of whether a trivia game is in progress or not.
    inProgress: bool

    def __init__(self):

        self.qAsked = QuestionAnswer("Question asked", "Answer asked")

        # This line prepopulates the question list and is only here to facilitate
        # ease of development. Had development continued far enough, this line would
        # be replaced with code that would read in the questions and answers from an
        # external source.
        self.qlist = QuestionList([QuestionAnswer("Question 1", "Answer 1")])

        self.inProgress = False

    ## @story{9} Responsible for starting the trivia game.
    # @return non-zero value to indicate failure, 0 to indicate success
    def start_game(self) -> int:
        if __debug__:
            assert type(self.inProgress) is bool, "The inProgress variable must be of type boolean"
            assert self.inProgress == False, "inProgress must be False when start_game is called"

            # Remainder of function not yet implemented, this is just a stub.

        return 0

    ## @story{9} Responsible for ending the trivia game.
    # @return non-zero value to indicate failure, 0 to indicate success
    def end_game(self) -> int:
        if __debug__:
            assert type(self.inProgress) is bool, "The inProgress variable must be of type boolean"
            assert self.inProgress == True, "inProgress must be True when the Trivia object is initialized"

            # Remainder of function not yet implemented, this is just a stub.

        return 0

    ## @story{9} Responsible for checking submitted answers to see if they are correct or not.
    # @return non-zero value to indicate failure, 0 to indicate success
    def check_answer(self, answer) -> int:
        if __debug__:
            assert type(answer) is str, "The answer argument must be of type str"

        if (self.qAsked.answer == answer):
            return 0
        else:
            return -1

    ## @story{9} Responsible for returning the status of the trivia game.
    # @return current status as string value
    def get_game_status(self) -> str:
        if __debug__:
            assert type(self.inProgress) is bool, "inProgress must be of type bool"

        if (self.inProgress):
            return "Trivia game in progress"
        else:
            return "Trivia game is not in progress"
