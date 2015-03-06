#comp20-spring2015-team14

##CookWithFriends- Project Proposal

##Project Title: CookWithFriends

**Problem Statement:** Collaborative cooking is difficult to plan.
**How do you solve the problem?:** We will design a website that allows multiple people to input the
ingredients they have in their houses. Based on this information, the website will generate a list of potential recipe matches based on the ingredients available, and the dietary restrictions and preferences of the group.

**List of all features that your team will implement**
 1. Simultaneous ingredient entry and meal planning collaboration among friends.
 2. View of a complete ingredient list with contributor info (e.g. “Frozen Veggies : Aditi”, "Paprika : Thomas")
 3. Utilize filters for recipes, e.g. “vegetarian,” “dairy-free,” “low calorie,” “short cook time,” "gluten free, “easy,” "breakfast", "desert" etc.
 4. “Cooking groups,” where users are all contributing to the same ingredient list
 5. A method of saying how many ingredients a group and what they still need in order to make the recipe
 6. User accounts/profiles

**Technologies**
 * *Bootstrap:* We will use Bootstrap for our front-end framework design
 * *Client-side data persistence:* Store ingredient lists,
 * *Server-side data persistence:*
  1. We will store data about user’s dietary restrictions and food preferences to more accurately come up with good    suggestions.
  2. We will store information about a users friends, and connections. In a way, a social network for cooking       e   enthusiasts.
  3. we will allow users to input their own recipes which we will store as part of our database.
  
* *Send emails, SMSes, or push notifications:* We will notify users about invitations to cook, or potential recipe       changes.
* *Data scraping:* The web-app will scrape cooking and recipe websites for potential recipes using the ingredients available.
* *Geolocation(Potential Feature):* Use geolocation to find users near you who have similar food preferences and are looking for people to cook with
 
##What data will your prototype be using and collecting
 1. Collecting ingredient list- types of food
 2. Using recipes off of external websites to provide back to client
 3. representations of internal recipes entered by users, stored on-site

## Any algorithms or special techniques that will be necessary
 * We will use a search algorithm to find a list of recipes that fit the group’s criteria.

##APIs:
* Facebook API: Integration of facebook login as a quick way of adding friends and connections
* google search API: to search the web for potential recipe matches

## Mockups
![Alt text](group_collaboration_page.png)
![Alt text](recipe_page.png)
![Alt text](recipe_search_page.png)
![Alt text](user_profile.png)

User profile (allergies, friends, submitted recipes, past recipes used)
Features: Ingredient list, Filters, needed ingredients for a recipe
Recipe page
Recipe search page
