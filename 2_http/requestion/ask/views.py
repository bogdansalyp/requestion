from django.http import HttpResponse
from django.template import loader


def main(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def hot(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def tag(request, tag_name):
    template = loader.get_template("tag.html")
    context = {}
    return HttpResponse(template.render(context, request))


def question(request, question_id):
    template = loader.get_template("question.html")
    context = {}
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template("login.html")
    context = {}
    return HttpResponse(template.render(context, request))


def signup(request):
    template = loader.get_template("signup.html")
    context = {}
    return HttpResponse(template.render(context, request))


def ask(request):
    template = loader.get_template("ask.html")
    context = {}
    return HttpResponse(template.render(context, request))