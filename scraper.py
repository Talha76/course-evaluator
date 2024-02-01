from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

good = []
bad = []

b = webdriver.Firefox()
b.get("https://sis.iutoic-dhaka.edu/login/")

wait = WebDriverWait(b, 10)

# Logging into the website
username = ""
password = ""
wait.until(ec.presence_of_element_located((By.NAME, "username")))
b.find_element(By.NAME, "username").send_keys(username)
wait.until(ec.presence_of_element_located((By.NAME, "password")))
b.find_element(By.NAME, "password").send_keys(password)
wait.until(ec.presence_of_element_located((By.ID, "m_login_signin_submit")))
b.find_element(By.ID, "m_login_signin_submit").click()
# Login end

while True:
    try:
        # Getting the evaluation list
        b.get("https://sis.iutoic-dhaka.edu/evaluation-list")
        wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='btn btn-primary btn-sm']")))
        b.find_element(By.CSS_SELECTOR, "a[class='btn btn-primary btn-sm']").click()     # Clicking on the first evaluation

        rating = 3
        comment = "N/A"

        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".kt-portlet__head-title")))
        name = b.find_element(By.CSS_SELECTOR, ".kt-portlet__head-title").text.split("(")[1].split(")")[0]

        # Filtering based on good and bad evaluations
        for short_name in good:
            if short_name in name:
                rating = 5
                comment = "Very responsible teacher"
                break
        for short_name in bad:
            if short_name in name:
                rating = 1
                comment = "Not good enough"
                break
        # Filtering end

        # Provide ratings
        wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, f"input[value='{rating}']")))
        for item in b.find_elements(By.CSS_SELECTOR, f"input[value='{rating}']"):
            item.click()

        # Provide comments
        wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, "textarea")))
        for item in b.find_elements(By.TAG_NAME, "textarea"):
            item.send_keys(comment)

        # Submitting the evaluation
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "button[class='btn btn-primary']")))
        b.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()
    except Exception as e:
        print(str(e))
        break

b.quit()
