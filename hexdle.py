from random import randint


class Hexdle:
    def __init__(self):
        self.red = randint(0, 255)
        self.green = randint(0, 255)
        self.blue = randint(0, 255)
        self.guesses = 0

    def hex_format(self):
        return '{:02X}{:02X}{:02X}'.format(self.red, self.green, self.blue)

    def guess_hex(self, guess):
        ans_hex = self.hex_format()
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

    def replace_index(self, ans_hex, loc):
        ans_hex = ans_hex[:loc] + '_' + ans_hex[loc + 1:]
        return ans_hex


if __name__ == '__main__':
    a = Hexdle()
    print(a.hex_format())
    print(a.guess_hex('FFAABB'))
