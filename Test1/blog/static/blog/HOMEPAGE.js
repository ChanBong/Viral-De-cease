$(document).ready(function(){

  $('[data-trigger="dropdown"]').on('mouseenter', function(){
    var submenu= $(this).parent().find('.submenu');
    submenu.addClass('active');
    $('.profile-menu').on('mouseleave', function(){
      $(this).find('.submenu').removeClass('active');
    });
  });



});
