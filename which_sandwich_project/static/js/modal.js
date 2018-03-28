$("document").ready(function() {
    $("#sandwich_display").click(function(e) {
        sandwich_id = e.target.closest('div[class^="sandwich"]').id;
        getSandwichModal(sandwich_id);
    }); 
});

function getSandwichModal(sandwich_id) {
    $.get('/whichsandwich/modal/', 
        { sandwich_id: sandwich_id, }, function(data) {
            $('#sandwichModal').replaceWith(data);
            $("#sandwichModal").modal("toggle");
        }); 
}
