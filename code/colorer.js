function colorer(txt,colors){

	words = txt.split(" ");

	// var colors = ["blue", "green"];

	function colorWords(words,colors) {
		coloredWords = [];
		
		for (var i=0; i<words.length; i++) {
			coloredWords[i] = '<span style="color:' + colors[i] + '">' + words[i] + ' ' + '</span>'
		}

		return coloredWords;
	}

	var newTxt = colorWords(words,colors);
	var newTxtString = "";
	for (var i=0; i<newTxt.length; i++) {
		newTxtString + newTxt[i];
	}
	return nexTxtString;
}

