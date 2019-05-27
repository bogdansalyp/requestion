from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from ask.models import Tag, User, Question, QuestionLike, QuestionTag, Answer, AnswerLike
import numpy as np

SIDE_USERS_NUMBER = 20
SIDE_TAGS_NUMBER = 20


def main(request):
    template = loader.get_template("index.html")

    questions_list = Question.objects.all()
    paginator = Paginator(questions_list, 10)
    page = request.GET.get('page')
    questions = paginator.get_page(page)

    context = {
        "title": "New Question",
        "questions": questions,
        "side_tags": {
            "title": "Popular Tags",
            "tags": Tag.objects.get_most_popular(SIDE_TAGS_NUMBER)},
        "best_members": {
            "title": "Best Members",
            "tags": User.objects.get_most_popular(SIDE_USERS_NUMBER)}}
    return HttpResponse(template.render(context, request))


def hot(request):
    template = loader.get_template("index.html")
    context = {
        "title": "Hot Questions",
        "side_tags": {
            "title": "Popular Tags",
            "tags": Tag.objects.get_most_popular(SIDE_TAGS_NUMBER)
        },
        "best_members": {
            "title": "Best Members",
            "tags": User.objects.get_most_popular(SIDE_USERS_NUMBER)
        }
    }
    return HttpResponse(template.render(context, request))


def tag(request, tag_name):
    template = loader.get_template("tag.html")

    questions_list = Question.objects.with_tag(tag_name)
    print(len(questions_list))
    paginator = Paginator(questions_list, 10)
    page = request.GET.get('page')
    questions = paginator.get_page(page)

    context = {
        "title": "Questions by tag '{}'".format(tag_name),
        "questions": questions,
        "side_tags": {
            "title": "Popular Tags",
            "tags": Tag.objects.get_most_popular(SIDE_TAGS_NUMBER)
        },
        "best_members": {
            "title": "Best Members",
            "tags": User.objects.get_most_popular(SIDE_USERS_NUMBER)
        }
    }
    return HttpResponse(template.render(context, request))


def question(request, question_id):
    template = loader.get_template("question.html")
    context = {
        "title": "Question #{}".format(question_id),
        "question": Question.objects.get(id=question_id),
        "side_tags": {
            "title": "Popular Tags",
            "tags": Tag.objects.get_most_popular(SIDE_TAGS_NUMBER)
        },
        "best_members": {
            "title": "Best Members",
            "tags": User.objects.get_most_popular(SIDE_USERS_NUMBER)
        }
    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template("login.html")
    context = {
        "title": "Log In",
        "side_tags": {
            "title": "Popular Tags",
            "tags": Tag.objects.get_most_popular(SIDE_TAGS_NUMBER)
        },
        "best_members": {
            "title": "Best Members",
            "tags": User.objects.get_most_popular(SIDE_USERS_NUMBER)
        }
    }
    return HttpResponse(template.render(context, request))


def signup(request):
    template = loader.get_template("signup.html")
    context = {
        "title": "Sign Up",
        "side_tags": {
            "title": "Popular Tags",
            "tags": Tag.objects.get_most_popular(SIDE_TAGS_NUMBER)
        },
        "best_members": {
            "title": "Best Members",
            "tags": User.objects.get_most_popular(SIDE_USERS_NUMBER)
        }
    }
    return HttpResponse(template.render(context, request))


def ask(request):
    template = loader.get_template("ask.html")
    context = {
        "title": "Ask your question",
        "side_tags": {
            "title": "Popular Tags",
            "tags": Tag.objects.get_most_popular(SIDE_TAGS_NUMBER)
        },
        "best_members": {
            "title": "Best Members",
            "tags": User.objects.get_most_popular(SIDE_USERS_NUMBER)
        }
    }
    return HttpResponse(template.render(context, request))


def settings(request):
    template = loader.get_template("settings.html")
    context = {
        "title": "Settings",
        "side_tags": {
            "title": "Popular Tags",
            "tags": Tag.objects.get_most_popular(SIDE_TAGS_NUMBER)
        },
        "best_members": {
            "title": "Best Members",
            "tags": User.objects.get_most_popular(SIDE_USERS_NUMBER)
        }
    }
    return HttpResponse(template.render(context, request))
