$(document).ready(function() {
    $('.comment_like_btn').click(function (){
        var commentIdVar;
        commentIdVar = $(this).attr('data-commentid');

        $.get('/like_comment/',
            {'comment_id': commentIdVar,
            'like_type': 'like'},
            function (data){
                $('#like_count'.concat(commentIdVar)).html(data)
                $('#like_btn'.concat(commentIdVar)).hide();
                console.log("here")
                $('#dislike_btn'.concat(commentIdVar)).show()
            })
    });
    
    $('.thread_like_btn').click(function (e){
        var threadIdVar;
        threadIdVar = $(this).attr('data-threadid');
        $.get('/like_thread/',
            {'thread_id': threadIdVar,
            'like_type': 'like'},
            function (data){
                $(('#like_count_thread'.concat(threadIdVar))).html(data);
                $('#threadbtn'.concat(threadIdVar)).hide()
                $('#thread_dislike'.concat(threadIdVar)).show();
            })
    });
    $('.thread_dislike_btn').click(function (e){
        var threadIdVar;
        threadIdVar = $(this).attr('data-threadid');
        $.get('/like_thread/',
            {'thread_id': threadIdVar,
            'like_type': 'dislike'},
            function (data){
                $(('#like_count_thread'.concat(threadIdVar))).html(data);
                $('#thread_dislike'.concat(threadIdVar)).hide();
                $('#threadbtn'.concat(threadIdVar)).show()
            })
    });
    $('.comment_dislike_btn').click(function (){
        var commentIdVar;
        commentIdVar = $(this).attr('data-commentid');

        $.get('/like_comment/',
            {'comment_id': commentIdVar,
            'like_type': 'dislike'},
            function (data){
                
                $('#like_count'.concat(commentIdVar)).html(data)
                $('#dislike_btn'.concat(commentIdVar)).hide();
                console.log("here")
                console.log("#like_btn".concat(commentIdVar))
                $('#like_btn'.concat(commentIdVar)).show();
            })
    });
    var $input = $('#refresh');

    $input.val() == 'yes' ? location.reload(true) : $input.val('yes');

    
});
