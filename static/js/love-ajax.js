$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/love/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});