from random import randint


class Hexdle:
    def __init__(self, red=randint(0, 255), green=randint(0, 255), blue=randint(0, 255)):
        self.red = red
        self.green = green
        self.blue = blue
        self.guesses = 0

    def answer_hex(self):
        return '#{:02X}{:02X}{:02X}'.format(self.red, self.green, self.blue)

    def guesses(self):
        return self.guesses

    def guess_hex(self, guess):
        ans_hex = self.answer_hex()[1:]
        response = []
        for i, v in enumerate(guess):
            loc = ans_hex.find(v)
            if loc >= 0:
                if loc == i:
                    response.append('Yes')
                    ans_hex = self.replace_index(ans_hex, loc)
                else:
                    response.append('Misplaced')
                    ans_hex = self.replace_index(ans_hex, loc)
            else:
                response.append('No')
        self.guesses += 1
        return response

    @staticmethod
    def replace_index(ans_hex, loc):
        ans_hex = ans_hex[:loc] + '_' + ans_hex[loc + 1:]
        return ans_hex

