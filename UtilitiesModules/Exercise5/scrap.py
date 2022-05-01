import requests
from bs4 import BeautifulSoup

# Fetches all the html from the Url
req = requests.get('https://realpython.github.io/fake-jobs')

# Parses all the html
soup = BeautifulSoup(req.content, "html.parser")

# Goes through the html an finds the div with the id ResultsContainer and takes all the html from inside the div & puts it inside a variable
results = soup.find(id="ResultsContainer")

# Goes through the ResultsContainer and and finds all the divs with the class name card-content and puts it in an (list)/(array)
job_elements = results.find_all("div", class_="card-content")


#for job_element in job_elements:
#    title_element = job_element.find("h2", class_="title")
#    company_element = job_element.find("h3", class_="company")
#    location_element = job_element.find("p", class_="location")
#    print("JOB:      " + title_element.text.strip())
#    print("COMPANY:  " + company_element.text.strip())
#    print("LOCATION: " + location_element.text.strip())
#    print()

python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
for job_element in python_job_elements:
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")


