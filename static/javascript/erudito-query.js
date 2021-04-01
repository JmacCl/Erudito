

$(document).ready(function () {
    $('about-btn').click(function (){
        alert("This button delivers a message thanks to Jquery");
    });
});

$('p').hover(
    function() {
        $(this).css('color', 'red');
    },
    function() {
        $(this).css('color', 'white');
    });