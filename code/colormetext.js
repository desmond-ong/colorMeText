/*
function findAllIndices(string, character) {
	var indices = [];
	for(var i=0; i<string.length;i++) {
    	if (string[i] === character) {
    		indices.push(i);
		}
	}
	return indices;
}

String.prototype.insert = function (index, string) {
  if (index > 0)
    return this.substring(0, index) + string + this.substring(index, this.length);
  else
    return string + this;
};
*/

var allColors = ["darkred", "#800000", "red", "#FF5050", "gray", "#3366FF", "blue", "medimublue", "darkblue"];	

		var xPoint = 30;
		var yPoint = 20;

		var c  = document.getElementsByTagName('canvas')[0];
		var ctx = c.getContext("2d");

		for(var i=0; i < allColors.length; i++) {
			var tyPoint = yPoint;
			var txPoint = xPoint * i;
			var colorCode = allColors[i];

				ctx.beginPath();
				ctx.fillStyle = colorCode;      
				ctx.rect(txPoint, tyPoint, 30 , 20);
				ctx.fill();
				ctx.stroke();
				ctx.closePath();

		}

function colorer(){
	var option = document.getElementById("dictionary").value;
	var input = document.getElementById("input").value;
	//pico.load("simplepython");
	//simplepython.returnColors(input, function(response){
    //	$('#output').html(response);  
  	//});
	//alert('Im going to start processing');
	$.ajax({
		type: "POST",
	  //crossDomain : true,
	  url: "code/masterAnnotator.py",
	  data: { param: input, lexicon: option},
	  //data: {'key':'value','key2':'value2'},
	  success: function(response){
	  	//alert(response.message);
        //alert(response.keys);
        //var lineBreakIndices = findAllIndices(input, 'h');
        var meanScore = response.mean;
        $("#score").html(meanScore);
        var words = input.split(" ");
		//var colors = o;
		var colors = response.colors;
		var coloredWords = [];	
		for (var i=0; i<words.length; i++) {
			coloredWords[i] = '<span style="color:' + colors[i] + '">' + words[i] + '</span>';
		}
		
		var coloredStr = "";
		for (var i=0; i<coloredWords.length; i++) {
			coloredStr = coloredStr + " " + coloredWords[i];
		}
		



		/*

		for (var i=0; i < lineBreakIndices.length; i++) {
			var thisIndex = lineBreakIndices[i];
			coloredStr = coloredStr.slice(0, thisIndex) + '</br>' + coloredStr.slice(thisIndex);
			//txt1.slice(0, 3) + "bar" + txt1.slice(3);
			coloredStr.insert(thisIndex, '</br>');
		}
		*/
		$("#output").html(coloredStr);
		
	}
});

}


function reverse() {
	var o = '';
	for (var i = input.length - 1; i >= 0; i--)
		o += input[i];
	showSlide("outputSlide");
	$("#output").html(o);
}