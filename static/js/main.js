/**
 * Name: Zunzo
 * Version: 1.0
 * Author: Themesflat
 * Author URI: http://www.themesflat.com
 */

/**
 * isMobile
 * responsiveMenu
 * headerFixed
 * topSearch
 * toogle cart
 * Sidebar menu
 * menu Mobie Style 02
 * timerInterval
 * slide
 * imgae slide about
 * testimonial
 * slide product
 * logo partner
 * slide product
 * goTop
 * retinaLogos
 * video
 * Preloader
 * Counter Number
 * input file name
 */

(function ($) {
  "use strict";

  var isMobile = {
    Android: function () {
      return navigator.userAgent.match(/Android/i);
    },
    BlackBerry: function () {
      return navigator.userAgent.match(/BlackBerry/i);
    },
    iOS: function () {
      return navigator.userAgent.match(/iPhone|iPad|iPod/i);
    },
    Opera: function () {
      return navigator.userAgent.match(/Opera Mini/i);
    },
    Windows: function () {
      return navigator.userAgent.match(/IEMobile/i);
    },
    any: function () {
      return (
        isMobile.Android() ||
        isMobile.BlackBerry() ||
        isMobile.iOS() ||
        isMobile.Opera() ||
        isMobile.Windows()
      );
    },
  };

  var responsiveMenu = function () {
    var menuType = "desktop";

    $(window).on("load resize", function () {
      var currMenuType = "desktop";

      if (matchMedia("only screen and (max-width: 991px)").matches) {
        currMenuType = "mobile";
      }

      if (currMenuType !== menuType) {
        menuType = currMenuType;

        if (currMenuType === "mobile") {
          var $mobileMenu = $("#mainnav").attr("id", "mainnav-mobi");
          var hasChildMenu = $("#mainnav-mobi").find("li:has(ul)");

          $("#header").after($mobileMenu);
          hasChildMenu.children("ul").hide();
          hasChildMenu.children("a").after('<span class="btn-submenu"></span>');
          $(".btn-menu").removeClass("active");
        } else {
          var $desktopMenu = $("#mainnav-mobi")
            .attr("id", "mainnav")
            .removeAttr("style");
          $desktopMenu.find(".submenu").removeAttr("style");
          $("#header").find(".nav-wrap").append($desktopMenu);
          $(".btn-submenu").remove();
        }
      }
    });

    $(document).on("click", "#mainnav-mobi li .btn-submenu", function (e) {
      $(this).toggleClass("active").next("ul").slideToggle(300);
      e.stopImmediatePropagation();
    });
    $(".btn-menu").on("click", function () {
      $("#mainnav-mobi").toggleClass("active");
      $(".overlay-menu-mobie").toggleClass("active");
    });
    $(".overlay-menu-mobie").on("click", function () {
      $("#mainnav-mobi").toggleClass("active");
      $(".overlay-menu-mobie").toggleClass("active");
    });
  };

  var headerFixed = function () {
    if ($("body").hasClass("header-sticky")) {
      var nav = $("#header");

      if (nav.length) {
        var offsetTop = nav.offset().top,
          headerHeight = nav.height(),
          injectSpace = $("", {
            height: headerHeight,
          }).insertAfter(nav);

        $(window).on("load scroll", function () {
          if ($(window).scrollTop() > offsetTop) {
            nav.addClass("downscrolled");
            injectSpace.show();
          } else {
            nav.removeClass("downscrolled");
            injectSpace.hide();
          }

          if ($(window).scrollTop() > 500) {
            nav.addClass("upscrolled");
          } else {
            nav.removeClass("upscrolled");
          }
        });
      }
    }
  };

  var topSearch = function () {
    $(document).on("click", function (e) {
      var clickID = e.target.id;
      if (clickID !== "s") {
        $(".top-search").removeClass("active");
      }
    });
    $(document).on("click", function (e) {
      var clickID = e.target.class;
      if (clickID !== "a111") {
        $(".show-search").removeClass("active-search");
      }
    });

    $(".show-search").on("click", function (event) {
      event.stopPropagation();
    });
    $("#searchform").on("click", function (event) {
      event.stopPropagation();
    });
    $(".show-search").on("click", function (event) {
      if (!$(".top-search").hasClass("active")) {
        $(".top-search").addClass("active");
        event.preventDefault();
      } else $(".top-search").removeClass("active");
      event.preventDefault();
      if (!$(".show-search").hasClass("active-search"))
        $(".show-search").addClass("active-search");
      else $(".show-search").removeClass("active-search");
    });
  }; //show search

  //toogle cart
  $(".minicar-overlay").on("click", function () {
    $(this).closest(".header").find(".nav-shop-cart").toggleClass("active");
    $(this)
      .closest(".header")
      .find(".minicar-overlay")
      .toggleClass("active-minicart");
  });
  $(".cart > a").on("click", function () {
    $(this).closest(".header").find(".nav-shop-cart").toggleClass("active");
    $(this)
      .closest(".header")
      .find(".minicar-overlay")
      .toggleClass("active-minicart");
  });
  $(".minicart-close").on("click", function () {
    $(this).closest(".header").find(".nav-shop-cart").toggleClass("active");
    $(this)
      .closest(".header")
      .find(".minicar-overlay")
      .toggleClass("active-minicart");
  }); //toogle cart

  $(".minicar-overlay").on("click", function () {
    $(this).closest(".header-v2").find(".nav-shop-cart").toggleClass("active");
    $(this)
      .closest(".header-v2")
      .find(".minicar-overlay")
      .toggleClass("active-minicart");
  });
  $(".cart > a").on("click", function () {
    $(this).closest(".header-v2").find(".nav-shop-cart").toggleClass("active");
    $(this)
      .closest(".header-v2")
      .find(".minicar-overlay")
      .toggleClass("active-minicart");
  });
  $(".minicart-close").on("click", function () {
    $(this).closest(".header-v2").find(".nav-shop-cart").toggleClass("active");
    $(this)
      .closest(".header-v2")
      .find(".minicar-overlay")
      .toggleClass("active-minicart");
  }); //toogle cart

  //Sidebar menu
  $(document).on("click", ".menu-item-has-children-mobile", function () {
    var args = { duration: 600 };
    if ($(this).hasClass("active")) {
      $(this).children(".sub-menu-sidebar").slideUp(args);
      $(this).removeClass("active");
    } else {
      $(".sub-menu-sidebar").slideUp(args);
      $(this).children(".sub-menu-sidebar").slideDown(args);
      $(".menu-item-has-children-mobile").removeClass("active");
      $(this).addClass("active");
    }
  });
  //Sidebar menu

  //Menu Mobie Style 02
  $(".line-1").on("click", function () {
    $(this)
      .closest(".header-v2")
      .find(".canvas-nav-wrap")
      .toggleClass("active");
    $(this)
      .closest(".header-v2")
      .find(".overlay-canvas-nav")
      .toggleClass("active");
  });
  $(".overlay-canvas-nav").on("click", function () {
    $(this)
      .closest(".header-v2")
      .find(".canvas-nav-wrap")
      .toggleClass("active");
    $(this)
      .closest(".header-v2")
      .find(".overlay-canvas-nav")
      .toggleClass("active");
  }); //Menu Mobie Style 02

  //timerInterval
  var timeMinutes = 10;
  var timeSeconds = timeMinutes * 60;
  var timer = document.getElementById("timer-sell-out");

  function startTimer() {
    timeSeconds--;
    var minutes = Math.floor(timeSeconds / 60);
    var seconds = timeSeconds % 60;

    if (timeSeconds < 0) {
      timer.textContent = "00:00";
      clearInterval(timerInterval);
      return;
    }
    if (minutes < 10) {
      minutes = "0" + minutes;
    }
    if (seconds < 10) {
      seconds = "0" + seconds;
    }
  //  timer.textContent = minutes + ":" + seconds;
  }

  var timerInterval = setInterval(startTimer, 1000);
  //timerInterval

  //Slide
  var swiper = new Swiper(".mySwiper", {
    effect: "fade",
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    },
  }); //Slide

  //Imgae Slide about
  var swiper3 = new Swiper(".image-carousel", {
    slidesPerView: 3,
    spaceBetween: 32,
    loop: true,
  }); //Imgae Slide about

  //Testimonial
  var swiper4 = new Swiper(".testimonial-wrap-v2", {
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
  $(".swiper-testimonial").owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    items: 1,
    autoplay: true,
    dots: false,
  });
  //Testimonial

  //slide product
  var swiper5 = new Swiper(".tf-slider-product", {
    effect: "fade",
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  }); //slide product

  //logo partner
  $(".sologan-logo").owlCarousel({
    loop: true,
    margin: 80,
    nav: false,
    dots: false,
    autoplay: true,
    responsive: {
      0: {
        items: 2,
      },
      600: {
        items: 4,
      },
      1000: {
        items: 6,
      },
    },
  }); //logo partner

  //slide product
  $(".owl-themes").owlCarousel({
    loop: true,
    margin: 30,
    nav: true,
    dots: false,
    autoplay: true,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 1,
      },
      1024: {
        items: 1,
      },
      1366: {
        items: 2,
      },
    },
  }); //slide product

  //goTop
  var goTop = function () {
    $(window).scroll(function () {
      if ($(this).scrollTop() > 800) {
        $(".go-top").addClass("show");
      } else {
        $(".go-top").removeClass("show");
      }
    });

    $(".go-top").on("click", function () {
      $("html, body").animate({ scrollTop: 0 }, 1000);
      return false;
    });
  }; //goTop

  //retinaLogos

  var retinaLogos = function () {
    var retina = window.devicePixelRatio > 1 ? true : false;

    if (retina) {
      $("#a2").attr({ src: logo2url, width: "190", height: "42" });
      $("#a3").attr({ src: logov2url, width: "124", height: "42" });
      $("#a1").attr({ src: logofooter2url, width: "125", height: "43" });
    }
  }; //retinaLogos

  //video
  var video = function () {
    if ($("div").hasClass("benefit-video")) {
      $(".popup-youtube").magnificPopup({
        type: "iframe",
      });
    }
  }; //video

  //preloader
  var preloader = function () {
    setTimeout(function () {
      $(".preload-container").fadeOut("slow", function () {
        $(this).remove();
      });
    }, 1000);
  }; //preloader

  //preloader2, submit
  var plandsub = function () {
  const mask = document.querySelector('.mask');
  const loadingImg = document.querySelector('.loadingImg');
  const paymentbutton = document.getElementById('payment-button');
  const submitbutton = document.getElementById('submit-form-button');

  try {
    paymentbutton.addEventListener("click", () => {
    mask.classList.remove('hidden');
  });
  } catch (err){
    console.log("");
  };


  try {
    submitbutton.addEventListener("click", () => {
      mask.classList.remove('hidden');
      document.querySelectorAll("input").forEach(input => {
        input.addEventListener("invalid", () => {
        // 검증 후 폼 요소에 was-validated 클래스로 표시해 둔다
          mask.classList.add('hidden');
          console.log("preloader!!")
        })
      })
    });
    } catch (err){
      console.log("");
    };

  
  };//preloader2, submit

  //Counter Number
  var detectViewport = function () {
    $('[data-waypoint-active="yes"]').waypoint(
      function () {
        $(this).trigger("on-appear");
      },
      { offset: "90%", triggerOnce: true }
    );

    $(window).on("load", function () {
      setTimeout(function () {
        $.waypoints("refresh");
      }, 100);
    });
  };

  var counter = function () {
    $(".flat-counter").on("on-appear", function () {
      $(this)
        .find(".numb-count")
        .each(function () {
          var to = parseInt($(this).attr("data-to"), 10),
            speed = parseInt($(this).attr("data-speed"), 10);
          console.log(speed);
          if ($().countTo) {
            $(this).countTo({
              to: to,
              speed: speed,
            });
          }
        });
    });
  }; //Counter Number

  //upload file name
  $("#file").on("change", function () {
    var fileName = $("#file").val();
    $(".upload-name").val(fileName);
  }); //upload file name

	
  $(function(){
      $("#guestrun-check").click(function() {
          if ($("input[name=guestrun]").is(":checked")) {
              $("#guest-run-sec").addClass("show-sec");
              $("#period-sec").addClass("show-sec");
              $("#message-title").text("4");
              $("#submit-title").text("5");
          } else {
              $("#guest-run-sec").removeClass("show-sec");
              $("#period-sec").removeClass("show-sec");
              $("#message-title").text("4");
              $("#submit-title").text("5");
          }
      })
  });


  // Dom Ready
  $(function () {
    if (matchMedia("only screen and (min-width: 991px)").matches) {
      headerFixed();
    }
    responsiveMenu();
    goTop();
    retinaLogos();
    topSearch();
    video();
    detectViewport();
    counter();
    preloader();
    plandsub();
  });
})(jQuery);
