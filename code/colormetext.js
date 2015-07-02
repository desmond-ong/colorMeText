

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
	  url: "simplepython.py",
	  data: { param: input, lexicon: option},
	  //data: {'key':'value','key2':'value2'},
	  success: function(response){
        	alert(response.message);
        //alert(response.keys);
        
        var words = input.split(" ");
		//var colors = o;
		var colors = response.colors;
		var coloredWords = "";	
		for (var i=0; i<words.length; i++) {
			coloredWords = coloredWords + '<span style="color:' + colors[i] + '">' + words[i] + ' ' + '</span>';
		}
		$("#output").html(coloredWords);
		
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