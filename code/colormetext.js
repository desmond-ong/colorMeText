
function findAllIndices(string, character) {
	var indices = [];
	for(var i=0; i<string.length;i++) {
    	if (string[i] === character) {
    		indices.push(i);
		}
	}
	return indices;
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
        	alert(response.message);
        //alert(response.keys);
        var lineBreakIndices = findAllIndices(input, "h");
        var words = input.split(" ");
		//var colors = o;
		var colors = response.colors;
		var coloredWords = [];	
		for (var i=0; i<words.length; i++) {
			coloredWords[i] = '<span style="color:' + colors[i] + '">' + words[i] + '</span>';
		}
		for (var i=0; i < lineBreakIndices.length; i++) {
			var thisIndex = lineBreakIndices[i];
			coloredWords.splice(thisIndex, 0, '</br>');
		}
		var coloredStr = "";
		for (var i=0; i<coloredWords.length; i++) {
			coloredStr = coloredStr + " " + coloredWords[i];
		}
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