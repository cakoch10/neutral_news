$(document).ready(function() {
  $('#urlError').hide();

  $('#submitUrlBtn').click(function() {
    var url = $('#searchInput').val();
    var urlRegex = /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/gi;
    if (url.match(urlRegex)) {
      $('#urlError').slideUp(250, "swing");
      findArticles(url);
    } else {
      $('#urlError').slideDown(250, "swing");
    }
  });

  $('#searchInput').keyup(function() {
    $('#urlError').slideUp(250, "swing");
  });

});

function findArticles(url) {{
  result = $.ajax({
    url: '', //put address to python function which will receieve url
    data: {requestedURL : url},
    type: 'POST',
    dataType: ''
  });
  result.done(fillArticlePreviews());
}

function fillArticlePreviews(data) {

}
