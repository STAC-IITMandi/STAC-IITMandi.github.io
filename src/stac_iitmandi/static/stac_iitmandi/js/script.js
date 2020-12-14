$(function () {

    $('.navbar-toggler').on('click', function() {
        if (!$('#mainNav').hasClass('navbar-reduce')) {
          $('#mainNav').addClass('navbar-reduce');
        }
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
        } else {
            if (!$("#navbarDefault").hasClass("show")) {
                $(".navbar-expand-md").removeClass("bg-light");
                $(".navbar-expand-md").removeClass("navbar-reduce");
                $('.dropdown-menu').removeClass('dropdown-reduce');               
            }
            $(".navbar-expand-md").addClass("navbar-trans");
            $('.dropdown-menu').addClass('dropdown-trans');
        }
    });
});(jQuery);