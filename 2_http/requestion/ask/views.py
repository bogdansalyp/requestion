from django.http import HttpResponse
from django.template import loader

def main(request):
    template = loader.get_template('index.html')
    context = {
        "title": "New Questions"
    }
    return HttpResponse(template.render(context, request))


def hot(request):
    return HttpResponse("Hot questions")


def tag(request, tag_name):
    return HttpResponse(tag_name)


def question(request, question_id):
    return HttpResponse(question_id)


def login(request):
    return HttpResponse("Login")


def signup(request):
    return HttpResponse("Signup")


def ask(request):
    return HttpResponse("Ask a question")