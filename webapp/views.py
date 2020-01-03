from django.shortcuts import render
from webapp.models import *

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def guesser(request):
    # Create a new board for this game
    board = Board.objects.create()
    board.generate_words()

    return render(request, 'guesser_board.html', {'words': board.word.all()})


def master(request):
    # Get the most recently generated board
    latest = Board.objects.latest('timestamp')
    board = Board.objects.filter(timestamp=latest.timestamp)[0]

    # Collect the classifications in an html class compatible format
    classifications = []
    for word in board.word.all():
        if word.classification == 'R':
            classifications.append('red')
        elif word.classification == 'B':
            classifications.append('blue')
        elif word.classification == 'X':
            classifications.append('assasin')
        elif word.classification == 'N':
            classifications.append('neutral')

    return render(request,'master_board.html', {'words': board.word.all(),
                                                 'classifications': classifications})
