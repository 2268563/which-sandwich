$(document).ready(function() {
    $("#like").click(function() {
	    var swname;
	    swname = $(this).attr("sandwich");
	    $.get("/whichsandwich/like/", {sandwich_name: swname}, function(data){
		    $("#like_count").html(data);
		        $("#like").hide();
			    $("#dislike").hide();
	    });
    });	
	
	$("#dislike").click(function() {
	    var swname;
	    swname = $(this).attr("sandwich");
	    $.get("/whichsandwich/dislike/", {sandwich_name: swname}, function(data){
		    $("#dislike_count").html(data);
		        $("#like").hide();
			    $("#dislike").hide();
	    });
    });	
	
});