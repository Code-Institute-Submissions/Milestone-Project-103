## Milestone Project 3 - Data Centric Development

# Recipe Book for Healthy Snacks and Treats

#### This is an online recipe book with recipes for drinks, sweet snacks and savoury snacks aimed at people who are following a healthy diet or fitness plan.



## User Stories

### Site Owner

- As the Site Owner I want to be able to create recipes on my site so that I can share them with my friends.

- As the Site Owner I want to be able to update recipes that are already on my site, e.g. due to spelling mistakes, missing information or to generally improve them over time.

- As the Site Owner I want to be able to delete recipes from my site.

- As the Site Owner I want to be able to manage the categories - this should include creating new categories, updating categories and deleting categories,

- As the Site Owner I want to make it easy for site users to find recipes, e.g. applying a category to each recipe which supports some kind of search/find functionality (drinks, savoury snacks, sweet snacks for example).


### Site Users

- As a **first time** Site User I want the site to be easy to use, easy to understand and easy to navigate, in particular I want it to be mobile or tablet friendly so that I can easily access it when I am in my kitchen from portable devices.

- As a **first time or returning** Site User I want to be able to view recipes in a way that helps me decide which recipe I fancy making, e.g. something sweet or something savory.

- As a **first time or returning** Site User I want to be able to search for recipes in some way so that I don't have to go through the entire recipe book looking for the one I want to make.

- As a **first time or returning** Site User I want to see a picture of the recipe to help me decide whether I like the look of it.


## Design

### Colour Scheme

The colour scheme is extremely simple with the aim of being inoffensive and allowing the images to stand out more than the page header.
All text is black.  Buttons either match the header colour (within the recipe book pages) or use the standard Bootstrap button colour for form submission.

### Typography (font)

The font used for headings 1 to 3 are Itim and Electrolize.  A backup font of either a generic cursive or sans serif font is used in case either of the former fonts are not imported correctly into the site for any user.
Each of the special fonts chosen are clear and easy to read keeping accessibility in mind for users with visual impairments.

### Imagery

Images are loaded as weblinks. Images are taken 


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


## Technolgies Used

### Languages

* HTML5
* CSS
* Python
* Javascript and JQuery

### Frameworks, Libraries and Programs

* Bootstrap and Font Awesome
* MongoDB
* Flask
* Google Fonts
* Git and Github
* MS Paint
* Heroku


## Project Management

I used the "Projects" tickets and issues functionality in Github to manage my tasks.  The board I created has 4 headings: To Do, In Progress, Test and Done.  
All tasks are created as individual tasks in To Do.  Once a task is started it is moved to In Progress.  Once the task is completed the ticket moves to Test.
As it may be that a number of tasks must be completed to form a single piece of functionality it may be necessary to move several tickets into Test before proper testing of that functionality can take place.
If the functionality passes the testing then the relevant tickets can be moved to Done.  
Any ticket tasks which do not pass testing or any ticket tasks which have thrown up issues while in progress may be turned into Issues and will be put into In Progress until resolved.  These tasks must then pass back through the Test phase.
Only ticket tasks which are completed AND have passed testing can be put in Done.


## Testing

### Testing Approach

1. Setup database and test connection through addition and retrieval of some test data via IDE.
2. Create Heroku app and test deployment.
3. Build application in IDE, test each slice of functionality before deployment at regular intervals.
4. Test responsiveness of app on various devices.
5. Test app on end users.

### Testing Results

1. During work on my database connection I realised that my environment variables were automatically being removed from the .bashrc file in Gitpod when my Gitpod connection was closed.  
After seeking advice on Slack I was directed to setting up an env.py file to hold these variables.  After creating the env.py file my database connection was stabilised. 
The test results for adding and retrieving data from my MondoDB showed success after correcting my reference to the collection (realising that reference to the name was case sensitive).
Test passed.

2. I created my Heroku app and set it so that it would receive automatic deployments from my Github repo.  Unfortunately I followed the course materials and also logged into Heroku from my CLI.
This resulted in all commits and pushes going directly to Heroku for one day rather than into Github.  After seeking advice on Slack I corrected this error, removing the Heroku remote.  
I brought Github up to date with the work I had done (on 13/9/2020), re-testing where commits and pushes were going.  Heroku continued to update through automatic deployment from Github.
Test passed.

3. Site Owner results

- As the Site Owner I want to be able to create recipes on my site so that I can share them with my friends.
-- Using the Add a Recipe page, all pieces of recipe information can be added into the form and upon submission all are stored in the mongo database.  
-- The form is easy to use and considered user-friendly by the one other person I was able to test it on.  

- As the Site Owner I want to be able to update recipes that are already on my site, e.g. due to spelling mistakes, missing information or to generally improve them over time.
-- This form is of the same layout as the add recipe form and so it was also deemed easy to use by my human test subject.  All data pulled through from mongodb as expected and updated back to mongodb as required.

- As the Site Owner I want to be able to delete recipes from my site.
-- Upon clicking the Delete button the recipe is immediately deleted from my site and mongodb.  If I were to extend this project I would perhaps add another step to make sure the user meant to click the button. 

- As the Site Owner I want to be able to manage the categories - this should include creating new categories, updating categories and deleting categories,
-- All CRUD operations on categories were tested and passed testing as being easy to understand and simple to do - the relevant categories showing on the initial edit page and if editing the category (due to spelling error for example) the second page the site owner is taken to enables that one category to be amended with the change being process back to mongodb immediately.
-- Again, testing proved that if the site owner clicks the Delete button the category is immediately deleted from mongodb.  This would have repercussions for the system as a whole as the site owner could currently delete a category which is in use in existing recipes, there is no checking procedure following the clicking of the Delete button to stop a category being deleted if currently in use.  This could impact on the Contents page and recipe editing functionality. 
If I were extending my project I would add further steps to the Delete process to ensure categories which are in use in the Recipes in mongodb cannot be deleted.

- As the Site Owner I want to make it easy for site users to find recipes, e.g. applying a category to each recipe which supports some kind of search/find functionality (drinks, savoury snacks, sweet snacks for example).
-- The Contents/Find a Recipe page is the 'Home' page of the site.  This is a simple accordion style page.  Testing proved that all recipes for each category would be listed as expected.  Clicking the View Recipe button will take the user through to a page to see that individual recipe.  Each accordion section opens one at a time to reduce the size of the full list if the 'recipe book' becomes quite large.

### Site Users

- As a **first time** Site User I want the site to be easy to use, easy to understand and easy to navigate, in particular I want it to be mobile or tablet friendly so that I can easily access it when I am in my kitchen from portable devices.
-- I tested general use of my site on one other person (due to Covid). Their feedback was that it is easy to navigate and the purpose of each page is easy to understand.  
-- I tested the responsiveness of the site via the Developer Tools in Google and then by testing the site through toggling the device toolbar.  The site resizes accordingly for all devices, including the change in location of the recipe image.
-- Safari, Firefox, Chrome...

- As a **first time or returning** Site User I want to be able to view recipes in a way that helps me decide which recipe I fancy making, e.g. something sweet or something savory.
-- My tester confirmed that using the Contents/Find a Recipe page was very straight forward and did indeed allow him to select by category and pick a specific recipe.

- As a **first time or returning** Site User I want to be able to search for recipes in some way so that I don't have to go through the entire recipe book looking for the one I want to make.
-- No "search" field was created, just the Contents page.  See above for finding a recipe.

- As a **first time or returning** Site User I want to see a picture of the recipe to help me decide whether I like the look of it.
-- A picture for each recipe has been included and can be seen whether using a computer, a tablet or a mobile phone.  The positioning of the picture was important and satisfied my tester when using his mobile phone as it is shown near the top of the recipe page on smaller devices, thus it is immediately seen.

### W3C testing

*ADD RESULTS IN HERE*

### Known Bugs

There are no known bugs remaining in this site following testing.  


## Deployment

### GitHub Pages

I deployed my project to GitHub Pages as follows...

1. Create a Repository in Github and use the Code Institute Full Template when doing so. 
2. Open the Repository and using the green Gitpod button, open my repository in a Gitpod workspace. 
3. In a Gitpod Terminal the standard Git CLI commands can be used to check the status of the local and remote repositories, add files, commit changes and push through to Github.

### Heroku

I deployed to Heroku as follows:

1. Create an app in Heroku.  
2. In your app, under the Settings tab include your configuration variables (in Config Vars section).  This should include your IP address, Port number and Mongo URI.
3. In your app, under the Deploy tab connect the app to your Github repository, enabling automatic deployments from your master branch.  Steps 2 and 3 should then enable deployment directly from Github pushes.
4. You may need to run a manual deployment (under Deploy tab) and/or restart dynos to see a successful deployment.


## Credits/Acknowledgements

I acknowledge this bootsnipp site https://bootsnipp.com/snippets/kM0M for its inspiration for my dynamic user-determined form field creation for adding or removing ingredients and methods.

My thanks go out to my mentor Aaron Sinnott for his advice and assistance in the direction and breadth of my project.  I also thank the tutors who've shared some inspirational resources and helped me understand some mongodb data access specifics.
My thanks also go out to the community on Slack.