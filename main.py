from random import randint
from card import Card
from bingogame import Gamer
from typing import List


class LotoGame:
    def __init__(self, gamers: List[Gamer]):
        # набор игроков для игры
        self.gamers = gamers
        #         минимальный номер первого боченка
        self.min_number = 1
        # максимальный номер последнего боченка
        self.max_number = Card.numbers_per_letter * Card.limit_line
        # список победителей
        self.winners: List[Gamer] = []
        # список выпавших номеров
        self.draw_numbers: List[int] = []
        #         шаг игры
        self.progress = 0

    def start(self) -> tuple[int, List[Gamer]]:
        while True:
            self.step_game()
            self.check_winners()
            if len(self.winners) > 0:
                break
        return self.progress, self.winners

    def step_game(self):
        while True:
            # берем случ число от мин до макс
            current_num = randint(self.min_number, self.max_number)
            # проверяем чтоб номер не выпадал а если есть то повторяем на новый
            if current_num not in self.draw_numbers:
                # запоминаем выпавший номер
                self.draw_numbers.append(current_num)
                break

        for gamer in self.gamers:
            #         игроки проверяют карточки
            gamer.mark_number(current_num)
            #         проверяем не выйграла ли карточка
            gamer.check_winner()

        self.progress += 1

    def check_winners(self):
        for gamer in self.gamers:
            if gamer.winner:
                self.winners.append(gamer)


if __name__ == '__main__':
    players_name = ['Oleksandra', 'Helen', 'Anna', 'Gosha', 'Nadya']

    gamers = []
    for name in players_name:
        card = Card()
        gamer = Gamer(name, card)
        gamers.append(gamer)

    game = LotoGame(gamers)
    quantity, winners = game.start()
    print(f"Колличество шагов {quantity}")
    print(f"Выпавшие номера {game.draw_numbers}")
    for winner in winners:
        print(f"Победитель {winner.name}")
        winner.card.pretty_info()
