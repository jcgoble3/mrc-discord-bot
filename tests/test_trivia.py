from utils.trivia import QuestionAnswer, QuestionList, Trivia

def test_QuestionAnswer():
    obj = QuestionAnswer("test question", "test answer")
    assert obj.question == "test question"
    assert obj.answer == "test answer"

def test_QuestionList():
    questions = []
    for letter in "ABCDEFGHIJKLM":
        questions.append(QuestionAnswer(letter, letter))
    qlist = QuestionList(questions)
    assert qlist.count == len(questions)
    assert len(qlist) == len(questions)
    for _ in range(25):
        assert qlist.get_random_question() in questions

    test_question = QuestionAnswer("test question", "test answer")
    qlist.add_question(test_question)
    assert qlist.count == len(questions) + 1

    questions2 = []
    for letter in "NOPQRSTUVWXYZ":
        questions2.append(QuestionAnswer(letter, letter))
    qlist.add_questions(questions2)

    all_questions = questions + questions2 + [test_question]
    assert qlist.count == len(all_questions)
    for q in all_questions:
        assert q in qlist._questions
    for q in qlist._questions:
        assert q in all_questions

def test_Trivia():
    trivia = Trivia()
    assert isinstance(trivia.qlist, QuestionList)
    assert trivia.inProgress is False

def test_Trivia_start():
    trivia = Trivia()
    assert trivia.start() == 0

def test_Trivia_status():
    trivia = Trivia()
    assert trivia.status() == "Trivia Status!"

def test_Trivia_check():
    trivia = Trivia()
    trivia.qAsked = QuestionAnswer("test question", "test answer")
    assert trivia.check("wrong answer") == -1
    assert trivia.check("test answer") == 0

def test_Trivia_end():
    trivia = Trivia()
    assert trivia.end() == 0
