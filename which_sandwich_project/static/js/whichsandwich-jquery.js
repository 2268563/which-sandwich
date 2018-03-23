$(document).ready(function() {
	$(".like").click(function() {
		{% sandwich.likes == sandwich.likes + 1 %};
	});
	
	$(".dislike").click(function() {
		{% sandwich.dislikes == sandwich.dislikes + 1 %};
	});
});