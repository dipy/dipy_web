$(window).scroll(function (event) {
	var scroll = $(window).scrollTop();
	if(scroll > 100 && window.matchMedia('(min-width: 1200px)').matches){
		if(! $("#websiteHeaderLogo").hasClass("smallNav")){
			$("#websiteHeaderLogo").addClass("smallNav");
			$("#websiteHeaderLogo").animate({"height": "1.4em"}, { duration: 400, queue: false });
			$(".navbar-right > li").animate({"padding": "0px"}, { duration: 400, queue: false });
			$("#websiteNavbar").animate({"min-height": "56px"}, { duration: 400, queue: false });
			console.log("header shrink");
		}
	}
	else if(scroll < 120 && window.matchMedia('(min-width: 1200px)').matches){
		if($("#websiteHeaderLogo").hasClass("smallNav")){
			$("#websiteHeaderLogo").removeClass("smallNav");
			$("#websiteNavbar").animate({"min-height": "80px"}, { duration: 200, queue: false });
			$(".navbar-right > li").animate({"padding": "0.9em 0.1em"}, { duration: 200, queue: false });
			$("#websiteHeaderLogo").animate({"height": "2.4em"}, { duration: 400, queue: false });
			console.log("header expand");
		}
	}
});