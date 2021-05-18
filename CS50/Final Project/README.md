Final Project [Video](https://www.youtube.com/watch?v=3pOB0Sdsuko)


This project is a web-based app called Ping Pong Meet.


Its aim is to help ping pong players find partners to play, keep track of their scores, and analyze their stats to improve.
It provides an environment to promote ping pong within a larger community (like a college) by making it easy to meet other players.
The reason for it is that there are usually few ping pong players, and it is important to keep them connected so they can play often.


Ping Pong Meet uses Python, SQLite, HTML, CSS and JavaScript as its programming languages.


The web is divided into different sections, which are the following:


Register: registers a new username, checking:
- Username is not taken
- Password meets some criteria
- Email and password are repeated correctly


Login/Logout:
- Login checks password is correct


Main page: shows the following stats:
- Total number of games played so far
- Top 5 players that the user has played with, and the number of games played
- Total number of games won and lost


Add match results: allows to add new match results, checking:
- Logged in user was in the game
- Result meets Ping Pong criteria (won by 2 points or more)
- Winner score > Loser score
- Assigns specific id to each match registered


Remove match results: allows to remove a match from the history in case it was registered incorrectly
- It will check if the logged in user trying to delete the match actually played in the match


My matches: displays a table with the history of all the matches played by the user:
- It will show winner, loser, their scores and the match id and date
- It highlights in green/red if the user won/lost that match


My schedule: Allows the user to choose from a table of checkboxes the timeframes when he/she will be available to play
- Originally displays last recorded schedule
- Allows for 10 timeframes, Mo-Fri Morning or Evening


Find: allows to search for another user with two options for searching (page modified with JavaScript upon choosing)
- Find by username: displays (if found) the username and the email for contact.
- Also displays stats with that particular user (matches played, won, lost) and his/her selected schedule.
- Useful for keeping track of performance agains one particular user.

- Find by schedule: allows to select up to the 10 timeframes (with table of checkboxes) to search for users available in those timeframes.
- It will display a table for each timeframe selected, showing all available users in that timeframe with their email.
- Very useful to meet with people who are only available on some timeframes, and to match people by availability.

