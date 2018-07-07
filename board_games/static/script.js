var game = {
    user: '',
    computer: ''
};

function start() {
    $('#startModal').modal('show');
}

function setFig(id) {
    if (id === 'x') {
        game.user = '<span class="fa fa-times"></span>';
        game.computer = '<span class="fa fa-circle-o"></span>';
    } else if (id === 'o') {
        game.user = '<span class="fa fa-circle-o"></span>';
        game.computer = '<span class="fa fa-times"></span>';
    }
}

setTimeout(start, 600);