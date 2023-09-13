from bs4 import BeautifulSoup
import requests
import random

# Initialize lists
easy_problems = [] 
easy_problems_names = []
medium_problems = []
medium_problems_names = []
hard_problems = []
hard_problems_names = []

# Easy Problems
page_to_scrape = requests.get('https://leetcode.com/problemset/all/?difficulty=EASY&page=1')
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
scrapes = soup.findAll("a", attrs={"class":"h-5 hover:text-blue-s dark:hover:text-dark-blue-s"})

for tag in scrapes:
    problem_name = tag.text
    href_url = tag['href']  # extract href attribute (without https://)
    array_url = "https://leetcode.com" + href_url  # adds https//
    easy_problems_names.append(problem_name)  # adds to lists
    easy_problems.append(array_url)

# Medium Problems
page_to_scrape = requests.get('https://leetcode.com/problemset/all/?page=1&difficulty=MEDIUM')
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
scrapes = soup.findAll("a", attrs={"class":"h-5 hover:text-blue-s dark:hover:text-dark-blue-s"})

for tag in scrapes:
    problem_name = tag.text
    href_url = tag['href']  # extract href attribute (without https://)
    array_url = "https://leetcode.com" + href_url  # adds https//
    medium_problems_names.append(problem_name)  # adds to lists
    medium_problems.append(array_url)

# Hard Problems
page_to_scrape = requests.get('https://leetcode.com/problemset/all/?page=1&difficulty=HARD')
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
scrapes = soup.findAll("a", attrs={"class":"h-5 hover:text-blue-s dark:hover:text-dark-blue-s"})

for tag in scrapes:
    problem_name = tag.text
    href_url = tag['href']  # extract href attribute (without https://)
    array_url = "https://leetcode.com" + href_url  # adds https//
    hard_problems_names.append(problem_name)  # adds to lists
    hard_problems.append(array_url)


#Functions to choose random problem
def random_easy():
    random_index = random.randint(0, len(easy_problems)-1)
    string = easy_problems_names[random_index] + ": " + easy_problems[random_index]
    return  string

def random_medium():
    random_index = random.randint(0, len(medium_problems)-1)
    string = medium_problems_names[random_index] + ": " + medium_problems[random_index]
    return string

def random_hard():
    random_index = random_number = random.randint(0, len(hard_problems)-1)
    string = hard_problems_names[random_index] + ": " + hard_problems[random_index]
    return string
