""" Imagine you are creating a Super Mario game. You need to define
a class to represent Mario. What would it look like? If you aren't
familiar with SuperMario, use your own favorite video or board game
to model a player."""

class Player(object):
    def __int__(self, player_name):
        self._player_name = player_name
        self._lives = 3
        self._height = 80
        self._width = 40

    def draw_player(self, sprite):
        pass

    def life_count(self):
        pass

    def spawn(self):
        pass

    def move(self, velocity):
        pass

    def jump(self, height):
        pass

    def score(self):
        pass
