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

9. Footer
- The footer contains the social media links for the website and contact details for the website owners
- It has been made responsive using Bootstrap grid elements and fixed to the bottom of the screen

![Footer](...)

### Features Left to Implement

1. Register to an Event
-

![Event Registration](...)

2. Create an Event
-

![Create Event](...)


3. Attendance List
-

![Attendance List](...)

4. Profile page
- 

![Profile](...)

## Testing 

### DevTools testing

This project was tested using DevTools on the deployed product. All links and buttons have been checked and are clickable and functional and the layout has been inspected and found satisfactory on all screen sizes using the "Responsive" Dimentions option and dragging the viewport to all possible and reasonable shapes and sizes.

### Responsiveness

The responsiveness of this project was further tested using the UI Am I Responsive? design checker.

![Am I Responsive video](...)

### Validator Testing 

The code was also checked using HTML, CSS, JS and Python validation systems.

1. HTML

Checked using the W3C HTML Validator

An error caused by an extra paragraph tag was flagged on the event_detail template. On further inspection this turned out to be due to Summernote adding paragraph tags around event descriptions, as seen below:

![Event detail template error](...)

This was fixed by changing the surrounding paragraph tags for div tags:

![Event detail template error fixed](...)

A second error was found in the event detail template due to the custom attributes on the edit and delete buttons were missing the prefacing "data-":

![Custom attribute error](...)

This was then added.

After this, all templates were passing HTML validation:

![HTML validation pass](...)

2. CSS

Checked using the W3C CSS Validator

No errors were found:

![CSS validation pass](...)

- JS

Checked using JSHint

No errors found:

![JS validation pass](...)

- Python

Checked using the CI Python Linter

Minor errors to do with indentation and spacing were found and resolved:

![Python validation pass](...)
  
### Performance and accessibility

The performance, accessibility, use of best practices and SEO for this project were tested using Lighthouse in Chrome for Developers, and had positive results:

![Lighthouse report](...)

### Django testing

TestCase was used to test our comment form as well as GET and POST requests on our event_detail view. This ammounted to four tests:
- To check for valid comment form submissions
  - The requirement being that the comment form not be blank
- To check for invalid comment form submissions
  - The requirement being that the comment form be blank, and, therefore, invalid
- To check an individual event page with a comment form is returned 
  - The requirements being that: 
    - The page loads
    - All required fields be completed in the correct format
    - All expected event fields are present on the returned page
    - The comment form be present on the returned page
- To check for successful posting of comments on an event
  - The requirements being that:
    - Comment forms are not submitted blank
    - The comments are posted to the database and returned on the page, with a confirmation message for the comment author

When correct data was entered into the tests, all four of them passed. The tests failed appropriately when the data entered did not match the expected outcome.

![Django test results](...)

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
