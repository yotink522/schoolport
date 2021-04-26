$(document).ready(function(){

    //Sidebar메뉴(dashboard, billingcenter, ...)를 클릭하였을때 ajax처리하는 부분
    $(document).on("click", "#menu li a", function(e){
        var tag_a = $(this);
        e.preventDefault();

        $.ajax({
          url: tag_a.attr("href"),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
            $("#div_main_contents").html("");
          },
          success: function (data) {
            $("#div_main_contents").html(data.html_index);
            
            $('#menu li').removeClass("active");
            tag_a.parent().addClass("active");

          }
        });
    });


});
