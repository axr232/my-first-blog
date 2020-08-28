from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_if_all_forms_present(self):
        cv_profile = self.browser.find_element_by_id('cv_profile').text
        cv_education = self.browser.find_element_by_id('cv_education').text
        cv_experience = self.browser.find_element_by_id('cv_experience').text
        cv_extracurricular_activities = self.browser.find_element_by_id('cv_extracurricular_activities').text
        cv_skills_and_interests = self.browser.find_element_by_id('cv_skills_and_interests').text

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
        self.check_if_all_forms_present()
        sub_header_check_list =["Profile","Education","Experience","Extra-curricular Achievements","Skills and Interests"]
        for i in range(len(sub_header_text)):
            self.assertEqual(sub_header_text[i].text,sub_header_check_list[i])
        #There are 5 forms
        
        #He clicks on the edit button to edit the CV

        #He clicks on the save button to save the new CV

        self.fail('Finish the test!')
if __name__=='__main__':
    unittest.main(warnings='ignore')