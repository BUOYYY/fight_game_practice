class BaseStage(object):
    STAGES = {
        'Desert': [0, 2, 4],
        'Forest': [1, 3, 5],
        'Mountains': [3, 6, 8],
        'Arctic': [4, 7, 9]
    }

    def __init__(self, type):
        self.type = type
        self.modifier = self._attribute_modifier()

    def _attribute_modifier(self, cls):
        attr_mod = cls.STAGES[self.type]
        return attr_mod


class StageGen(BaseStage):
    def __init__(self, type):
        super(StageGen, self).__init__(type)

    def attribute_calc(self, ap):
        power = ap
        for n in self.modifier:
            if n in ap:
                power = power * 2
        return power


class Stage(StageGen):
    def __init__(self, type):
        super(Stage, self).__init__(type)

    def prepare(self, player):
        stats = self.attribute_calc(player)
        return stats
