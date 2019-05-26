from django.db import models
from datetime import datetime    
from django.contrib.auth.models import AbstractUser


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class User(AbstractUser):
#     registration_date = models.DateTimeField(default=datetime.now)
#     rating = models.IntegerField(default=0)
#     path = models.CharField(max_length=200)

#     def __str__(self):
#         return self.username


class User(models.Model):
    pass


class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    rating = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    edit_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.text


class QuestionLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'question',)


class QuestionTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    rating = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    edit_date = models.DateTimeField(default=datetime.now, blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class AnswerLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'answer',)
