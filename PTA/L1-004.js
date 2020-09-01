var readline = require('readline'); 
var rl = readline.createInterface({ 
	input: process.stdin,
	output: process.stdout
});

rl.on('line', function(line) { 
    var F = Number(line.trim()); 
    var C = 5 * (F - 32) / 9;
    var Celsius = parseInt(C);
    console.log("Celsius = " + Celsius);
	rl.close();
});