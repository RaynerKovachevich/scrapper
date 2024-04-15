import requests
from bs4 import BeautifulSoup

url = "https://www.glassdoor.nl"

if "__main__" == __name__:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    def has_junior_software_developer_and_english(tag):
        return tag.name == "a" and "Junior Software Developer" in tag.get_text().strip() and "english" in tag.get_text().strip(),lower()
    
    results = soup.find_all(has_junior_software_developer_and_english)

with open("jobs.txt", "w", encoding="utf-8") as file:
    for job in results:
        try:
            title = job.find("div")
            class_= "TwoColumnLayout_container___jk7P".get_text().strip()
            company = job.find_next("span", class_="jobCompany").get_text().strip()
            joblink = job["href"]
            salary = job.find_next("span", class_="jobSalary")
            salary = salary.get_text().strip() if salary else 'n/a'

            job_info = "Title: {}\nCompany: {}\nSalary: {}\nLink: {}\n\n"
            job_info = job_info.format(title, company, salary, joblink)
         
            file.write(job_info)   
        except Exception as e: 
            print("Exception: {}".format(e))
            pass    


