from django.contrib.auth.models import User
from qa.models import Question, Answer
from random import randint

def rnd_str(m):
    s = ''
    for _ in range(m):
        s += chr(randint(65, 90))
    return s

# Create Users
for i in range(1, 6):
    User.objects.create_user(id=i, username=rnd_str(5))

# Questions & Answers
for i in range(1, 16):
    Question.objects.create(id=i, title=rnd_str(5), text=rnd_str(10), rating=randint(0, 10), author=User.objects.get(id=randint(1,5)))
    Answer.objects.create(text=rnd_str(10), author=User.objects.get(id=randint(1,5)), question_id=i)
    Answer.objects.create(text=rnd_str(10), author=User.objects.get(id=randint(1,5)), question_id=i)
