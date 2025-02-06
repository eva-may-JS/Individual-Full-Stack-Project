# Coven Connect

Welcome to Coven Connect, a magical platform where witches, wizards, and mystical beings unite to socialize, learn, and celebrate the enchantment in everyday life.

![Am I Responsive](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/AmIResponsive.png)

Coven Connect is a social networking site tailored for magical practitioners. From spellcasters to potion makers, this platform provides a space for connecting through events, sharing wisdom, and forming lifelong friendships.

## UX/UI

The goals of this project are:

- An accesible website which clearly states and is oriented toward the intended audience (magical practicioners)
- A place for users to browse events they may be interested in attending, and find out the relevant details
- A place where users can interact and let others know they plan on attending an event in the coments section

The user stories, wireframes, colour scheme and overall design of this webpage have been tailored to these goals.

### Wireframes

The following is a wireframe of how the page is planned to look on a mobile:

![Wireframe mobile](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/Mobile%20wireframe%20V.3.png)

This is a wireframe of how the page is planned to look on a laptop/desktop:

![Wireframe laptop](...)

The project may deviate from this wireframe due to potential design improvements during the process

### User stories

All user stories were met and have been closed in the Kanban board for this project (link to the project board: https://github.com/users/eva-may-JS/projects/4)

Site user stories:
  - As a user, I want a clear and accessible navigation bar so that I can easily browse through different sections of the site.
  - As a user, I want to see a recognizable logo in the navbar so that I know I am on the official Coven Connect page.
  - As a user, I want to learn about the purpose and mission of Coven Connect so that I can decide if it is the right fit for me
  - As a visitor, I want to register for an account so that I can participate in events and access members-only features.
  - As a user, I want to log in to my account so that I can have full use of the website features
  - As a user, I want to log out securely and be redirected to the home page.
  - As a user, I want an events page where I can browse all upcoming events with details like date, time, and location so I can decide if I want to go
  - As a user I can see the event detail page when clicking on an event from the Events page list so that I can view all relevant information about the event (e.g. attire, familiar required)
  - As a user, I want a comments section on each event page where I can discuss the event details with other attendees
  - As a user, I want to edit or delete my comments to ensure my contributions are accurate and relevant.
  - As a user, I want to receive feedback messages (e.g., success, error, or warning) so that I know if my actions (like logging in, registering, or commenting) were successful or not.
  - As a user, I want a footer with important links and information (e.g., contact and social media) so that I can find additional resources easily.

Product owner and site admin user stories:
  - As a Product Owner, I want to showcase the philosophy and purpose of Coven Connect so that I can attract the people most likely to return
  - As a Product Owner, I want an events page for users to browse so that people attend my events
  - As a Site Admin I can create, read, update and delete events so that I can manage my content
  - As a Site Admin I can create draft posts so that I can finish writing the content later
  - As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments
  
  
## Features 

The user stories used to plan and structure this project reflect the need for the existing features of the website, listed below.

### Existing Features

1. Navigation bar
- The NavBar is fully responsive and contains the website logo and the navigation elements "Home" and "Events". It also changes dynamically based on user authentication status (e.g., showing login/register for guests and logout for authenticated users).
- It is made with Bootstrap and collapses into the burger icon for small devices and expands along the top of the page in larger devices.
- Bold text indicates to the user what part of the webpage they are on

![NavBar](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/Navbarvideo-ezgif.com-video-to-gif-converter.gif)

2. Logo
- A distinctive site logo is positioned in the navigation bar to reinforce branding.
- Clicking the logo redirects users to the homepage for easy and intuitive navigation.

![Logo](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/logo.png)

3. User feedback messages
- Flash messages provide real-time feedback for user actions (e.g., successful login, form submission errors, or comment submitted for approval).
- Messages appear at the top of the screen and have a Close button to ensure a smooth user experience.

![Alerts](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/Alerts.png)

4. Introductory information section
- The homepage includes an introduction to the site’s purpose, guiding new users on how to engage with the community.

![Intro](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/Intro%20section.png)

5. Register
- Secure authentication system allowing users to register
- Built-in Django authentication ensures data security and session management.

![Register](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/Register-ezgif.com-video-to-gif-converter.gif)

6. Log In / Log Out
- Secure authentication system allowing users to log in and log out.
- Users must be logged in to interact with the site (e.g., posting comments).
- Built-in Django authentication ensures data security and session management.

![Log In](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/Login-ezgif.com-video-to-gif-converter.gif)

![Log Out](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/Logout-ezgif.com-video-to-gif-converter.gif)


7. Events page
- Displays a list of upcoming events with key details such as title, date, location, and category.
- Each event has a dedicated detail page showing a full description and an associated discussion section.

![Events](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/Events-ezgif.com-video-to-gif-converter.gif)

![Event detail](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/Event%20detail.png)


8. Comments section
- Authenticated users can post comments under event detail pages.
- Comments can be edited or deleted by their authors.
- New or newly edited comments require admin approval before being visible to ensure content moderation.

![Comments](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/Comments.png)

9. Footer
- A fixed footer is displayed across all pages, containing links to social media and contact details for website admin.
- It has been made responsive using Bootstrap grid elements.

![Footer](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/Footer-ezgif.com-video-to-gif-converter.gif)

### Features Left to Implement

There are several features planned for a future iteration which have not yet been implemented:

1. Register to an Event
- Users will be able to register for events directly from the event detail page.
- A "Register" button will be added, allowing users to confirm attendance with a single click.
- Registrations will be stored in the database and linked to the authenticated user’s profile.
- Users will receive a confirmation message upon successful registration.
- Users will also be able to de-register from events

2. Create an Event
- Authenticated users will be able to create and post their own events.
- A "Create Event" form will allow users to input event details, such as title, date, location, and description.
- Events will undergo an approval process before being displayed on the events page.
- Users will have the ability to edit or delete their own events.

3. Attendance List
- Each event page will display a list of registered attendees, visible to all authenticated users.
- The attendance list will include clickable usernames which link to the attending users profile.

4. Profile page
- A dedicated profile page where users can update personal information.
- Users can add optional details such as a short bio, interests, types of magical ability, and profile picture.


## Models and ERD's

The following is an image of the ERD for this project, showcasing the models used and their relationships:

![ERD](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/Basic%20ERD.png)

## Technical information

### Languages
- HTML
- CSS
- JavaScript
- Python

### Tools and technologies
- Django
- Bootstrap
- Crispy Forms
- Summernote
- Cloudinary
- AllAuth
- Whitenoise
- PostgreSQL
- Gunicorn

## Testing 

### DevTools testing

This project was tested using DevTools on the deployed product. All links and buttons have been checked and are clickable and functional and the layout has been inspected and found satisfactory on all screen sizes using the "Responsive" Dimentions option and dragging the viewport to all possible and reasonable shapes and sizes.

### Responsiveness

The responsiveness of this project was further tested using the UI Am I Responsive? design checker.

![Am I Responsive video](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/AmIResponsivevideo-ezgif.com-video-to-gif-converter.gif)

### Validator Testing 

The code was also checked using HTML, CSS, JS and Python validation systems.

1. HTML

Checked using the W3C HTML Validator

An error caused by an extra paragraph tag was flagged on the event_detail template. On further inspection this turned out to be due to Summernote adding paragraph tags around event descriptions, as seen below:

![Event detail template error](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/HTML%20event%20detail%20page%20error.png)

This was fixed by changing the surrounding paragraph tags for article tags.

A second error was found in the event detail template due to the custom attributes on the edit and delete buttons were missing the prefacing "data-":

![Custom attribute error](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/custom%20attribute%20error.png)

This was then added.

After this, all templates were passing HTML validation:

![HTML validation pass](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/HTML%20validation%20pass.png)

2. CSS

Checked using the W3C CSS Validator

No errors were found:

![CSS validation pass](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/CSS%20validation%20pass.png)

- JS

Checked using JSHint

No errors found:

![JS validation pass](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/JS%20validator%20pass.png)

- Python

Checked using the CI Python Linter

Minor errors to do with visual indent and spacing were found and resolved:

![Python validation pass](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/Python%20validation%20pass.png)
  
### Performance and accessibility

The performance, accessibility, use of best practices and SEO for this project were tested using Lighthouse in Chrome for Developers, and had positive results:

![Lighthouse report](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/Accessibility%20report%20lighthouse.png)

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

![Django test results](https://github.com/eva-may-JS/Individual-Full-Stack-Project/blob/main/static/images/4%20tests%20passing.png)

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
