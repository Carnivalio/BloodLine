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

**TEMPORARY**
## Front-End Functionality

## Administrator

- Able to add, edit, and delete User, Bank, and Blood Data

## Find a Centre

- Able to search a blood centre through postcode or name

## Rare Blood Donor Database

- Able to search donors through bloodtype

### User Index Page (Administrator Only)

- Show the list of the user
- User list is click-able, redirecting user to the User Detail page
- Feature to add new user

### User Detail Page (Administrator Only)

- Show all details of the selected user

### Create User Page (Administrator Only)
- Self explanatory, this page is to be used for adding user

## Back-End Functionality

