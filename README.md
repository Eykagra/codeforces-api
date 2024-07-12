Installation
Clone the repository:

git clone <repository-url>
cd codeforces-user-details-scraper


Install dependencies:

pip install -r requirements.txt


Usage
Run the Flask application:
python app.py
This starts the Flask server locally.

Access user details:

Open your web browser and go to http://localhost:5000/user/<username>, replacing <username> with the Codeforces username you want to retrieve details for.

Alternatively, you can use tools like curl or Postman to send GET requests to the endpoint:
curl http://localhost:5000/user/Adam


Response:

The server responds with JSON data containing the fetched user details from the Codeforces profile.

Dependencies
Flask: Web framework for Python.
Requests: HTTP library for making requests.
BeautifulSoup4: HTML parsing library for extracting data from HTML documents.
