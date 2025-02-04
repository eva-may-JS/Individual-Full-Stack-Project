# Coven Connect

Welcome to Coven Connect, a magical platform where witches, wizards, and mystical beings unite to socialize, learn, and celebrate the enchantment in everyday life.

![Am I Responsive](...)

Coven Connect is a social networking site tailored for magical practitioners. From spellcasters to potion makers, this platform provides a space for connecting through events, sharing wisdom, and forming lifelong friendships.

## UX/UI

The goals of this project are:

- An accesible website which clearly states and is oriented toward the intended audience (magical practicioners)
- A place for users to browse events they may be interested in attending, and find out the relevant details
- A place where users can interact and let others know they plan on attending an event in the coments section
- (A page where users can create and showcase their own events for others to attend)

To this end, 

The following is a wireframe of how the page is planned to look on a mobile:

![Wireframe](...)

The project may deviate from this wireframe due to potential design improvements during the process

## Features 

### Existing Features

1. Navigation bar
- The NavBar is fully responsive and contains the website logo and the navigation elements "Home" and "Events". Logged out users also see: "Register" and "Login" and logged in users see "Logout"
- The navbar is made with Bootstrap and collapses into the burger icon for small devices and expands along the top of the page in larger devices.
- Bold text indicates to the user what part of the webpage they are on

![NavBar](...)

2. Logo
-

![Logo](...)

3. User feedback messages
-

![Alerts](...)

4. Introductory information section
- 

![Intro](...)

5. Register


![Register](...)

6. Log In / Log Out


![Log In and Log Out](...)

7. Events page
-

![Events](...)


8. Comments section
-

![Comments](...)

9. Create an Event
-

![Create Event](...)

10. Footer
- The footer contains the social media links for the website and contact details for the website owners
- It has been made responsive using Bootstrap grid elements and fixed to the bottom of the screen

![Footer](...)

### Features Left to Implement

1. Register to an Event
-

![Event Registration](...)

2. Attendance List
-

![Attendance List](...)

3. Profile page
- 

![Profile](...)

## Testing 

This project was tested using DevTools on the deployed product. All links and buttons have been checked and are clickable and functional and the layout has been inspected and found satisfactory on all screen sizes using the "Responsive" Dimentions option and dragging the viewport to all possible and reasonable shapes and sizes.

The code was also checked using HTML, CSS, JS and Python validation systems.

### Validator Testing 

- HTML
An error caused by an extra </p> tag was flagged on the event_detail template. On further inspection this turned out to be due to Summernote adding paragraph tags around event descriptions, as seen below:

![Event detail template error](...)

This was fixed by changing the surrounding paragraph tags for div tags:

![Event detail template error fixed](...)

After this, all templates were passing HTML validation:

![HTML validation pass](...)

- CSS

- JS

- Python
  
### Unfixed Bugs



## Deployment

- The site was coded in GitHub and deployed to Heroku. The steps to deploy on Heroku are as follows:
  1. IDE: Ensure your code is updated and ready for deployment
  2. Heroku: Create New App 
  - In your Heroku dashboard, create a new app using the "New" button followed by the "Create new app" button.
  - Give your app a meaningful name
  - Select your location (Europe was selected for this project)
  - Select "Create app"
  3. Heroku: Deployment
  - Navigate to the "Deploy" tab
  - Select your GitHub repository and connect it to Heroku
  - Select the main branch and choose automatic deployment if desired
  - Navigate to the "Settings" tab and enter the required environment variables
  - Navigate to the "Resources" tab and ensure you are using the correct Dyno type and Add-ons if any are needed.
  - Return to the "Deploy" tab and select "Deploy Branch"
  - Once the deployment process is complete, the "View" button will appear, which takes you to the live website

The live link can be found here - https://coven-connect-c3728f5c8927.herokuapp.com/


## Credits 

### Content 

- The fonts were obtained from Google Fonts (https://fonts.google.com/)
- The Favicon was developed using Favicon.io (https://favicon.io/)
- The images are royalty-free and were taken from Pixabay (https://pixabay.com/) and Pexels (https://www.pexels.com/)
- The logo was created using logo.com (https://logo.com/)

### Design

- The Wireframes were developed on Balsamiq Wireframes (https://balsamiq.com/wireframes/)
- The ERD's were created on SmartDraw (https://www.smartdraw.com)
