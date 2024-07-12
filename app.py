from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_user_info(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        user_info = data['result'][0]
        return user_info
    else:
        raise Exception("Error fetching user info")

def scrape_user_profile(handle):
    url = f"https://codeforces.com/profile/{handle}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    profile_info = {}

    img_tag = soup.select_one('.title-photo img')
    if img_tag:
        profile_info['title_photo'] = img_tag['src']
    
    user_name_tag = soup.select_one('.user-rank .rated-user')
    if user_name_tag:
        profile_info['username'] = user_name_tag.text.strip()

    rank_tag = soup.select_one('.user-rank .user-green')
    if rank_tag:
        profile_info['rank'] = rank_tag.text.strip()
    
    bio_tag = soup.select_one('.main-info div:nth-of-type(2)')
    if bio_tag:
        profile_info['bio'] = bio_tag.text.strip()

    rating_tag = soup.select_one('li img[alt="User\'s contest rating in Codeforces community"] + span')
    if rating_tag:
        profile_info['contest_rating'] = rating_tag.text.strip()
    
    contribution_tag = soup.select_one('li img[alt="User\'s contribution into Codeforces community"] + span')
    if contribution_tag:
        profile_info['contribution'] = contribution_tag.text.strip()

    friends_tag = soup.select_one('li img[alt="Friend of: 27 users"] + span')
    if friends_tag:
        profile_info['friends_count'] = friends_tag.text.strip()
    
    email_tag = soup.select_one('li img[alt="Email"] + a')
    if email_tag:
        profile_info['email'] = email_tag.text.strip()
    
    facebook_tag = soup.select_one('li a[href^="https://facebook.com/"]')
    if facebook_tag:
        profile_info['facebook'] = facebook_tag['href']
    
    last_visit_tag = soup.select_one('li:contains("Last visit:") span')
    if last_visit_tag:
        profile_info['last_visit'] = last_visit_tag.text.strip()
    
    registered_tag = soup.select_one('li:contains("Registered:") span')
    if registered_tag:
        profile_info['registered'] = registered_tag.text.strip()
    
    return profile_info

@app.route('/<string:handle>', methods=['GET'])
def get_profile(handle):
    try:
        user_info = get_user_info(handle)
        
        profile_info = scrape_user_profile(handle)
        
        combined_info = {
            'api_data': user_info,
            'scraped_data': profile_info
        }

        return jsonify(combined_info)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
