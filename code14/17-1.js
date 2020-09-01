var array = Array();
var result = "";
for (var i = 1; i <= 100; i++) {
    array.push(i);
}

for (var j = 0; j < array.length; j++) {
    if (hasThree(array[j])) {
        result += "PA";
    } else {
        result += array[j];
    }
    if (j != array.length - 1) {
        result += ",";
    }
}

function hasThree(num) {
    var pa_string = num.toString();
    if (num % 3 == 0 || pa_string.indexOf("3") != -1) {
        return true;
    } else {
        return false;
    }
}

console.log(result);
