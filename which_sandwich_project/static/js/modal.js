$("document").ready(function() {
    $("#sandwich_display").click(function(e) {
        sandwich_container = e.target.closest('div[class^="sandwich"]');
        sandwich_id = sandwich_container.id;
        sandwich_name = $(sandwich_container).attr("name");

        // Set modal title to sandwich name
        $("#sandwich-modal-title").text(sandwich_name);
        getSandwichModal(sandwich_id);
        $("#sandwichModal").modal("toggle");
    }); 
});

function getSandwichModal(sandwich_id) {
    console.log(sandwich_id);
    $.get('/whichsandwich/modal_sandwich/', 
        { sandwich_id: sandwich_id, }, function(data) {
            $('.modal-body').html(data);
        }); 
}
