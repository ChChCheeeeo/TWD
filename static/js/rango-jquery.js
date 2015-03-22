$(document).ready(function() {

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

	# used to find id 
	. used to find classes

*/ 

	$("#about-btn").click( function(event){
		alert("You clicked the button using Jqury");
	});


	$("p").hover(
		/*
			Over "p" elements, should change from
			blue to red. Chaning "this" to "p" 
			breaks the color change.
			the hover function to assign an event
			handler to the on hover event, and
			then used the css function to change 
			the color of the element. 
		*/
		
		function() {
            $(this).css('color', 'red');
    	},
   		
   		function() {
            $(this).css('color', 'blue');
    	}
    );//end hover

	/*
		change link color after clicking.
	*/
    $('#likes').click(
		function() {
            $(this).css('color', 'red');
    	},
   		
   		function() {
            $(this).css('color', 'yellow');
    	}
    	// ,
    	// function(){
    	// 	console.log("like clicked");
    	// 	alert('clicked');
    	// 	document.write('fuck');
    	// }
    );//end click



    // $("#about-btn").addClass('btn btn-primary')
    // $("#about-btn").click( function(event) {
    	/*
    		It is also possible to access the 
    		html of a particular element.
    		On click of the element with id 
    		#about-btn, we first get the html 
    		inside the element with id msg and 
    		appeand “o” to it. Then we change 
    		the html inside the element by 
    		calling the html function again, 
    		but this time passing through string 
    		msgstr to replace the html inside 
    		that element.
    	*/
		
		// msgstr = $("#msg").html()
		// msgstr = msgstr + "o"

		// $("#msg").html(msgstr)
	 // }); // end click

}); // end document ready
