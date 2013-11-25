$(function(){
  $('input[type="text"]').attr('autocomplete', 'off');    

  $('#id_username').attr('placeholder','Username');
  $('#id_password').attr('placeholder','Password');

  if($('#id_username').val() != ''){
    $('#id_password').focus();
  }
})
