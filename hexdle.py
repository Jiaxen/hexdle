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

    @staticmethod
    def validate_guess(guess):
        if len(guess) != 6:
            return False
        for i in guess:
            if i not in '0123456789ABCDEF':
                return False
        return True

    def guess_hex(self, guess):
        if not self.validate_guess(guess):
            raise ValueError('Not a valid colour!')
        else:
            ans_hex = self.answer_hex()[1:]
            response = [''] * 6
            for i, v in enumerate(guess):
                if ans_hex[i] == v:
                    response[i] = 'green'
                    guess = self.replace_index(guess, i)
                    ans_hex = self.replace_index(ans_hex, i)
            for i, v in enumerate(guess):
                if v != '_':
                    loc = ans_hex.find(v)
                    if loc >= 0:
                        response[i] = 'yellow'
                        ans_hex = self.replace_index(ans_hex, loc)
                    else:
                        response[i] = 'red'
            self.guesses += 1
            return response

    @staticmethod
    def replace_index(ans_hex, loc):
        ans_hex = ans_hex[:loc] + '_' + ans_hex[loc + 1:]
        return ans_hex