//document.write("Hello World")
//document.getElementById("idp").innerHTML="This para tag";
/*
var foodCost = prompt("Enter Cost:- ");
document.write("This was the food cost:- ",foodCost,"<br>")
alert("Each one of you has to pay:- " + (foodCost/3).toFixed(2))
*/

/*
var age = prompt("Enter age")
if (age<20)
{
    document.write("You go the school");
}
else if (age<10 && age>3)
{
    document.write("You also go to the school");
}
else
{
    document.write("Do whatever you want to do");
}

*/

/*
for (var i = 0; i < 2; i++) {
    document.write(i,"<br>")
}
*/
/*
function test() {
    document.write("Test Function")
    console.log("OK this is test function")
}

test();
*/
/*
$(function() {
  $("#addMore").click(function(e) {
    e.preventDefault();
    $("#fieldList").append("<li>&nbsp;</li>");
    $("#fieldList").append("<li><input type='text' name='name[]' placeholder='Name' /></li>");
    $("#fieldList").append("<li><input type='text' name='phone[]' placeholder='Phone' /></li>");
    $("#fieldList").append("<li><input type='text' name='email[]' placeholder='E-Mail' /></li>");
  });
});
*/
/*
//jQuery plugin
(function( $ ) {

   $.fn.uploader = function( options ) {
     var settings = $.extend({
       MessageAreaText: "No files selected.",
       MessageAreaTextWithFiles: "File List:",
       DefaultErrorMessage: "Unable to open this file.",
       BadTypeErrorMessage: "We cannot accept this file type at this time.",
       acceptedFileTypes: ['pdf', 'jpg', 'gif', 'jpeg', 'bmp', 'tif', 'tiff', 'png', 'xps', 'doc', 'docx',
        'fax', 'wmp', 'ico', 'txt', 'cs', 'rtf', 'xls', 'xlsx']
     }, options );

     var uploadId = 1;
     //update the messaging
      $('.file-uploader__message-area p').text(options.MessageAreaText || settings.MessageAreaText);

     //create and add the file list and the hidden input list
     var fileList = $('<ul class="file-list"></ul>');
     var hiddenInputs = $('<div class="hidden-inputs hidden"></div>');
     $('.file-uploader__message-area').after(fileList);
     $('.file-list').after(hiddenInputs);

    //when choosing a file, add the name to the list and copy the file input into the hidden inputs
     $('.file-chooser__input').on('change', function(){
        var file = $('.file-chooser__input').val();
        var fileName = (file.match(/([^\\\/]+)$/)[0]);

       //clear any error condition
       $('.file-chooser').removeClass('error');
       $('.error-message').remove();

       //validate the file
       var check = checkFile(fileName);
       if(check === "valid") {

         // move the 'real' one to hidden list
         $('.hidden-inputs').append($('.file-chooser__input'));

         //insert a clone after the hiddens (copy the event handlers too)
         $('.file-chooser').append($('.file-chooser__input').clone({ withDataAndEvents: true}));

         //add the name and a remove button to the file-list
         $('.file-list').append('<li style="display: none;"><span class="file-list__name">' + fileName + '</span><button class="removal-button" data-uploadid="'+ uploadId +'"></button></li>');
         $('.file-list').find("li:last").show(800);

         //removal button handler
         $('.removal-button').on('click', function(e){
           e.preventDefault();

           //remove the corresponding hidden input
           $('.hidden-inputs input[data-uploadid="'+ $(this).data('uploadid') +'"]').remove();

           //remove the name from file-list that corresponds to the button clicked
           $(this).parent().hide("puff").delay(10).queue(function(){$(this).remove();});

           //if the list is now empty, change the text back
           if($('.file-list li').length === 0) {
             $('.file-uploader__message-area').text(options.MessageAreaText || settings.MessageAreaText);
           }
         });

         //so the event handler works on the new "real" one
         $('.hidden-inputs .file-chooser__input').removeClass('file-chooser__input').attr('data-uploadId', uploadId);

         //update the message area
         $('.file-uploader__message-area').text(options.MessageAreaTextWithFiles || settings.MessageAreaTextWithFiles);

         uploadId++;

       } else {
         //indicate that the file is not ok
         $('.file-chooser').addClass("error");
         var errorText = options.DefaultErrorMessage || settings.DefaultErrorMessage;

         if(check === "badFileName") {
           errorText = options.BadTypeErrorMessage || settings.BadTypeErrorMessage;
         }

         $('.file-chooser__input').after('<p class="error-message">'+ errorText +'</p>');
       }
     });

     var checkFile = function(fileName) {
       var accepted          = "invalid",
           acceptedFileTypes = this.acceptedFileTypes || settings.acceptedFileTypes,
           regex;

       for ( var i = 0; i < acceptedFileTypes.length; i++ ) {
         regex = new RegExp("\\." + acceptedFileTypes[i] + "$", "i");

         if ( regex.test(fileName) ) {
           accepted = "valid";
           break;
         } else {
           accepted = "badFileName";
         }
       }

       return accepted;
    };
  };
}( jQuery ));

//init
$(document).ready(function(){
  $('.fileUploader').uploader({
    MessageAreaText: "No files selected. Please select a file."
  });
});
*/

// Add the following code if you want the name of the file appear on select
$(".custom-file-input").on("change", function() {
  var fileName = $(this).val().split("\\").pop();
  $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
});
