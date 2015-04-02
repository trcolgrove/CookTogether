var username = '';
var ingredient = '';
var amount = '';

$(document).ready(function(){

  $.getJSON('/foodlist?meal_id=0', function( data ) {
      var init_meal = data;
      for(var i = 0; i < init_meal.length; i++){
        username = init_meal[i].username;
        ingredient = init_meal[i].ingredient;
        amount = init_meal[i].amount;
        listIngredient();

      }
  });


  $('.inputbox').change( function() {
      var date = Date();
      var id = this.id;
      if(id == 'username_input'){
          username = $('#username_input').val();
      }
      else if(id == 'ingr_input'){
          ingredient = $('#ingr_input').val();
      }
      else if(id == 'amount_input'){
          amount = $('#amount_input').val();
      }
      else{
        throw 'invalid element id';
      }
  });
  $('input[type=submit]').click(function(){
    listIngredient();
    $.post('/foodlist?meal_id=0', {'username':username, 'ingredient':ingredient, 'amount':amount});
    clearInputs();
  });
});

function clearInputs(){
  $('#ingr_input').val('');
  $('#username_input').val('');
  $('#amount_input').val('');
}

function listIngredient(){
  $('#userlist').prepend('<li class="list-group-item">' + username + '</li>');
  $('#ingredientlist').prepend('<li class="list-group-item">' +  ingredient + '</li>');
  $('#amountlist').prepend('<li class="list-group-item">' +  amount + '</li>');
}
/*
$('.inputbox').change( function() {
    var date = Date();
    var id = this.id;
    if(id == 'username'){
        username = $('#username').val();
    }
    else if(id == 'ingredient'){
        ingredient = $('#ingredient').val();
    }
    else if(id == 'amount'){
        amount = $('#amount').val();
    }
    else{
      throw 'invalid element id';
    }
});
$('input[type=submit]').click(function(){
  var meal_string = "<p>user: " + username + " ingredient: " + ingredient + " x" + amount + "</p>"
  $('#log').prepend(meal_string);
  $.post('/foodlist?meal_id=0', {'username':username, 'ingredient':ingredient, 'amount':amount});
});*/
