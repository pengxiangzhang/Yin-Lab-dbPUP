
var activeBubble = '';
var activeBubbleElem = '';
bubbleOrigHTML = new Object();
var count1 = 0;

$(function() {

   $(document).keyup(function(e) {
      if (e.keyCode == 27 && activeBubble != '') { hideBubble(activeBubble); }
   });

   $('.bubbleDialog').each(function() {
      var id = $(this).attr('id');
      bubbleOrigHTML[id] = $(this).find('.bubbleText').html();
   });
       
   $('#login').click(function() {
       showBubble('log_in_bubble', $(this) );
   });       
   
   $('#login_continue').click(function() {
      $.post('ajax.html', {'action' : 'Log in', 'email' : $('#login_email').val(), 'pwd' : $('#login_pwd').val() }, function(data) {
         if (data.user_id < 1) {
            if (data.reset == 'complete') {
               $('#login_error').html('A temporary password has been emailed to you.').effect("highlight", {}, 1000);
            }
            else {
               $('#login_error').html('Error!  Incorrect e-mail or password. Try again.').effect("highlight", {}, 500);
            }
         }
         else {
            document.forms['log_in_form'].submit();
            //window.location.href = 'index.html';
         }
      }, 'json');
      return false;
   });   

   $('#create_account').click(function() {
      showBubble('create_account_bubble', $(this) );
   });
   
   $('#log_in_from_create').click(function() {
      showBubble('log_in_bubble', activeBubbleElem);
   });
   
   $('#create_account_poll_continue').click(function() {
      var thisPoll = $('#poll_id').val();
      var myChoice = $('#my_choice').val();
      var checked = (  $('#create_account_poll_daily').attr('checked')  ) ? 'on' : ''; 
      var privacy_agree = (  $('#poll_privacy_agree').attr('checked')  ) ? 'on' : ''; 
      
      if (privacy_agree != 'on') {
         $('#poll_error').html('<p>You must agree to the Privacy Policy.</p>').effect("highlight", {}, 1000);
         return false;
      }
      if ($('#create_account_poll_email').val() == '') {
         $('#poll_error').html('<p>Please enter an e-mail address.</p>').effect("highlight", {}, 1000);
         return false;
      }      
      
      $('#poll_error').html('<p>Your account is being created.  <img src="/loading.gif" border=0></p>').effect("highlight", {}, 500);
   
      $.post('ajax.html', {'action' : 'Create account', 'first_name' : $('#create_account_poll_name').val(), 'email' : $('#create_account_poll_email').val(), 'pwd' : $('#create_account_poll_pwd').val(), 'send_email' : checked, 'this_poll' : thisPoll, 'my_choice' : myChoice }, function(data) {
         if (data == 'in use') {        
            $('.bubbleDialog .error').html('<p>That e-mail address is already registered.</p><p>Please <span class="pseudolink" id="log_in_from_bubble">log in</span>.</p>').effect("highlight", {}, 500);
            $('#log_in_from_bubble').click(function() {
               showBubble('log_in_bubble', activeBubbleElem);     
            });  
         }
         else {
            var keepW = $('#' + activeBubble).width();
            $('#' + activeBubble + ' .bubbleText').html( data );
            $('#' + activeBubble).width(keepW);               
         }
      });
   });
   
   $('#create_account_continue').click(function() {
   
      var checked = (  $('#create_account_daily').attr('checked')  ) ? 'on' : '';
      var privacy_agree = (  $('#privacy_agree').attr('checked')  ) ? 'on' : ''; 
      
      if (privacy_agree != 'on') {
         $('#create_error').html('<p>You must agree to the Privacy Policy.</p>').effect("highlight", {}, 1000);
         return false;
      }      
      
      if ($('#create_account_email').val() == '') {
         $('#create_error').html('<p>Please enter an e-mail address.</p>').effect("highlight", {}, 1000);
         return false;
      }       
      
      $('#create_error').html('<p>Your account is being created.  <img src="/loading.gif" border=0></p>').effect("highlight", {}, 500);
  
      $.post('ajax.html', {'action' : 'Create account', 'first_name' : $('#create_account_name').val(), 'email' : $('#create_account_email').val(), 'pwd' : $('#create_account_pwd').val(), 'send_email' : checked }, function(data) {
         if (data == 'in use') {        
            $('.bubbleDialog .error').html('<p>That e-mail address is already registered.</p><p>Please <span class="pseudolink" id="log_in_from_bubble">log in</span>.</p>').effect("highlight", {}, 500);
            $('#log_in_from_bubble').click(function() {
               showBubble('log_in_bubble', activeBubbleElem);     
            });  
         }
         else {
            var keepW = $('#' + activeBubble).width();
            $('#' + activeBubble + ' .bubbleText').html( data );
            $('#' + activeBubble).width(keepW);               
         }
      });
   });   
      
});

function showBubble(id, elem) {   
      var offset = $(elem).offset();
      var thisBubble = $('#' + id);
      var newTop = offset.top - 31;
      var newLeft = offset.left - ( $(thisBubble).width() + 41);   
      $(thisBubble).css('top', newTop);
      $(thisBubble).css('left', newLeft);
      $('.bubbleDialog').hide();
      var origHTML = bubbleOrigHTML[id];
      var currentHTML = $(thisBubble).find('.bubbleText').html();
      if (origHTML != currentHTML) {
         $(thisBubble).find('.bubbleText').html(' '+origHTML);
      }
      $(thisBubble).show();
      $('#overlay').show();
      activeBubble = id;
      activeBubbleElem = elem;
      count1++;
}
   
function hideBubble(id) {
      if (id == 'all') {
         $('.bubbleDialog').hide();
      }
      else {
         $('#' + id).hide();
      }         
      $('#overlay').hide();      
      activeBubble = '';
      activeBubbleElem = '';
}

function fbShare() {

   var attachment = {
      'name': 'Correlated.org - Discover surprising correlations',
      'href': 'https://www.correlated.org',
      'description': "Today's correlation: " + $('.first .stat').html() + "\n\nHelp us discover tomorrow's correlation by responding to the daily poll: " + $('.today_poll').html(),
      'media':[{
         'type': 'image',
         'src': 'https://www.correlated.org/correlated_thumb.png',
         'href': 'http://correlated.org'
      }]
   };   
   
   var attachment2 = {
      'name': 'Correlated.org - Discover surprising correlations',
      'href': 'https://www.correlated.org',
      'description': "Today's correlation: " + $('.first .stat').html() + "\n\nHelp us discover tomorrow's correlation by responding to the daily poll: " + $('.today_poll').html(),
      'media':[{
         "type": "flash", 
         "swfsrc": "http://www.youtube.com/v/jULQeW4HCpY?fs=1&hl=en_US", 
         "imgsrc": "http://i4.ytimg.com/vi/jULQeW4HCpY/default.jpg", 
         "width": "90", 
         "height": "56",
         "expanded_width": "398", 
         "expanded_height": "243"
      }]
   };      

   FB.ui({
      method: 'stream.publish',
      message: '',
      attachment: attachment2,
      user_message_prompt: 'Post this link'
      },
      function(response) {
         if (response && response.post_id) {
            //show_preview();
         } 
         else {
            //alert('Post was not published.');
         }
      }
   );

}


function show_preview() {

   showBubble('preview_bubble', $('#share_fb .pseudolink') );
   $.post('ajax.html', {'action' : 'Generate preview' }, function(data) {
      $('#preview_bubble .results').html(data);
   });

}