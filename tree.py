# tree.py

class Node:

    def __init__(
        self,
        text,
        choice1=None,
        choice2=None,
        next1=None,
        next2=None,
        ending=False,
        image=None,
        sound=None,
        title=""
    ):

        # Cerita / narasi node
        self.text = text
        self.title = title

        # Pilihan player
        self.choice1 = choice1
        self.choice2 = choice2

        # Node berikutnya
        self.next1 = next1
        self.next2 = next2

        # Apakah node ini ending?
        self.ending = ending

        # Gambar dan suara untuk node ini
        self.image = image
        self.sound = sound