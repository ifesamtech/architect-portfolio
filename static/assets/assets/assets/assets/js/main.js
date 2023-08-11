$(document).ready(function(){
    let $btns = $('.project-area .button-group button');
    $btns.click(function(e){
        $('.project-area .button-group button').removeClass('active');
        e.target.classList.add('active');

        let selector = $(e.target).attr("data-filter");
        $('.project-area .grid').isotope({
            filter:selector
        })

        return false;
    })

    $('project-area .button-group #btn1').trigger("click");

    $('.project-area .grid .test-popup-link').magnificPopup({
        type: 'image',
        gallery:{enabled:true}
        // other options
      });

    //   owl-carousel

    $('.site-main .about-me-area .owl-carousel').owlCarousel({
        loop:true,
        autoplay:true,
        dots:true,
        responsive:{
            0:{
                items:1
            },
            544:{
                items:2
            }
        }
    })

    // sticky nav menu


    // $(window).on("scroll", function() {
    //     if ($ (window).scrollTop()) {
    //         $('nav').addClass('navbar_fixed');
    //     }else{
    //         $('nav').removeClass('navbar_fixed');
    //         }


    //     });

    // const banner_img = document.getElementById('')




    // custom animate

//     function anim(){
//     var animate = document.querySelectorAll(".anim")
//     for (var i = 0; i < animate.length; 1++) {
//         var windowHeight = window.innerHeight;
//         var elementTop = reveals[i].getBoundingClientRect().top;
//         var elementVisible = 150;
//         if (elementTop < windowHeight - elementVisible) {
//             animate[i].classList.add("anim");
//         } else {
//             animate[i].classList.remove("anim")
//         }
//     }
// }

    const body = document.body;
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = (window.pageYOffset)

        if (currentScroll <= 0) {
            body.classList.remove("scroll-up")
            body.classList.remove("scroll-down")
        }

        if (currentScroll > lastScroll && !body.classList.contains("scroll-down")){
            body.classList.remove("scroll-up")
            body.classList.add("scroll-down")
        }

        if (currentScroll < lastScroll && body.classList.contains("scroll-down")){
            body.classList.add("scroll-up")
            body.classList.remove("scroll-down")
        }

        lastScroll = currentScroll;
    })

    // $(window).on("scroll", function () {
    //     AOS.init();
    // });

    const proj = document.querySelector(".proj");
    const slider = document.querySelector(".slider");
    const navbar = document.querySelector(".navbar");
    // const proj = document.querySelector(".hero");
    const headline = document.querySelector(".headline");
    // const proj = document.querySelector(".hero");
    
    const tl = new TimelineMax();
    
    tl.fromTo(proj,1, {height:"0%"}, {height: '80%', ease: Power2.easeInOut}
    ).fromTo(
        proj,
        1.2,
        {width:"100%"},
        {width:"80%", ease: Power2.easeInOut}
    )

    .fromTo(slider, 1.2, {x:"-100%"}, {x:'0%', ease:Power2.easeInOut}, "-=1.2")



});
// click to scroll Top

$('.move-up span').click(function(){
    $('html, body').animate({
        scrollTop: 0
    }, 2000);
})