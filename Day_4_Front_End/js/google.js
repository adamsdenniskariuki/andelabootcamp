/* function to validate user input */

$("#search_form").submit(function( event ) {

	if($.trim($('#q').val()) == ""){
		$('#error').html('Input cannot be empty');
		event.preventDefault();
	}
	
});