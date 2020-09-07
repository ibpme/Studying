export class Player {
  constructor(name, cash, num) {
    this.playerNum = num;
    this.name = name;
    this.cash = cash;
    this.status = {
      fold: false,
      requiredCall: 0,
      action: "check",
    };
  }
  cashIn(amount) {
    //Method is applied when a player puts money on the pot
    this.cash = this.cash - amount;
    Game.pot += amount;
    this.status.requiredCall = 0;
    this.status.action = "check";
  }
  winner() {
    //Method applied on the winner by adding the game pot to the player cash
    this.cash = this.cash + Game.pot;
    Game.pot = 0;
  }
  gameAction(action) {
    this.status.action = action;
    switch (action) {
      case "raise":
        const raiseAmount = 500;
        this.raise(raiseAmount);
        break;
      case "fold":
        this.fold();
        break;
      case "call":
        this.checkOrCall();
        break;
    }
  }
  checkOrCall() {
    this.cashIn(this.status.requiredCall);
  }
  raise(amount) {
    if (amount < Game.currentHighestRaise) {
      console.log("Not valid Raise");
      this.gameAction("raise");
    }
    this.cashIn(amount);
    Game.adjustRequiredCalls(amount, player.playerNum);
  }
  fold() {
    this.status.fold = true;
    this.status.requiredCall = 0;
  }
}

export class CreateGame {
  constructor() {
    this.players = [];
    this.numOfPlayers = 0;
    this.pot = 0;
    this.currentHighestRaise = 0;
  }
  createPlayer(name, cash) {
    //Create and push the created player object into the game class
    const player = new Player(name, cash, this.numOfPlayers);
    this.numOfPlayers = this.numOfPlayers + 1;
    this.players.push(player);
  }
  checkActivePlayers() {
    //Check each player for an active(not in fold status) status to continue the game
    //If the number of players active is equal to 1 then the method returns true
    let numOfActivePlayers = 0;
    this.players.forEach((player) => {
      if (!player.status.fold) {
        numOfActivePlayers++;
      }
    });
    return numOfActivePlayers === 1;
  }
  adjustRequiredCalls(raiseAmount, playerNum) {
    //After a raise amount is made this method checks each player's requiredCall amount
    this.players.forEach((player) => {
      if (playerNum !== player.playerNum) {
        player.requiredCall += raiseAmount - Game.currentHighestRaise;
      }
    });
    Game.currentHighestRaise = raiseAmount;
  }
}
