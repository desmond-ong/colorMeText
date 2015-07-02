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
	  	alert(response.message);
        //alert(response.keys);
        //var lineBreakIndices = findAllIndices(input, 'h');
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
		
		var xPoint = 30;
		var yPoint = 30;

		var c  = document.getElementsByTagName('canvas')[0];
		var ctx = c.getContext("2d");

		for(var i =1; i<=6;i++)
		{
			var tyPoint = yPoint * i;
			for(var j=1;j<=6;j++)
			{
				var txPoint = xPoint * j;  
				var colorcode = CalculateHEX();


				ctx.beginPath();
				ctx.fillStyle = colorcode ;      
				ctx.rect(20, 20, txPoint , tyPoint );
				ctx.fill();
				ctx.stroke();
				ctx.closePath();
			}

		}

		function CalculateHEX()
		{
			alert('HEX');
			var rgbCode ="#";
			for(var c = 0;c< 3;c++)
			{
				var y = Math.floor((Math.random() * 255) + 1);
				rgbCode  = rgbCode + Number(y).toString(16);
			}
			return rgbCode;

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