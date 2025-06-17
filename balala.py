class Score:
    def __init__(self, base_chips, base_mult):
        self.base_chips = base_chips
        self.base_mult = base_mult
        self.chips = base_chips
        self.mult = base_mult

    def __str__(self):
        return f"{self.chips} X {self.mult}"

    def reset(self):
        self.chips = self.base_chips
        self.mult = self.base_mult

    def calculate(self):
        ret = self.chips * self.mult
        print()
        print(str(self) + " = " + str(ret))
        return ret

        
class Step:
    def __init__(self, chips, mult_plus, mult_x):
        self.chips = chips
        self.mult_plus = mult_plus
        self.mult_x = mult_x
        
    def proc(self, score: Score):
        score.chips += self.chips
        score.mult += self.mult_plus
        score.mult *= max(1, self.mult_x)
        print(str(score))
        

class Card(Step):
    def __init__(self, label, chips, mult_plus=0, mult_x=0):
        super().__init__(chips, mult_plus, mult_x)
        self.label = label

    def proc(self, score: Score):
        print(self.label)
        super().proc(score)


class HangingChad(Step):
    def __init__(self, step: Step):
        super().__init__(0, 0, 0)
        self.step = step
        
    def proc(self, score: Score):
        print("\nHanging Chad again")
        self.step.proc(score)
        self.step.proc(score)


class XMult(Step):
    def __init__(self, label, x):
        super().__init__(0, 0, x)
        self.label = label

    def proc(self, score: Score):
        print("\n" + self.label)
        super().proc(score)


class PlusMult(Step):
    def __init__(self, label, mult_plus):
        super().__init__(0, mult_plus, 0)
        self.label = label

    def proc(self, score: Score):
        print("\n" + self.label)
        super().proc(score)


class Baron(XMult):
    def __init__(self):
        super().__init__("Baron", 1.5)


class Campfire(XMult):
    def __init__(self, x=2):
        super().__init__("Campfire", x)


class DriversLicence(XMult):
    def __init__(self):
        super().__init__("Drivers licence", 3)


class Foil(Step):
    def __init__(self):
        super().__init__(50, 0, 0)

    def proc(self, score: Score):
        print("\nFoil")
        super().proc(score)


class Holographic(Step):
    def __init__(self):
        super().__init__(0, 10, 0)

    def proc(self, score: Score):
        print("\nHolographic")
        super().proc(score)


class Gluttonous(PlusMult):
    def __init__(self, card: Card):
        super().__init__("Gluttonous", 3)
        self.card = card
    
    def proc(self, score: Score):
        self.card.proc(score)
        super().proc(score)


def evaluate(score: Score, steps: list[Step]):
    for step in steps:
        step.proc(score)

    ret = score.calculate()
    score.reset()
    return ret