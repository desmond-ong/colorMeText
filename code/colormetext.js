function showSlide(id) {
  $(".slide").hide();
  $("#"+id).show();
}

showSlide("inputSlide");

var input = document.getElementById("input").value;

function reverse() {
  var o = '';
  for (var i = input.length - 1; i >= 0; i--)
    o += input[i];
	showSlide("outputSlide");
  $("#output").html(o);
}