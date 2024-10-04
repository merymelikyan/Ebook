
  (function ($) {
   
  "use strict";

    // MENU
    $('.navbar-collapse a').on('click',function(){
      $(".navbar-collapse").collapse('hide');
    });
    
    // CUSTOM LINK
    $('.smoothscroll').click(function(){
      var el = $(this).attr('href');
      var elWrapped = $(el);
      var header_height = $('.navbar').height();
  
      scrollToDiv(elWrapped,header_height);
      return false;
  
      function scrollToDiv(element,navheight){
        var offset = element.offset();
        var offsetTop = offset.top;
        var totalScroll = offsetTop-navheight;
  
        $('body,html').animate({
        scrollTop: totalScroll
        }, 300);
      }
    });

    $("#contact").on("submit", (e) => {
      e.preventDefault();
      const data = {
        'name': $('input[name=name]').val(),
        'email': $('input[name=email]').val(),
        
        'csrfmiddlewaretoken': '{{ csrf_token }}'
      };
      $.post("http://127.0.0.1:8000/messages/receive_message/", data, () => {
        console.log("all is okay");
      });
    
      e.target.reset();
      });
    


  
  })(window.jQuery);


