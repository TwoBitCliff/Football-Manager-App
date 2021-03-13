# Squad Management

[View the live website here](https://squad-management-app.herokuapp.com/)

![Homepage](README_files/homepage.jpg)

This is my third project for the 
Code Institute's Full Stack Developer course.

In this project, I have utilised skills I have develoepd over the 
length of the course, such as HTML, CSS, JavaScript, Python and database 
structures and management systems. It also incorporates the principles of 
responsive design, reacting differently to devices of different sizes,
giving the user a more satisfying experience. This is achieved by resizing
elements, hiding table columns and using a side-nav. Materialize was also 
used extensively for both speed and consitency in creating the site.
This website adheres to the CRUD principles, allowing for users to input, 
search, edit and delete data from a database utilizing MongoDB.

This app, "Football Manager", is designed to assists football managers in the
day to day running of their team. It allows them to manage fixtures, results and
players by bringing it all together in one place.


## UX

### User Stories

* Returning and Frequent Visitor Goals
    1. As a Returning or Frequent Visitor, I want to be able to easily sign in and log out.
    1. As a Returning or Frequent Visitor, I want to be able to easily navigate the site.
    1. As a Returning or Frequent Visitor, I want to be able to easily manage my players, 
    and compare their stats.
    1. As a Returning or Frequent Visitor, I want to see all upcoming fixtuers, previous 
    results and have the ability to edit them.

* Site Owner Goals
1. The Site Owner's goal is ease admin for football managers.
1.  The Site Owner's goal is to use this app for his own team.


### Design

* Colour Scheme
    
    * The author has chosen a teal base for the majority of elements and a white
     background. The simplicity of the colours makes elements distinct, without distracting 
     from the content.

* Typography
    

* Imagery
    * No Imagery have been used across the site. Icons were taken from [Font Awesome](https://fontawesome.com/)

* Wireframes
    * [Wireframe](https://github.com/TwoBitCliff/Football-Manager-App/blob/master/README.md)

* Database Diagram
    * [Diagram](#) or here to see the live version [Live](#)

## Features

* Responsive across all devices.

* Interactive elements:
    * This site allows users to input player and fixture data from the team they manage.
    * On the Register page, the User can create an account, allowing them access to the rest 
    of the site.
    * On the Profile page, there are links to update and input data.
    * On the Squad and Fixtures pages, it displays the relevant data, and has links to create 
    edit and delete data. It Only displays the data of the user, so they cannot acces other teams
    using the site.
    * On the Squad page there is the ability to search players.     
    * On the relevant Add pages, the User can add any data that they wish to input into the site.
    * On the relevant Edit pages, the User can edit any data that they they have input into the site.
    * The Logout function allows a User to cancel their interaction with the site.

### Features left to implement

* In the future the author would like to implement the ability to add player photos, and easily display indivdual 
player datasuch as their email and contact nummbers.
* In the future the author would like to implement the ability to sort players by goals, appearances etc.
* In the future the author would like to combine the manager details and the user information into the same collection.

## Technologies Used

### Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Lily Script One' and 'Yanone Kaffeesatz' fonts into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive and other Bootstrap functions.
1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
1. [Mockplus:](https://www.mockplus.com/)
    - Mockplus was used to create the [wireframes](https://en.wikipedia.org/wiki/Website_wireframe) during the design process.
1. [Materialize](https://materializecss.com/)
    - Was used for styling and ensure that the site's functions correctly.
1. [MongoDB](https://www.mongodb.com/)
    - Was used to host the data that form the database and allows the User to input their data and use the CRUD functions to amend and create said data.
1. [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine))
    - Allows for template functionality, working alongside Python code and performing various functions to ensure the User only sees what they need to. 
1. [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))
    - Helps to support other applications that ensure the site functions correctly.

## Testing

### Testing User Stories from User Experience (UX) Section

* Returning and Frequent Visitor Goals
    1. As a Returning or Frequent Visitor, I want to be able to easily sign in and log out.
        1. The sight has easily sign in and log out features, as well as regestration.

    1. As a Returning or Frequent Visitor, I want to be able to easily navigate the site.
        1. The site has a simple layout, with bright colours against a white background.

    1. As a Returning or Frequent Visitor, I want to be able to easily manage my players, 
    and compare their stats.
        1. The user can easily create and edit players, and the players are listed in a well laid out table.

    1. As a Returning or Frequent Visitor, I want to see all upcoming fixtuers, previous 
    results and have the ability to edit them.
        1. The fixtures and results are displayed on the same page, in clear tables. When a fixture is updated,
         it moves to the results table automatically.


* Site Owner Goals
    1. The Site Owner's goal is ease admin for football managers.
        1. The site gives a basic yet comprehensive ability to manage players and upcoming fixtures/ previous results.
    1.  The Site Owner's goal is to use this app for his own team.
        1. The site owners 5 a side team has been entered ahead of the next season.


### Achieved Testing

    1. Throughout the project, I have been viewing my site across several devices of different sisez. This includes 
    mobiles, tablets, a range
     of monitors with different ratios.

    1. Multiple accounts were created, along with data from each account, to ensure users only saw the relevant 
    information, and forms inserted data correctly.

    1. All links were ested to ensure they directed to the correct page.

    1. Family were used to test the site to find bugs the author may have missed.

### Further Testing

* A test user account was created as the default user to test the site.

### Known Issues


### Validators

Due to the nature of using Jinja Templating, the author felt it unnecessary to include HTML validators as they came up with
 a host of errors. Please find the CSS validator included below.


#### CSS

![CSS Test](README_files/cssvalidation.jpg)

#### PEP8

![PEP8 Test](README_files/pep8validation.jpg)

## Deployment

### Heroku

The project was deployed to Heroku using the following steps (which can be found here) [Heroku Deployment](https://blog.heroku.com/six-strategies-deploy-to-heroku)...

1. Log in to Heroku and select 'Create New App'
2. You are then presented with the ability to name your app, which is what creates the URL and must be unique.
3. Select the region that is closest to yourself, once selected, click 'Create App'.
4. On the 'Deployment method' section click on the GitHub 'Connect to GitHub' option.
5. Search for your repository using its name with the Heroku Search function, once found, click 'Connect' to connect the repository from GitHub to Heroku.
6. You then need to select the 'Settings' tab and find the 'Reveal Config Vars' button.
7. Upon clicking the 'Reveal Config Vars' button, input the appropriate IP, PORT, SECRET_KEY, MONGO_URI and MONGO_DBNAME fields,
    with their relevant data from the env.py file.
8. Due to the creation of the Procfile and the requirements.txt file, we can select the 'Enable Automatic Deploys' button to ensure any changes pushed to
    GitHub are also synchronised with Heroku.
9. As there is only one branch, we can select the 'Deploy Branch' button to ensure Heroku receives changes from GitHub.
10. Once this is selected, you should see Heroku building our app and a 'Your app was successfully deployed' message should appear.
11. Simply click 'View' below this to view your live website.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Content

All content has been written or created by the author.

### Media

No media was used for this site.

### Acknowledgements

* Thanks to my Code Institute Tutor, Mentor and Student Support team for offering me advice and support
during the creation of this project.

* Various forums were used to help fix minor bugs. 

* Code Institutes mini task-manager project provided inspiration and guidance to help with functionality.

* I'd like to acknowledge this [Link](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/).
    For showing me how to create custom error pages.

