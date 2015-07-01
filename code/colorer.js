var txt = "This text.";

var words = txt.split(" ");

var colors = ["blue", "green"];

function colorWords(words,colors) {
	coloredWords = [];
	
	for (var i=0; i<words.length; i++) {
		coloredWords[i] = '<span style="color:' + colors[i] + '">' + words[i] + ' ' + '</span>'
	}

	return coloredWords;
}

var newTxt = colorWords(words,colors);

for (var i=0; i<newTxt.length; i++) {
	document.write(newTxt[i]);
}