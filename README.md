# **Data Centric Development**

## **Milestone Project**

### **Paper to Screen**
My third milestone project is entitled Paper to Screen. One of the Data Centric Development Milestone Project ideas was to Build a book review and recommendation site. With the intent to help external users find books they would like to read and support the site owner’s in earning money on each book purchased via a link from the site. The website includes a forum which allows users to upload details of books, including book name, author name, description and any other relevant fields such as star rating and whether they have read or watched or both. It also allows users to write comments about any book and upvote it. The Website follows the CRUD (Create Read Update Delete) to allow users to add new books and reviews to the site, edit them and delete them. Within the “Our Choices” page each book features an affiliate link to Amazon. Note this is not an actual affiliate link, but rather just a way to demonstrate how this could work. Instead, for this project, we encourage you to just keep the tag value as something fake. Also, note that in general it's better to link directly to the book's page in the store, but that's a bit more difficult.

#### **The business goals of this website are:**
* Build awareness of novels that have been adapted to the big screen.
* Provide information on the site owner’s top choices and a way of adding books for other people to purchase and read.
* Provide contact info to ensure all users are kept up to date. 
* Excellent UX to users on site long enough to obtain all information they would need.

#### **The customer goals of this website are:**
* Searching for popular books and films/series and where to buy them.
* Find contact information and social sites. 
* Clear and easy to find info on the sites owners. There top choices and what the website is about.

### **UX**
This website is aimed at existing fans and possible new ones. It advertises new and existing books and films/series, information on the site’s owners with their top recommendations and a clear way to contact them. (B2B) As a developer I wanted to create a colour scheme and picture aesthetic across all 4 pages to allow the website to flow, there would be no drastic changes and I ultimately wanted the user experience to be almost calming so it subconsciously gives Paper to Screen an aura of relaxation. (B2B & B2C) I also wanted the navigation system to be fairly simple so the user knows where the menu is sending them. Nothing ambiguous. I looked at many book recommendation websites and forums of what fans wanted. (B2C)
   
 
I started off by using Balsamiq to create my wireframes but then moved onto Publisher to create the other pages. This is mainly because I find the layout on Balsamiq easier to use however the colour and font elements on publisher opens more creative avenues.

### **Features**

#### **Header**
The very first feature you will see are social links. These will link the user to said social sights. They are on the top left of the page and they are only small to essentially be a feature elements. It gives users different ways of connecting with the site’s owners also current users of the site too. The social links are placed on every page in the header and footer again equalling easy access. They are in white to contrast against the black background. The header also contains the title of the site “From Paper to Screen” this takes up a large proportion of the screen and is this positioned in the centre. Then when viewing on a mobile device the text flows better. The menu bar is again featured on every page. They are linked to each individual page for easy navigation. There is a hvr-sweep-to-bottom in a dusky lilac so it adds to the aesthetic of the page.

#### **Footer**
The footer is also featured on every page. There are four pages in total with the Header and Footer being present on each. There is a menu bar in the footer, listing the pages of the website, next to that is a list of the site owners top picks and finally at the bottom right of the page there are the social links just promoting other ways you can follow the site owners. The bootstrap grid method has been utilised on every page just with the layout being slightly different.
Section

#### **Home**
The Homepage of the website. It features some information on what the site is about, profile cards of each of the site owner with links to more in depth information. Then lastly a soundtrack video to add aesthetic to the website. This page only features snippets of information. Just enough to grab attention, focusing on colour schemes and the use of different fonts. This page works as a set up for the rest of the website.

#### **About**
The about page is laid out the same as the home with information about the site then a row of four pictures. Underneath a user will find information on the 3 site owners. How they formed, their top choices and a short bio with their pictures. When a user keeps scrolling down they will find a form to fill out which will email the owners in case of an enquiry. As aforementioned every page includes the Header and the Footer elements.

#### **Top Choices**
This page features three books that are suggested to read, LOTR, Harry Potter and The Hobbit. Each book is laid out in a bootstrap row and col-md-4. They also feature a “Read More/ Read Less” function with an affiliate link to amazon at the bottom of each column. The row underneath is laid out in the same format, instead of displaying books it displays movies/series to watch.

#### **Forum**
The forum page has most of the MongoDB database featured. It follows the CRUD functionality. So you can see the suggested list, create another suggestion, edit the book, and then mark if it has been read or watched or both. Underneath that there is a HTML only form subscribing a user to the newsletter.

#### **Existing Features**
* Header Navigation Bar - Exists on every page and allows all users to easily navigate all the website's pages and find what they are looking for quickly. 
* Header Title – Exists on every page acts almost like a logo but doesn’t link to the homepage. 
* Header Social Icons – Exists on every page and allows all users to access the social platforms that the artist uses. 
* Footer Social Icons - Exists on every page and allows all users to access the social platforms that the artist uses
* Home Page – profile cards and link to youtube.
* About - Allows potential fans and business contacts to connect with the sites owners without overloading them with information. Allows users to see the best way to contact the sites owners, in regards to professional or personal.
* Forum Page – last page which allows a user to get involved by following the CRUD Functionality.

#### **Features to Implement in future**
* FAQ page, table with FAQs and dropdown buttons to view answers - Gives potential clients easy to find answers to their common questions. 
* Blog - Allows new and existing fans to discover the website through articles written by the members about topics such as their books/films/series what they have been up to and what they would like to accomplish. 
* Option to choose the language of the website - As the site expands it wouldn’t place a limit on their following. 
* Promotional Video - Allows potential clients to connect with the site. 

### **Technology Used**
* This project uses HTML and CSS programming languages. 
* Cloud9 - This developer used Cloud9 for their IDE while building the website. 
* BootstrapCDN
* FontAwesome 
* Google Fonts  
* W3Schools
* Javascript
* Python
* PHP
* Flask
* MongoDB

### **Testing**
* W3C CSS validation 
* W3C Markup Validation o The developer used W3C CSS Validation Service and W3C Markup Validation Service to check the validity of the website code.

#### **Testing client stories from UX section of README.md**
* As a new visitor to the website, I want to easily navigate the site, so I can find what I need efficiently. 
    * No matter what page the new visitor lands on, they can easily find and use the navigation bar.
* As a new visitor to the website, I want to know what books are recommended, so I can decide if I want to follow their work.
* As a visitor to the website, I am curious to know more about the sites owners, so I can connect with them on a personal level. 
    * A clearly labelled About page is easy to find on the navigation on every page. 
    * The page contains photos of the sites owners and short but compelling text with info on each girl.
* As a user, I want to know what people think of the books and the screen adaptation. 
    * On the home page, top choices from the sites owners are easy to find and to read.
* As a user, I want to view suggestions for books/films/series, so I can decide if it is within my budget to order. 
    * Once the visitor to the website has already been led by call to action buttons from the Home page, and through to the Our Choices, they are then led to amazon through an affiliate link.
* As an interested client, I want an easy way to be able to contact the sites owner, if I have a more personal request or a business enquiry. 
* As an interested observer and/or potential client, I want to follow the sites owners on social media, so I can keep up with her latest news.
* Social media icons can be found in the header and footer on every page of the website.

#### **Manual testing**

##### **Header:**
* Go to the "Home" page from a desktop.
* Change the screen size from desktop to mobile to verify that the navigation bar looks good on smaller screen sizes also.
* When checking responsiveness of navbar, verify that there is no overflow causing ugly size changes to menu items.
* Hover over the menu bar to test the hover elements.
* Hover over social links to see the colour change.
* Click on each navigation menu item and verify that it links to the correct page.
* Change screen size to small and verify that menu text is centred.
* Repeat verification of functionality and responsiveness on div tools.

##### **Footer:**
* Hover over each social media icon and confirm colour and size transitions expected.
* Reduce and expand width of window to verify that the footer is responsive and looks good on all device widths.
* Review all functionality and responsiveness on div tools.

##### **Page images:**
* Hover over each image in the content and confirm that the alt title for each appears.
* Reduce and expand width of window to verify that each image behaves and centres the way expected, and that they look good on all device widths.

##### **Page content:**
* Reduce and expand width of window to verify that each line of text behaves the way expected, and that the text arrangement looks good on all device widths.
* Read More/Read Less – ensure each column is centred. 
* Contact form: 
    * Go to the "Contact Us" page
    * Try to submit the empty form and verify that an error message about the required fields appears
    * Try to submit the form with an invalid email address and verify that a relevant error message appears
    * Try to submit the form with all inputs valid and verify that a success message appears.
* Click “Edit” “Read” “Watched” and “Add a Book” to make sure they link to the correct pages.
* Run app.py

### **Deployment**

This project was developed using the Cloud9 IDE, committed to git and pushed to GitHub using the built in function within cloud9. To deploy this page to Heroku from its GitHub repository, the following steps were taken:

#### **Deploying to Production with Git** 
The most common, but also the simplest method: pushing code from a Git repository to a Heroku app. You simply add your Heroku app as a remote to an existing Git repository, then use git push to send your code to Heroku. Heroku then automatically builds your application and creates a new release.
Because this method requires a developer with full access to manually push code to production, it's better suited for pre-production deployments or for projects with small, trusted teams.
##### **Pros:**
* Simple to add to any Git-based workflow
* Supports Git submodules

##### **Cons:**
* Requires access to both the Git repository and Heroku app

#### **GitHub Integration** 
If your repository is hosted on GitHub, you can use GitHub integration to deploy changes directly to Heroku. After linking your repository to a Heroku app, changes that are pushed to your repository are automatically deployed to the app. You can configure automatic deployments for a specific branch, or manually trigger deployments from GitHub. If you use continuous integration (CI), you can even prevent deployments to Heroku until your tests pass. 
GitHub integration is also useful for automating pipelines. For example, when a change is merged into the master branch, you might deploy to a staging environment for testing. Once the change has been validated, you can then promote the app to production.
##### **Pros:** 
* Automatically deploys apps and keeps them up-to-date
* Integrates with pipelines and review apps to create a continuous delivery workflow
* If you use a CI service (such as Heroku CI) to build/test your changes, Heroku can prevent deployment when the result is fail

##### **Cons:** 
* Requires administrator access to the repository, so it’s only useful for repositories you own
* Does not support Git submodules

### **Credits**

#### **Content**
* The text for the website was created for Paper to Screen by Elizabeth Perrey. 
* The text was proof-read/edited by Elizabeth Perrey

#### **Media**
* All the photos used in this site were obtained from pinterest.

#### **Code**
* CSS
* HTML
* JavaScript
* Python

#### **Acknowledgements**
* I received inspiration for this project from my own experience of building and maintaining a WordPress Blog for personal use in the past years.

