from random import randint
from collections import UserDict


class Card(UserDict):
    numbers_per_letter = 15
    limit_line = 5
    loto_fields = ["B", "I", "N", "G", "O"]

    def __init__(self):
        super().__init__()
        self.start_num = 1
        self.end_num = self.numbers_per_letter
        self.create_card()

    def create_card(self):
        for letter in self.loto_fields:
            self.data[letter] = []

            while len(self.data[letter]) < self.limit_line:
                next_num = randint(self.start_num, self.end_num)
                if next_num not in self.data[letter]:
                    self.data[letter].append(next_num)

            self.start_num = self.end_num + 1
            self.end_num = self.end_num + self.numbers_per_letter

    def pretty_info(self) -> None:
        # view = ''
        # view = view + '{:^5}{:^5}{:^5}{:^5}{:^5}'.format(*self.data) + '\n'
        print('{:^5}{:^5}{:^5}{:^5}{:^5}'.format(*self.data))
        for i in range(self.limit_line):
            line = []
            for letter in self.loto_fields:
                line.append(self.data[letter][i])
            # view = view + '{:^5}{:^5}{:^5}{:^5}{:^5}'.format(*line) + '\n'
            # print(view)
            line.clear()


if __name__ == '__main__':
    card = Card()
    print(card)
    card.pretty_info()
