from typing import Dict, List




ROOM_DETAILS: Dict[str, List] = {}

class User:

    def __init__(self, name:str, balance:int=10000) -> None:
        self.name = name
        self.balance = balance
        self.in_game = False

    # check that user have enough balance
    def validate_balance(self, number:int):
        if number < self.balance:
            return True
        return False

    # deduct balance on bet
    def deduct_balance(self, number:int):
        self.balance -= number

    # add balance on winning
    def add_balance(self, number:int):
        self.number += number


class TeenPatti:

    room_limit = 5

    def __init__(self, room_name:str):
        self.cards_distributed = False
        self.game_started = False
        self.room_name = room_name
        self.players = 0
        self.active_player = []
        self.folded_player = []

        if room_name not in ROOM_DETAILS:
            ROOM_DETAILS[room_name] = {'users': []}

        print("Room Created With The Name: ", room_name)

    # start game
    def start_game(self):
        if len(self.active_player) < 3:
            return ("Need at least 3 players to start the game", 0)
        self.game_started = True
        self.distribute_cards()
        return ("Game is started", 1)

    # distribute cards
    def distribute_cards(self):
        print("Distributed Card")
        self.cards = {}
        #TODO: From json import cards and randomly distribute 3 cards

    # join room
    def join_room(self, user:User):
        if self.players <= self.room_limit:
            self.active_player.append(user)
            print(f"Player {user} has joined the room")
        print("Room is full")

    # record player stats
    def record_player_stats(self):
        pass


    # perform show side
    def perform_show(self):
        pass

    # fold after show side
    def fold(self):
        pass

    # define winning condition
    def winning_conditions(self):
        pass
    
    def check_user_is_folded(self):
        pass

    def table_history_user_wise(self):
        pass