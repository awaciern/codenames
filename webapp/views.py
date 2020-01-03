from django.shortcuts import render
from webapp.models import *

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def guesser(request):
    # Create a new board for this game
    board = Board.objects.create()
    board.generate_words()
    print(board.word.all())

    return render(request, 'guesser_board.html', {'words': board.word.all()})
