from django.db.models.query_utils import Q
from django.shortcuts import render
from django.core import serializers
from .models import Quiz, Question, Choice
from django.shortcuts import redirect
from django.http import HttpResponse
import json
from quiz.dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from quiz.services import QuizResultService
import uuid


all_Quiz = serializers.serialize(
    "json",
    Quiz.objects.all(),
    fields=['uuid', 'title'])
all_Question = serializers.serialize(
    "json",
    Question.objects.all(),
    fields=['uuid', 'for_which_quiz', 'text'])
all_Choice = serializers.serialize(
    "json",
    Choice.objects.all(),
    fields=['uuid', 'for_which_question', 'text'])


# Формируем список вопросов с правильной позицией ответа
questions = []
for crnt_question in Question.objects.all():
    choices = []
    for crnt_choice in Choice.objects.all():
        if str(crnt_question.uuid) == str(crnt_choice.for_which_question.uuid):
            choices.append(
                ChoiceDTO(
                    str(crnt_choice.uuid),
                    crnt_choice.text,
                    crnt_choice.is_correct
                ))
    questions.append(
        QuestionDTO(
            crnt_question.uuid,
            crnt_question.text,
            choices
        ))


# Костль для считывания выбора ответа пользователя
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.data = None


user_choices = Singleton()


def index(request):
    return render(request, 'my_quiz_app/index.html')


def user_rating(request):
    if request.is_ajax():
        data = json.loads(request.body)
        user_choices.data = data
    if user_choices.data is None:
        return HttpResponse('Вы ещё не прошли тестирование')
    else:
        counter = 0
        user_result = 0
        for el in user_choices.data:
            user_uuid = []
            for crnt_uuid in user_choices.data[el]['user_choices']:
                for chs in Choice.objects.all():
                    if crnt_uuid == str(chs.uuid):
                        user_uuid.append(chs.uuid)
            answers = [AnswerDTO(el, user_uuid)]
            answers_dto = AnswersDTO("1", answers)
            quiz_dto = QuizDTO(
                Quiz.objects.first().uuid,
                Quiz.objects.first().title,
                [questions[counter]])
            reslt = QuizResultService(quiz_dto, answers_dto)
            user_result = user_result + reslt.get_result()
            counter = counter + 1

            user_right_answer = round(
                (user_result / len(Question.objects.all())) * 100, 1)
        return render(
            request,
            'my_quiz_app/user_result.html',
            {'data': user_right_answer})


def questions_list(request):
    return render(
        request,
        'my_quiz_app/questions_list.html',
        {'all_Quiz': all_Quiz,
            'all_Question': all_Question,
            'all_Choice': all_Choice})
