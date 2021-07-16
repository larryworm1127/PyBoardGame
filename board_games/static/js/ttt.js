'use strict'

// game variable storing useful information
const game = {
  user: '',
  user_two: '',
  computer: '',
  currentPlayer: '',
  pvp: false,
};

// constants
const COMPUTER = 0;
const USER = 1;
const USER_TWO = 2;
const HTML_INDEX = 0;
const SYMBOL_INDEX = 1;

// other variables
const symbol = {
  'circle': ['<i id="circle" class="far fa-circle"></i>', 'O'],
  'cross': ['<i id="cross" class="fas fa-times"></i>', 'X']
};

// selected elements
const prompt = $('#prompt');
const gameField = $('.game-field');

const startHumanButton = $('#start-human');
const startCompButton = $('#start-comp');
const startPvp = $('#pvp');
$('#surrender').click(reset);
startHumanButton.click(setFig);
startCompButton.click(setFig);
startPvp.click(setFig);

// Set figures corresponding to user selection
function setFig(e) {
  const id = e.target.id;
  if (id === 'start-comp' || id === 'comp-icon') {
    game.computer = symbol.cross;
    game.user = symbol.circle;
    game.currentPlayer = COMPUTER;

    prompt.text(promptText(game.computer[SYMBOL_INDEX]));
    setup();
    comp_move()

  } else if (id === 'start-human' || id === 'human-icon') {
    game.user = symbol.cross;
    game.computer = symbol.circle;
    game.currentPlayer = USER;

    prompt.text(promptText(game.user[SYMBOL_INDEX]));
    setup();

  } else if (id === 'pvp' || id === 'pvp-icon') {
    game.user = symbol.cross;
    game.user_two = symbol.circle;
    game.currentPlayer = USER;
    game.pvp = true;

    prompt.text(promptText(game.user[SYMBOL_INDEX]));
    setup();
  }

  gameField.attr('onclick', 'draw(this.id)');

  // disable other options
  startHumanButton.removeAttr('onclick');
  startCompButton.removeAttr('onclick');
  startPvp.removeAttr('onclick')
}

// Draw the correct symbol onto the grid
function draw(id) {
  const cell = $('#' + id);

  if (game.currentPlayer === USER) {
    cell.html(game.user[HTML_INDEX]);
    cell.removeAttr('onclick');

    update(id, game.user[SYMBOL_INDEX]);
    switchPlayer(USER)

  } else if (game.currentPlayer === USER_TWO) {
    cell.html(game.user_two[HTML_INDEX]);
    cell.removeAttr('onclick');

    update(id, game.user_two[SYMBOL_INDEX]);
    switchPlayer(USER_TWO);

  } else if (game.currentPlayer === COMPUTER) {
    cell.html(game.computer[HTML_INDEX]);
    cell.removeAttr('onclick');

    update(id, game.computer[SYMBOL_INDEX]);
    switchPlayer(COMPUTER)
  }

  checkWin()
}

// Computer player control functions
function comp_move() {
  $.getJSON("/games/ttt/get_move", {}, function (data) {
    draw(data.id)
  });
}

/* Util functions */
function switchPlayer(currentUser) {
  if (currentUser === USER) {
    if (game.pvp) {
      game.currentPlayer = USER_TWO;
      prompt.text(promptText(game.user_two[SYMBOL_INDEX]));
    } else {
      game.currentPlayer = COMPUTER;
      prompt.text(promptText(game.computer[SYMBOL_INDEX]));

      comp_move()
    }

  } else if (currentUser === COMPUTER || currentUser === USER_TWO) {
    game.currentPlayer = USER;
    prompt.text(promptText(game.user[SYMBOL_INDEX]));
  }
}

function promptText(symbol) {
  return 'Player ' + symbol + ' turn!'
}

function endGame() {
  gameField.removeAttr('onclick');

  startHumanButton.click(reset);
  startCompButton.click(reset);
  startPvp.click(reset);
}

/* Back-end functions */
function update(id, symbol) {
  $.getJSON("/games/ttt/update", {
    id: id,
    symbol: symbol
  });
}

function setup() {
  $.get("/games/ttt/setup", {
    human: game.user[SYMBOL_INDEX],
    pvp: game.pvp
  });
}

function checkWin() {
  $.getJSON("/games/ttt/check_win", {}, function (data) {
    if (data.state === 'end') {
      prompt.text(data.result + '\nPress any figure to restart.');
      reset_game_var();
      endGame();
    }
  });
}

/* Reset function */
function reset() {
  reset_game_var();
  gameField.html('');
  prompt.text('Who will start over?');

  startHumanButton.click(setFig);
  startCompButton.click(setFig);
  startPvp.click(setFig);
}

function reset_game_var() {
  game.currentPlayer = '';
  game.computer = '';
  game.user_two = '';
  game.user = '';
  game.pvp = false;
}
