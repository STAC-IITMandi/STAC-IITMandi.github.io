$(function () {

    $('.navbar-toggler').on('click', function() {
        if (!$('#mainNav').hasClass('navbar-reduce')) {
          $('#mainNav').addClass('navbar-reduce');
        }
    });

    // Back to top button
    $('.back-to-top').on('click', function() {
        $('html, body').animate({
            scrollTop: 0
        }, 1000, 'easeInOutExpo');
        return false;
    });

    // navbar-toggler button
    $('.toggle-button').on('click', function () {
        $('.animated-icon').toggleClass('open');
    });
    
    /*--/ Navbar Menu Reduce /--*/
    $(window).trigger("scroll");
    $(window).on("scroll", function() {
        var pixels =50;
        var top = 1200;
        if ($(window).scrollTop() > pixels) {
            $(".navbar-expand-md").addClass("bg-light");
            $(".navbar-expand-md").addClass("navbar-reduce");
            $(".navbar-expand-md").removeClass("navbar-trans");
            $('.dropdown-menu').removeClass('dropdown-trans');
            $('.dropdown-menu').addClass('dropdown-reduce');
            $('.back-to-top').fadeIn('slow');
        } else {
            if (!$("#navbarDefault").hasClass("show")) {
                $(".navbar-expand-md").removeClass("bg-light");
                $(".navbar-expand-md").removeClass("navbar-reduce");
                $('.dropdown-menu').removeClass('dropdown-reduce');               
            }
            $(".navbar-expand-md").addClass("navbar-trans");
            $('.dropdown-menu').addClass('dropdown-trans');
            $('.back-to-top').fadeOut('slow'); 
        }
    });
    // venobox 
    $(document).ready(function(){
        $('.venobox').venobox(); 
        $('.venobox_custom').venobox({
            framewidth : '300px',                            
            frameheight: '200px',                            
            border     : '10px',                             
            bgcolor    : '#5dff5e',                         
            titleattr  : 'data-title',                     
            numeratio  : true,                             
            infinigall : true,                     
        });
    });

  // slider carousel (uses the Owl Carousel library)
  $(".slider-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    items: 1
  });
});(jQuery);
