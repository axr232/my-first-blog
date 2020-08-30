from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
    def tearDown(self):
        self.browser.quit()

    def check_if_all_forms_present(self):
        cv_address = self.browser.find_element_by_id('cv_address').text
        cv_phone = self.browser.find_element_by_id('cv_phone').text
        cv_profile = self.browser.find_element_by_id('cv_profile').text
        cv_education = self.browser.find_element_by_id('cv_education').text
        cv_experience = self.browser.find_element_by_id('cv_experience').text
        cv_extracurricular_achievements = self.browser.find_element_by_id('cv_extracurricular_achievements').text
        cv_skills_and_interests = self.browser.find_element_by_id('cv_skills_and_interests').text
        return_list = [cv_address]
        return_list.append(cv_phone)
        return_list.append(cv_profile)
        return_list.append(cv_education)
        return_list.append(cv_experience)
        return_list.append(cv_extracurricular_achievements)
        return_list.append(cv_skills_and_interests)
        return return_list

    def cv_edit_get_all_forms(self):
        cv_address = self.browser.find_element_by_id('id_address')
        cv_phone = self.browser.find_element_by_id('id_phone_number')
        cv_profile = self.browser.find_element_by_id('id_profile')
        cv_education = self.browser.find_element_by_id('id_education')
        cv_experience = self.browser.find_element_by_id('id_experience')
        cv_extracurricular_achievements = self.browser.find_element_by_id('id_extracurricular_achievements')
        cv_skills_and_interests = self.browser.find_element_by_id('id_skills_and_interests')
        return_list = []
        return_list.append(cv_address)
        return_list.append(cv_phone)
        return_list.append(cv_profile)
        return_list.append(cv_education)
        return_list.append(cv_experience)
        return_list.append(cv_extracurricular_achievements)
        return_list.append(cv_skills_and_interests)
        return return_list

    def test_can_edit_forms(self):
        #Alex goes on a site to check his CV
        #When he arrives on the home screen he clicks the briefcase icon to check his CV
        self.browser.get('http://127.0.0.1:8000/cv_page')
        self.assertIn('Bridging Coursework',self.browser.title)
    
        #He sees the CV form, which has the different sections separated by a sub header(h3)
        
        header_text = self.browser.find_element_by_tag_name('h2').text
        print(header_text)
        self.assertIn('CV',header_text)
        sub_header_text = self.browser.find_elements_by_tag_name('h3')
        sub_header_check_list =["Profile","Education","Experience","Extra-curricular Achievements","Skills and Interests"]
        for i in range(len(sub_header_text)):
            self.assertEqual(sub_header_text[i].text,sub_header_check_list[i])

        #There are 7 forms

        self.assertEquals(len(self.check_if_all_forms_present()),7)

        #He clicks on the edit button to edit the CV

        cv_edit_button = self.browser.find_element_by_id("cv_edit_button")
        cv_edit_button.click()

        #He can type in the text boxes
        
        test_input=["test_address","test_phone","test_profile","test_education","test_experience","test_extracurricular_achievements","test_skills_and_interests"]
        element_list = self.cv_edit_get_all_forms()
 
        for text_box in element_list:
            text_box.send_keys(test_input[element_list.index(text_box)])

        #He clicks on the save button to save the new CV
        
        cv_save_button = self.browser.find_element_by_id("cv_save_button")
        cv_save_button.submit()
        self.browser.get('http://127.0.0.1:8000/cv_page')
        actual_input = self.check_if_all_forms_present()
        self.assertEqual(actual_input,test_input)

if __name__=='__main__':
    unittest.main(warnings='ignore')
