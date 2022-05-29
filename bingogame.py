from card import Card


class Gamer:
    def __init__(self, name: str, card: Card):
        self.card = card
        self.name = name
        self.winner = False

    # метод проверки выйгр. ли карта игрока
    def check_winner(self):
        #     проверить горизонтальные линии
        for row in self.card.values():
            if sum(row) == 0:
                self.winner = True
        for i in range(self.card.limit_line):
            row = []
            for key in self.card.keys():
                row.append(self.card[key][i])
            if sum(row) == 0:
                self.winner = True
    # проверить вертикальные линии

    # отмечаем выпавший номер(и обнуляем его в карте)
    def mark_number(self, num: int):
        for line in self.card.values():
            if num in line:
                for i in range(len(line)):
                    if line[i] == num:
                        line[i] = 0
