var username = '';
var ingredient = '';
var amount = '';
var list_num = 0;
var group_name = "The Food Legends"
var collaborators = "trcolgrove"
var ingredients = [];
var group_id = -1;

function getUrlVars()
{
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}

$(document).ready(function(){

  var args = getUrlVars();

  group_id = args['group_id'];

  pollDB();

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
    var post_url = '/foodlist?group_id=' + group_id;
    $.post(post_url, {'username':username, 'ingredient':ingredient, 'amount':amount});
    list_num++;
    clearInputs();
  });

  $('.name').text(group_name);

  setInterval(pollDB, 10000);
});


function pollDB(){
  var groupURL = "/foodlist?group_id=" + group_id;
  $.getJSON(groupURL, function(data) {
      var init_meal = data;
      for(var i = list_num; i < init_meal.length; i++){
        username = init_meal[i].username;
        ingredient = init_meal[i].ingredient;
        amount = init_meal[i].amount;
        ingredients.push(ingredient);
        listIngredient();
   }
      list_num = init_meal.length;
      console.log(list_num);
  });

}


function clearInputs(){
  $('#ingr_input').val('');
  $('#username_input').val('');
  $('#amount_input').val('');
}

function listIngredient(){
  $('#userlist').prepend('<li class="list-group-item" id="foodlistitem">' + "placeholder" + '</li>');
  $('#ingredientlist').prepend('<li class=list-group-item id="foodlistitem">' +  ingredient + '</li>');
  $('#amountlist').prepend('<li class="list-group-item" id="foodlistitem">' +  amount + '</li>');
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
          $("#recipes").append('<p>source: <a href="' + recipe.url + '" target="_blank">' + recipe.source + "</a></p>");
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
