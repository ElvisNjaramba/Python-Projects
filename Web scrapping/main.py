from bs4 import BeautifulSoup
import requests
import time

print("Enter the skills to filter out")
unfamiliar_skills = input(">")
print("filtering out ", unfamiliar_skills)

def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs= soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'days' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name:  {company_name.strip()} \n")
                    f.write(f"Required Name:  {skills.strip()} \n")
                    f.write(f"More Info:  {more_info} \n")

                print(f'file saved: {index}')

if __name__ == '__main__':
    find_job()
    time_wait = 10
    time.sleep(time_wait * 60)
    print(f"waiting {time_wait} minutes...")