function statusChangeCallback(response) {
    if (response.status === 'connected') {
        FB.api('/me', function(response) {
        name = response.name;
        id = response.id;

        FB.api('/me/permissions', function(response){
        });

        FB.api('/me/friends', function (response) {
          if (response && !response.error) {
            friends = response;
          }
          else {
            friends = {};
          }
          user = {
            'username' : name,
            'user_id' : id,
            'friends' : friends,
            'groups' : [],
            'diet_restrict' : []
          };

          $.getJSON('/userinfo.json?user_id=' + user.user_id, function(data){
            console.log("GET");
            console.log(data);

            if ($.isEmptyObject(data)) {
              $.ajax({
                type: "POST",
                url: "/sendUserInfo",
                // The key needs to match your method's input parameter (case-sensitive).
                data: JSON.stringify(user),
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                //success: function(data){ alert(data);},
                failure: function(errMsg) { alert(errMsg);}
              });

              //REDIRECT TO NEW USER PREFERENCES
              window.location = '/newuser?user_id='+user.user_id;
            }
            else {
              //REDIRECT TO PROFILE
              window.location = '/userprofile?user_id='+user.user_id;
              user.groups = data['groups'];
              user.diet_restrict = data['diet_restrict'];
            }

          });
        });
      });
    }
  }

function checkLoginState() {
  console.log('check login state called');
  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });
}

window.fbAsyncInit = function() {
FB.init({
  appId      : '1401516633500673',
  cookie     : true,
  xfbml      : true,
  version    : 'v2.2'
});
FB.getLoginStatus(function(response) {
  statusChangeCallback(response);
  if (response.status === 'connected') {
    var uid = response.authResponse.userID;
    var accessToken = response.authResponse.accessToken;
} else if (response.status === 'not_authorized') {

} else {

}
});

};
// Load the SDK asynchronously
(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/sdk.js";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

// Here we run a very simple test of the Graph API after login is
// successful.  See statusChangeCallback() for when this call is made.
function testAPI() {
  console.log('Welcome!  Fetching your information.... ');
  FB.api('/me', function(response) {
    console.log('Successful login for: ' + response.name);
    document.getElementById('status').innerHTML =
      'Thanks for logging in, ' + response.name + '!';
      console.log("no more redirect");
  });
}
