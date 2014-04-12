$( document ).ready(function() {
    console.log( "ready!" );
    $("#search-button").click(function() {
    	var searchQuery = $("#search-bar").val();
    	console.log(searchQuery);
    	$.ajax({
		  type: "GET",
		  url: "search/?q=" + searchQuery,
		  success: function(data) {
		    console.log("success");;
		    console.log(data);
		  }
		});
    });
});