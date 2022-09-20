import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Users\\ergun\\OneDrive\\Belgeler\\chromedriver.exe')
successful = False
successfulcount = 0
while not successful:
    try:
        #amazon FR ---- Zotac Gaming GeForce RTX 3060 Ti twin edge oc
        driver.get("https://www.amazon.fr/_itm/dp/B08P3BJ9Y8")
        driver.find_element_by_id("buy-now-button").click()
        email = driver.find_element_by_name("email")
        email.send_keys("erguncan06@gmail.com")
        email.send_keys(Keys.RETURN)
        password = driver.find_element_by_name("password")
        password.send_keys("%s" % "yourpassword")
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.find_element_by_id("checkoutCurrencyMarketplace").click()
        time.sleep(1)
        driver.find_element_by_name("placeYourOrder1").click()
        time.sleep(2)
        driver.get("https://amazon.fr/gp/flex/sign-out.html?path=%2Fgp%2Fyourstore%2Fhome&signIn=1&useRedirectOnSuccess=1&action=sign-out&ref_=nav_AccountFlyout_signout")
        continue

    except:
        try:
            #amazon CO UK ---- Gigabyte GeForce RTX 3070 GAMING OC
            driver.get("https://www.amazon.co.uk/_itm/dp/B08KHL21CV")
            driver.find_element_by_id("buy-now-button").click()
            email = driver.find_element_by_name("email")
            email.send_keys("erguncan06@gmail.com")
            email.send_keys(Keys.RETURN)
            password = driver.find_element_by_name("password")
            password.send_keys("yourpassword")
            password.send_keys(Keys.RETURN)
            time.sleep(3)
            driver.find_element_by_id("checkoutCurrencyMarketplace").click()
            time.sleep(3)
            driver.find_element_by_name("placeYourOrder1").click()
            time.sleep(3)
            driver.get("https://amazon.co.uk/gp/flex/sign-out.html?path=%2Fgp%2Fyourstore%2Fhome&signIn=1&useRedirectOnSuccess=1&action=sign-out&ref_=nav_AccountFlyout_signout")
            continue
        except:
            try:
                #amazon ES ---- MSI GeForce RTX 3070 Gaming X Trio
                driver.get("https://www.amazon.es/_itm/dp/B08LNPPCWJ")
                driver.find_element_by_id("buy-now-button").click()
                email = driver.find_element_by_name("email")
                email.send_keys("erguncan06@gmail.com")
                email.send_keys(Keys.RETURN)
                password = driver.find_element_by_name("password")
                password.send_keys("yourpassword")
                password.send_keys(Keys.RETURN)
                time.sleep(3)
                driver.find_element_by_id("checkoutCurrencyMarketplace").click()
                time.sleep(1)
                driver.find_element_by_name("placeYourOrder1").click()
                driver.get("https://amazon.es/gp/flex/sign-out.html?path=%2Fgp%2Fyourstore%2Fhome&signIn=1&useRedirectOnSuccess=1&action=sign-out&ref_=nav_AccountFlyout_signout")
                continue
            except:
                try:
                    #amazon CO UK ---- MSI GeForce RTX 3080 Gaming X Trio
                    driver.get("https://www.amazon.co.uk/_itm/dp/B08HM4V2DH")
                    driver.find_element_by_id("buy-now-button").click()
                    email = driver.find_element_by_name("email")
                    email.send_keys("erguncan06@gmail.com")
                    email.send_keys(Keys.RETURN)
                    password = driver.find_element_by_name("password")
                    password.send_keys("yourpassword")
                    password.send_keys(Keys.RETURN)
                    time.sleep(3)
                    driver.find_element_by_id("checkoutCurrencyMarketplace").click()
                    time.sleep(1)
                    driver.find_element_by_name("placeYourOrder1").click()
                    driver.get("https://amazon.co.uk/gp/flex/sign-out.html?path=%2Fgp%2Fyourstore%2Fhome&signIn=1&useRedirectOnSuccess=1&action=sign-out&ref_=nav_AccountFlyout_signout")
                    continue
                except:
                        try:
                            #amazon IT ---- ASUS Dual GeForce RTX 3070 8 GB OC Edition
                            driver.get("https://www.amazon.it/_itm/dp/B08KHFZN9P")
                            driver.find_element_by_id("buy-now-button").click()
                            email = driver.find_element_by_name("email")
                            email.send_keys("erguncan06@gmail.com")
                            email.send_keys(Keys.RETURN)
                            password = driver.find_element_by_name("password")
                            password.send_keys("yourpassword")
                            password.send_keys(Keys.RETURN)
                            time.sleep(3)
                            driver.find_element_by_id("checkoutCurrencyMarketplace").click()
                            time.sleep(1)
                            driver.find_element_by_name("placeYourOrder1").click()
                            driver.get("https://amazon.it/gp/flex/sign-out.html?path=%2Fgp%2Fyourstore%2Fhome&signIn=1&useRedirectOnSuccess=1&action=sign-out&ref_=nav_AccountFlyout_signout")
                            continue
                        except:
                                try:
                                    #amazon ES ---- MSI GeForce RTX 3070 SUPRIM X
                                    driver.get("https://www.amazon.es/_itm/dp/B08P37HYZM?tag=partalertes-21&linkCode=ogi&th=1&psc=1&smid=A1AT7YVPFBWXBL")
                                    driver.find_element_by_id("buy-now-button").click()
                                    email = driver.find_element_by_name("email")
                                    email.send_keys("erguncan06@gmail.com")
                                    email.send_keys(Keys.RETURN)
                                    password = driver.find_element_by_name("password")
                                    password.send_keys("yourpassword")
                                    password.send_keys(Keys.RETURN)
                                    time.sleep(3)
                                    driver.find_element_by_id("checkoutCurrencyMarketplace").click()
                                    time.sleep(1)
                                    driver.find_element_by_name("placeYourOrder1").click()
                                    driver.get("https://amazon.es/gp/flex/sign-out.html?path=%2Fgp%2Fyourstore%2Fhome&signIn=1&useRedirectOnSuccess=1&action=sign-out&ref_=nav_AccountFlyout_signout")
                                    continue
                                except:
                                    try:
                                        #amazon FR ---- Gigabyte GeForce RTX 3070 Vision OC
                                        driver.get("https://www.amazon.fr/_itm/dp/B08LNWPYRS?tag=partalertfr-21&linkCode=ogi&th=1&psc=1&smid=A1X6FK5RDHNB96")
                                        driver.find_element_by_id("buy-now-button").click()
                                        email = driver.find_element_by_name("email")
                                        email.send_keys("erguncan06@gmail.com")
                                        email.send_keys(Keys.RETURN)
                                        password = driver.find_element_by_name("password")
                                        password.send_keys("yourpassword")
                                        password.send_keys(Keys.RETURN)
                                        time.sleep(3)
                                        driver.find_element_by_id("checkoutCurrencyMarketplace").click()
                                        time.sleep(1)
                                        driver.find_element_by_name("placeYourOrder1").click()
                                        driver.get("https://amazon.fr/gp/flex/sign-out.html?path=%2Fgp%2Fyourstore%2Fhome&signIn=1&useRedirectOnSuccess=1&action=sign-out&ref_=nav_AccountFlyout_signout")
                                        continue
                                    except:
                                        try:
                                            #amazon IT ---- Gigabyte AORUS GeForce RTX 3060 Ti
                                            driver.get("https://www.amazon.it/_itm/dp/B08NW5CGXT?tag=partalertit-21&linkCode=ogi&th=1&psc=1&smid=A11IL2PNWYJU7H")
                                            driver.find_element_by_id("buy-now-button").click()
                                            email = driver.find_element_by_name("email")
                                            email.send_keys("erguncan06@gmail.com")
                                            email.send_keys(Keys.RETURN)
                                            password = driver.find_element_by_name("password")
                                            password.send_keys("yourpassword")
                                            password.send_keys(Keys.RETURN)
                                            time.sleep(3)
                                            driver.find_element_by_id("checkoutCurrencyMarketplace").click()
                                            time.sleep(1)
                                            driver.find_element_by_name("placeYourOrder1").click()
                                            driver.get("https://amazon.it/gp/flex/sign-out.html?path=%2Fgp%2Fyourstore%2Fhome&signIn=1&useRedirectOnSuccess=1&action=sign-out&ref_=nav_AccountFlyout_signout")
                                            continue
                                        except:
                                            try:
                                                #amazon DE ---- ASUS ROG Strix NVIDIA GeForce RTX 3080 OC
                                                driver.get("https://www.amazon.de/_itm/dp/B08J6F174Z?tag=partalertde-21&linkCode=ogi&th=1&psc=1&smid=A3JWKAKR8XB7XF")
                                                driver.find_element_by_id("buy-now-button").click()
                                                email = driver.find_element_by_name("email")
                                                email.send_keys("erguncan06@gmail.com")
                                                email.send_keys(Keys.RETURN)
                                                password = driver.find_element_by_name("password")
                                                password.send_keys("yourpassword")
                                                password.send_keys(Keys.RETURN)
                                                time.sleep(3)
                                                time.sleep(1)
                                                driver.find_element_by_name("placeYourOrder1").click()
                                                driver.get("https://amazon.de/gp/flex/sign-out.html?path=%2Fgp%2Fyourstore%2Fhome&signIn=1&useRedirectOnSuccess=1&action=sign-out&ref_=nav_AccountFlyout_signout")
                                                continue
                                            except:
                                                continue