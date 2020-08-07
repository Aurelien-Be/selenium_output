from selenium import webdriver

edge_browser = webdriver.Edge(R'C:\Users\Asus\Documents\Python\msedgedriver.exe')

edge_browser.maximize_window()
edge_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in edge_browser.title
show_message_button = edge_browser.find_element_by_class_name("btn-default")
#print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in edge_browser.page_source

user_message = edge_browser.find_element_by_id('user-message')
user_button2 = edge_browser.find_element_by_css_selector('#get-input > .btn')
user_message.send_keys('Je suis super cool')
print(user_button2)

show_message_button.click()
output_message = edge_browser.find_element_by_id('display')

edge_browser.quit()


assert 'Je suis super cool' in output_message.text