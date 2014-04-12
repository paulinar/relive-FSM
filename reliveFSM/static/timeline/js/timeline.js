$( document ).ready(function() {
    console.log( "timeline.js ready!" );
    $("#search-button").click(function() {
    	$("#my-picture").fadeOut("slow", function() {
    		var searchQuery = $("#search-bar").val();
	    	console.log(searchQuery);
	    	$.ajax({
			  type: "GET",
			  url: "search/?q=" + searchQuery,
			  success: function(data) {
			    console.log(data.docs);
			    filterDate = $("#filter-date").is(":checked");
			    filterImage = $("#filter-image").is(":checked");
			    if(filterDate) {
			    	var withDate = filter("date", data.docs);
			        data.docs = withDate;
			    }
			    if(filterImage) {
			    	var withImage = filter("image", data.docs);
			        data.docs = withImage;
			    }
				var template = $("#timeline-template").html();
				var html = Mustache.render(template, data.docs);
				$("#timeline-list").html(html);
			  }
			});
    	});
    });
});

var filter = function(attr, list) {
	translate = {"date": "fsmDateCreated", "image": "fsmImageUrl"};
	filterBy = translate[attr];
	var newData = [];
	for (var i=0, len=list.length; i<len; i++) {
    	if (!list[i].hasOwnProperty(filterBy)) {
    		console.log("filtering");
    	} else {
    		newData.push(list[i])
    	}
    }
    return newData;
}