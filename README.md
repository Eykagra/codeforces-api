# Codeforces User Details Scraper

This Flask application fetches user details from Codeforces profiles using web scraping techniques.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd codeforces-user-details-scraper


## Install dependencies:
```pip install -r requirements.txt```


## Usage: 
Run the Flask application
```python app.py```


## Access user details: 
Open your web browser and go to ```http://localhost:5000/user/<username>```, replacing ```<username>``` with the Codeforces username.

Example using curl:
```curl http://localhost:5000/user/Adam```


## Response: 
The server responds with JSON data containing the fetched user details from the Codeforces profile.
Dependencies
Flask
Requests
BeautifulSoup4
