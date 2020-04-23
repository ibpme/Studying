n = int(input("Number of Players: "))



class Player:
    num_of_players = 0
    def __init__(self, name, cash, condition, call_amount,playerNum):
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
        self.playerNum = playerNum
        Game.num_of_players += 1

    @classmethod
    def from_input(cls,num):
        """Gets input for the game"""
        return cls(
            input('Nama: '),
            int(input('Cash: ')), 'check', 0,num)

class Game(Player):
    pot = 0
    raise_max = 0

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

    def applyRaise(self):
        """
        This method take in a raise value of the player to cash into the pot
        """
        raise_amount=int(input(" Enter Raise Amount: "))
        if raise_amount< Game.raise_max :
            print('Not A Valid Raise')
            self.applyRaise()
        self.call_amount = raise_amount - Game.raise_max
        Game.raise_max = raise_amount
        self.cashIn(raise_amount)
        set_condition('check')

    def win(self):
        self.cash = int(self.cash + Player.pot)
        Player.pot = 0

    def check_fold():
        f = 0
        for folds in player:  # fold checking
            if player[folds].condition == 'fold':
                f += 1
        return True if f == n - 1 else False

    def check_call():  # Check the consecutive call made after a raise
        c = 0
        for caller in player:
            if player[caller].call_amount == 0:
                c += 1
        Game.raise_max = 0 if c == n else pass

    def restart_game():
        Game.raise_max = 0
        for i in player:
            player[i].condition = 'active'
            player[i].call_amount = 0
        game()

    def quit_game():
        for f in range(n):
            print(player[f].name, player[f].cash)
        x = input("Press Enter to Quit Game: ")
        if x == '':
            quit()


for i in range(n):
    player[i]=Player(input('Name: '),int(input('Cash: ')), 'check', 0,n)
def game():
    for i in range(n):
        print('')
        if getattr(Player,'num') == 'fold':
            pass
        else:
            print(player[i].name, player[i].cash)
            player[i].get_condition(player[i].condition)
            if player[i].condition=='call':
                player[i].cashIn(player[i].call_amount)
                player[i].call_amount = 0
            elif player[i].condition=='raise':
                player[i].applyRaise()
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
                Game.restart_game()
            elif letter_condition == 'QUIT':
                Game.quit_game()
            print(player[i].name, player[i].cash)
        Game.check_call()
        if Game.check_fold():
            for j in range(n):
                if player[j].condition != 'fold':
                    player[j].win()
            print('')
            for p in range(n):
                print(player[p].name, player[p].cash)
            Game.restart_game()
    game()


player_input()
restart_game()
