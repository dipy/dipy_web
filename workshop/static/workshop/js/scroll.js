var width = 800;

(function ($) {
  $.fn.invisible = function () {
    return this.each(function () {
      $(this).css("visibility", "hidden");
    });
  };
  $.fn.visible = function () {
    return this.each(function () {
      $(this).css("visibility", "visible");
    });
  };
})(jQuery);

$(".left-arrow").invisible();

$(".right-arrow").click(function (e) {
  e.preventDefault();
  let slider = $(this).siblings(".m-highlights-img-holder");
  let scroll = slider.attr("scroll");
  if (scroll + window.innerWidth < width) {
    slider.animate({ scrollLeft: window.innerWidth }, 300);
    scroll += window.innerWidth;
  } else {
    slider.animate({ scrollLeft: width }, 300);
    scroll = width;
    $(this).invisible();
  }
  slider.attr("scroll", scroll);
  $(this).siblings(".left-arrow").visible();
});

$(".left-arrow").click(function (e) {
  e.preventDefault();
  let slider = $(this).siblings(".m-highlights-img-holder");
  let scroll = slider.attr("scroll");
  if (scroll - window.innerWidth > 0) {
    slider.animate({ scrollLeft: -window.innerWidth }, 300);
    scroll -= window.innerWidth;
  } else {
    slider.animate({ scrollLeft: 0 }, 300);
    scroll = 0;
    $(this).invisible();
  }
  slider.attr("scroll", scroll);
  $(this).siblings(".right-arrow").visible();
});
