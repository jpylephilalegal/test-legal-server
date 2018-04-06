# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
import os
import re
import sys
import csv

counts = dict(first=1, second=2, third=3, fourth=4, fifth=5, sixth=6, seventh=7, eighth=8, ninth=9, tenth=10)

@step('I open the URL "?([^"]+)"?')
def visit_url(step, url):
    world.browser.get(url)
    world.browser.wait_for_it()

@step('I log in to "?([^ "]+)"? as "?([^ "]+)"?')
def login(step, server, username):
    world.da_path = 'https://' + re.sub(r'/+$', r'', server)
    if server not in world.passwords:
        sys.exit("There are no passwords for " + server + " in " + world.password_file)
    if username not in world.passwords[server]:
        sys.exit("There are no passwords for " + username + " for " + server + " in " + world.password_file)
    password = world.passwords[server][username]
    world.browser.get(world.da_path)
    world.browser.wait_for_it()
    elem = world.browser.find_element_by_id(world.browser.find_element_by_xpath('//label[text()="Username"]').get_attribute("for"))
    elem.clear()
    elem.send_keys(username)
    elem = world.browser.find_element_by_id(world.browser.find_element_by_xpath('//label[text()="Password"]').get_attribute("for"))
    elem.clear()
    elem.send_keys(password)
    world.browser.find_element_by_xpath('//input[@type="submit" and @value="Login »"]').click()
    world.browser.wait_for_it()

@step('I open case ID ([0-9]+E*-[0-9]+)')
def open_case_id(step, caseid):
    world.browser.execute_script('jQuery("a:contains(\'Case ID\')").click()')
    world.browser.switch_to.frame(world.browser.find_element_by_id("fancybox-frame"))
    elem = world.browser.find_element_by_id(world.browser.find_element_by_xpath('//label[text()="Case ID"]').get_attribute("for"))
    elem.clear()
    elem.send_keys(caseid)
    world.browser.find_element_by_xpath('//input[@type="submit" and @value="Continue »"]').click()
    world.browser.wait_for_it()

@step('I log out')
def log_out(step):
    world.browser.find_element_by_xpath('//li[@class="logout"]').click()
    world.browser.wait_for_it()
    
@step('I click the menu link "([^"]*)"')
def click_menu_link(step, value):
    world.browser.execute_script('window.location.href = jQuery("a:contains(\'' + value + '\')").attr("href");')
    world.browser.wait_for_it()

@step('I upload the file "([^"]*)"')
def do_upload(step, value):
    elem = world.browser.find_element_by_xpath("//input[@type='file']")
    elem.clear()
    elem.send_keys(os.path.join(os.getcwd(), value))

@step('I set the text area to "([^"]*)"')
def set_text_area(step, value):
    elem = world.browser.find_element_by_xpath("//textarea")
    elem.clear()
    elem.send_keys(value)

@step('If I see it, I will click the link "([^"]+)"')
def click_link_if_exists(step, link_name):
    try:
        world.browser.find_element_by_xpath('//a[text()="' + link_name + '"]').click()
        world.browser.wait_for_it()
    except:
        pass

@step('I wait forever')
def wait_forever(step):
    time.sleep(999999999)
    world.browser.wait_for_it()

@step('I click the button "([^"]+)"')
def click_button(step, button_name):
    try:
        elem = world.browser.find_element_by_xpath('//button[text()="' + button_name + '"]')
    except:
        try:
            elem = world.browser.find_element_by_xpath('//input[@type = "submit" and @value = "' + button_name + '"]')
        except:
            elem = world.browser.find_element_by_xpath('//input[@type = "button" and @value = "' + button_name + '"]')
    elem.click()
    world.browser.wait_for_it()

@step('I click the labels "([^"]+)"')
def click_labels(step, label_name):
    for elem in world.browser.find_elements_by_xpath('//label[text()="' + label_name + '"]'):
        elem.click()
    world.browser.wait_for_it()

@step('I click the link "([^"]+)"')
def click_link(step, link_name):
    world.browser.find_element_by_xpath('//a[text()="' + link_name + '"]').click()
    world.browser.wait_for_it()

@step('I click the second link "([^"]+)"')
def click_second_link(step, link_name):
    world.browser.find_element_by_xpath('(//a[text()="' + link_name + '"])[2]').click()
    world.browser.wait_for_it()

@step('I should see the phrase "([^"]+)"')
def see_phrase(step, phrase):
    assert world.browser.text_present(phrase)

@step('I should not see the phrase "([^"]+)"')
def not_see_phrase(step, phrase):
    assert not world.browser.text_present(phrase)

@step('I set input field "([^"]+)" to "([^"]*)"')
def set_field_by_name(step, name, value):
    elem = world.browser.find_element_by_name(name)
    try:
        elem.clear()
    except:
        pass
    elem.send_keys(value)
    
@step('I set "([^"]+)" to "([^"]*)"')
def set_field(step, label, value):
    found = False
    try:
        for lab in world.browser.find_elements_by_xpath('//label[text()="' + label + '"]'):
            if lab.is_displayed():
                elem = world.browser.find_element_by_id(lab.get_attribute("for"))
                found = True
                break
    except:
        pass
    if not found:
        for inp in world.browser.find_elements_by_xpath('//input[@placeholder="' + label + '"]'):
            if inp.is_displayed():
                elem = inp
                found = True
                break
    assert found
    try:
        elem.clear()
    except:
        pass
    elem.send_keys(value)

@step('I set the (first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth) pulldown to "([^"]+)"')
def nth_select(step, ordinal, value):
    number = str(counts[ordinal])
    elem = world.browser.find_element_by_xpath('(//select)[' + number + ']')
    found = False
    for option in elem.find_elements_by_tag_name('option'):
        if option.text == value:
            option.click()
            found = True
            break
    assert found

@step('I set the (first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth) text box to "([^"]+)"')
def nth_select(step, ordinal, value):
    number = str(counts[ordinal])
    elem = world.browser.find_element_by_xpath('(//input[@type!="hidden" and @type!="button"])[' + number + ']')
    try:
        elem.clear()
    except:
        pass
    elem.send_keys(value)

@step('I set the (first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth) text area to "([^"]+)"')
def nth_select(step, ordinal, value):
    number = str(counts[ordinal])
    elem = world.browser.find_element_by_xpath('(//textarea)[' + number + ']')
    try:
        elem.clear()
    except:
        pass
    elem.send_keys(value)

@step('I click the continue button')
def submit_page(step):
    elem = world.browser.find_element_by_xpath('//input[@type="submit" and @value="Continue »"]')
    world.browser.execute_script("return arguments[0].click();", elem)
    world.browser.wait_for_it()

@step('I click "([^"]+)" under "([^"]+)"')
def legend_click(step, value, legend):
    fieldset = world.browser.find_element_by_xpath('//span[text()="' + legend + '"]/ancestor::fieldset')
    found = False
    for label in fieldset.find_elements_by_tag_name('label'):
        if label.text == value:
            label.click()
            found = True
            break
    assert found        

@step('I select "([^"]+)" as the "([^"]+)"')
def select_option(step, value, label):
    elem = world.browser.find_element_by_id(world.browser.find_element_by_xpath('//label[text()="' + label + '"]').get_attribute("for"))
    found = False
    for option in elem.find_elements_by_tag_name('option'):
        if option.text == value:
            option.click()
            found = True
            break
    assert found

@step('I choose "([^"]+)"')
def select_option_from_only_select(step, value):
    elem = world.browser.find_element_by_xpath('//select')
    found = False
    for option in elem.find_elements_by_tag_name('option'):
        if option.text == value:
            option.click()
            found = True
            break
    assert found

@step('I wait (\d+) seconds?')
def wait_seconds(step, seconds):
    time.sleep(float(seconds))
    world.browser.wait_for_it()

@step('I should see that "([^"]+)" is "([^"]+)"')
def value_of_field(step, label, value):
    try:
        elem = world.browser.find_element_by_id(world.browser.find_element_by_xpath('//label[text()="' + label + '"]').get_attribute("for"))
    except:
        elem = world.browser.find_element_by_id(world.browser.find_element_by_xpath('//a[text()="' + label + '"]/ancestor::label').get_attribute("for"))
    if elem.tag_name in ('span', 'a', 'button', 'div'):
        assert elem.text == value
    elif elem.tag_name in ('select'):
        select = Select(elem)
        selected_option = select.first_selected_option
        assert selected_option.text == value
    else:
        assert elem.get_attribute("value") == value

@step('I set the text box to "([^"]*)"')
def set_text_box(step, value):
    elem = world.browser.find_element_by_xpath("//input[contains(@alt, 'Input box')]")
    try:
        elem.clear()
    except:
        pass
    elem.send_keys(value)

@step('I click the "([^"]+)" option under "([^"]+)"')
def set_mc_option_under(step, option, label):
    div = world.browser.find_element_by_xpath('//label[text()="' + label + '"]/following-sibling::div')
    span = div.find_element_by_xpath('.//span[text()="' + option + '"]')
    option_label = span.find_element_by_xpath("..")
    option_label.click()
        
@step('I click the "([^"]+)" option')
def set_mc_option(step, choice):
    span_elem = world.browser.find_element_by_xpath('//span[text()="' + choice + '"]')
    label_elem = span_elem.find_element_by_xpath("..")
    label_elem.click()

@step('I should see "([^"]+)" as the title of the page')
def title_of_page(step, title):
    assert world.browser.title == title

@step('I should see "([^"]+)" as the URL of the page')
def url_of_page(step, url):
    assert world.browser.current_url == url

@step('I exit by clicking "([^"]+)"')
def exit_button(step, button_name):
    world.browser.find_element_by_xpath('//button[text()="' + button_name + '"]').click()
    time.sleep(1.0)

@step('I run the template "([^"]+)"')
def run_template(step, templatefilename):
    templatefile = os.path.join('templates', templatefilename)
    if not os.path.isfile(templatefile):
        sys.exit("Template file " + datafilename + " not found")
    with open(templatefile, 'r') as template_fp:
        template_lines = template_fp.readlines()
    for line in template_lines:
        command = line.strip()
        if command:
            step.given(command)

@step('I run "([^"]+)" using "([^"]+)"')
def template_apply(step, templatefilename, datafilename):
    datafile = os.path.join('data', datafilename)
    if not os.path.isfile(datafile):
        sys.exit("Data file " + datafilename + " not found")
    templatefile = os.path.join('templates', templatefilename)
    if not os.path.isfile(templatefile):
        sys.exit("Template file " + datafilename + " not found")
    with open(templatefile, 'r') as template_fp:
        template_lines = template_fp.readlines()
    with open(datafile, 'rb') as data_fp:
        for row in csv.DictReader(data_fp):
            for line in template_lines:
                command = line.format(**row).strip()
                if command:
                    step.given(command)
                    
    
