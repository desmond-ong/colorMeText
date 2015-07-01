
function colorer(){
	var input = document.getElementById("input").value;
	var dictionary = document.getElementById("dictionary").value;
	var words = input.split(" ");
	var colors = ["blue", "green"];
	var coloredWords = "";	
	for (var i=0; i<words.length; i++) {
		coloredWords = coloredWords + '<span style="color:' + colors[i] + '">' + words[i] + ' ' + '</span>';
	}
	
	$("#output").html(coloredWords);
}


function reverse() {
  var o = '';
  for (var i = input.length - 1; i >= 0; i--)
    o += input[i];
	showSlide("outputSlide");
  $("#output").html(o);
}