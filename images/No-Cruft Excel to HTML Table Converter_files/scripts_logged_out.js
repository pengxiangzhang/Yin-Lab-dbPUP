
$(function() {    

   $('.poll_option').click(function() {
      var optionID = $(this).attr('id');
      var thisVal = $(this).attr('value');
      var pollID = $(this).attr('data-poll-id');
      optionID = optionID.replace('poll_option_','');
      $('#my_choice').val( optionID );    
      
      $.post('ajax.html', {'action' : 'Vote by IP', 'poll_id' : pollID, 'option_id' : optionID }, function(data) {
         //alert(pollID + ',' + optionID);
      });
      
      showBubble('create_account_from_poll', $(this) );
      $('#create_account_from_poll h3').html('Thanks! We\'ve recorded your "' + thisVal + '" response!');     
   });   
   
   $('#log_in_from_poll').click(function() {
      showBubble('log_in_bubble', $('#login') );
   });  
   
   $('#see_login').click(function() {
      showBubble('log_in_bubble', $('#see_login') );
   });     
   
   $('#see_create_account').click(function() {
      showBubble('create_account_bubble', $('#see_create_account') );
   });     
   
   $('#about').click(function() {
      showBubble('about_bubble', $('#about') );
   });    

});