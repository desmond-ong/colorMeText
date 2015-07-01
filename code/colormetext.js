

function colorer(){
	//	  var dictionary = document.getElementById("dictionary").value;
	var input = document.getElementById("input").value;
	//pico.load("simplepython");
	//simplepython.returnColors(input, function(response){
    //	$('#output').html(response);  
  	//});
	
	$.ajax({
	  type: "POST",
	  crossDomain : true,
	  url: "simplepython.py",
	  data: { param: input}
	}).done(function( o ) {
		var words = input.split(" ");
		var colors = o;
		//var colors = ["blue", "green"];
		var coloredWords = "";	
		for (var i=0; i<words.length; i++) {
			coloredWords = coloredWords + '<span style="color:' + colors[i] + '">' + words[i] + ' ' + '</span>';
		}
		$("#output").html(o);
	});


}


function reverse() {
  var o = '';
  for (var i = input.length - 1; i >= 0; i--)
    o += input[i];
	showSlide("outputSlide");
  $("#output").html(o);
}