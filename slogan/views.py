from slogan.models import Slogan
from django.http import HttpResponse
import json
import random

# Create your views here.


def get_slogan(request):
    s = Slogan.objects
    count = len(s.all())
    i = random.randint(0, count - 1)
    data = s.values('text', 'by').all()[i]
    return HttpResponse(json.dumps(data))
