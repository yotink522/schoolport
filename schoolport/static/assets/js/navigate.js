var navigate_func;

$(document).ready(function(){
    //해당 아이콘(앱)을 클릭하였을때 ajax처리부분
      navigate_func = function(param){
        var tag_a = param;
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
            window.history.pushState("","",tag_a.attr("href")); //AJAX로 호출한 URL로 변경시키기(address bar)
          }
        });
    };

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
            window.history.pushState("","",tag_a.attr("href")); //AJAX로 호출한 URL로 변경시키기(address bar)
          }
        });
    });

    $(document).on("click", ".main_item_title", function(e){
        navigate_func($(this));
        e.preventDefault();
        /*
        var tag_a = $(this);
        
      
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
            window.history.pushState("","",tag_a.attr("href")); //AJAX로 호출한 URL로 변경시키기(address bar)
          }
      });
      */
    });

    //billingcenter/coursefee 에서 New Course 와 New General Course단추를 눌렀을때 처리하는 부분
    $(document).on("click", ".coursefeebtn", function(e){
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
            window.history.pushState("","",tag_a.attr("href")); //AJAX로 호출한 URL로 변경시키기(address bar)
          }
      });
    });
});

