##Status Report 1

Zoe Monosson, Sylvie Abookire, Aditi Ashok, Thomas Colgrove

4/10/15

1) This week:

##Front End:
Created more detailed mockups for the current meal planner screen.
Continued exploring Bootstrap.
	Currently, Bootstrap front-end templates for the main screen and the log in screen are in progress.
Worked on integrating outside Frameworks with the Bootstrap libraries such as Font Awesome and Social Buttons.

##Back End:
1. Implemented Server Side Data Persistence and allowed inputted ingredients to be stored between multiple users. Entries are stored in a database, and have a "meal_id" representing the specific collaboration plan, username, ingredient, and ammount. 
2. Successful to queries to the Edemam food api and recipie generation using user inputed ingredients. Try it out at http://cooktogether.herokuapp.com/plan (submit some entries and hit generate, if you scroll down it should have a list of recepies and required ingredients)

Note: Currently, we have disabled (commented out)retrieval from the database on our main page for API testing purposes, but it is fully functional and can be enabled by uncommenting the get statement in our foodlist.js file

#Challenges:
*backend
A significant challenge regarding the backend of this project will be implementing an algorithm that isn't wasteful of api calls. Currently we query the api based on all of the ingredients user's input. The problem with this is that if there is one ingredient that doesn't match results, the query turns up empty. However if we queried the API many times based on all different combinations, not only would this be a factorial (combinatorics) runtime for large inputs, it would be incredibly wasteful of API calls. I plan to do some research on whether the edemam api can handle this behavior, or if any other api's implement something to this effect. 
If not, I propose using google searches to determine which combinations of ingredients are likely to generate more hits on a call to the api. Furthermore, my first thought is to do a dynamic programming approach to generating search queries to google (ie find the best combination of 2 ingredients, then the best combination of those ingredients and one more ingredient etc.) In truth, We need to do more research to find the best approach to this problem.

*Front End:
Had a little bit of difficulty integrating Bootstrap frameworks such as Font Awesome and Social Buttons initially
Trying to figure out how to translate Mock Up color schemes into Bootstrap.


##Goals For Next Week
Finish Mockups
Begin translating Bootstrap code to more closely resemble how the Mockups look.
Learn how to use Facebook API and integrate it in order to allow users to log in.
Improve algorithm for generating a query string to the edamam recepie API




