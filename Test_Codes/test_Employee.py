from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Test_Locators import locators
from Test_Data import data
import pytest


class Test_Employee:
    @pytest.fixture
    def bootingfunction(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 30)
        self.driver.maximize_window()
        self.driver.get(data.Employee_Data().url)

    
    def test_searchbox(self, bootingfunction):
        # Test case-1:
        self.wait.until(EC.presence_of_element_located((By.NAME, locators.Employee_Locators().username_locator))).send_keys(data.Employee_Data().username)
        self.wait.until(EC.presence_of_element_located((By.NAME, locators.Employee_Locators().password_locator1))).send_keys(data.Employee_Data().password1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().submitBox_locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().Adminbox_locator))).click()

        side_pane = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().Sidepane_locator)))
        assert side_pane, side_pane.is_displayed()
        print("Validation is successfull")

        side_pane_1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().Sidepane1_locator)))
        assert side_pane_1, side_pane.is_displayed()
        print("Validation is  not successfull")

        search_box = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().searchbox_locator)
        search_terms = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard","Directory", "Maintenance", "Buzz"]
        for a in search_terms:
            search_box.send_keys(a.upper())
            sleep(1)
            search_box.send_keys(Keys.CONTROL, 'a')
            search_box.send_keys(Keys.BACKSPACE)
            sleep(1)
        for a in search_terms:
            search_box.send_keys(a.lower())
            sleep(1)
            search_box.send_keys(Keys.CONTROL, 'a')
            search_box.send_keys(Keys.BACKSPACE)
            sleep(1)
        print("Testcase-1 Searchbox validating is successfull")

    # Test case-2
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().Adminbox_locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().Usermanagement_locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().Userselecting_locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().UsernameBox_locator))).send_keys(data.Employee_Data().UsernameBox)
        userrole1 = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().userrole)
        userrole1.click()
        dropdown1 = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().dropdown1_locator).text
        if dropdown1.__contains__("Admin"):
            self.driver.execute_script("var a=arguments[0];a.innerHTML='Admin'", userrole1)
        option1 = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().value1)
        option1.click()
        dropdown2 = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().dropdown2_locator).text
        if dropdown2.__contains__("Enabled"):
            self.driver.execute_script("var a=arguments[0];a.innerHTML='Enabled'", option1)
        sleep(2)
        userrole2 = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().userrole)
        userrole2.click()
        dropdown3 = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().dropdown1_locator).text
        if dropdown3.__contains__("ESS"):
            self.driver.execute_script("var a=arguments[0];a.innerHTML='ESS'", userrole2)
        option2 = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().value2)
        option2.click()
        dropdown4 = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().dropdown2_locator).text
        if dropdown4.__contains__("Disabled"):
            self.driver.execute_script("var a=arguments[0];a.innerHTML='Disabled'", option2)
        print("Testcase-2 Admin page Drop_down button validating is successfull")
    #Test case-3
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().Pimmodulebutton_locator))).click()
        sleep(2)
        self.driver.find_element(by=By.LINK_TEXT, value=locators.Employee_Locators().AddEmployee_locator).click()
        sleep(2)
        self.driver.find_element(by=By.NAME, value=locators.Employee_Locators().Firstname_locator).send_keys(data.Employee_Data().UsernameBox)
        self.driver.find_element(by=By.NAME, value=locators.Employee_Locators().Middlename_locator).send_keys(data.Employee_Data().middleName)
        self.driver.find_element(By.NAME, value=locators.Employee_Locators().Lastname_locator).send_keys(data.Employee_Data().lastName)
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().Radiobutton_locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().User_locator).send_keys(data.Employee_Data().UsernameBox)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().Password_locator2).send_keys(data.Employee_Data().Password2)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().Confirmpassword_locator).send_keys(data.Employee_Data().Password2)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().saveBox_locator).click()
        sleep(2)
        print("Testcase-3 Employeedetails are added")

    # Test case-4
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().Pimmodulebutton_locator))).click()
        sleep(2)
        self.driver.find_element(by=By.LINK_TEXT, value=locators.Employee_Locators().Employeelist_locator).click()
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().Employeename_locator).send_keys(data.Employee_Data().Employeename)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().Searchbutton_locator).click()
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().click_button_locator).click()
        sleep(4)
        print('Testcase-4 Employeelist is verified')

    # Test case-5
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().Nickename_locator))).send_keys(data.Employee_Data().Nickname)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().otherid_locator))).send_keys(data.Employee_Data().otherid)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().Drivinglicensenumber_locator))).send_keys(data.Employee_Data().Drivinglicensenumber)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().LicenseExpiryDate_locator))).send_keys(data.Employee_Data().LicenseExpiryDate)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().SINNumber_locator))).send_keys(data.Employee_Data().SINNumber)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().SSNNumber_locator))).send_keys(data.Employee_Data().SSNNumber)
        nationality_enter = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().Nationality_locator)
        nationality_enter.click()
        selecting_nationality = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().Nationality_selector)
        selecting_nationality.click()
        maritalstatus_entry = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().marital_status)
        maritalstatus_entry.click()
        selecting_maritalstatus = self.driver.find_element(by=By.XPATH,value=locators.Employee_Locators().maritalstatus_selector)
        selecting_maritalstatus.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().GenderBox_locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().Dateofbirth_locator))).send_keys(data.Employee_Data().Dateofbirth)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().MilitaryService_locator))).send_keys(data.Employee_Data().MilitaryServiceBox)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().Save1_locator).click()
        blood_groupoption = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().bloodgroup_locator)
        blood_groupoption.click()
        bg_selector = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().bloodgroup_selector)
        bg_selector.click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().Save2_locator).click()
        sleep(5)
        print('Testcase-5 Employeepersonaldetails are added')

    # Testcase-6
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().Pimmodulebutton_locator))).click()
        sleep(2)
        self.driver.find_element(by=By.LINK_TEXT, value=locators.Employee_Locators().Employeelist_locator).click()
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().Employeename_locator).send_keys(data.Employee_Data().Employeename)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().Searchbutton_locator).click()
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().click_button_locator).click()
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, locators.Employee_Locators().Contactdetail_locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().street1_locator))).send_keys(data.Employee_Data().street1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().street2_locator))).send_keys(data.Employee_Data().street2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().city_locator))).send_keys(data.Employee_Data().city_name)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().state_locator))).send_keys(data.Employee_Data().state_name)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().zipcode_locator))).send_keys(data.Employee_Data().zip_code)
        country_enter = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().country_locator)
        country_enter.click()
        selecting_country = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().country_selector)
        selecting_country.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().home_locator))).send_keys(data.Employee_Data().home_number)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().moblie_locator))).send_keys(data.Employee_Data().mobile_number)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().work_locator))).send_keys(data.Employee_Data().work_name)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().work_mail_locator))).send_keys(data.Employee_Data().work_mailid)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().other_mailid_locator))).send_keys(data.Employee_Data().other_mail)
        sleep(6)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().save_button1_locator).click()
        sleep(6)
        assert self.driver.title == self.driver.title

        print('Testcase-6 Contactdetail are added')

    # Testcase-7
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, locators.Employee_Locators().emergencyContants_locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().emergencyaddbutton_locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().name_locator))).send_keys(data.Employee_Data().name)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().relationship_locator))).send_keys(data.Employee_Data().relationship)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().homenumber_locator))).send_keys(data.Employee_Data().home_telephone)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().mobilenumber_locator))).send_keys(data.Employee_Data().mobile_number1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().worknumber_locator))).send_keys(data.Employee_Data().work_telephone)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().save_button2_locator).click()
        sleep(5)
        assert self.driver.title == self.driver.title

        print("Testcase-7 Emergencydetails are added")

    # Testcase-8
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, locators.Employee_Locators().dependent_locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().dependentsadd_locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().dependentsname_locator))).send_keys(data.Employee_Data().dependentname)
        relationshipenter = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().relationshipbutton_locator)
        relationshipenter.click()
        sleep(3)
        relationshipchoose = self.driver.find_element(by=By.XPATH,value=locators.Employee_Locators().relationshipselecting_locator)
        relationshipchoose.click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().relationdateob_locator).send_keys(data.Employee_Data().realtion_dob)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().save_button3_locator).click()
        sleep(5)
        assert self.driver.title == self.driver.title

        print("Testcase-8 Dependentdetails are added")

    # Testcase-9
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, locators.Employee_Locators().jobbutton_locator))).click()
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().joined_locator))).send_keys(data.Employee_Data().joined_date)
        jobtitle_enter = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().job_title_locator)
        jobtitle_enter.click()
        selecting_jobtitle = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().JobTitle_selector)
        selecting_jobtitle.click()
        jobcategory_enter = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().job_category_locator)
        jobcategory_enter.click()
        selecting_title = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().jobcategory_selector)
        selecting_title.click()
        sleep(3)
        subunit_enter = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().subunit_locator)
        subunit_enter.click()
        selecting_subunit = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().subunit_selector)
        selecting_subunit.click()
        location_enter = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().location_locator)
        location_enter.click()
        selecting_location = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().location_selector)
        selecting_location.click()
        employment_status_enter = self.driver.find_element(by=By.XPATH,value=locators.Employee_Locators().employeestatus_locator)
        employment_status_enter.click()
        employment_status_title = self.driver.find_element(by=By.XPATH,value=locators.Employee_Locators().employmentstatus_selector)
        employment_status_title.click()
        sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().EmploymentContractDetailsbutton_locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().ContractStartDate_locator))).send_keys(data.Employee_Data().ContractStartDate)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().ContractEndDate_locator))).send_keys(data.Employee_Data().ContractEndDate)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().save_button5_locator).click()
        sleep(5)
        assert self.driver.title == self.driver.title

        print("Testcase-9 Employee jobdetials are added")

    # Testcase-10
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().terminatebutton_locator).click()
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().terminatedate_locator))).send_keys(data.Employee_Data().termination_date)
        Terminate_reason_entry = self.driver.find_element(by=By.XPATH,value=locators.Employee_Locators().Terminatereason_locator)
        Terminate_reason_entry.click()
        sleep(3)
        Terminatereasonselecting = self.driver.find_element(by=By.XPATH,value=locators.Employee_Locators().Terminatereasonselector_locator)
        Terminatereasonselecting.click()
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().note))).send_keys(data.Employee_Data().terminate_note)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().save_button6_locator).click()
        sleep(5)
        assert self.driver.title == self.driver.title

        print("Testcase-10 Terminateemployee is executed")

    # Testcase-11
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().activation_locator).click()
        sleep(3)
        assert self.driver.title == self.driver.title

        print("Testcase-11 Activateemployment is executed")

    # Testcase-12
        sleep(3)
        self.driver.find_element(by=By.LINK_TEXT, value=locators.Employee_Locators().salarybutton_locator).click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().salary_add).click()
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().salarycomponent_locator))).send_keys(data.Employee_Data().salarycomponent)
        paygrade_entry = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().Paygrade_locator)
        paygrade_entry.click()
        sleep(2)
        selecting_paygrade = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().paygrade_selector)
        selecting_paygrade.click()
        sleep(3)
        payfrequency_entry = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().payfrequency_locator)
        payfrequency_entry.click()
        sleep(2)
        selecting_payfrequency = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().payfrequency_selector)
        selecting_payfrequency.click()
        sleep(3)
        currency_entry = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().currency_locator)
        currency_entry.click()
        sleep(2)
        selecting_currency = self.driver.find_element(By.XPATH, value=locators.Employee_Locators().currency_selector)
        selecting_currency.click()
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().amount1_locator))).send_keys(data.Employee_Data().amount1)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().DirectDepositDetailsbuttton_locator).click()
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().Accountnumber_locator))).send_keys(data.Employee_Data().Accountnumber)
        accounttype_entry = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().accounttype_locator)
        accounttype_entry.click()
        sleep(2)
        selecting_accounttype = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().accounttype_selector)
        selecting_accounttype.click()
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().routingnumber_locator))).send_keys(data.Employee_Data().routingnumber)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().amount2_locator))).send_keys(data.Employee_Data().amount2)
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().save_button7_locator).click()
        sleep(5)
        assert self.driver.title == self.driver.title
        print("Testcase-12 Salarydetails is added")

    # Testcase-13
        sleep(3)
        self.driver.find_element(by=By.LINK_TEXT, value=locators.Employee_Locators().TaxExemptionsbutton_locator).click()
        sleep(2)
        FederalIncomeTaxstatus_entry = self.driver.find_element(by=By.XPATH,value=locators.Employee_Locators().FederalIncomeTaxstatus_locator)
        FederalIncomeTaxstatus_entry.click()
        selecting_FederalIncomeTaxstatus = self.driver.find_element(by=By.XPATH,value=locators.Employee_Locators().FederalIncomeTaxstatus_selector)
        selecting_FederalIncomeTaxstatus.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().FederalIncomeTaxExemptions_locator))).send_keys(data.Employee_Data().FederalIncomeTaxExemptions)
        sleep(3)
        state_entry = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().StateIncomeTaxstate_locator)
        state_entry.click()
        selecting_state = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().StateIncomeTaxstate_selector)
        selecting_state.click()
        sleep(3)
        StateIncomeTaxstatus_entry = self.driver.find_element(by=By.XPATH,value=locators.Employee_Locators().StateIncomeTaxstatus_locator)
        StateIncomeTaxstatus_entry.click()
        selecting_StateIncomeTaxstatus = self.driver.find_element(by=By.XPATH,value=locators.Employee_Locators().StateIncomeTaxstatus_selector)
        selecting_StateIncomeTaxstatus.click()
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Employee_Locators().StateIncomeTaxExemptions_locator))).send_keys(data.Employee_Data().StateIncomeTaxExemptions)
        UnemploymentState_entry = self.driver.find_element(by=By.XPATH,value=locators.Employee_Locators().UnemploymentState_locator)
        UnemploymentState_entry.click()
        selecting_UnemploymentState = self.driver.find_element(by=By.XPATH,value=locators.Employee_Locators().UnemploymentState_selector)
        selecting_UnemploymentState.click()
        sleep(3)
        workstate_entry = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().Workstate_locator)
        workstate_entry.click()
        selecting_workstate = self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().workstate_selector)
        selecting_workstate.click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Employee_Locators().Save_button8_locator).click()
        sleep(5)
        print("Testcase-13 TaxExemptionsdetails is added")
        assert self.driver.title == self.driver.title
        self.driver.quit()