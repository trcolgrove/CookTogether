var username = '';
var ingredient = '';
var amount = '';

var ingredients = [];
$(document).ready(function(){

  $.getJSON('/foodlist?meal_id=0', function( data ) {
      var init_meal = data;
      for(var i = 0; i < init_meal.length; i++){
        username = init_meal[i].username;
        ingredient = init_meal[i].ingredient;
        amount = init_meal[i].amount;
        ingredients.push(ingredient);
        listIngredient();

      }
      console.log(ingredients);
  });

  $('.inputbox').change( function() {
      var date = Date();
      var id = this.id;
      console.log(id);
      if(id == 'username_input'){
          username = $('#username_input').val();
          console.log(username);
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
  $('#add_ingr').click(function(){
    ingredients.push(ingredient);
    listIngredient();
    $.post('/foodlist?meal_id=0', {'username':username, 'ingredient':ingredient, 'amount':amount});
    clearInputs();
  });
  $('#generate').click(function() {
          getRecipes();
  });
});

function clearInputs(){
  $('#ingr_input').val('');
  $('#username_input').val('');
  $('#amount_input').val('');
}

function listIngredient(){
  $('#userlist').prepend('<li class="list-group-item">' + "placeholder" + '</li>');
  $('#ingredientlist').prepend('<li class=list-group-item>' +  ingredient + '</li>');
  $('#amountlist').prepend('<li class="list-group-item">' +  amount + '</li>');
}

function getRecipes(){
    var url = 'https://api.edamam.com/search?q='
    for(var i = 0; i < ingredients.length; i++){
      url += "," + ingredients[i];
    }
    url += '&app_id=a9e44233&app_key=4e60143490cec408c5aaf35215ab8ef6'
    $("#recipes").empty();
    $.ajax({
      url: url,
      type: 'GET',
      crossDomain: true,
      dataType: "jsonp",
      success: function(response){
        var results = response['hits'];
        //console.log(results);
        for( var i = 0; i < results.length; i++){
          var recipe = results[i].recipe;
          var ingr = recipe.ingredients;

          $("#recipes").append("<h3>" + recipe.label + "</h3>");
          $("#recipes").append("<img src=" + recipe.image + " alt=" + recipe.label + ">");
          console.log(recipe.url);
          $("#recipes").append("<p>source: <a href=" + recipe.url + ">" + recipe.source + "</a></p>");
          $("#recipes").append("<p>servings: "+ recipe.yield + "</p>");

          var newentry = "<p> ingredients : "
          for( var j = 0;  j < ingr.length; j++ ){
            newentry += ingr[j].food.label + ", "
          }
          $("#recipes").append(newentry + "</p>");
        }
      },
      error: function (xhr, status) {
                  alert("error querying edamam database");
      }
  });
}