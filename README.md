## Milestone Project 3 - Data Centric Development

# Recipe Book for Healthy Snacks and Treats

#### This is an online recipe book with recipes for drinks, sweet snacks, and savoury snacks aimed at people who are following a healthy diet or fitness plan.



## User Stories

### Site Owner

- As the Site Owner I want to be able to create recipes on my site so that I can share them with my friends.

- As the Site Owner I want to be able to update recipes that are already on my site, e.g. due to spelling mistakes, missing information, or to generally improve them over time.

- As the Site Owner I want to be able to delete recipes from my site.

- As the Site Owner I want to be able to manage the categories - this should include creating new categories, updating categories and deleting categories,

- As the Site Owner I want to make it easy for site users to find recipes, e.g. applying a category to each recipe that supports some kind of search/find functionality (drinks, savoury snacks, sweet snacks for example).


### Site Users

- As a **first time** Site User I want the site to be easy to use, easy to understand, and easy to navigate. In particular, I want it to be mobile or tablet friendly so that I can easily access it when I am in my kitchen from portable devices.

- As a **first time or returning** Site User I want to be able to view recipes in a way that helps me decide which recipe I fancy making, e.g. something sweet or something savory.

- As a **first time or returning** Site User I want to be able to search for recipes in some way so that I don't have to go through the entire recipe book looking for the one I want to make.

- As a **first time or returning** Site User I want to see a picture of the recipe to help me decide whether I like the look of it.


## Design

### Colour Scheme

The colour scheme is extremely simple with the aim of being inoffensive and allowing the images to stand out more than the page header.
All text is black.  Buttons either match the header colour (within the recipe book pages) or use the standard Bootstrap button colour for form submission.

### Typography (font)

The fonts used for headings 1 to 3 are Itim and Electrolize.  A backup font of either a generic cursive or sans serif font is used in case either of the former fonts is not imported correctly into the site for any user.
Each of the special fonts chosen is clear and easy to read keeping accessibility in mind for users with visual impairments.

### Imagery

Images are loaded as weblinks. Images were found via Google and taken from other public recipe books.  Credits for images are listed in the "Credits" section below.


## Features

- The site has a responsive design for ease of use across a wide range of devices.

- The site also has an interactive design for both site owner and site users.


## Wireframes

* Designs for the recipe book have been created for desktop and tablet to have the same layout and mobile phone devices to have a different layout.

### Desktop/tablet

- [Recipe Page Design](../blob/master/wireframes/Wireframe-DesktopTablet-recipeview.jpg)
- [Contents Page Design](../blob/master/wireframes/Wireframe-DesktopTablet-contentspage.jpg)
- [Add Recipe](../blob/master/wireframes/Wireframe-DesktopTablet-add_recipe.jpg)
- [Add Category](../blob/master/wireframes/Wireframe-DesktopTablet-addcategory.jpg)
- [Edit Category (list of categories to choose from)](../blob/master/wireframes/Wireframe-DesktopTablet-editcategory1.jpg)
- [Edit Category (edit the chosen category)](../blob/master/wireframes/Wireframe-DesktopTablet-editcategory2.jpg)

### Mobile

- [Recipe Page Design](../blob/master/wireframes/Wireframe-Mobile-recipeview.jpg)
- [Contents Page Design](../blob/master/wireframes/Wireframe-Mobile-contentspage.jpg)
- [Add Recipe](../blob/master/wireframes/Wireframe-Mobile-add_recipe.jpg)
- [Add Category](../blob/master/wireframes/Wireframe-Mobile-addcategory.jpg)
- [Edit Category (list of categories to choose from)](../blob/master/wireframes/Wireframe-Mobile-editcategory1.jpg)
- [Edit Category (edit the chosen category)](../blob/master/wireframes/Wireframe-Mobile-editcategory2.jpg)


## Technologies Used

### Languages

* HTML5
* CSS
* Python
* Javascript and JQuery

### Frameworks, Libraries, and Programs

* Bootstrap and Font Awesome - these were used for the page layouts, app responsiveness across devices, buttons, and button icons
* MongoDB - this is the database that holds my data documents about categories and recipes
* Flask - this is the framework or 'code library' I used in my app. It provides pre-written code for common operations that I could simply reuse for doing things like configuring my application, creating routes, and interacting with the MongoDB database  
* Google Fonts - this was used for styling the heading fonts
* Git and Github - these were used for keeping a remote backup of my work, for version control between my local files and remote files, and supported deployment to Heroku
* Microsoft Paint - this was used for drawing my wireframes 
* Heroku - this was used as the platform through which to deploy my app to share the finished product with other people


## Project Management

I used the "Projects" tickets and issues functionality in Github to manage my tasks.  The board I created has 4 headings: To Do, In Progress, Test, and Done.  
All tasks are created as individual tasks in To-Do.  Once a task is started it is moved to In Progress.  Once the task is completed the ticket moves to Test.
As it may be that a number of tasks must be completed to form a single piece of functionality it may be necessary to move several tickets into Test before proper testing of that functionality can take place.
If the functionality passes the testing then the relevant tickets can be moved to Done.  
Any ticket tasks which do not pass testing or any ticket tasks which have thrown up issues while in progress may be turned into Issues and will be put into In Progress until resolved.  These tasks must then pass back through the Test phase.
Only ticket tasks which are completed AND have passed testing can be put in Done.


## Testing

### Testing Approach

1. Setup database and test connection through the addition and retrieval of some test data via IDE.
2. Create a Heroku app and test deployment.
3. Build an application in the IDE, test each slice of functionality before deployment at regular intervals.
4. Test responsiveness of the application on various devices.
5. Test the application on end users.

### Testing Results

1. During work on my database connection I realised that my environment variables were automatically being removed from the .bashrc file in Gitpod when my Gitpod connection was closed.  
After seeking advice on Slack I was directed to set up an env.py file to hold these variables.  After creating the env.py file my database connection was stabilised. 
The test results for adding and retrieving data from my MongoDB showed success after correcting my reference to the collection (realising that reference to the name was case sensitive).
Test passed.

2. I created my Heroku app and set it so that it would receive automatic deployments from my Github repo.  Unfortunately, I followed the course materials and also logged into Heroku from my CLI.
This resulted in all commits and pushes going directly to Heroku for one day rather than into Github.  After seeking advice on Slack I corrected this error, removing the Heroku remote.  
I brought Github up to date with the work I had done (on 13/9/2020), re-testing where commits and pushes were going.  Heroku continued to update through automatic deployment from Github.
Test passed.

3. Site Owner results

As the Site Owner, I want to be able to create recipes on my site so that I can share them with my friends.
- Using the Add a Recipe page, all pieces of recipe information can be added into the form and upon submission, all are stored in the Mongo database.  The user knows their addition has been successful as they are redirected to the view recipes page and can see their added recipe there.
- The form is easy to use and considered user-friendly by the one other person I was able to test it on (due to Covid restrictions).  

Test results examples:
- [Recipes before](../blob/master/testing/recipes1.jpg)
- [Recipes after](../blob/master/testing/recipes2.jpg)

As the Site Owner, I want to be able to update recipes that are already on my site, e.g. due to spelling mistakes, missing information, or to generally improve them over time.
- This form is of the same layout as the add recipe form and so it was also deemed easy to use by my human test subject.  All data pulled through from MongoDB as expected when choosing a specific recipe to edit, and updated back to MongoDB as required.  The user can see their changes have taken place as they are redirected to the view recipes page and can see their changes reflected there.

As the Site Owner, I want to be able to delete recipes from my site.
- Upon clicking the Delete button the recipe is immediately deleted from my site and MongoDB.  This is evidenced to the user again by redirecting them to the view recipes page where they can no longer see the recipe they have deleted.  If I were to extend this project I would perhaps add another step to make sure the user meant to click the button. 

As the Site Owner, I want to be able to manage the categories - this should include creating new categories, updating categories and deleting categories,
- All CRUD operations on categories were tested and passed testing as being easy to understand and simple to do - the relevant categories showing on the initial edit page and if editing the category (due to spelling error for example) the second page the site owner is taken to enables that one category to be amended with the change being processed back to MongoDB immediately.
- Again, testing proved that if the site owner clicks the Delete button the category is immediately deleted from MongoDB as the user is redirected to the "Edit Categories" page where they can no longer see the category.  This would have repercussions for the system as a whole as the site owner could currently delete a category which is in use in existing recipes, there is no checking procedure following the clicking of the Delete button to stop a category being deleted if currently in use.  This could impact on the Contents page and recipe editing functionality. 
If I were extending my project I would add further steps to the Delete process to ensure categories which are in use in the Recipes in MongoDB cannot be deleted.

Test results examples:
- [Categories before](../blob/master/testing/categories1.jpg)
- [Categories after adding a category - screen feedback](../blob/master/testing/categories2.jpg)
- [Categories after adding a category - database feedback](../blob/master/testing/categories3.jpg)
- [Cateories after editing a category - screen feedback](../blob/master/testing/categories4.jpg)
- [Cateories after editing a category - database feedback](../blob/master/testing/categories5.jpg)
- [Categories after deleting a category - screen feedback](../blob/master/testing/categories6.jpg)
- [Categories after deleting a category - database feedback](../blob/master/testing/categories7.jpg)

As the Site Owner, I want to make it easy for site users to find recipes, e.g. applying a category to each recipe that supports some kind of search/find functionality (drinks, savoury snacks, sweet snacks for example).
- The Contents/Find a Recipe page is the 'Home' page of the site.  This is a simple accordion style page.  Testing proved that all recipes for each category would be listed as expected.  Clicking the View Recipe button will take the user through to a page to see that individual recipe.  Each accordion section opens one at a time to reduce the size of the full list if the 'recipe book' becomes quite large.

4. Site User results

As a **first time** Site User, I want the site to be easy to use, easy to understand, and easy to navigate. In particular, I want it to be mobile or tablet friendly so that I can easily access it when I am in my kitchen from portable devices.
- I tested general use of my site on one other person (due to Covid). Their feedback was that it is easy to navigate and the purpose of each page is easy to understand.  
- I tested the responsiveness of the site via the Developer Tools in Google and then by testing the site through toggling the device toolbar.  The site resizes accordingly for all devices, including the change in location of the recipe image.
- The site renders as expected when tested on Safari, Firefox, and Chrome.

As a **first time or returning** Site User, I want to be able to view recipes in a way that helps me decide which recipe I fancy making, e.g. something sweet or something savory.
- My tester confirmed that using the Contents/Find a Recipe page was very straight forward and did indeed allow him to select by category and then view a specific recipe.

As a **first time or returning** Site User, I want to be able to search for recipes in some way so that I don't have to go through the entire recipe book looking for the one I want to make.
- No "search" field was created, just the Contents page with the dynamic filtering function.  See above for finding a recipe.

As a **first time or returning** Site User, I want to see a picture of the recipe to help me decide whether I like the look of it.
- A picture for each recipe has been included and can be seen whether using a computer, a tablet, or a mobile phone.  The positioning of the picture was important and satisfied my tester when using his mobile phone as it is shown near the top of the recipe page on smaller devices, thus it is immediately seen.

### W3C testing

All HTML and CSS tests passed.  
[W3C output](../blob/master/testing/W3C%20results.docx)

### Known Bugs

There are no known bugs remaining in this site following testing.  


## Deployment

### Heroku

I deployed my project to Heroku as follows:

1. I signed up and created a new app in Heroku, giving it a name and choosing the region of Europe so that the app is delivered slightly more quickly than if I chose a server further away.  
2. In my app, under the Settings tab I included my configuration variables (in the Config Vars section).  This includes my IP address, Port number, and Mongo URI.  
3. I then created a requirements.txt file for my application.  This file contains a list of applications needed for Heroku to run.
4. In my app, under the Deploy tab, I connected the app to my Github repository, enabling automatic deployments from my master branch.  I did not create any forks in Github.  Doing this enabled deployment directly from my code pushes to Github.
(N.B. Initially I also logged into Heroku from my IDE terminal. After testing my application setup I discovered that git pushes were bypassing Github and going straight to Heroku. I fixed this issue by removing Heroku as a remote from my terminal - code pushed to Heroku from Github via the automation)
5. I ran a manual deployment (under the Deploy tab) and restarted dynos to see my first successful deployment.
6. I pushed my project files to Github regularly so that (a) my Github repository was kept up-to-date with my progress/changes, and (b) so that I deployed updates to my app regularly as I developed it through each stage.  I checked the Actions tab in Heroku to ensure the app was rebuilding when expected.  

To open my app from Heroku I logged in, went into the app I had created and in the top right-hand corner of the main section of the screen I clicked the "Open app" button.


## Credits/Acknowledgements

### Credits

I credit this Bootsnipp site https://bootsnipp.com/snippets/kM0M for its inspiration for my dynamic user-determined form field creation for adding or removing ingredients and methods.

I credit the following sites for use of their images:

- https://sheilaspantry.com/2018/03/flapjack/
- https://www.glutenfreepalate.com/gluten-free-double-chocolate-muffins/
- http://www.best-ever-cookie-collection.com/lemon-bars.html
- https://www.ambitiouskitchen.com/30-minute-skinny-banana-chocolate-chip-muffins/
- https://fitfoodiefinds.com/creamy-strawberry-chia-smoothie/
- https://www.recipetineats.com/healthy-egg-muffins/
- https://mealplannerpro.com/member-recipes/Healthy-Oat-Smoothies-Blueberry-Muffin-Smoothie-Peach-Cobbler-399119

My thanks go out to my mentor Aaron Sinnott for his advice and assistance in the direction and breadth of my project.  I also thank the tutors who've shared some inspirational resources and helped me understand some MongoDB data access specifics.
My thanks also go out to the community on Slack.