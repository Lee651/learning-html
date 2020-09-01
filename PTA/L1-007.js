let readline = require('readline'); 
const { PassThrough } = require('stream');
let rl = readline.createInterface({ 
	input: process.stdin,
	output: process.stdout
});

rl.on('line', function(line) { 
    let N = Number(line.trim()); 
    let t = new Array();
    let dic = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4':'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu'};
    let a = "";
    let count = 0;
    if (N >= 0) {
        for (let i = 0; i < N.toString().length; i++) {
            let tmp = parseInt(N / (10 ** (N.toString().length - i - 1)) % 10);
            t.push(tmp);
        }
        for (let z of t) {
            count += 1;
            for (let x in dic) {
                if (Number(x) == z) {
                    if (count < t.length) {
                        a += (dic[x] + " ");
                    } else {
                        a += dic[x];
                    }
                } else {
                    continue;
                }
            }
        }
        console.log(a);
    } else {
        for (let i = 0; i < N.toString().length - 1; i++) {
            let tmp = parseInt(Math.abs(N) / (10 ** (N.toString().length - i - 2)) % 10);
            t.push(tmp);
        }
        for (let z of t) {
            count += 1;
            for (let x in dic) {
                if (Number(x) == z) {
                    if (count < t.length) {
                        a += (dic[x] + " ");
                    } else {
                        a += dic[x];
                    }
                } else {
                    continue;
                }
            }
        }
        console.log("fu" + " " + a);
    }
	rl.close();
});