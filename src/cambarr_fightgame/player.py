import time
import hashlib
import uuid


class SeedGenerator(object):
    def __call__(self, name, uuid, time):
        return self._gen_hash(name, uuid, time)

    def _gen_hash(name, uuid, time):
        hash_seed = "{name}{uuid}{time}".encode('utf-8')
        return hashlib.sha256(hash_seed).hexdigest()


class BasePlayer(object):
    def __init__(self, name):
        self.name = name
        self.uuid = self.uuid_gen
        self.ap = 0
        self.wins = 0

    def _uuid_gen():
        return uuid.uuid4()


class PlayerGen(BasePlayer):
    def __init__(self, name):
        super(PlayerGen, self).__init__(name)

    def gen_attack_power(self):
        attackTime = time.strftime("%Y%m%dT%H%M%S")
        self.seed = SeedGenerator(self.name, self.uuid, attackTime)
        return hash(self.seed)

    def get_seed(self):
        return self.seed


class Player(PlayerGen):
    def __init__(self, name):
        super(Player, self).__init__(name)
        self.ap = self._set_ap()

    def _set_ap(self):
        attack_power = self.gen_attack_power()
        self.ap = attack_power
