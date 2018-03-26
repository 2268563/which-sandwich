$(document).ready(function() {
    $("#favourite").click(function() {
	    var swname;
	    swname = $(this).attr("sandwich");
	    $.get("/whichsandwich/favourite/", {sandwich_name: swname}, function(data){
			$("#favourite_button").html(data);
		        $("#favourite").hide();
	    });
    });	
});