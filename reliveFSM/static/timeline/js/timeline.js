$( document ).ready(function() {
    console.log( "timeline.js ready!" );
    $("#search-button").click(function() {
    	var searchQuery = $("#search-bar").val();
    	console.log(searchQuery);
    	$.ajax({
		  type: "GET",
		  url: "search/?q=" + searchQuery,
		  success: function(data) {
		  	// var template = "derp";
		  	// var html = Mustache.to_html(template, data);
		  	// $("#timeline-list").html(html);
		    console.log(data.docs);
			var template = $("#timeline-template").html();
			console.log(template)
			var html = Mustache.render(template, data.docs);
			console.log(html)
			$("#timeline-list").html(html);
		  }
		});
    });
});