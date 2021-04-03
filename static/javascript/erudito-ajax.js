$(document).ready(function() {
    $('.comment_like_btn').click(function (){
        var commentIdVar;
        commentIdVar = $(this).attr('data-commentid');

        $.get('/like_comment/',
            {'comment_id': commentIdVar},
            function (data){
                $('#like_count'.concat(commentIdVar)).html(data)
                $('#like_btn'.concat(commentIdVar)).hide();
            })
    });
    
    $('.thread_like_btn').click(function (e){
        var threadIdVar;
        threadIdVar = $(this).attr('data-threadid');
        $.get('/like_thread/',
            {'thread_id': threadIdVar},
            function (data){
                $(('#like_count_thread'.concat(threadIdVar))).html(data);
                $('#threadbtn'.concat(threadIdVar)).hide();
            })
    });

});