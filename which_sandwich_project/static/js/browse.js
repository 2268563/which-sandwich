$("document").ready(function() {
    filterSandwiches('top');

    $("#top, #new, #controversial").click(function(e) {
        filterSandwiches(e.target.id);
    });
});

function filterSandwiches(filter){
    $.get('/whichsandwich/browse_filter/', { sort_filter: filter, }, function(data) {
        $('#sandwich_display').html(data);
        $('#sortButton').text(filter);
    });
}
