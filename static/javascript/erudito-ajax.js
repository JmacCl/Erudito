$(document).ready(function() {
    $('#like_btn').click(function (){
        var commentIdVar;
        commentIdVar = $(this).attr('data-commentid');
        console.log('#'.concat('like_count_comm',commentIdVar))

        $.get('/like_comment/',
            {'comment_id': commentIdVar},
            function (data){
                $('#like_count').html(data);
                $('#like_btn').hide();
            })
    });
    
    $('.thread_like_btn').click(function (e){
        var threadIdVar;
        threadIdVar = $(this).attr('data-threadid');
        console.log('#'.concat('like_count',threadIdVar))
        $.get('/like_thread/',
            {'thread_id': threadIdVar},
            function (data){
                $(('#'.concat('like_count',threadIdVar))).html(data);
                $('#threadbtn'.concat(threadIdVar)).hide();
            })
    });

});