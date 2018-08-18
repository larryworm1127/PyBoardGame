/* Game control variable */
var game = {
    currentCell: 'None',
    pencil: false,
    undo: 0
};


/* Constants */
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

const ref = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'};


/* Game core functions */
function verifyBoard() {
    /*
    This function calls back-end to verify the state of
    the board and commit corresponding actions to various states
    */

    // clear any error before assigning new ones
    clearError();

    // call back-end to see the state of the board
    $(function () {
        $.getJSON("/games/sudoku/verify", {}, function (data) {
            // get the data passed in from back-end
            var result = data.result;
            var id_list = data.id_list;

            // if result is true, meaning the game is won, call end game function
            if (result === true) {
                endGame()
            }

            // if result is false, meaning the board isn't complete, do nothing
            else if (result === false) {
            }

            // else, meaning there are errors on board, highlight the wrong number
            else {
                // loop through all the ids of the wrong number
                for (var i = 0; i < id_list.length; i++) {
                    var cell = $('p', '#' + id_list[i]);

                    // remove the base color
                    cell.removeClass('not-pencil');
                    try {
                        // if the move was made by the player, remove player move color too
                        if (cell.attr('class').includes('player')) {
                            cell.removeClass('player');
                        }
                    } catch (TypeError) { // silence type error
                    }

                    // add error color to the numbers
                    cell.addClass('error');
                }
            }
        });
    })
}

function reset() {
    /*
    This function resets entire board and game variables in preparation for new game
     */

    // remove color for current cell
    $('#' + game.currentCell).removeClass('selected');

    // set game variables to original state
    game.currentCell = 'None';
    game.pencil = false;
    game.undo = 0;

    // update information panel
    updateInfo();

    // loop through all cells and clear the content in it
    for (var i = 1; i <= 9; i++) {
        for (var j = 1; j <= 9; j++) {

            // get id and select the cell
            id = ref[i] + '-' + ref[j];
            var cell = $('#' + id);

            // clear board content and remove all associated classes
            cell.html('');
        }
    }
}

function start() {
    /*
    This function commit a number of actions to get a game started
     */

    // assign event handlers to side-bar number pad and game board cells
    $('.num').attr('onclick', 'setNum(this.id)');
    $('.game-field').attr('onclick', 'selectCell(this.id)');

    // calls back-end to setup sudoku board in back-end
    $(function () {
        $.get("/games/sudoku/setup")
    });

    // calls helper functions generate puzzle
    initialize();
}

function clearError() {
    /*
    This function clears any error previously assigned
     */

    // loop through all cells to remove errors assigned to cells
    for (var i = 1; i <= 9; i++) {
        for (var j = 1; j <= 9; j++) {

            // select the cell
            id = ref[i] + '-' + ref[j];
            var cell = $('p', '#' + id);

            // remove error color and add base non-pencil color
            cell.removeClass('error');
            cell.addClass('not-pencil');

            // add player move color is the move made by player
            try {
                if (cell.attr('class').includes('player-con')) {
                    cell.addClass('player')
                }
            } catch (TypeError) {   // silence TypeError
            }
        }
    }
}

function renderBoard(board) {
    /*
    This function renders the given board onto the web page
     */

    // loop through every element in the given 2D-array board
    for (var i = 0; i < 9; i++) {
        for (var j = 0; j < 9; j++) {

            // get value from the given board on position (i, j)
            var id = ref[i + 1] + '-' + ref[j + 1];
            var val = board[i][j];

            // if value on board isn't 0, then draws the correct number onto the web page
            if (val !== 0) {
                var cell = $('#' + id);
                cell.html(num_ref[ref[val]][0]);

                // remove onclick attribute to prevent user from changing base puzzle
                cell.removeAttr('onclick');

                // call function to add number in back-end board
                addMove(id, val)
            }
        }
    }
}


/* Event handlers - button handlers */
function setNum(num) {
    /*
    This function is linked with all number pad numbers. It draws the
    selected number into the cell that is currently selected by user
     */

    // run following only if a cell is selected
    if (game.currentCell !== 'None') {
        // select current cell with jquery
        var cell = $('#' + game.currentCell);


        // if pencil feature is toggled, draw penciled number into cell
        if (game.pencil) {

            // if the original element is null, then save move with a different way
            if ($('p', cell).html() == null) {
                saveMove(game.currentCell, false, false);
                cell.html(num_ref[num][1]);
            }

            // if the original element is penciled, then save move with the pencil way
            else {
                // draw
                cell.html(num_ref[num][1]);

                // calls function to save this move for undo feature
                var innerEle = $('p', cell);
                saveMove(game.currentCell, innerEle.html(), game.pencil);
            }
        }

        // if pencil feature isn't on, draw non-penciled number into cell with player move color
        else {
            // check whether the user is trying to enter in the same number
            if ($('p', cell).html() != num_ref[num][2] && !$('p', cell).attr('class').includes()) {

                // calls function to save this move for undo feature
                saveMove(game.currentCell, false, game.pencil);

                // draw
                cell.html(num_ref[num][0]);

                // add player color to number
                var innerEle = $('p', cell);
                innerEle.addClass('player');
                innerEle.addClass('player-con');

                // call function to update back-end board
                addMove(game.currentCell, num_ref[num][2]);

                // call function to verify board
                verifyBoard()
            }
        }
    }
}

function selectCell(id) {
    /*
    This function links with all the cells on the game board.
    It updates game variable and highlight currently selected cell.
     */

    // if there is already a cell being selected, remove the highlighting on that cell
    if (game.currentCell !== 'None') {
        $('#' + game.currentCell).removeClass('selected')
    }

    // highlight current selected cell and save it to game variable
    $('#' + id).addClass('selected');
    game.currentCell = id
}

function togglePencil() {
    /*
    This function links with pencil toggle button. It turns pencil feature on or off
     */
    game.pencil = !game.pencil;

    // update info pad
    updateInfo()
}

function newGame() {
    /*
    This function links with new game button. It resets board and start a new game
     */
    reset();
    start()
}

function erase() {
    /*
    This function links with erase button. It erase number in currently selected cell
    and update the back-end board, and verifies the new board.
     */

    // select current cell with jquery
    var currentCell = $('#' + game.currentCell);

    // if pencil is toggled, then
    try {
        // if the current cell is written with pencil, save the move for undo
        if (currentCell.attr('class').includes('pencil')) {
            var innerEle = $('p', '#' + game.currentCell);
            saveMove(game.currentCell, innerEle.html(), game.pencil);
        }

        // if the current cell isn't with pencil, save the move for undo, and update board
        else {
            saveMove(game.currentCell, false, game.pencil);
            addMove(game.currentCell, 0);
        }
    } catch (TypeError) {  // silence TypeError
    }

    // erase content in current cell
    currentCell.html('');

    // calls function to verify the board
    verifyBoard()
}

function undo(id, num, pencil) {
    /*
    This function links with undo button. It undoes player's last move
     */

    // if id passed in isn't empty
    if (id !== false) {

        // update info pad
        game.undo++;
        updateInfo();

        // if number passed in isn't 0
        if (num !== 0) {

            // if pencil passed in is true, then draw number in cell with pencil
            if (pencil) {
                $('#' + id).html(num_ref[ref[num]][1]);
            }

            // if pencil passed in is false, then draw number in cell without pencil
            else {
                $('#' + id).html(num_ref[ref[num]][0]);
                $('p', '#' + id).addClass('player')
            }
        }

        // if number passed in is 0, then empty the cell
        else {
            $('#' + id).html('');
        }

        // calls function to verify the board
        verifyBoard()
    }
}


/* til functions */
function endGame() {
    /* End game function that toggles the end game modal */
    reset();
    $('#win-modal').modal('show')
}

function initialize() {
    /* Init function that calls function to generate a puzzle and render it */
    var currentPuzzle = generatePuzzle(1);
    renderBoard(currentPuzzle);
    //renderBoard(testBoard)
}

function updateInfo() {
    /* Update info function that re-draws the info pad with updated info */
    $('#numUndo').text("Undo: " + game.undo);

    if (game.pencil) {
        $('#pencilOn').text("Pencil: On")
    } else {
        $('#pencilOn').text("Pencil: Off")
    }
}

function saveMove(id, num, pencil) {
    /* Back-end link function that save move passed in for undo feature */
    $(function () {
        $.get("/games/sudoku/save_move", {
            id: id,
            num: num,
            pencil: pencil
        })
    });
}

function addMove(id, num) {
    /* Back-end link function that add move passed in to update back-end board */
    $(function () {
        $.get("/games/sudoku/add_move", {
            id: id,
            num: num
        });
    });
}

function getLastMove() {
    /* Back-end link function that get the last move made by the player for undo feature */
    $(function () {
        $.getJSON("/games/sudoku/get_move", {}, function (data) {
            undo(data.result, data.num, data.pencil)
        });
    });
}


/* Sudoku game logic functions */
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
    } else {
        return board;
    }
}

function getZone(i) {
    if (i < 3) {
        return 0;

    } else if (i < 6) {
        return 1;

    } else {
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
    } else {
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

        // easy check
        if (difficulty === 1 && knownCount <= 40) {
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
        } else {
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

var testBoard = [
    [5, 3, 4, 6, 7, 8, 9, 1, 0],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
];
