function lets_look_for_a_wife() {
    $.get('search_wife', function(data) {
        $( "#wife" ).text(data);
    });
}

$(document).ready(function() {
   $( "#search_for_a_wife" ).click(lets_look_for_a_wife);
});
