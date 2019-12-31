from webapp.models import Word

with open('csv_version/words.txt', 'r') as words:
    for word in words:
        Word.objects.create(text=word)
