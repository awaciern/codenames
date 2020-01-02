from django.db import models
from django.utils import timezone

# Create your models here.
class Word(models.Model):
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text


class Board(models.Model):
    # Class containing info needed for a word on the board
    class BoardWord(models.Model):
        CLASSIFICATION = (
            ('R', 'Red'),
            ('B', 'Blue'),
            ('N', 'Neutral'),
            ('X', 'Assasin'),
        )
        text = models.CharField(max_length=100)
        classification = models.CharField(max_length=1, choices=CLASSIFICATION)
        position = models.IntegerField()

        def __str__(self):
            return '{0}. {1} ({2})'.format(self.position, self.text,
                                           self.classification)

    word = models.ManyToManyField(BoardWord)

    # Creates the board wicells.remove(cells[index])th all 25 words
    def generate_words(self):
        import random

        # Lists for randomized classifications of board posisitions
        positions = list(range(0, 25))
        classifications = [None for i in range(0, 25)]

        # Randomly assign 9 blue positions
        for i in range(0, 10):
            index = random.randint(0, len(positions) - 1)
            classifications[positions[index]] = 'B'
            positions.remove(positions[index])

        # Randomly assign 8 red positions
        for i in range(0, 9):
            index = random.randint(0, len(positions) - 1)
            classifications[positions[index]] = 'R'
            positions.remove(positions[index])

        # Randomly assign 1 assasin position
        index = random.randint(0, len(positions) - 1)
        classifications[positions[index]] = 'X'
        positions.remove(positions[index])

        # Assign remaining 7 positions to netrual
        for pos in positions:
            classifications[pos] = 'N'

        print(classifications)

        # Generate the words and add them to the board
        for i in range(1, 26):
            word = str(Word.objects.order_by('?').first())
            while self.word.filter(text=word):
                word = str(Word.objects.order_by('?').first())
            board_word = Board.BoardWord.objects.create(text=word,
                                                        classification=classifications[i - 1],
                                                        position=i)
            print(board_word)
            self.word.add(board_word)
