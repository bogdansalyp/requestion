from django.db import models
from django.utils import timezone


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    registration_date = models.DateTimeField(default=timezone.now())
    rating = models.IntegerField(default=0)
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    rating = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now(), blank=True)
    edit_date = models.DateTimeField(default=timezone.now(), blank=True)

    def __str__(self):
        return self.text


class QuestionLike(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'question',)


class QuestionTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tag', 'question',)


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    rating = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now(), blank=True)
    edit_date = models.DateTimeField(default=timezone.now(), blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class AnswerLike(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'answer',)
