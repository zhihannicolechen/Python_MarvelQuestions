from components import vars
from PIL import Image
from emoji import emojize


def total(value):
    # do some test

    if value <= 20:
        print("You are most similar with ", vars.characters[2], "!")
        im = Image.open("Loki.jpg")
        im.show()

    elif value <= 30:
        print("You are most similar with ", vars.characters[1],"!")
        im = Image.open("BlackWidow.jpg")
        im.show()

    elif value <= 40:
        print ("You are most similar with ", vars.characters[0],"!")
        im = Image.open("hulk.png")
        im.show()

    elif value <= 70:
        print ("You are most similar with ", vars.characters[3],"!")
        im = Image.open("Iron_man.jpg")
        im.show()
