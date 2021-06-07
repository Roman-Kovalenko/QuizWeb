from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List


class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self) -> float:
        # your code here
        for current_questions, current_answers in zip(self.quiz_dto.questions, self.answers_dto.answers):

            # Существуюшие ответы и их правильность
            existed_uuid = {}
            # Количество правильных ответов
            amount_true_answers = 0
            for choice in current_questions.choices:
                existed_uuid[choice.uuid] = choice.is_correct
                if choice.is_correct:
                    amount_true_answers += 1

            # Правильность ответов пользователя
            is_user_choces_right = []
            for user_choice in current_answers.choices:
                if str(user_choice) in existed_uuid and existed_uuid[str(user_choice)]:
                    is_user_choces_right.append(True)
                else:
                    is_user_choces_right.append(False)
            if len(is_user_choces_right) == 0:
                is_user_choces_right = ['']
            if len(is_user_choces_right) != amount_true_answers:
                is_user_choces_right = ['']

        return float(all(is_user_choces_right))
