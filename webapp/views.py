from django.shortcuts import render
from webapp.models import *

# Create your views here.
def display(request):
    # Create a new board for this game
    board = Board.objects.create()
    board.generate_words()
    print(board.word.all())

    return render(request, 'board.html', {'words': board.word.all()})
