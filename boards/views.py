from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from boards.models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

# boards_names = list()
#
#   for board in boards:
#       boards_names.append(board.name)
#
#   response_html = '<br>'.join(boards_names)
#
#   return HttpResponse(response_html)
