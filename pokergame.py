n = int(input("Number of Players: "))
player = {}


class Player:
    num_of_players = 0
    pot = 0
    raise_max = 0

    def __init__(self, name, cash, condition, call_amount):
        """
        Name: The players name
        Cash: Amount of cash the player has.
        Condition: fold or active
        Call Amount : The amount of money required to call; if =0 is check
        """
        self.name = name
        self.cash = cash
        self.condition = condition
        self.call_amount = call_amount  # sisa call yang bisa dilakukan
        Player.num_of_players += 1

    def cashing(self, value):
        self.cash = int(self.cash - value)
        Player.pot += value

    def fold(self):
        self.condition = 'fold'
        self.call_amount = 0

    def win(self):
        self.cash = int(self.cash + Player.pot)
        Player.pot = 0

    @classmethod
    def from_input(cls):
        return cls(
            input('Nama: '),
            int(input('Cash: ')), 'active', 0, )


def player_input():
    for i in range(n):
        player_info = Player.from_input()
        player[i] = player_info


def check_call():  # Check the consecutive call made after a raise
    c = 0
    for caller in range(n):
        if player[caller].call_amount == 0:
            c += 1
        else:
            pass
    if c == n:
        Player.raise_max = 0
    else:
        pass


def restart_game():
    Player.raise_max = 0
    for i in range(n):
        player[i].condition = 'active'
        player[i].call_amount = 0
    game()


def check_fold():
    f = 0
    for folds in range(n):  # fold checking
        if player[folds].condition == 'fold':
            f += 1
    if f == n - 1:
        return True
    else:
        return False


def quit_game():
    for f in range(n):
        print(player[f].name, player[f].cash)
    x = input("Press Enter to Quit Game: ")
    if x == '':
        quit()

def get_letter_condition(i):
    if player[i].call_amount == 0:
        letter_condition = input("Check(C)/Raise(R)/Fold(F): ")
    else:
        print('Current Raise: ', Player.raise_max)
        print('To Call: ', player[x].call_amount)
        letter_condition = input("Call(C)/Raise(R)/Fold(F): ")
    if letter_condition=='C' or letter_condition=='c' or letter_condition=='call':
        letter_condition='C'
    elif letter_condition=='R' or letter_condition=='r' or letter_condition=='raise':
        letter_condition='R'
    elif letter_condition=='F' or letter_condition=='f' or letter_condition=='fold':
        letter_condition='F'
    elif letter_condition=='SPLIT' or letter_condition=='split':
        letter_condition='SPLIT'
    elif letter_condition=='Q' or letter_condition=='q' or letter_condition=='quit':
        letter_condition='QUIT'
    else: #If plalyer gives an invalid input it repeats the function until otherwise
        print('Invalid Input!')
        print('Q:to quit game', 'RG to restart')
        get_letter_condition(i)

def game():
    for i in range(n):
        print('')
        if player[i].condition == 'fold':
            pass
        else:
            print(player[i].name, player[i].cash)
            get_letter_condition(i)
            if letter_condition == 'C':
                player[i].cashing(player[i].call_amount)
                player[i].call_amount = 0
            elif letter_condition == 'R':
                raise_amount = int(input(" Enter Raise Amount: "))  # The raise
                player[i].call_amount = raise_amount - Player.raise_max  # How much value is added from the raise
                Player.raise_max = raise_amount  # The change in raise max
                player[i].cashing(raise_amount)
                for k in range(n):  # update the raise_max database
                    if k != i:
                        player[k].call_amount = player[k].call_amount + player[i].call_amount
                player[i].call_amount = 0
            elif letter_condition == 'F':
                player[i].fold()
            elif letter_condition == 'SPLIT':
                num_of_split = n
                for split in range(n):
                    if player[split].condition == 'fold':
                        num_of_split -= 1
                Player.pot = Player.pot / num_of_split
                for win in range(n):
                    if player[win].condition == 'fold':
                        pass
                    else:
                        player[win].cash = int(player[win].cash + Player.pot)
                Player.pot = 0
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
