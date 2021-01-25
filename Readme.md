**Data Centric Project**

Cookies Book Club is an online library resource and a review portal. The purpose
of this site is for users to be able to search for books and to read, or leave
reviews. Books that have more reviews are more likely to brought, therefore
aiding the user to help making a decision to purchase the book. Also a lot of
readers like to have a voice and to share their opinions on books they have
read. This helps authors to view how well their book is doing too.

**UX Design**

The 5 planes of UX design helped me with structure of my site, these have been
identified below:

**Strategy**

The idea behind this design is to for the user to be able to search for the book
using the following criteria:

-   Author

-   Title

-   ISBN

-   Subject

Once the search is complete, the user is presented with a number of titles based
on the search criteria. Upon selecting the book, the user can either read the
review (if it has been reviewed), or leave a review. Following on from this, the
user can navigate back home and search for another book, or can choose to
edit/update, or delete their current review (CRUD). These functions have been
developed based upon the following User Stories:

**User Stories**

-   As a user I want be able to search for a book using categories including
    title, author, ISBN and subject. (READ)

-   As a user I want to be able read reviews from selected books, as available.
    (READ)

-   As a user I want to be able to add a review to a selected book. (CREATE)

-   As a user I want to be able to a rating to a book with my review.

-   As a user I want to be able to edit my review as necessary. (UPDATE)

-   As a user I want to be able to delete my review from the database. (DELETE)

**Structure**

Features and Functionality

To affirm to the user that it is an online book library there are some featured
books displayed.

-   The site has a simple search bar where they can search for the book they
    desire. Once the search button is activated the data is pulled in from the
    (openlibrary API) and the results appear on the Results page. The results
    page displays 16 books based upon the users search criteria.

-   The user can then select the version of the book that they desire which then
    directs them to the book page.

-   The book page displays the information on the book selected with the added
    of feature of being able to leave a review on the book. If the user wishes
    to leave a review, the user can complete the review section at the bottom of
    the page. They are required to enter their name, a rating and their review.
    Without all 3 of these components being entered, the user should not be able
    to submit their review.

>   Upon submission, a record is created in MongoDB containing a unique
>   identifier plus the user data (name, review and ISBN). (CREATE)

-   From this point the user can search for another book using the navigation
    bar HOME function which will return them back to the home screen.

-   If a different user searches for a book which has already been reviewed. The
    user is able to read the review which presented to the bottom of the screen
    (RETRIEVE).

-   At the same time, the user is able to EDIT (UPDATE) the review presented to
    them (future functionality will require users to create an account to
    prevent the database being spammed).

-   From this point the user is also able to (DELETE) the record entirely.

-   Place holder text is provided in the text box/area in the forms as an
    indication to the input required. Each field is validated (non-empty) before
    submitting data to the database.

**Surface**

The colours were kept fresh and light, for an aesthetic feel, and that the
users’ attention would go to the featured books. This is in turn would motivate
them to search for books intuitively.

Keeping with the theme of the site, a Cookie and tea image was chosen to give a
homely feel so that they felt they were at the actual library.

**Skeleton**

Wireframes were drawn in mobile, desktop and larger displays (5k+). Wireframes
are located here:

<https://github.com/Tia112/Data-Centric-Development-Milestone-Project-/tree/master/Wireframes>

**Technologies Used**

\- HTML

\- CSS

\- Python3

\- Mongo DB

\- Bootstrap

\- API integration (openlibrary)

**Testing**

| **Test Description**           | **Expected Outcome**                                                                                                                  | **Actual Outcome**                                                                                                                                                                                                                                                                                                                                                                                                   | **Result**                  |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| Check links in the Navbar      | Home and contact links should direct user to the right page                                                                           | Pass                                                                                                                                                                                                                                                                                                                                                                                                                 | Pass                        |
| Search bar (API Search)        | Search query should return JSON response from open library API                                                                        | Pass – a huge amount of data is received based on search criteria. This needed to be filtered based upon the attributed which define a book – title, author and ISBN.                                                                                                                                                                                                                                                | Pass                        |
| Results Page                   | Book information is formatted correctly on the html page                                                                              | Some of the text was displayed using square brackets. The card sizes were uneven due to different length of information being pulled. Edited - The elements height and width had to be changed Converted data to string                                                                                                                                                                                              | Fail Fail Pass              |
| Results Page                   | Limit API response to 16 items - list 16 items of data to be displayed in Results page.                                               | As noted above, there was too much data to filter, so used a loop to extract specific about the book. For uniformity, and not to overwhelm the user, I restricted the results to a maximum of 16 books.                                                                                                                                                                                                              | Pass                        |
| Adding Reviews Editing Reviews | Allow user to add a review upon selecting their book. Edit review of a previously selected book where a review by the user was added. | Passed – and add a record in MongoDB. This is core function from which all other functions for CRUD are based upon. The entry in the MongoDB collection is created using the user name, rating and more importantly – the ISBN. The record is added with a uniquely assigned ID from Mongo which gives us the ability to recall and edit or delete as required. Passed – and edited/updated a record in the MongoDB. | Passed Passed               |
| Deleting a Review              | Delete a review from a previously selected book.                                                                                      | Passed – this triggers the appropriate function to delete the record from the MongoDB.                                                                                                                                                                                                                                                                                                                               | Passed                      |
| Responsiveness in mobile view. | Render all components in respective mobile views – without distortion of data and switching between orientation, and screen sizes.    | Failed - Cards kept shifting to the left on the results page. Amended, Failed – text area, text box, disproportionate to the screen – amended in CSS. Failed – Carousel displaying in a single column – amended in CSS. Edited - custom CSS to override bootstrap styling.                                                                                                                                           | Passed Passed Passed Passed |
| Responsiveness in 5k view      | All pictures and fonts                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                      |                             |
| Deployment                     | Deployment to Github Deploying Project to Heroku                                                                                      | Deploying project to Github Failed – Deployment kept failing, several attempts Used gunicorn in procfile                                                                                                                                                                                                                                                                                                             | Pass Fail Pass              |

**Code Validation**

Python code was validated using pep8online (<http://pep8online.com/>)

CSS was validated using the W3C CSS Validation Service
(<https://jigsaw.w3.org/css-validator/>)

HTML was validated using the W3C Markup Validation Service
(<https://validator.w3.org/>)

**Deployment (GitHub)**

The project is stored in Github, and deployed in Heroku.

As part of the deployment to Heroku, the following steps must be taken to
incorporate the code into the Github repo:

1.  Create local workspace on PC. Log into Github account and create new
    repository:

2.  Link newly created repo to local workspace using Github repo URL and Github
    desktop:

3.  This is has now created a channel between remote and local repos for
    staging, push and commits. Visual Studio Code or Atom can be used to login
    to the selected Github repo and facilitate this function during the
    development process. The repo is located here:

[Data-Centric-Development-Milestone-Project-](https://github.com/Tia112/Data-Centric-Development-Milestone-Project-)

For the first time, I made use of branch functionality by having a Master and
Review-Function branch respectively. When updating code for each, I used GitHub
desktop to push code to each branch and eventually merge the code before
deployment to Heroku.

**Deployment (Heroku)**

Before deploying to Heroku we need Heroku to build our environment based on
requirements and how to run our application.

1.  First, create a requirements.txt file locally from the console using:

pip3 freeze \> requirements.txt

1.  Then, create a Procfile (case-sensitive) from the console using:

>   echo web: gunicorn app:app \> Procfile

1.  Commit all code to the correct Git repository (to ensure that
    requirements.txt and Procfile are committed to the Master branch).

2.  Connect to Heroku and login. Click **Create App**, select the region closest
    to you, and give the app a name.

3.  Next, Go to **Settings** tab, and configure variables for:

IP: 0.0.0.0

MONGO_URI – as created in Mongo

MONGO_DB: as created in Mongo

1.  Click **Deploy** and in **Deployment Method**, select **GitHub** and click
    **Connect** to connect to the relevant repository.

2.  Choose the **Master** branch and Click **Deploy Branch**. This will initiate
    the build using the requirements file and prepare the app for launch using
    the Procfile.

3.  Once complete, click **View App** to see the fully functioning app

The web app can be accessed from any device from the following URL:

https://cookies-book-club.herokuapp.com/

**Future features**

As a future feature I would create a login for users so that **only** they are
able to edit their own comments. They would have control of their own reviews
because at present anyone can type in the same name etc… and change the review
of any user, on any book. Along with the log in, any reviews will need to be
approved or moderated by an Administrator – otherwise reviews can contain any
kind of text. With their own logins, users can maintain their own profiles which
can include their own favorite books, their reviews, avatars etc…

A prominent future feature would also include the ability to read an excerpt of
the book, and links to purchase the book directly from a retailer
(Amazon/Google). Also an added feature that would allow them to store their
favorite books would be something users would appreciate.

A contact us form would be available in the future for any issues or information
or alternatively an FAQs page.

**References**

**Images**

Open library API

Unsplash.com

**Fonts**

Fontawsome.com

Cssfontstack.com

**Code**

W3Schools.com

Getbootstrap.com (used and amended as a guide for modal and buttons and navbars
and carousel).

All the information on the site is written by myself.

#### Acknowledgements

A huge Thankyou to my mentor Brian Macharia for all his time and efforts to
guide me through this project at times of crisis.

Student care for being understanding at a difficult period.

**Disclaimer**

This site and its contents were for educational purposes only.
