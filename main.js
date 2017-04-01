$(document).ready(function() {
  var modal = $('#imgModal');

  // Open modal image when user clicks on expand button
  $('.image-overlay-expand').click(function() {
    var img = $(this.closest('.image-container')).find('img');
    var modalImg = $('#modalContent');
    var captionText = $('#caption');
    var imgCredits = $(this).parent().find('.image-overlay-credits');
    var imgAlbums = $(this).parent().find('.image-overlay-albums');
    var imgDate = $(this).parent().find('.image-overlay-date');
    $(modal).css('display', 'block');
    $(modalImg).attr('src', $(img).attr('src'));
    $(captionText).html($(img).attr('alt') + " - " + $(imgCredits).html()
      + '<br/>'  + $(imgAlbums).html() + '<br/>' + $(imgDate).html());
  });

  // Hide modal when user clicks on close button
  $('.close').click(function() {
    $(modal).css('display', 'none');
  });

  // Hide modal if user clicks anywhere on the modal outside of the image
  $(window).click(function(e) {
    if (e.target.id === "imgModal") {
      $(modal).css('display', 'none');
    }
  });
});
