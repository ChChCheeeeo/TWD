/*
 add an event handler to the element with id #likes,
  i.e. the button. When clicked, it extracts the 
  category id from the button element, then makes
   an AJAX GET request which calls to
   /rango/like_category/ encoding the category_id in 
   the request. If successful, then 
   the HTML element with id like_count (i.e. the 
   <strong> ) is updated with the data returned by the
    request, and the HTML element with id likes (i.e. 
    the <button>) is hidden. when the button is clicked an AJAX
    request is made, given our url mapping, this invokes 
    the like_category view which updates the category and
     returns the new number of likes. When the AJAX 
     request receives the response it updates parts of
      the page, i.e. the text and the button. The #likes 
      button is hidden.
*/
$('#likes').click(
	function(){
    	var catid;
    	/*
    		When clicked, it will extract the 
    		category id from the button element
    	*/
    	catid = $(this).attr("data-catid");
    	// ajax get request
    	/*
    		then make an AJAX GET request which 
    		will make a call to /rango/like_category/ 
    		encoding the category_id in the request.
    	*/
    	$.get('/rango/like_category/', 
    		{category_id: catid},

    		function(data){
    			/*
    				If successful, the HTML element 
    				with id like_count (i.e. the <strong> ) 
    				is updated with the data returned by the 
    				request
    			*/
               $('#like_count').html(data);
               /*
               		and the HTML element with id likes 
               		(i.e. the <button>) is hidden.
               */
               $('#likes').hide();
    		} // end function
    	);
	} // end function
); // end click


$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/rango/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});


/*
	attached an event handler to the HTML input element with
	 id="suggestion" to trigger when a keyup event occurs. When it 
	 does the contents of the input box is obtained and placed into
	  the query variable. Then a AJAX GET request is made calling 
	  /rango/category_suggest/ with the query as the parameter. On
	  success, the HTML element with id=”cats” i.e. the div, is 
	  updated with the category list html.
*/
$('#suggestion').keyup(
	function(){
        var query;
        query = $(this).val();
        $.get('/rango/suggest_category/', 
        	{suggestion: query}, 
        	function(data){
         		$('#cats').html(data);
        	}
        );
	}
); //end keyup