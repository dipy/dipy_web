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
  let scroll = parseInt(slider.attr("scroll"));
  if (scroll + 2 * window.innerWidth < width) {
    scroll += window.innerWidth;
    slider.animate({ scrollLeft: scroll }, 300);
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
  let scroll = parseInt(slider.attr("scroll"));
  if (scroll - 2 * window.innerWidth > 0) {
    scroll -= window.innerWidth;
    slider.animate({ scrollLeft: scroll - window.innerWidth }, 300);
  } else {
    slider.animate({ scrollLeft: 0 }, 300);
    scroll = 0;
    $(this).invisible();
  }
  slider.attr("scroll", scroll);
  $(this).siblings(".right-arrow").visible();
});
