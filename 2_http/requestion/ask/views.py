from django.http import HttpResponse
from django.template import loader
import numpy as np

titles = [
    "How to build a moon park?",
    "How to patch KDE for FreeBSD?",
    "Why?", "How?", "When?",
    "What's yellow and dangerous? ",
    "What do you get when you multiply six by seven?",
    "How many coders does it take to change a lightbulb?",
    "How many roads must a man walk down?",
    "Answer to the Ultimate Question of Life, the Universe, and Everything"
]

texts = [
    "Bacon ipsum dolor amet bresaola picanha shank leberkas boudin. Biltong chuck pork chop, tenderloin capicola meatloaf kevin pig spare ribs ham alcatra pork loin porchetta t-bone. Short ribs meatball turducken hamburger, pork chop tri-tip porchetta pastrami t-bone capicola boudin spare ribs strip steak tenderloin. Chicken t-bone spare ribs capicola pork loin pork belly pig. Ham hock tongue tri-tip, boudin shankle chuck swine beef ribs pork frankfurter turkey jowl turducken kielbasa. Doner short loin beef beef ribs prosciutto sirloin. Kevin pork chop pork loin prosciutto tenderloin boudin ribeye andouille burgdoggen pancetta fatback turducken ham hock.",
    "Chase red laser dot pushes butt to face. Spend all night ensuring people don't sleep sleep all day i heard this rumor where the humans are our owners, pfft, what do they know?!, cat meoooow i iz master of hoomaan, not hoomaan master of i, oooh damn dat dog cat is love, cat is life for have a lot of grump in yourself because you can't forget to be grumpy and not be like king grumpy cat chase the pig around the house ignore the squirrels, you'll never catch them anyway. Furrier and even more furrier hairball kitty scratches couch bad kitty yet while happily ignoring when being called and lick yarn hanging out of own butt yet attack the child. My left donut is missing, as is my right relentlessly pursues moth jump five feet high and sideways when a shadow moves. Sleep in the bathroom sink chase mice, play time run up and down stairs.",
    "Sweet roll sesame snaps sesame snaps. Jelly sweet soufflé. Gummies sweet sugar plum gummies macaroon. Ice cream apple pie croissant candy sweet lollipop gummies sesame snaps sugar plum.",
    "Doomsday device? Ah, now the ball's in Farnsworth's court! Ok, we'll go deliver this crate like professionals, and then we'll go ride the bumper cars. It's a T. It goes 'tuh'. You'll have all the Slurm you can drink when you're partying with Slurms McKenzie!",
    "Che guevara French café patron blacksmith by jingo., el snort by jingo. give him what-for mouthbrow blacksmith che guevara clone zone shopper French café patron dali jimi hendrix andrew weatherall, blacksmith mouthbrow andrew weatherall French café patron funny walk brad pitt jimi hendrix freestyle spaghetti western mark lawrenson caterpillar doctor watson. give him what-for theodore roosevelt el snort dali clone zone shopper che guevara by jingo..",
    "?!?!?!?!?!!?!?!",
    "I can't do it....",
    "I'm too dumb to google that",
    "I tried everything",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin elementum nisl nisl, eu vulputate nunc maximus in. Integer eget orci neque. Fusce consectetur auctor dignissim. Proin pellentesque ac lorem id egestas. Proin imperdiet odio quis placerat sollicitudin. In condimentum, ligula vel ornare gravida, turpis diam imperdiet est, ac semper ante risus nec est. Curabitur augue neque, lacinia nec dictum eget, tincidunt in nisl. Sed cursus imperdiet mollis. Maecenas eu tempor massa. Pellentesque semper varius vulputate. Phasellus malesuada et ante eget dignissim. Donec eu eleifend felis."
]

question_tags = [
    "python", "perl", "django", "js", "webpack", "react", "redux", "keras", "tensorflow",
    "tensorboard", "numpy", "pandas", "datascience", "http", "docker", "babel"
]

best_members = [
    "Volodin", "Voloshin", "Dart Veider", "Van Halen", "shkolnik1998", "hellboy3000",
    "DoomGuy", "Elon Musk", "Elon Tusk"
]


def main(request):
    template = loader.get_template("index.html")
    
    context = {
        "title": "New Question",
        "questions": [
            {
                "id": 42,
                "title": np.random.choice(titles),
                "text": np.random.choice(texts),
                "tags": [np.random.choice(question_tags) for _ in range(np.random.randint(1, 5))],
                "answers_amount": np.random.randint(100)
            } for _ in range(50)
        ],
        "side_tags": {
            "title": "Popular Tags",
            "tags": question_tags
        },
        "best_members": {
            "title": "Best Members",
            "tags": best_members
        }
    }
    return HttpResponse(template.render(context, request))


def hot(request):
    template = loader.get_template("index.html")
    context = {
        "title": "Hot Questions",
        "side_tags": {
            "title": "Popular Tags",
            "tags": question_tags
        },
        "best_members": {
            "title": "Best Members",
            "tags": best_members
        }
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
        ],
        "side_tags": {
            "title": "Popular Tags",
            "tags": question_tags
        },
        "best_members": {
            "title": "Best Members",
            "tags": best_members
        }
    }
    return HttpResponse(template.render(context, request))


def question(request, question_id):
    template = loader.get_template("question.html")
    context = {
        "title": "Question #{}".format(question_id),
        "side_tags": {
            "title": "Popular Tags",
            "tags": question_tags
        },
        "best_members": {
            "title": "Best Members",
            "tags": best_members
        }
    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template("login.html")
    context = {
        "title": "Log In",
        "side_tags": {
            "title": "Popular Tags",
            "tags": question_tags
        },
        "best_members": {
            "title": "Best Members",
            "tags": best_members
        }
    }
    return HttpResponse(template.render(context, request))


def signup(request):
    template = loader.get_template("signup.html")
    context = {
        "title": "Sign Up",
        "side_tags": {
            "title": "Popular Tags",
            "tags": question_tags
        },
        "best_members": {
            "title": "Best Members",
            "tags": best_members
        }
    }
    return HttpResponse(template.render(context, request))


def ask(request):
    template = loader.get_template("ask.html")
    context = {
        "title": "Ask your question",
        "side_tags": {
            "title": "Popular Tags",
            "tags": question_tags
        },
        "best_members": {
            "title": "Best Members",
            "tags": best_members
        }
    }
    return HttpResponse(template.render(context, request))

def settings(request):
    template = loader.get_template("settings.html")
    context = {
        "title": "Settings",
        "side_tags": {
            "title": "Popular Tags",
            "tags": question_tags
        },
        "best_members": {
            "title": "Best Members",
            "tags": best_members
        }
    }
    return HttpResponse(template.render(context, request))