$(window).scroll(function (event) {
	var scroll = $(window).scrollTop();
	if(scroll > 100){
		if(! $("#websiteHeaderLogo").hasClass("smallNav")){
			$("#websiteHeaderLogo").addClass("smallNav");
			$("#websiteHeaderLogo").animate({"height": "1.4em"}, { duration: 400, queue: false });
			$(".websiteNavbarList").animate({"padding": "0px"}, { duration: 400, queue: false });
			$("#websiteNavbar").animate({"min-height": "56px"}, { duration: 400, queue: false });
			console.log("header shrink");
		}
	}
	else if(scroll < 80){
		if($("#websiteHeaderLogo").hasClass("smallNav")){
			$("#websiteHeaderLogo").removeClass("smallNav");
			$("#websiteHeaderLogo").animate({"height": "2.4em"}, { duration: 400, queue: false });
			$(".websiteNavbarList").animate({"padding": "0.9em 0.1em"}, { duration: 400, queue: false });
			$("#websiteNavbar").animate({"min-height": "80px"}, { duration: 400, queue: false });
			console.log("header expand");
		}
	}
});