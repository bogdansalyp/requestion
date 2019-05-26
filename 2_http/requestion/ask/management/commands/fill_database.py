from django.core.management.base import BaseCommand, CommandError
from ask.models import Tag, User, Question, QuestionLike, QuestionTag, Answer, AnswerLike
from datetime import datetime
from django.utils import timezone
import numpy as np


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'


    def _clear_tables(self):
        print('STARTING PURGE')
        for table in [AnswerLike, Answer, QuestionTag, QuestionLike, Question, Tag, User]:
            table.objects.all().delete()
            print('Cleared {}...'.format(table.__name__))
        print('PURGE FINISHED.')


    def _fill_user(self):
        print('FILLING USER MODEL...')
        for ix in range(500):
            temp_user = User(
                username='User{}'.format(ix+1),
                registration_date=timezone.now(),
                rating=5,
                path='user{}'.format(ix+1)
            )
            temp_user.save()
        print('ADDED {} USERS.'.format(User.objects.count()))


    def _fill_tag(self):
        print('FILLING TAG MODEL...')
        for ix in range(500):
            temp_tag = Tag(
                name='Tag{}'.format(ix+1)
            )
            temp_tag.save()
        print('ADDED {} TAGS'.format(Tag.objects.count()))


    def _fill_question(self):
        print('FILLING QUESTION MODEL...')
        for ix in range(500):
            temp_question = Question(
                title='Question{}'.format(ix+1),
                text='QuestionText{}'.format(ix+1),
                author=np.random.choice(User.objects.all()),
                rating=42,
                creation_date=timezone.now(),
                edit_date=timezone.now()
            )
            temp_question.save()
        print('ADDED {} QUESTIONS'.format(Question.objects.count()))


    def _fill_question_like(self):
        print('FILLING QUESTION_LIKE MODEL...')
        for ix in range(500):
            temp_question_like = QuestionLike(
                user=User.objects.all()[ix],
                question=Question.objects.all()[ix]
            )
            temp_question_like.save()
        print('ADDED {} QUESTION LIKES'.format(QuestionLike.objects.count()))


    def _fill_question_tag(self):
        print('FILLING QUESTION_TAG MODEL...')
        for ix in range(500):
            temp_question_tag = QuestionTag(
                tag=Tag.objects.all()[ix],
                question=Question.objects.all()[ix]
            )
            temp_question_tag.save()
        print('ADDED {} QUESTION_TAG TAGS'.format(QuestionTag.objects.count()))


    def _fill_answer(self):
        print('FILLING ANSWER MODEL...')
        for ix in range(500):
            temp_answer = Answer(
                question=np.random.choice(Question.objects.all()),
                text='Answer{}'.format(ix),
                rating=42,
                creation_date=timezone.now(),
                edit_date=timezone.now(),
                is_correct=False
            )
            temp_answer.save()
        print('ADDED {} ANSWERS'.format(Answer.objects.count()))


    def _fill_answer_like(self):
        print('FILLING ANSWER_LIKE MODEL...')
        for ix in range(500):
            temp_answer_like = AnswerLike(
                user=User.objects.all()[ix],
                answer=Answer.objects.all()[ix]
            )
            temp_answer_like.save()
        print('ADDED {} ANSWER LIKES'.format(AnswerLike.objects.count()))

    def handle(self, *args, **options):
        self._clear_tables()
        self._fill_user()
        self._fill_tag()
        self._fill_question()
        self._fill_question_like()
        self._fill_question_tag()
        self._fill_answer()
        self._fill_answer_like()