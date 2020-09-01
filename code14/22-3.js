// 字符串头尾去除空格（包括全角、半角空格）
function diyTrim(str) {
    let result = "";
    result = str.replace(/(^\s*)|(\s*$)/g, "");
    return result;
}
console.log(diyTrim(" ａｂ ｆ　123　"));

// 字符串去除所有空格（包括全角、半角空格）
function diyTrim(str) {
    let result = "";
    let regOne = new RegExp(" ", "g");
    let regTwo = new RegExp("　", "g");
    let a = str.replace(regOne, result);
    result = a.replace(regTwo, result);
    return result;
}
console.log(diyTrim("　123 ａｂｃ　456 "));

// 去掉字符串str中，连续重复的地方
function removeRepetition(str) {
    let result = "";
    let len = str.length;
    for (let i = 0; i < len; i++) {
        if (str[0] == str[1]) {
            str = str.slice(1);
        } else {
            result += str[0];
            str =str.slice(1);
        }
    }
    return result;
  }
console.log(removeRepetition(""));

// 二维数组排序
var arr = [[10, 14], [16, 60], [7, 44], [26, 35], [22, 63]];
function f(a, b) {
    return (b[1] - a[1]);
}
console.log(arr.sort(f));

// 按元素对象的某个值从小到大排序
var arr = [
    {
        id: 1,
        name: 'candy',
        value: 40
    }, {
        id: 2,
        name: 'Simon',
        value: 50
    }, {
        id: 3,
        name: 'Tony',
        value: 45
    }, {
        id: 4,
        name: 'Annie',
        value: 60
    }
];

function f(a, b) {
    return (a.name - b.name);
    // return (a.id - b.id);
    // return (a.value - b.value);
}

console.log(arr.sort(f));

