var game = {
    currentNum: '',
    pencil: false,
    start: '',
    time: 0,
    elapsed: '0.0',
    paused: false,
    undo: 0
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
    if (game.currentNum[2] !== 0) {
        if (game.pencil) {
            $('#' + id).html(game.currentNum[1]);
        } else {
            $('#' + id).html(game.currentNum[0]);
        }

        saveMove(id);
        addMove(id, game.currentNum[2])
    }
}

function selectNum(id) {
    game.currentNum = num_ref[id];
    game.currentNum = num_ref[id];

    $('#currentNum').text("Current Number: " + game.currentNum[2])
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


// util functions
function start() {
    game.start = new Date().getTime();
    window.setTimeout(timer, 100);
    $('#start').removeAttr('onclick');

    $('.num').attr('onclick', 'selectNum(this.id)');
    $('.game-field').attr('onclick', 'setNum(this.id)');

    $(function () {
        $.getJSON("/games/sudoku/setup")
    });

    initialize();
}

function initialize() {
    var currentPuzzle = generatePuzzle(1);
    renderBoard(currentPuzzle);
    getCurrentBoard();
}

function printBoard(board) {
    for (var i = 0; i < 9; i++) {
        var line = "";
        for (var j = 0; j < 9; j++) {
            line += " " + board[i][j];
        }
        window.console && console.log(line);
    }
}

function togglePencil() {
    if (game.pencil) {
        game.pencil = false;
        $('#pencilOn').text("Pencil: Off")
    } else {
        game.pencil = true;
        $('#pencilOn').text("Pencil: On")
    }
}

function undo(id) {
    if (id !== null) {
        game.undo++;
        $('#numUndo').text("Undo: " + game.undo);
        $('#' + id).html('')
    }
}


// back-end link functions
function saveMove(id) {
    $(function () {
        $.getJSON("/games/sudoku/save_move", {id: id})
    });
}

function addMove(id, num) {
    $(function () {
        $.getJSON("/games/sudoku/add_move", {
            id: id,
            num: num
        }, function (data) {
            console.log(data.result)
        });
    });
}

function getLastMove() {
    $(function () {
        $.getJSON("/games/sudoku/get_move", {}, function (data) {
            undo(data.result)
        });
    });
}

function getCurrentBoard() {
    $(function () {
        $.getJSON("/games/sudoku/get_board", {}, function (data) {
            console.log(data);
            printBoard(data.result)
        });
    })
}


// sudoku game logic functions
function solveSudoku(inputBoard, stats) {

    var stats = stats || {};
    stats['easy'] = true;
    var board = JSON.parse(JSON.stringify(inputBoard));
    var possibilities = [[], [], [], [], [], [], [], [], []];

    for (var i = 0; i < 9; i++) {
        for (var j = 0; j < 9; j++) {
            possibilities[i][j] = [false, true, true, true, true, true, true, true, true, true];
        }
    }

    var solved = false;
    var impossible = false;
    var mutated = false;
    var needCheckFreedoms = false;

    var loopCount = 0;

    outerLoop: while (!solved && !impossible) {
        solved = true;
        mutated = false;
        loopCount++;

        var leastFree = [];
        var leastRemaining = 9;

        for (var i = 0; i < 9; i++) {
            for (var j = 0; j < 9; j++) {

                if (board[i][j] === 0) {

                    solved = false;
                    var currentPos = possibilities[i][j];

                    var zoneRow;
                    var zoneCol;

                    if (loopCount === 1) {
                        zoneRow = getZone(i) * 3;
                        zoneCol = getZone(j) * 3;
                        currentPos[10] = zoneRow;
                        currentPos[11] = zoneCol;
                    } else {
                        zoneRow = currentPos[10];
                        zoneCol = currentPos[11];
                    }

                    var wasMutated = reducePossibilities(board, i, j, currentPos, zoneRow, zoneCol);

                    if (wasMutated) {
                        mutated = true;
                    }


                    // check if the contraints above left us with only one valid option
                    var remaining = 0;
                    var lastDigit = 0;

                    for (var k = 1; k <= 9; k++) {
                        if (currentPos[k]) {
                            remaining++;
                            lastDigit = k;
                        }
                    }

                    if (remaining === 0) {
                        impossible = true;
                        break outerLoop;
                    }
                    else if (remaining === 1) {
                        board[i][j] = lastDigit;
                        mutated = true;
                        continue;
                    }

                    if (needCheckFreedoms) {
                        var solution = checkFreedoms(board, i, j, possibilities, zoneRow, zoneCol);

                        if (solution !== 0) {

                            board[i][j] = solution;
                            mutated = true;
                            continue;
                        }

                        if (remaining === leastRemaining) {
                            leastFree.push([i, j]);
                        }
                        else if (remaining < leastRemaining) {
                            leastRemaining = remaining;
                            leastFree = [[i, j]];
                        }
                    }

                }
            }
        }

        if (mutated === false && solved === false) {

            // time to break out freedom checking
            if (needCheckFreedoms === false) {
                needCheckFreedoms = true;
                stats['medium'] = true;
                continue;
            }

            // we're stuck, time to start guessing
            return solveByGuessing(board, possibilities, leastFree, stats);

        }
    }

    if (impossible) {
        return null;
    }
    else {
        return board;
    }
}

function getZone(i) {
    if (i < 3) {
        return 0;
    }
    else if (i < 6) {
        return 1;
    }
    else {
        return 2;
    }
}


function reducePossibilities(board, row, column, currentPos, zoneRow, zoneCol) {

    var mutated = false;

    //eliminate items already taken in the column and row
    for (var k = 0; k < 9; k++) {
        if (currentPos[board[row][k]] || currentPos[board[k][column]]) {
            mutated = true;
        }
        currentPos[board[row][k]] = false;
        currentPos[board[k][column]] = false;
    }

    //eliminate items already taken in the region
    for (var x = zoneRow; x <= (zoneRow + 2); x++) {
        for (var y = zoneCol; y <= (zoneCol + 2); y++) {
            var zoneDigit = board[x][y];

            if (currentPos[zoneDigit]) {
                mutated = true;
            }

            currentPos[zoneDigit] = false;
        }
    }

    return mutated;
}

function checkFreedoms(board, i, j, possibilities, zoneRow, zoneCol) {

    var answer = 0;
    var currentPos = possibilities[i][j];

    //see if only one square can realize a possibility
    var uniquePosRow = currentPos.slice(0);
    var uniquePosCol = currentPos.slice(0);
    var uniquePosCube = currentPos.slice(0);

    for (var k = 0; k < 9; k++) {
        for (var l = 1; l <= 9; l++) {
            if (board[i][k] === 0 && possibilities[i][k][l] && k !== j) {
                uniquePosRow[l] = false;
            }
            if (board[k][j] === 0 && possibilities[k][j][l] && k !== i) {
                uniquePosCol[l] = false;
            }
        }
    }

    var remainingRow = 0;
    var remainingCol = 0;
    var lastDigitRow = 0;
    var lastDigitCol = 0;

    for (var k = 1; k <= 9; k++) {
        if (uniquePosRow[k]) {
            remainingRow++;
            lastDigitRow = k;
        }
        if (uniquePosCol[k]) {
            remainingCol++;
            lastDigitCol = k;
        }
    }

    if (remainingRow === 1) {
        answer = lastDigitRow;
        return answer;
    }

    if (remainingCol === 1) {
        answer = lastDigitCol;
        return answer;
    }

    for (var x = zoneRow; x <= (zoneRow + 2); x++) {
        for (var y = zoneCol; y <= (zoneCol + 2); y++) {
            for (var l = 1; l <= 9; l++) {
                if (board[x][y] === 0 && possibilities[x][y][l] && (x !== i || y !== j)) {
                    uniquePosCube[l] = false;
                }
            }
        }
    }

    var remainingCube = 0;
    var lastDigitCube = 0;

    for (var k = 1; k <= 9; k++) {
        if (uniquePosCube[k]) {
            remainingCube++;
            lastDigitCube = k;
        }
    }

    if (remainingCube === 1) {
        answer = lastDigitCube;
    }

    return answer;
}

function solveByGuessing(board, possibilities, leastFree, stats) {
    if (leastFree.length < 1) {
        return null;
    }

    if ('hard' in stats) {
        stats['vhard'] = true;
    }
    else {
        stats['hard'] = true;
    }

    // choose a space with the least # of possibilities
    var randIndex = getRandom(leastFree.length);
    var randSpot = leastFree[randIndex];

    var guesses = [];
    var currentPos = possibilities[randSpot[0]][randSpot[1]];

    for (var i = 1; i <= 9; i++) {
        if (currentPos[i]) {
            guesses.push(i);
        }
    }

    shuffleArray(guesses);

    for (var i = 0; i < guesses.length; i++) {
        board[randSpot[0]][randSpot[1]] = guesses[i];
        var result = solveSudoku(board, stats);
        if (result != null) {
            return result;
        }
    }

    // board is impossible
    return null;
}


// returns a random number in the range 0 to limit - 1 inclusive
function getRandom(limit) {
    return Math.floor(Math.random() * limit);
}

// shuffle an array Fisher-Yates style
function shuffleArray(array) {
    var i = array.length;

    if (i !== 0) {
        while (--i) {
            var j = Math.floor(Math.random() * (i + 1));
            var temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }
}

function generatePuzzle(difficulty) {

    if (difficulty !== 1 && difficulty !== 2 &&
        difficulty !== 3 && difficulty !== 4 &&
        difficulty !== 5) {

        difficulty = 1;
    }

    var solvedPuzzle = solveSudoku(emptyPuzzle);

    var indexes = new Array(81);

    for (var i = 0; i < 81; i++) {
        indexes[i] = i;
    }

    shuffleArray(indexes);

    var knownCount = 81;

    for (var i = 0; i < 81; i++) {

        if (knownCount <= 25) {
            break;
        }

        //easy check
        if (difficulty === 1 && knownCount <= 35) {
            break;
        }

        var index = indexes[i];

        var row = Math.floor(index / 9);
        var col = index % 9;
        var currentValue = solvedPuzzle[row][col];
        var state = {};
        solvedPuzzle[row][col] = 0;
        solveSudoku(solvedPuzzle, state);

        // some clarity -- what the solver considers 'medium' is hard for most users
        var undo = false;
        if (difficulty <= 2 && state.medium) {
            undo = true;
        } else if (difficulty <= 3 && state.hard) {
            undo = true;
        } else if (difficulty <= 4 && state.vhard) {
            undo = true;
        }

        if (undo) {
            solvedPuzzle[row][col] = currentValue;
        }
        else {
            knownCount--;
        }
    }

    return solvedPuzzle;
}

var emptyPuzzle = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
];


const ref = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'};

function renderBoard(board) {
    for (var i = 0; i < 9; i++) {
        for (var j = 0; j < 9; j++) {
            var id = ref[i + 1] + '-' + ref[j + 1];
            var val = board[i][j];

            if (val !== 0) {
                var cell = $('#' + id);
                cell.html(num_ref[ref[val]][0]);
                cell.removeAttr('onclick');

                addMove(id, val)
            }
        }
    }
}
