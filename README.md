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

The font used for headings 1 to 3 are Itim and Electrolize.  A backup font of ????? is used in case either of these are not imported correctly into the site for any user.
Each of the special fonts chosen are clear and easy to read keeping accessibility in mind for users with visual impairments.

### Imagery

Images are loaded as weblinks 


## Features

- Responsive design across a wide range of devices.

- Interactive design for both site owner and site users.


## Wireframes

* Designs for the recipe book have been created for desktop and tablet to have the same layout and mobile phone devices to have a different layout.

### Desktop/tablet

[Recipe Page Design] - (../blob/master/wireframes/Wireframe-DesktopTablet-recipeview.jpg)
Contents Page Design - https://github.com/littlemonkee/Milestone-Project-3/blob/master/wireframes/Wireframe-DesktopTablet-contentspage.jpg
Add Recipe - https://github.com/littlemonkee/Milestone-Project-3/blob/master/wireframes/Wireframe-DesktopTablet-add_recipe.jpg
Add Category - https://github.com/littlemonkee/Milestone-Project-3/blob/master/wireframes/Wireframe-DesktopTablet-addcategory.jpg
Edit Category (list of categories to choose from) - https://github.com/littlemonkee/Milestone-Project-3/blob/master/wireframes/Wireframe-DesktopTablet-editcategory1.jpg
Edit Category (edit the chosen category) - https://github.com/littlemonkee/Milestone-Project-3/blob/master/wireframes/Wireframe-DesktopTablet-editcategory2.jpg

### Mobile

Recipe Page Design - https://github.com/littlemonkee/Milestone-Project-3/blob/master/wireframes/Wireframe-Mobile-recipeview.jpg
Contents Page Design - https://github.com/littlemonkee/Milestone-Project-3/blob/master/wireframes/Wireframe-Mobile-contentspage.jpg
Add Recipe - https://github.com/littlemonkee/Milestone-Project-3/blob/master/wireframes/Wireframe-Mobile-add_recipe.jpg
Add Category - https://github.com/littlemonkee/Milestone-Project-3/blob/master/wireframes/Wireframe-Mobile-addcategory.jpg
Edit Category (list of categories to choose from) - https://github.com/littlemonkee/Milestone-Project-3/blob/master/wireframes/Wireframe-Mobile-editcategory1.jpg
Edit Category (edit the chosen category) - https://github.com/littlemonkee/Milestone-Project-3/blob/master/wireframes/Wireframe-Mobile-editcategory2.jpg


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

I used the Projects tickets and issues functionality in Github to manage my tasks.  The board I created has 4 headings: To Do, In Progress, Test and Done.  
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

3. 





Acknowledgements

https://bootsnipp.com/snippets/kM0M for the dynamic user-determined form field creation.
My mentor, Aaron
Tutor support