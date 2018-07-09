var game = {
    user: '',
    computer: '',
    currentPlayer: ''
};

function setFig(id) {
    if (id === 'start-computer') {
        game.computer = '<i id="cross" class="fas fa-times"></i>';
        game.user = '<i id="circle" class="far fa-circle"></i>';
        game.currentPlayer = 'computer'
    } else if (id === 'start-human') {
        game.user = '<i id="cross" class="fas fa-times"></i>';
        game.computer = '<i id="circle" class="far fa-circle"></i>';
        game.currentPlayer = 'user'
    }
}

function draw(id) {
    let cell = $('#' + id);

    if (game.currentPlayer === 'user') {
        cell.html(game.user);
        cell.removeAttr('onclick');
        game.currentPlayer = 'computer';

    } else if (game.currentPlayer === 'computer') {
        cell.html(game.computer);
        cell.removeAttr('onclick');
        game.currentPlayer = 'user';
    }
}

