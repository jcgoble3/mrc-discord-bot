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
    assert qlist._questions == questions

def test_QuestionList_add_question():
    qlist = QuestionList([])
    test_question = QuestionAnswer("test question", "test answer")
    qlist.add_question(test_question)
    assert qlist._questions == [test_question]

def test_QuestionList_add_questions():
    qlist = QuestionList([])
    questions = []
    for letter in "ABCDEFGHIJKLM":
        questions.append(QuestionAnswer(letter, letter))
    qlist.add_questions(questions)
    assert qlist._questions == questions

def test_QuestionList_count_len():
    questions = []
    for letter in "ABCDEFGHIJKLM":
        questions.append(QuestionAnswer(letter, letter))
    qlist = QuestionList(questions)
    assert len(qlist) == qlist.count == len(questions)

def test_QuestionList_random_question():
    test_question = QuestionAnswer("test question", "test answer")
    qlist = QuestionList([test_question])
    assert qlist.get_random_question() == test_question

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
