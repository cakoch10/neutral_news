$(document).ready(function() {
  $('#urlError').hide();
  $('.success-message').hide();
  $('#submitUrlBtn').click(function() {
    var url = $('#searchInput').val();
    var urlRegex = /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/gi;
    if (url.match(urlRegex)) {
      $('#urlError').slideUp(250, "swing");
      $('.success-message').slideDown(250, "swing");
      findArticles(url);

    } else {
      $('.success-message').slideUp(250, "swing");
      $('#urlError').slideDown(250, "swing");
    }
  });

  $('#searchInput').keyup(function() {
    $('#urlError').slideUp(250, "swing");
  });

});

function findArticles(url) {
  $.ajax({
    url: '/checkURL', //put address to python function which will receieve url
    data: $('#searchForm').serialize(),
    type: 'POST',
    dataType: 'json',
    success: function(response) {
      console.log(response);
    },
    error: function(error) {
      console.log(error);
    }
  });
}
