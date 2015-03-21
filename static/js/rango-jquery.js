$(document).ready(function() {

// JQuery code to be added in here.
/*
	This piece of JQuery, first selects the document
	object (with $(document)), and then makes a call
	to ready(). Once the document is ready i.e. the
	complete page is loaded, then the anonymous
	function denoted by function(){ } will be
	 executed. It is pretty typical, if not
	  standard, to wait until the document has
	  been finished loading before running
	   the JQuery functions.
*/ 

	$("#about-btn").click( function(event){
		alert("You clicked the button using Jqury");

	});
});
