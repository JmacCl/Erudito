$(document).ready(function() {
    $('#like_btn').click(function (){
        var commentIdVar;
        commentIdVar = $(this).attr('data-commentid');

        $.get('/erudito/like_comment/',
            {'comment_id': commentIdVar},
            function (data){
            $('#like_count').html(data);
            $('#like_btn').hide();
            })
    });
});