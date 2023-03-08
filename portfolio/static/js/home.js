$(document).ready(function(){   
    $(window).on("scroll", function() {
        if($(window).scrollTop() > 300 && $(window).width()>425) {
            $("header").addClass("active");
        }
        else if($(window).width()<425){
            $("header").addClass("active");
        } 
        else {
            //remove the background property so it comes transparent again (defined in your css)
        $("header").removeClass("active");
        }
    });
    $(".nav-toggle-label").click(function(){
        $("header").toggleClass("click");
      });

    
    
    new WOW().init();
    setTimeout(function () {
        $('.loader_bg').fadeToggle();
    }, 1200);
});
