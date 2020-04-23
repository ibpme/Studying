n = int(input("Number of Players: "))
player = {}

class Game:
    num_of_players = 0
    pot = 0
    raise_max = 0

    def __init__(self, name, cash, condition, call_amount):
        """
        Name: The players name
        Cash: Amount of cash the player has.
        Condition: fold,call,raise or check
        Call Amount : The amount of money required to call; if =0 is check
        PlayerNumber : The initialize player number
        """
        self.name = name
        self.cash = cash
        self.condition = condition
        self.call_amount = call_amount
        self.player_number = num_of_players+1
        Game.num_of_players += 1

    @classmethod
    def from_input(cls):
        """Gets input for the game"""
        return cls(
            input('Nama: '),
            int(input('Cash: ')), 'check', 0, )

    def cashIn(self, value):
        """Event that happens to the player when it puts money on the pot"""
        self.cash = int(self.cash - value)
        Game.pot += value


    def get_condition(self,initialCondition):
        """This method tries to apply a condtion with the set_condition method
        by taking an input and the initialCondition of the player"""

        if initialCondition =='check':
            letter_condition=input("Check(C)/Raise(R)/Fold(F): ")
        else:
            letter_condition=input("Call(C)/Raise(R)/Fold(F): ")
        if letter_condition=='C' or letter_condition=='c' or letter_condition=='call':
            set_condition('call')
        elif letter_condition=='R' or letter_condition=='r' or letter_condition=='raise':
            set_condition('raise')
        elif letter_condition=='F' or letter_condition=='f' or letter_condition=='fold':
            set_condition('fold')
        elif letter_condition=='SPLIT' or letter_condition=='split':
            set_condition('split')
        elif letter_condition=='Q' or letter_condition=='q' or letter_condition=='quit':
            pass
        elif letter_condition=='RG' or letter_condition=='rg' or letter_condition=='restart' or letter_condition== 'restartgame':
            pass
        else: #If plalyer gives an invalid input it repeats the function until otherwise
            print('Invalid Input!')
            print('Q:to quit game', 'RG to restart')
            self.get_condition(initialCondition)

    def set_condition(self,_condition):
        """
        Changing the condition for the player for values : 'raise' 'fold' 'check' 'call'
        """
        self.condition = _condition
        if _condition == 'fold' or 'check':
            self.call_amount = 0



def game():
    for i in range(n):
        print('')
        if player[i].condition == 'fold':
            pass
        else:
            print(player[i].name, player[i].cash)
            player[i].get_condition(player[i].condition)
            if player[i].condition=='call':
                player[i].cashIn(player[i].call_amount)
                player[i].call_amount = 0
            elif player[i].condition=='raise':
                raise_amount = int(input(" Enter Raise Amount: "))  # The raise
                player[i].call_amount = raise_amount - Game.raise_max  # How much value is added from the raise
                Game.raise_max = raise_amount  # The change in raise max
                player[i].cashIn(raise_amount)
                for k in range(n):  # update the raise_max database
                    if k != i:
                        player[k].call_amount = player[k].call_amount + player[i].call_amount
                player[i].call_amount = 0
            elif player[i].condition=='fold':
                pass
            elif player[i].condition=='split':
                num_of_split = n
                for split in range(n):
                    if player[split].condition == 'fold':
                        num_of_split -= 1
                Game.pot = Game.pot / num_of_split
                for win in range(n):
                    if player[win].condition == 'fold':
                        pass
                    else:
                        player[win].cash = int(player[win].cash + Game.pot)
                Game.pot = 0
                print('')
                for p in range(n):
                    print(player[p].name, player[p].cash)
                restart_game()
            elif letter_condition == 'QUIT':
                quit_game()
            print(player[i].name, player[i].cash)
        check_call()
        if check_fold():
            for j in range(n):
                if player[j].condition != 'fold':
                    player[j].win()
            print('')
            for p in range(n):
                print(player[p].name, player[p].cash)
            restart_game()
    game()


player_input()
restart_game()
