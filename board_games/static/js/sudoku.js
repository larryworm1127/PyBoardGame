var currentNum = '';
var pencil = false;

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
    $('#' + id).html(currentNum);
    $('#currentNum').text("Current Number: " + currentNum)
}

function selectNum(id) {
    console.log(id);
    if (pencil) {
        currentNum = num_ref[id][1]
    } else {
        currentNum = num_ref[id][0];
    }
}

// util functions
function togglePencil() {
    if (pencil) {
        pencil = false;
        $('#pencilOn').text("Pencil: Off")
    } else {
        pencil = true;
        $('#pencilOn').text("Pencil: On")
    }

    console.log(pencil)
}


var start = new Date().getTime(),
    time = 0,
    elapsed = '0.0';

function instance() {
    time += 100;

    elapsed = Math.floor(time / 100) / 10;
    if (Math.round(elapsed) === elapsed) {
        elapsed += '.0';
    }

    $('#time').text("Time: " + elapsed);

    var diff = (new Date().getTime() - start) - time;
    window.setTimeout(instance, (100 - diff));
}

window.setTimeout(instance, 100);


