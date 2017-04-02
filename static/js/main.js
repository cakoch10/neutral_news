$(document).ready(function() {
  $('#urlError').hide();
  $('.success-message').hide();
  $('.loader').hide();
  $('.swiper-container').hide();
  $('.swiper-wrapper').hide();
  $('#submitUrlBtn').click(function() {
    var url = $('#searchInput').val();
    var urlRegex = /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/gi;
    if (url.match(urlRegex)) {
      $('#articleListWrapper').html("");
      $('#urlError').slideUp(250, "swing");
      $('#success').html("Success! Please wait a few seconds as we retrieve stories from other sources...");
      $('.success-message').slideDown(250, "swing");
      var oldURL = url;
      var index = 0;
      var newURL = oldURL;
      index = oldURL.indexOf('?');
      if(index == -1) {
          index = oldURL.indexOf('#');
      }
      if(index != -1) {
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
    $('.success-message').slideUp(250, "swing");
  });
});

$( document ).ajaxStart(function() {
  $('.loader').fadeIn();
  $('.swiper-container').slideDown(250, "swing");
});

$( document ).ajaxComplete(function() {
  $('.loader').fadeOut();
  $('.swiper-wrapper').fadeIn();
  var swiper = new Swiper('.swiper-container', {
      nextButton: '.swiper-button-next',
      prevButton: '.swiper-button-prev',
      spaceBetween: 30,
      effect: 'coverflow',
      coverflow: {
          rotate: 50,
          stretch: 0,
          depth: 100,
          modifier: 1,
          slideShadows : false
      },
      centeredSlides: true,
      slidesPerView: '3'
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
      url_titles = data['url_titles'];
      url_leans = data['url_leans'];
      originalLeans = data['originalLeans'].toUpperCase();
      $('#articleListWrapper').html("");
      $('#success').html("Your source's political alignment: " + originalLeans + ". <br/> Here are some similar stories from other credible sources: ");
      makePreviewDivs(url_arr, url_titles, url_leans);
    },
    error: function(error) {
      $('#articleListWrapper').html("");
      console.log(error);
    }
  });
}

function makePreviewDivs(url_arr, url_titles, url_leans) {
  url_arr.forEach(function(url) {
    $('#articleListWrapper').append(makeframe(url, url_titles, url_leans));
  });
}

function makeframe(url, titles, leans) {
    var orig = new URL(url);
    orig = orig.hostname;
    orig = orig.split(".");
    orig = orig[1];
    orig = orig.toUpperCase();
    var title = titles[url];
    if (title == "") {
      title = "Title Could Not Be Retrieved";
    }
    var leans = leans[url];
    var iconUrl = "https://www.google.com/s2/favicons?domain_url="+url;
    leans = leans.toUpperCase();
    console.log(url + " " + title + " " + leans);
    html = '<div class="swiper-slide"><a href="'+url+'" target="_blank"><h2>'+title+'</h2><h3>Source: <img src="'+iconUrl+'"/> '+orig+'</h3> <h3>Political Alignment: '+leans+'</h3></a></div>';
    return html;
}
