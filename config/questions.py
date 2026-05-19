'''
Author:     Daniyal
LinkedIn:   https://www.linkedin.com/in/daniyal-automation/
GitHub:     https://github.com/syed-daniyalH
Version:    26.01.20.5.08
'''

###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "Daniyal_Resume.pdf"      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience?
years_of_experience = "5"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "Yes"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = "https://example.com"                        # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/daniyal-undefined-084b1a400"       # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Other"



## SOME ANNOYING QUESTIONS BY COMPANIES  ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 1200000          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs),
then it will add '.' before last 5 digits and answer. Examples:
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 800000            # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs),
then it will add '.' before last 5 digits and answer. Examples:
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg:
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 30                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months),
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "AI Automation Engineer | Python, Playwright, SQLite Expert" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
AI Automation Engineer with 5 years of experience in Python, Playwright, and SQLite.
Passionate about building efficient automation solutions and scaling AI systems.
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
'''

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Cover Letter
"""
##> ------ Daniyal - AI Automation Engineer ------

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc.
user_information_all = """
# Daniyal
**AI Automation Engineer | Python & Browser Automation Specialist**  
 Los Angeles, CA |  +1 (234) 567-890 |  daniyal.ai@example.com  
 [LinkedIn](https://www.linkedin.com/in/daniyal-automation/) |  [GitHub](https://github.com/syed-daniyalH)

---

##  Professional Summary
Highly skilled and results-oriented AI Automation Engineer with 5+ years of experience in designing, developing, and deploying robust web automation systems. Expert in **Python**, **browser automation (Playwright, Selenium)**, and **AI integration (OpenAI, Gemini)**. Proven track record of optimizing complex workflows and scaling AI-driven applications to improve operational efficiency.

---

##  Core Skills
- **Languages**: Python (Expert), JavaScript, SQL, Bash.
- **Web Automation**: Selenium WebDriver, Playwright, undetected-chromedriver.
- **AI/ML**: OpenAI API (GPT-4), Google Gemini, DeepSeek, Prompt Engineering.
- **Backend & Database**: Flask, FastAPI, SQLite, MongoDB.
- **Tools**: Git, Docker, LinkedIn API, Web Scraping (BeautifulSoup, Scrapy).
- **Environment**: Linux, Windows Automation, CI/CD.

---

##  Professional Experience

### **Senior Automation Engineer | AI Solutions Corp**  
*January 2021  Present*
- Engineered a modular LinkedIn automation engine that increased application rates by 300% for candidate sourcing.
- Implemented **GPT-4 based prompt engineering** to automate complex job form responses with 95% accuracy.
- Optimized browser anti-detection mechanisms, significantly reducing account bans and session timeouts.
- Built a real-time dashboard using **Flask** to track automation success metrics and history.

### **Automation Developer | TechSync Systems**  
*June 2018  December 2020*
- Developed automated testing suites using **Pytest** and **Selenium**, reducing manual QA time by 60%.
- Integrated third-party APIs for automated data synchronization between CRM and recruitment platforms.
- Managed and maintained a fleet of automated browser workers in a headless Linux environment.

---

##  Key Projects
### **LinkedIn AI Auto Job Applier**
- Built a comprehensive Python-based bot that searches, filters, and applies to jobs on LinkedIn.
- Integrated multiple AI providers (OpenAI, Gemini, DeepSeek) for dynamic field answering.
- Developed a modern SaaS-style web dashboard for real-time monitoring.

### **Automated Resume Extractor & Tailor**
- Created a tool to scan job descriptions and automatically tailor PDFs to match required skills.
- Used **Natural Language Processing (NLP)** to identify and prioritize keywords for ATS optimization.

---

##  Education
**Bachelor of Science in Computer Science**  
*State University of Technology*

---

##  Certifications
- **Professional Python Automation Specialist**
- **AI-Powered Software Development Certification**
- **Advanced Web Scraping & Anti-Detection Techniques**

---
*Visit my [GitHub](https://github.com/syed-daniyalH) to see these projects and more in action!*
"""
##<

# Name of your most recent employer
recent_employer = "Current Tech" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "8"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##

# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = True         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive


############################################################################################################
'''
THANK YOU for using my tool ! Wishing you the best in your job hunt !









Gratefully yours ,
Daniyal
'''
############################################################################################################
