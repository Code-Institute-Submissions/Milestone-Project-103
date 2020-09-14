## Milestone Project 3 - Data Centric Development

# Recipe Book for Healthy Snacks and Treats

#### This is an online recipe book with recipes for drinks, sweet snacks and savoury snacks aimed at people who are following a healthy diet or fitness plan.



## User Stories

### Site Owner

#### As the Site Owner I want to be able to upload recipes to my site so that I can share them with my friends.

##### (Potential methods of categorising recipes are: drinks, savoury snacks, sweet snacks, amount of time needed to make the recipe,...

### Site Users

#### As a Site User I want to be able to view recipes in a way that helps me decide which recipe I fancy making, e.g. something sweet or something savory.

#### As a Site User I want to be able to search for recipes, perhaps by filtering out drinks or filtering on categorised lengths of time needed to prepare the recipes.

#### As a Site User I want to see a picture of the recipe to help me decide whether I like the look of it.

#### As a Site User I want the site to be easy to use, in particular I want it to be mobile or tablet friendly so that I can easily access it when I am in my kitchen.


## Wireframes

* Desktop design - https://github.com/littlemonkee/Milestone-Project-3/blob/master/Wireframes/Wireframe-Desktop.jpg

* Mobile design - https://github.com/littlemonkee/Milestone-Project-3/blob/master/Wireframes/Wireframe-Mobile.jpg


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