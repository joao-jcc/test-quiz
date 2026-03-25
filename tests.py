import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct


# 10 novos testes
def test_remove_choice_by_id():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)
    question.remove_choice_by_id(1)
    assert len(question.choices) == 2
    assert question.choices[0].text == 'b'
    assert question.choices[1].text == 'c'

def test_remove_all_choices():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)
    question.remove_all_choices()
    assert len(question.choices) == 0

def test_set_correct_choices():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)
    question.set_correct_choices([1, 3])
    assert question.choices[0].is_correct == True
    assert question.choices[1].is_correct == False
    assert question.choices[2].is_correct == True

def test_correct_selected_choices():
    question = Question(title='q1', max_selections=2)
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)
    question.set_correct_choices([1, 3])
    assert question.correct_selected_choices([1, 2]) == [1]
    assert question.correct_selected_choices([1, 3]) == [1, 3]
    with pytest.raises(Exception):
        question.correct_selected_choices([1, 2, 3])

# 2 novos testes
def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question(title='q1', points=0)
    with pytest.raises(Exception):
        Question(title='q1', points=101)

def test_create_question_with_invalid_max_selections():
    with pytest.raises(Exception):
        Question(title='q1', max_selections=0)
    with pytest.raises(Exception):
        Question(title='q1', max_selections=101)

def test_create_question_with_valid_max_selections():
    question = Question(title='q1', max_selections=1)
    assert question.max_selections == 1
    question = Question(title='q1', max_selections=100)
    assert question.max_selections == 100  

def test_create_question_with_invalid_points_and_max_selections():
    with pytest.raises(Exception):
        Question(title='q1', points=0, max_selections=1)
    with pytest.raises(Exception):
        Question(title='q1', points=101, max_selections=1)
    with pytest.raises(Exception):
        Question(title='q1', points=1, max_selections=0)
    with pytest.raises(Exception):
        Question(title='q1', points=100, max_selections=101)

def test_create_question_with_valid_points_and_max_selections():
    question = Question(title='q1', points=1, max_selections=1)
    assert question.points == 1
    assert question.max_selections == 1
    question = Question(title='q1', points=100, max_selections=100)
    assert question.points == 100
    assert question.max_selections == 100