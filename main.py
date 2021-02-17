# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python



# Resources
btnum0 = driver.find_element_by_id("com.android.calculator2:id/digit_0")
btnum1 = driver.find_element_by_id("com.android.calculator2:id/digit_1")
btnum2 = driver.find_element_by_id("com.android.calculator2:id/digit_2")
btnum3 = driver.find_element_by_id("com.android.calculator2:id/digit_3")
btnum4 = driver.find_element_by_id("com.android.calculator2:id/digit_4")
btnum5 = driver.find_element_by_id("com.android.calculator2:id/digit_5")
btnum6 = driver.find_element_by_id("com.android.calculator2:id/digit_6")
btnum7 = driver.find_element_by_id("com.android.calculator2:id/digit_7")
btnum8 = driver.find_element_by_id("com.android.calculator2:id/digit_8")
btnum9 = driver.find_element_by_id("com.android.calculator2:id/digit_9")

btPlus = driver.find_element_by_accessibility_id("plus")
btEquals = driver.find_element_by_accessibility_id("equals")

# Actions
btnum1.click()
btPlus.click()
btnum5.click()
btPlus.click()
btnum9.click()
btEquals.click()

driver.quit()