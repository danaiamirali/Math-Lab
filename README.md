# MATH LAB

#### https://www.youtube.com/watch?v=7Pab41cllvw
#### Description:

## What is Math Lab?
Math Lab is a web application developed with Flask that supports Calculus calculations using the Wolfram Alpha API. These Calculus calculations include limits, derivatives, and integrals, which are essentially the cornerstones of the subject.

#### Design Choices
The most important design choice was regarding how to handle the fact that there are multiple types of integrals. 

When a user selects integral calculations, they are redirected to another menu page where they pick the specific type of integral. This was both a user and computer friendly way of handling the different types of integrals, as opposed to my original idea of having one page for all types of integrals, where, if you wanted an indefinite integral, you'd just leave the lower and upper bounds blank. That would be a poor design choice in how it could potentially lead to confusion, and required some sort of intrusive message on the page explicitly explaining to the user how to use the page. Thus, the design choice of having another separate menu was made.

In terms of "branding", the site is referred to as "Math Lab" rather than "Calculus Lab" due to **future plans** to add more mathematical functions to the site.

---

## Project Files
#### Python
> application.py
The application file is the "controller" of the application, handling redirects and passing in the answers of the users queries to the applicable HTML file.

> helpers.py
The helpers file contains the "Wolfram" function, which is responsible for contacting the Wolfram Alpha API and returning a response and handling errors if any do occur in the contacting process. The function receives the users query as well as PODSCANNER, the latter of which is integral to safeguarding the application from malicious user input (e.g. querying Wolframalpha for local weather instead of a function)

#### HTML
> layout.html
The layout file provides the layout for all the other HTML files using Jinja2 in flask. In this layout there notably lies the Bootstrap tags in the header, which is helpful as Bootstrap is used throughout the site, from the navbar to form groups.

> index.html
The homepage of the site has a cardgroup with links to the three main functionalities of the site: calculating limits, derivatives, and integrals. The cardgroup is derived from Bootstrap, with a custom cardgroup header.

> limit.html and derivative.html
The limit and derivative pages provide form groups for their respective operations, with dropdown menus for the side of the limits and the order of the derivatives. On submission, application.py extracts the user inputs and redirects the users to the same page but with the user's answer now provided below the form group using Jinja2.

> integral.html
When the user chooses integrals in the homepage, they are sent to integral.html, which contains another card group from which the user picks between definite, indefinite, and improper integrals. Each type has a different page (integral-def.html, integral-indef.html, integral-improper.html), which have different form groups as appropriate for their respective calculation (e.g., integral-def provides users an input for a lower and upper bound while integral-indef does not.) On submission, the page works just like the limit and derivative pages, sending the user back to the same page but with the answer now below the form group.

> error.html
The error page is used when the user enters malicious input, such as asking for local weather instead of entering a function to integrate. Using the error handling of Wolfram function in helpers.py, error.html provides error messages while also providing a link to return to the homepage of the site, index.html.

#### CSS
> styles.css
Most of the styles of the site are handled by Bootstrap, but styles.css contains custom container width as well as the code for the custom card-group headers used in integral.html and index.html