from typing import Type

class Player:

    def __init__(self,name:str,cash:int):
        self.name = name
        self.cash = cash
        self.fold = False
        self.required_call = 0
        self.is_player_turn = False
    
    def cash_into_pot(self,amount:int):
        self.cash -= amount
    
    def set_required_calls(self,amount:int):
        self.required_call = amount

    def set_turn(self,state:bool):
        self.is_player_turn = state

    def action_fold(self):
        self.fold = True

    def cash_from_pot(self,amount:int):
        self.cash += amount

class Game :

    def __init__(self,num_of_players:int):
       self.players = []
       self.pot = 0
       self.max_raise = 0
       self.num_of_players = num_of_players

    def new_player(self,name:str,cash:int):
        if len(self.players) == self.num_of_players:
            raise Exception("Players Limit Execeded!")
        player = Player(name,cash)
        self.players.append(player)
        return player

    def list_player_info(self):
        for player in self.players :
            print(player.__dict__)
    
    def info(self):
        print(self.__dict__)

    def add_to_pot(self,amount:int):
        self.pot += amount 
    
    def adjust_required_calls(self):
        if all([player.required_call == 0 for player in self.players]):
            self.max_raise = 0

    def adjust_max_raise(self,current_player:Type[Player],amount:int):
        for player in self.players:
            if not(player is current_player or player.fold) :
                player.set_required_calls(amount-self.max_raise)
            else :
                print(player.name)
        self.max_raise = amount
        self.adjust_required_calls()
    
    def player_raise(self,player:Type[Player],amount:int):
        player.cash_into_pot(amount)
        self.add_to_pot(amount)
        player.set_required_calls(0)
        self.adjust_max_raise(player,amount)

    def player_fold(self,player:Type[Player]):
        player.action_fold()
        player.set_required_calls(0)
        self.adjust_required_calls()

    def player_check_or_call(self,player:Type[Player]):
        player.cash_into_pot(player.required_call)
        self.add_to_pot(player.required_call)
        player.set_required_calls(0)
        self.adjust_required_calls()

    def set_winner(self,player:Type[Player]):
        player.cash_from_pot(self.pot)
        self.new_round()

    def check_win_state(self):            
        active_players = 0
        for player in self.players:
            if not(player.fold) :
                active_players.append(player)
        if len(active_players) == 1 :
            self.set_winner(active_players[0])
        else:
            pass
    
    def new_round(self):
        self.max_raise = 0
        self.pot = 0 
        for player in self.players:
            player.fold = False
        self.set_player_turn(self.players[0])
    
    def set_player_turn(self,current_player:Type[Player]):
        for player in self.players:
            if current_player is player :
                player.set_turn(True)
            else:
                player.set_turn(False)

    def check_player_turn(self)->Type[Player]:
        for player in self.players:
            if player.is_player_turn:
                return player
            else:
                raise Exception("No Round Started")

    def find_next_player_turn(self):
        current_player_turn = self.check_player_turn()
        for player_index in self.num_of_players:
            if current_player_turn == self.players[player_index]:
                current_player_index= player_index

        next_player_index = (current_player_index + 1) % self.num_of_players
        while self.player[next_player_index].fold:
            next_player_index = (current_player_index + 1) % self.num_of_players
        
        self.set_player_turn(self.players[next_player_index])
        
if __name__ == "__main__":
    game = Game(3)
    Budi = game.new_player("Budi",10000)
    Dimas = game.new_player("Dimas",10000)
    Dipta = game.new_player("Dipta",10000)
    game.player_raise(Budi,1000)
    game.list_player_info()
    game.info()
