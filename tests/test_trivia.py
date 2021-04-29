from utils.trivia import QuestionAnswer, QuestionList, Trivia
from utils.lists import load_trivia_questions

## @story{9}
def test_QuestionAnswer():
    obj = QuestionAnswer("test question", "test answer")
    assert obj.question == "test question"
    assert obj.answer == "test answer"

## @story{9}
def test_QuestionList():
    questions = []
    for letter in "ABCDEFGHIJKLM":
        questions.append(QuestionAnswer(letter, letter))
    qlist = QuestionList(questions)
    assert qlist._questions == questions

## @story{9}
def test_QuestionList_add_question():
    qlist = QuestionList([])
    test_question = QuestionAnswer("test question", "test answer")
    qlist.add_question(test_question)
    assert qlist._questions == [test_question]

## @story{9}
def test_QuestionList_add_questions():
    qlist = QuestionList([])
    questions = []
    for letter in "ABCDEFGHIJKLM":
        questions.append(QuestionAnswer(letter, letter))
    qlist.add_questions(questions)
    assert qlist._questions == questions

## @story{9}
def test_QuestionList_count_len():
    questions = []
    for letter in "ABCDEFGHIJKLM":
        questions.append(QuestionAnswer(letter, letter))
    qlist = QuestionList(questions)
    assert len(qlist) == qlist.count == len(questions)

## @story{9}
def test_QuestionList_random_question():
    test_question = QuestionAnswer("test question", "test answer")
    qlist = QuestionList([test_question])
    assert qlist.get_random_question() == test_question

## @story{9}
def test_load_trivia_questions():
    questions = load_trivia_questions("tests/testquestions.txt")
    expected = [
        QuestionAnswer("Question A", "Answer A"),
        QuestionAnswer("Question B", "Answer B"),
        QuestionAnswer("Question C", "Answer C"),
        QuestionAnswer("Question D", "Answer D"),
    ]
    assert questions == expected

## @story{9}
def test_Trivia():
    trivia = Trivia()
    assert isinstance(trivia.qlist, QuestionList)
    assert trivia.inProgress is False

## @story{9}
def test_Trivia_start():
    trivia = Trivia()
    assert trivia.start_game() == 0

## @story{9}
def test_Trivia_status_not_in_progress():
    trivia = Trivia()
    trivia.inProgress = False
    assert trivia.get_game_status() == "Trivia game is not in progress"

## @story{9}
def test_Trivia_status_in_progress():
    trivia = Trivia()
    trivia.inProgress = True
    assert trivia.get_game_status() == "Trivia game in progress"

## @story{9}
def test_Trivia_check_wrong():
    trivia = Trivia()
    trivia.qAsked = QuestionAnswer("test question", "test answer")
    assert trivia.check_answer("wrong answer") == -1

## @story{9}
def test_Trivia_check_right():
    trivia = Trivia()
    trivia.qAsked = QuestionAnswer("test question", "test answer")
    assert trivia.check_answer("test answer") == 0

## @story{9}
def test_Trivia_end():
    trivia = Trivia()
    trivia.inProgress = True
    assert trivia.end_game() == 0
