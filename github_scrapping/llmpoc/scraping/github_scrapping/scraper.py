import requests
from bs4 import BeautifulSoup
import json

# the URL of the target repo to scrape
url = 'https://github.com/luminati-io/luminati-proxy'

# download the target page
page = requests.get(url)
# parse the HTML document returned by the server
soup = BeautifulSoup(page.text, 'html.parser')

# initialize the object that will contain the scraped data
repo = {}

# repo scraping logic
name_html_element = soup.select_one('[itemprop="name"] a')
name = name_html_element.get_text().strip() if name_html_element else "Unknown"

main_branch = "master"

# scrape the repo history data
relative_time_html_element = soup.select_one('relative-time')
latest_commit = relative_time_html_element['datetime'] if relative_time_html_element else "Unknown"

commits_parent_element = soup.select_one('a[href$="/commits/master"]')
commits_html_element = commits_parent_element.select_one('span.d-none.d-sm-inline') if commits_parent_element else None
commits = commits_html_element.get_text().strip().replace(',', '') if commits_html_element else "Unknown"

# scrape the repo details in the right box
bordergrid_html_element = soup.select_one('.BorderGrid')

description_html_element = bordergrid_html_element.select_one('p.f4') if bordergrid_html_element else None
description = description_html_element.get_text().strip() if description_html_element else "No description available"

star_icon_html_element = bordergrid_html_element.select_one('a[href$="/stargazers"] .octicon-star') if bordergrid_html_element else None
stars_html_element = star_icon_html_element.find_next_sibling('strong') if star_icon_html_element else None
stars = stars_html_element.get_text().strip().replace(',', '') if stars_html_element else "0"

eye_icon_html_element = soup.select_one('a[href$="/watchers"]')
watchers_html_element = eye_icon_html_element.select_one('strong') if eye_icon_html_element else None
watchers = watchers_html_element.get_text().strip().replace(',', '') if watchers_html_element else "0"

fork_icon_html_element = bordergrid_html_element.select_one('a[href$="/forks"] .octicon-repo-forked') if bordergrid_html_element else None
forks_html_element = fork_icon_html_element.find_next_sibling('strong') if fork_icon_html_element else None
forks = forks_html_element.get_text().strip().replace(',', '') if forks_html_element else "0"

pull_requests_parent_element = soup.select_one('a[href$="/pulls"]')
pull_requests_html_element = pull_requests_parent_element.select_one('span.Counter') if pull_requests_parent_element else None
pull_requests = pull_requests_html_element.get_text().strip().replace(',', '') if pull_requests_html_element else "Unknown"

releases_parent_element = soup.select_one('a[href$="/releases"]')
releases_html_element = releases_parent_element.select_one('span.Counter') if releases_parent_element else None
releases = releases_html_element.get_text().strip().replace(',', '') if releases_html_element else "Unknown"

contributors_parent_element = soup.select_one('a[href$="/contributors"]')
contributors_html_element = contributors_parent_element.select_one('span.Counter') if contributors_parent_element else None
contributors = contributors_html_element.get_text().strip().replace(',', '') if contributors_html_element else "Unknown"

activities = []
for event in soup.select('.js-commits-list-item'):
    event_text = event.get_text(strip=True)
    activities.append(event_text)

# build the URL for README.md and download it
readme_url = 'https://github.com/luminati-io/luminati-proxy/tree/master'
readme_page = requests.get(readme_url)

readme = None
# if there is a README.md file
if readme_page.status_code != 404:
    readme = readme_page.text
else:
    readme = "No README available"

# store the scraped data
repo['name'] = name
repo['latest_commit'] = latest_commit
repo['commits'] = commits
repo['main_branch'] = main_branch
repo['description'] = description
repo['stars'] = stars
repo['watchers'] = watchers
repo['forks'] = forks
repo['pull_requests']=pull_requests
repo['releases']=releases
repo['contributors']=contributors
repo['activities']=activities
repo['readme'] = readme

# export the scraped data to a repo.json output file
with open('repo.json', 'w') as file:
    json.dump(repo, file, indent=4)

# print the output for verification
print(json.dumps(repo, indent=4))
