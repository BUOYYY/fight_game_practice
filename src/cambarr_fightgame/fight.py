from stage import Stage
from player import Player


class FightEngine(object):
    def __init__(self, stage, *players):
        self.rounds = 3
        self.players = []
        self.stage = Stage(stage)
        for player in players:
            self.players.append(Player(player))

    def _create_match(self):
        '''
        Returns Match object with array of players and their attributes
            ie.. p = [player1, player2]
                 p[0].ap = 20,
                 p[1].ap = 50
        '''
        match = MatchMaker(self.stage, self.players)
        return match

    def _fight(self):
        self.match = self._create_match()
        top_player_index = 0
        for i, p in enumerate(self.match.players):
            print("Player{i} has an AP of {p.ap}")
            if p.ap > self.match.players[top_player_index].ap:
                top_player_index = i
        return top_player_index

    def start_round(self):
        while self.rounds is not 0:
            win = self._fight()
            self.match.players[win].win += 1
            self.rounds -= 1


class MatchMaker(object):
    def __init__(self, stage, players):
        if len(players) == 2:
            self.players = players
        else:
            raise ValueError("Only exactly 2 players are \
                supported at this time by MatchMaker")
        self._start_match(stage)

    def _start_match(self, stage):
        for p in self.players:
            p.ap = stage.prepare(p)
