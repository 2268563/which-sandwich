$(document).ready(function() {
    // Draggable code
    $("#available-ingredients").sortable({
        connectWith: "#used-ingredients"
    });

    // Links both lists
    $("#used-ingredients").sortable({
        connectWith: "#available-ingredients"
    });

    // Mouse enter detects when mouse has dropped ingredient
    $("#used-ingredients, #available-ingredients").mouseenter(function() {
        $("#id_ingredients").children().prop("selected", false);
        var used_ings = $("#used-ingredients").children();
        used_ings.each(function() {
            var arg = "value=" + $(this).attr("value").toString();
            $("#id_ingredients option["+arg+"]").prop("selected", "selected");;
        });
    });

    $("#submitButton").click(function() {
        var used_ings = $("#used-ingredients").children();
        if (used_ings.length == 0) {
           var t = $("#ingredients-warning").removeClass("invisible");
        }
    });

    $("#resetButton").click(function() {
        location.reload();      
    });
});
