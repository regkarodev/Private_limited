"""
Configuration settings for the NSWS automation system.
Contains URLs, element selectors, timeouts, and credentials.
"""

# URL configuration
LOGIN_URL = "https://www.nsws.gov.in/auth/realms/madhyam/protocol/openid-connect/auth?client_id=portal-prod&redirect_uri=https%3A%2F%2Fwww.nsws.gov.in%2Fportal%2Flogin&state=77141a1b-714d-4222-8286-81ecdf9b0c20&response_mode=fragment&response_type=code&scope=openid&nonce=b0351311-b479-4dd5-8169-845619f83b23&code_challenge=3UjsoghZvrBhETFPS-VGT0jVSc7ha2nBMaN_45BWYoc&code_challenge_method=S256"

# Credentials
EMAIL = "ihdminfotechnologies070325@gmail.com"
PASSWORD = "Qwerty@123"

# Data file
DATA_FILE = "textdb.json"

# Element selectors - Login page
USERNAME_FIELD_ID = "username"
PASSWORD_FIELD_ID = "userPassword"
LOGIN_BUTTON_ID = "kc-login"
ORGANIZATION_XPATH = "//div[contains(@class, 'content-list') and contains(., 'IHDM INFO TECHNOLOGIES LLP')]"

# Element selectors - Apply section
APPLY_NOW_CSS = "button.button.action-button"
APPLY_NOW_XPATH = "//button[normalize-space()='Apply Now']"

# Element selectors - Form fields
ABOUT_STARTUP_NAME = "about_start_up_6710415_120167790"
MOBILE_APP_ID = "Mobile App"
MOBILE_APP_NAME = "mobile_app_6710416_120167792"
WEBSITE_ID = "Website"
WEBSITE_NAME = "website_6710417_120167793"
UDYOG_AADHAAR_ID = "Udyog Aadhaar"
UDYOG_AADHAAR_NAME = "udyog_aadhaar_6710418_120167788"

# Element selectors - Dropdown
DROPDOWN_CSS = "div.ant-select-selection-overflow .ant-select-selection-search-input"
DROPDOWN_SELECTORS = [
    "body > div:nth-child(15) > div > div > div > div > div > div.ant-select-tree-list > div > div > div > div:nth-child(1) > span.ant-select-tree-node-content-wrapper.ant-select-tree-node-content-wrapper-normal > span",
    "body > div:nth-child(15) > div > div > div > div > div > div.ant-select-tree-list > div > div > div > div:nth-child(2) > span.ant-select-tree-node-content-wrapper.ant-select-tree-node-content-wrapper-normal > span"
]

# Element selectors - Founder details
FOUNDER_NAME_ID = "Name"
FOUNDER_NAME_NAME = "name_6710439_120167892"
FOUNDER_DESIGNATION_ID = "Designation"
FOUNDER_DESIGNATION_NAME = "designation_6710440_120167893"
FOUNDER_MOBILE_ID = "Mobile Number"
FOUNDER_EMAIL_ID = "Email Address"

# Element selectors - Director details
DIRECTOR_NAME_XPATH = "//input[@id='Name' and @name='name_6710443_120167876']"
DIRECTOR_DIN_XPATH = "//input[@id='DIN/DPIN' and @name='din/dpin_6710444_120167873']"
DIRECTOR_MOBILE_XPATH = "//input[@type='tel' and @name='phoneNumber' and @placeholder='Mobile Number']"
DIRECTOR_POSTAL_XPATH = "//input[@id='Postal Address' and @name='postal_address_6710447_120167875']"
DIRECTOR_EMAIL_XPATH = "//input[@id='Email Address' and @name='email_address_6710448_120167878']"

# Element selectors - Business details
EMPLOYEES_XPATH = "//input[@id='Current Number of Employees(including founders)' and @name='current_number_of_employees(including_founders)_6710449_120167883']"
EMPLOYMENT_CHECKBOX_XPATH = "//input[@type='checkbox' and @value='Employment Generation']"
BRIEF_NOTE_NAME = "please_submit_a_brief_note_supporting_the_options_chosen_above_for_innovation,_improvement_and_scalability._6710469_120167902"

# Business details textarea mapping
TEXTAREA_MAP = [
    ("problemSolving", "what_is_the_problem_the_startup_is_solving?_6710475_120167907"),
    ("proposalToSolve", "how_does_the_startup_propose_to_solve_the_problem?_6710476_120167909"),
    ("uniquenessOfSolution", "what_is_the_uniqueness_of_the_solution?_6710477_120167905"),
    ("revenueGeneration", "how_does_the_startup_generate_revenue?_6710478_120167903"),
]

# Timeouts
SHORT_WAIT = 3
MEDIUM_WAIT = 10
LONG_WAIT = 30
FORM_LOAD_WAIT = 7