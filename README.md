# PITCHES
## This is a pitch application where users have one minute to write out their pitches in different categories and have those pitches voted on. The users also have a chance to comment on each pitch posted.
 
 ## Author
## By **[JOSEPHAT OTIENO](https://github.com/josphat-otieno)**

## User Stories
These are the behaviours/features that the application implements for use by a user.

* Logs in into the application
* Sees various categories for the pitche
* Selects the ones they prefer and see available pitches in that category
* Upvote or downvote a pitch
* Leave a comment on different pitches
* Post their own pitches
* Upload their profile photos and update thier bio

## Behaviour Driven Development
## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| User signs in or creates a new account | **On page load** | user sees various categories for the pitches and the pitches posted |
| User clicks on a category | **On Tab link click** | Various pitches of that category are displayed |
| user clicks on upvote or downvote | **Click a news source** | values for upvote and downvote increase and decrease by one respectively |
| user clicks on comment | **On page load** | comment page is loaded where users can write and post thier comments |
| user clicks on profle  | **Click an article** | profile page is loaded and users can can upload profle photos, update their bio and see various pitches they posted |

## Prerequisites
* Python3.8

## Setup/Installation Requirements
* Clone [this repository]( https://github.com/josphat-otieno/pitch-app.git)  using the following commamnd  in the terminal: `git clone  https://github.com/josphat-otieno/pitch-app.git`. 
* Note:<em>You will need to git installed in your machine. You can install using the following comman: `$ sudo apt-get install git.`</em>
* After cloning, navigate to the folder where the repo was cloned and open it with your favorite code editor and run the `manage.py` file to interact with the application using the following command `$python3.8 manage.py`
* Run tests units using the following command `$python3.8 manage.py test`
## Known Bugs

No known bugs

## Technologies Used
- Python3.8
- Flask
- Heroku

## Contacts
# Tel: +254717878813
Email: josephat.otieno@student.moringaschool.com
