$(document).ready(function(){
   $('#myCarousel').carousel({interval: 100000});

   $('.search-box-close').click(function(){
  $('.search-container').addClass("hide");
});

   $('.find-centre-btn').click(function(){
  $('.search-container').removeClass("hide");
  $('.search-input').attr('placeholder', 'Enter postcode or suburb');
});

   $('.search-database-btn').click(function() {
      $('.search-container').removeClass("hide");
      $('.search-input').attr('placeholder','database');

   })
});