$(document).ready(function() {
  $('#urlError').hide();
  $('.success-message').hide();
  $('#submitUrlBtn').click(function() {
    var url = $('#searchInput').val();
    var urlRegex = /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/gi;
    if (url.match(urlRegex)) {
      $('#urlError').slideUp(250, "swing");
      $('.success-message').slideDown(250, "swing");
      var oldURL = url;
      var index = 0;
      var newURL = oldURL;
      index = oldURL.indexOf('?');
      if(index == -1){
          index = oldURL.indexOf('#');
      }
      if(index != -1){
          newURL = oldURL.substring(0, index);
      }
      console.log(newURL);
      findArticles(newURL);
    } else {
      $('.success-message').slideUp(250, "swing");
      $('#urlError').slideDown(250, "swing");
    }
  });

  $('#searchInput').keyup(function() {
    $('#urlError').slideUp(250, "swing");
  });

  //initialize swiper when document ready
  var swiper = new Swiper('.swiper-container', {
      nextButton: '.swiper-button-next',
      prevButton: '.swiper-button-prev',
      spaceBetween: 30,
      effect: 'coverflow',
      grabCursor: true,
      centeredSlides: true,
      slidesPerView: '3',
      coverflow: {
          rotate: 0,
          stretch: 50,
          depth: 100,
          modifier: 1,
          slideShadows : false
      }
  });
});

function findArticles(url) {
  $.ajax({
    url: '/checkURL', //put address to python function which will receieve url
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify({inputURL: url}),
    type: 'POST',
    dataType: 'json',
    success: function(data) {
      console.log(data);
      url_arr = data['url_arr'];
      // fiter out source url
      if (url_arr.indexOf(url) != -1) {
        url_arr = url_arr.filter(function(a){return a !== url});
      }
      makePreviewDivs(url_arr);
      var swiper = new Swiper('.swiper-container', {
          nextButton: '.swiper-button-next',
          prevButton: '.swiper-button-prev',
          spaceBetween: 30,
          effect: 'coverflow',
          grabCursor: true,
          centeredSlides: true,
          slidesPerView: '3',
          coverflow: {
              rotate: 0,
              stretch: 50,
              depth: 100,
              modifier: 1,
              slideShadows : false
          }
      });
      $('iframe').error(function() {
        this.hide();
      });
    },
    error: function(error) {
      console.log(error);
    }
  });
}

function makePreviewDivs(url_arr) {
  url_arr.forEach(function(url) {
    $('#articleListWrapper').append(makeiFrame(url));
  });
}

function makeiFrame(url) {
  if (url.includes("nytimes.com")) {
    html = '<a class="swiper-slide not-displayed">Sorry! This article is from the NY Times and cannot be displayed. Click here to go directly to their site.</a>'
  } else {
    html = '<iframe class="swiper-slide" src="'+url+'"></iframe>';
  }
  return html;
}
