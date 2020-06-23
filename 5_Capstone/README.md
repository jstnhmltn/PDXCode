# Capstone Proposal -  justin hamilton
## Project Name Ideas:

****

## Project Overview

*A BLOG SITE/IMAGE GALLERY* 

## Functionality

- Build a web application that allows users to create an account,  upload images and videos, create blog posts, rate other blog posts, list their favorite places on Google Maps.

- User can set images to **public** or **private**


## Data Model

1. Multiple Users
    - Take in user information to store in sqlite3 db
2. User Authentication
    - Use a *django user model* to authenticate users and manage permissions
3. User Homepage
    - The authenticated users have ability to upload images for the puzzle generator, collage-maker and slideshow
4. Main page
    - Unauthenticated users have access to this page and are able to view other images that are set to **public**
    - Authenticated users have access to all **public** images, but only their own **private** images


## Schedule

### WEEK ONE:
- Develop the Django directory structure
- Establish a 'base.html' to extend to the other HTML pages
- Configure a layout of django views necessary for admin/user functionality

### WEEK TWO:
- Develop custom user model or develop **django.contrib.auth.users** model
- Configure views based on user model type (class-based views or function-based views)
- Choose a color scheme and typography for the HTML/CSS

### WEEK THREE:
- Full functionality. Successful navigation using links
- Integrate new ideas
- Troubleshoot

### WEEK FOUR:
- Troubleshoot
- Deploy 
- Troubleshoot