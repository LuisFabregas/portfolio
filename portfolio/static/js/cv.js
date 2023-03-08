$(document).ready(function(){   
    $(window).on("scroll", function() {
        if($(window).scrollTop() > 200) {
            $("header").addClass("active");
        } else {
            //remove the background property so it comes transparent again (defined in your css)
        $("header").removeClass("active");
        }
    });
    $(".nav-toggle-label").click(function(){
        $("header").toggleClass("click");
        $("nav ul").toggleClass("click");
      });
});
