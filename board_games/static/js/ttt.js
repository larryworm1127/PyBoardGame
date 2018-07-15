// game variable storing useful information
var game = {
    user: '',
    user_two: '',
    computer: '',
    currentPlayer: '',
    pvp: false,
};

// constants
const computer = 0;
const user = 1;
const user_two = 2;

// other variables
symbol = {
    'circle': ['<i id="circle" class="far fa-circle"></i>', 'O'],
    'cross': ['<i id="cross" class="fas fa-times"></i>', 'X']
};

// set figures corresponding to user selection
function setFig(id) {
    if (id === 'start-computer') {
        game.computer = symbol.cross;
        game.user = symbol.circle;
        game.currentPlayer = computer;

        $('#prompt').text(promptText(game.computer[1]));
        setup();
        comp_first_move()

    } else if (id === 'start-human') {
        game.user = symbol.cross;
        game.computer = symbol.circle;
        game.currentPlayer = user;

        $('#prompt').text(promptText(game.user[1]));
        setup();

    } else if (id === 'pvp') {
        game.user = symbol.cross;
        game.user_two = symbol.circle;
        game.currentPlayer = user;
        game.pvp = true;

        $('#prompt').text(promptText(game.user[1]));
        setup();
    }

    $('.game-field').attr('onclick', 'draw(this.id)');

    // disable other options
    $('#start-human').removeAttr('onclick');
    $('#start-computer').removeAttr('onclick');
    $('#pvp').removeAttr('onclick')
}

// draw the correct symbol onto the grid
function draw(id) {
    let cell = $('#' + id);

    if (game.currentPlayer === user) {
        cell.html(game.user[0]);
        cell.removeAttr('onclick');

        update(id, game.user[1]);
        switchPlayer(user)

    } else if (game.currentPlayer === user_two) {
        cell.html(game.user_two[0]);
        cell.removeAttr('onclick');

        update(id, game.user_two[1]);
        switchPlayer(user_two);

    } else if (game.currentPlayer === computer) {
        cell.html(game.computer[0]);
        cell.removeAttr('onclick');

        update(id, game.computer[1]);
        switchPlayer(computer)
    }

    checkWin()
}

// computer player control functions
function comp_first_move() {
    draw('two-two')
}

function comp_move() {
    $(function () {
        $.getJSON("/games/ttt/get_move", {}, function (data) {
            console.log(data.result);
            console.log(data.id);
            draw(data.id)
        });
        return false;
    });

    $('.game-field').attr('onclick', 'draw(this.id)')
}

/* util functions */
function switchPlayer(currentUser) {
    if (currentUser === user) {
        if (game.pvp) {
            game.currentPlayer = user_two;
            $('#prompt').text(promptText(game.user_two[1]));
        } else {
            game.currentPlayer = computer;
            $('.game-field').removeAttr('onclick');
            $('#prompt').text(promptText(game.computer[1]));

            setTimeout(function () {
                comp_move()
            }, 500)
        }

    } else if (currentUser === computer || currentUser === user_two) {
        game.currentPlayer = user;
        $('#prompt').text(promptText(game.user[1]));
    }
}

function promptText(symbol) {
    return 'Player ' + symbol + ' turn!'
}

function endGame() {
    $('.game-field').removeAttr('onclick');

    $('#start-human').attr('onclick', 'reset()');
    $('#start-computer').attr('onclick', 'reset()');
    $('#pvp').attr('onclick', 'reset()')
}

/* back-end functions */
function update(id, symbol) {
    $(function () {
        $.getJSON("/games/ttt/update", {
            id: id,
            symbol: symbol
        }, function (data) {
            console.log(data.result)
        });
        return false;
    });
}

function setup() {
    $(function () {
        $.getJSON("/games/ttt/setup", {
            human: game.user[1],
            pvp: game.pvp
        })
    });
}

function checkWin() {
    $(function () {
        $.getJSON("/games/ttt/check_win", {}, function (data) {
            if (data.state === 'end') {
                console.log(data.result);
                $('#prompt').text(data.result + '\nPress any figure to restart.');
                reset_game_var();
                endGame()
            }
        });
        return false;
    });
}

/* reset function */
function reset() {
    reset_game_var();
    let gameField = $('.game-field');
    gameField.html('');
    $('#prompt').text('Who will start over?');

    $('#start-human').attr('onclick', 'setFig(this.id)');
    $('#start-computer').attr('onclick', 'setFig(this.id)');
    $('#pvp').attr('onclick', 'setFig(this.id)');
}

function reset_game_var() {
    game.currentPlayer = '';
    game.computer = '';
    game.user_two = '';
    game.user = '';
    game.pvp = false;
}
