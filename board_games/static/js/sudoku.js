var currentNum = '';

const num_ref = {
    'one': '<p>&sup1;</p>',
    'two': '<p>&sup2;</p>',
    'three': '<p>3</p>',
    'four': '<p>4</p>',
    'five': '<p>5</p>',
    'six': '<p>6</p>',
    'seven': '<p>7</p>',
    'eight': '<p>8</p>',
    'nine': '<p>9</p>'
};

// game core functions
function setNum(id) {
    console.log(id);
    $('#' + id).html(currentNum)
}

function selectNum(id) {
    console.log(id);
    currentNum = num_ref[id]
}
