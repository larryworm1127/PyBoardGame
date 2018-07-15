var game = {
    currentNumHtml: '',
    currentNum: 0,
    pencil: false,
    start: new Date().getTime(),
    time: 0,
    elapsed: '0.0',
    paused: false
};

const num_ref = {
    'one': ['<p class="not-pencil">1</p>', '<p class="pencil">1</p>', 1],
    'two': ['<p class="not-pencil">2</p>', '<p class="pencil">2</p>', 2],
    'three': ['<p class="not-pencil">3</p>', '<p class="pencil">3</p>', 3],
    'four': ['<p class="not-pencil">4</p>', '<p class="pencil">4</p>', 4],
    'five': ['<p class="not-pencil">5</p>', '<p class="pencil">5</p>', 5],
    'six': ['<p class="not-pencil">6</p>', '<p class="pencil">6</p>', 6],
    'seven': ['<p class="not-pencil">7</p>', '<p class="pencil">7</p>', 7],
    'eight': ['<p class="not-pencil">8</p>', '<p class="pencil">8</p>', 8],
    'nine': ['<p class="not-pencil">9</p>', '<p class="pencil">9</p>', 9]
};

// game core functions
function setNum(id) {
    console.log(id);
    $('#' + id).html(game.currentNumHtml);
}

function selectNum(id) {
    console.log(id);
    if (game.pencil) {
        game.currentNumHtml = num_ref[id][1]
    } else {
        game.currentNumHtml = num_ref[id][0];
    }

    game.currentNum = num_ref[id][2];
    $('#currentNum').text("Current Number: " + game.currentNum)
}

// util functions
function togglePencil() {
    if (game.pencil) {
        game.pencil = false;
        $('#pencilOn').text("Pencil: Off")
    } else {
        game.pencil = true;
        $('#pencilOn').text("Pencil: On")
    }

    console.log(game.pencil)
}

function timer() {
    game.time += 100;

    game.elapsed = Math.floor(game.time / 100) / 10;
    if (Math.round(game.elapsed) === game.elapsed) {
        game.elapsed += '.0';
    }

    $('#time').text("Time: " + game.elapsed + 's');

    var diff = (new Date().getTime() - game.start) - game.time;
    window.setTimeout(timer, (100 - diff));
}

window.setTimeout(timer, 100);
