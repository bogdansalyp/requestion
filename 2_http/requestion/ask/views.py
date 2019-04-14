from django.http import HttpResponse
from django.template import loader


def main(request):
    template = loader.get_template("index.html")
    context = {
        "title": "New Question",
        "questions": [
            {
                "title": "How to build a moon park?",
                "text": "Guys, I have a trouble with a Moon park...",
                "tags": ["perl", "python", "moon"],
                "answers_amount": 3
            },
            {
                "title": "How the hell?!?!?!",
                "text": "Test test test",
                "tags": ["test", "test2", "test3"],
                "answers_amount": 42
            }
        ]
    }
    return HttpResponse(template.render(context, request))


def hot(request):
    template = loader.get_template("index.html")
    context = {
        "title": "Hot Questions"
    }
    return HttpResponse(template.render(context, request))


def tag(request, tag_name):
    template = loader.get_template("tag.html")
    context = {
        "title": "Questions by tag '{}'".format(tag_name),
        "questions": [
            {
                "title": "How to build a moon park?",
                "text": "Guys, I have a trouble with a Moon park...",
                "tags": [tag_name, "perl", "python", "moon"],
                "answers_amount": 3
            },
            {
                "title": "How the hell?!?!?!",
                "text": "Test test test",
                "tags": [tag_name, "test", "test2", "test3"],
                "answers_amount": 42
            }
        ]
    }
    return HttpResponse(template.render(context, request))


def question(request, question_id):
    template = loader.get_template("question.html")
    context = {
        "title": "Question #{}".format(question_id)
    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template("login.html")
    context = {
        "title": "Log In"
    }
    return HttpResponse(template.render(context, request))


def signup(request):
    template = loader.get_template("signup.html")
    context = {
        "title": "Sign Up"
    }
    return HttpResponse(template.render(context, request))


def ask(request):
    template = loader.get_template("ask.html")
    context = {
        "title": "Ask your question"
    }
    return HttpResponse(template.render(context, request))

def settings(request):
    template = loader.get_template("settings.html")
    context = {
        "title": "Settings"
    }
    return HttpResponse(template.render(context, request))