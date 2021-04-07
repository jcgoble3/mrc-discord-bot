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
