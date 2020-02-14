from django.contrib.auth.models import User
from qa.models import Question, Answer
from random import randint

def rnd_str(m):
    s = ''
    for _ in range(m):
        s += chr(randint(65, 90))
    return s

# Create Users
for _ in range(5):
    User.objects.create_user(username=rnd_str(5))

# Questions & Answers
for _ in range(15):
    Question.objects.create(title=rnd_str(5), text=rnd_str(10), rating=randint(0, 10), author=User.objects.get(id=randint(1,5)))
    Answer.objects.create(text=rnd_str(10), author=User.objects.get(id=randint(1,5)), question_id=_)
    Answer.objects.create(text=rnd_str(10), author=User.objects.get(id=randint(1,5)), question_id=_)
