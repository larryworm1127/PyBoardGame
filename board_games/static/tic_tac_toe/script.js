// game variable storing useful information
var game = {
    user: '',
    user_two: '',
    computer: '',
    currentPlayer: '',
    pvp: false
};

// set figures corresponding to user selection
function setFig(id) {
    if (id === 'start-computer') {
        game.computer = '<i id="cross" class="fas fa-times"></i>';
        game.user = '<i id="circle" class="far fa-circle"></i>';
        game.currentPlayer = 'computer';
        comp_move()

    } else if (id === 'start-human') {
        game.user = '<i id="cross" class="fas fa-times"></i>';
        game.computer = '<i id="circle" class="far fa-circle"></i>';
        game.currentPlayer = 'user'
    } else {
        game.user = '<i id="cross" class="fas fa-times"></i>';
        game.user_two = '<i id="circle" class="far fa-circle"></i>';
        game.currentPlayer = 'user';
        game.pvp = true
    }
}

// draw the correct symbol onto the grid
function draw(id) {
    let cell = $('#' + id);

    if (game.currentPlayer === 'user') {
        cell.html(game.user);
        cell.removeAttr('onclick');

        if (game.pvp) {
            game.currentPlayer = 'user_two';
        } else {
            game.currentPlayer = 'computer';
            comp_move()
        }

    } else if (game.currentPlayer === 'user_two') {
        cell.html(game.user_two);
        cell.removeAttr('onclick');
        game.currentPlayer = 'user';
    }
}

// calls python function to get the appropriate move
function comp_move() {
    console.log("computer move");
    game.currentPlayer = 'user';
}

