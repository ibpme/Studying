player = {}
n=0

def main():##TODO Make execption Trial for Input
    global n
    n = int(input("Number of Players: "))
    global player
    for t in range(n):
        playerName=input('Name: ')
        playerCash=int(input('Cash: '))
        player[t] = Player(playerName,playerCash, 'check', 0, t)
    Game.restart_game()

class Player:

    def __init__(self, name, cash, condition, call_amount, playerNum):
        """
        Name: The players name
        Cash: Amount of cash the player has.
        Condition: fold - active (call,raise or check)
        Call Amount : The amount of money required to call; if =0 is check
        PlayerNumber : The initialize player number
        """
        self.name = name
        self.cash = cash
        self.condition = condition
        self.call_amount = call_amount
        self.playerNum = playerNum

    @classmethod
    def from_input(cls, num):
        """Gets input for the game"""
        return cls(
            input('Nama: '),
            int(input('Cash: ')), 'check', 0, num)

    def cashIn(self):
        """Event that happens to the player when it puts money on the pot"""
        self.cash = int(self.cash - self.call_amount)
        Game.pot += self.call_amount
        self.call_amount = 0
        self.set_condition('check')

    def win(self):
        """Event that happens to the player when he wins"""
        self.cash = int(self.cash + Game.pot)
        Game.pot = 0

    def get_condition(self, initialCondition):
        """This method tries to apply a condition with the set_condition method
        by taking an input and the initialCondition of the player"""

        if initialCondition == 'check':
            letter_condition = input("Check(C)/Raise(R)/Fold(F): ")
        else:
            print('Current Raise: ', Game.raise_max)
            print('To Call: ', self.call_amount)
            letter_condition = input("Call(C)/Raise(R)/Fold(F): ")
        if letter_condition == 'C' or letter_condition == 'c' or letter_condition == 'call':
            if initialCondition == 'check':
                self.set_condition('check')
            elif initialCondition == 'call':
                self.set_condition('call')
        elif letter_condition == 'R' or letter_condition == 'r' or letter_condition == 'raise':
            self.set_condition('raise')
        elif letter_condition == 'F' or letter_condition == 'f' or letter_condition == 'fold':
            self.set_condition('fold')
        elif letter_condition == 'SPLIT' or letter_condition == 'split':
            self.set_condition('split')
        elif letter_condition == 'Q' or letter_condition == 'q' or letter_condition == 'quit':
            self.set_condition('QUIT')
        elif letter_condition == 'RG' or letter_condition == 'rg' or letter_condition == 'restart' or \
                letter_condition == 'restartgame':
            Game.restart_game()
        else:  # If player gives an invalid input it repeats the function until otherwise
            print('Invalid Input!')
            print('Q:to quit game', 'RG to restart')
            self.get_condition(initialCondition)

    def set_condition(self, _condition):
        """
        Changing the condition for the player for values : 'raise' 'fold' 'check' 'call'
        """
        self.condition = _condition
        if _condition == 'fold' or _condition == 'check':
            self.call_amount = 0
        else:
            pass

    def applyRaise(self):
        """
        This method take in a raise value of the player to cash into the pot
        and gives a raise max value to the game(modifies call amount of each player accordingly
        """
        raise_amount = int(input(" Enter Raise Amount: "))
        if raise_amount < Game.raise_max:
            print('Not A Valid Raise')
            self.applyRaise()
        # The process below puts the raise into the pot
        self.call_amount = raise_amount
        self.cashIn()
        # The process puts modifies other players required call_amount
        for k in range(n):
            if k != self.playerNum:
                player[k].call_amount += raise_amount - Game.raise_max
        Game.raise_max = raise_amount


class Game(Player):
    pot = 0
    raise_max = 0

    @staticmethod
    def check_fold():
        f = 0
        for folds in player:
            if player[folds].condition == 'fold':
                f += 1
        if f == n - 1:
            return True
        else:
            return False

    @staticmethod
    def check_call():
        """This method checks the consecutive call to a raise made after a raise to make
        sure that when all raise are a called the maximum raise resets
        then it also apply a condition based on the call amount and intial condition"""
        c = 0
        for caller in player:
            if player[caller].call_amount == 0:
                c += 1
                if player[caller].condition == 'fold':
                    pass
                else:
                    player[caller].condition = 'check'
            else:
                player[caller].condition = 'call'
        if c == n:
            Game.raise_max = 0
        else:
            pass

    @staticmethod
    def restart_game():  # TODO: Set a database storing the cash of each player in every round to be able to reset pot
        """This restart the  game after the pot  is settled"""
        Game.raise_max = 0
        for i in player:
            player[i].condition = 'check'
            player[i].call_amount = 0
        game()

    @staticmethod
    def quit_game():
        for f in range(n):
            print(player[f].name, player[f].cash)
        x = input("Press Enter to Quit Game: ")
        if x == '':
            quit()

def game():
    for i in range(n):
        print('')
        print(player[i].name, player[i].cash)
        player[i].get_condition(player[i].condition)
        if player[i].condition == 'call':
            player[i].cashIn()
        elif player[i].condition == 'raise':
            player[i].applyRaise()
        elif player[i].condition == 'fold':
            pass
        elif player[i].condition == 'split':
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

        elif player[i].condition == 'QUIT':
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

if __name__ == '__main__':
    main()
