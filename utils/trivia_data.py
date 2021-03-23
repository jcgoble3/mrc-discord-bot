from dataclasses import dataclass
import random

from typing import Iterable, List


@dataclass
class QuestionAnswer:
    """Hold a single trivia question with its answer."""
    question: str
    answer: str


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
