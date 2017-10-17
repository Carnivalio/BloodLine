# BloodLine

## Code Style Rules

-	Use imports for packages and modules only.
-	Import each module using the full pathname location of the module.
-	Avoid global variables.
-	Do not terminate your lines with semi-colons and do not use semi-colons to put two commands on the same line.
-	Maximum line length is 80 characters.
-	Use parentheses sparingly.
-	Indent your code blocks with 4 spaces.
-	Two blank lines between top-level definitions, one blank line between method definitions.
-	Follow standard typographic rules for the use of spaces around punctuation.
-	Be sure to use the right style for module, function, method and in-line comments.
-	If a class inherits from no other base classes, explicitly inherit from object. This also applies to nested classes.
-	Use the format method or the % operator for formatting strings, even when the parameters are all strings. Use your best judgement to decide between + and % (or format) though.
-	Explicitly close files and sockets when done with them.
-	Use TODO comments for code that is temporary, a short-term solution, or good-enough but not perfect.
-	Imports should be on separate lines.
-	Use single quotes for strings, or a double quote if the the string contains a single quote. Don’t waste time doing unrelated refactoring of existing code to conform to this style.
-	Use underscores, not camelCase, for variable, function and method names (i.e. poll.get_unique_voters(), not poll.getUniqueVoters()).Use InitialCaps for class names (or for factory functions that return classes).Use four spaces for indenting
-	Have a comment on every function that describes its purpose
-	Embed function comments in /* */
-	Don't abbreviate local variables (e.g., 'total' not 'tot')
-	In test docstrings, state the expected behavior that each test demonstrates. Don’t include preambles such as “Tests that” or “Ensures that”.
-	Reserve ticket references for obscure issues where the ticket has additional details that can’t be easily described in docstrings or comments. Include the ticket number at the end of a sentence
-	Use four space hanging indentation rather than vertical alignment:
raise AttributeError(
    'Here is a multine error message '
    'shortened for clarity.'
)
Instead of:
raise AttributeError('Here is a multine error message '
                     'shortened for clarity.')
-	Avoid use of “we” in comments, e.g. “Loop over” rather than “We loop over”.
-	In Django template code, put one (and only one) space between the curly brackets and the tag contents.
-	In Django views, the first parameter in a view function should be called request.’
-	Field names should be all lowercase, using underscores instead of camelCase.

## About BloodLine

BloodLine is a web-app that connects people who want to donate their blood, people who need a specific blood, and the hospital or blood bank organizations

### Why BloodLine?

Bloodline can be regarded as a bridge among donor, people need blood and healthcare organizations. For the donors, they can request an appointment to donate their blood easily. For people need blood, especially people who have a rare kind of blood(e.g. O-Negative), they can connect with people having the same type of blood. For healthcare organizations, they have a large database to search the available blood donors and blood sources, which can save time at emergencies. 

## Front-End Functionality
-----------------------------------------------------------
## Home

- Functionality: On home page, users could learn more about blood donation

## Donate

- Functionality: Through donate function, users could request an appointment with the blood centres, the system will automatically record the information of the requesting donor by his login information
- Usage: Choose the donation centre, donation type and appointment, then the system will record this request

## Find a Centre

- Funtinality: Able to search a blood centre through postcode or name, this is an ajax function, which means the page does not need to be reload
- Usage: Type in the postcode or name into the input space and the information of corresponding centres will be shown

## Blood Donor Database

- Functionality: Able to search donors through bloodtype, this is an ajax function, which means the page does not need to be reload
- Usage: Type in the blood type into the input space and the users with that blood type will be shown

## Log In

- Functionality: Now we support two kinds of login, one is normal login, another one is login by Google

## Sign Up

- Functionality: Sign up a new user with his personal information and blood information. If the user tick "Public profile", then his information will be added to the donor database and could be searched later

## Web Service Functionality
------------------------------------------------
## Twitter Posts

- Functionality: We believe that Twitter has a large social influence. Thus, everytime a user donates the blood, the news about it will be posted on our public page on Twitter

## Administration Zone
------------------------------------------------
- Functionality: Control all the database (user, bank, and blood/donation)

## RESTFUL API
------------------------------------------------




