from django.http import HttpResponse
from django.template import loader


def main(request):
    template = loader.get_template("index.html")
    context = {
        "title": "New Question"
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
        "title": "Questions by tag '{}'".format(tag_name)
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