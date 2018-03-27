$("document").ready(function() {
    filterSandwiches('top');

    $("#top, #new, #controversial").click(function(e) {
        filterSandwiches(e.target.id);
    });

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

function filterSandwiches(filter){
    $.get('/whichsandwich/browse_filter/', { sort_filter: filter, }, function(data) {
        $('#sandwich_display').html(data);
        $('#sortButton').text(filter);
    });
}

function getSandwichModal(sandwich_id) {
    console.log(sandwich_id);
    $.get('/whichsandwich/sandwich_modal/', { sandwich_id: sandwich_id, }, function(data) {
        $('.modal-body').html(data);
    });
}
