# -*- coding: utf-8 -*-
import os
import re
import json
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# output dir. => {project path}/output
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
# calls data json file path. => {project path}/output/calls.json
calls_json_f = "{}/calls.json".format(output_dir)
# puts data json file path. => {project path}/output/puts.json
puts_json_f = "{}/puts.json".format(output_dir)

class YahooSpider():

    def __init__(self):
        self.driver = None

    def set_driver(self):
        try:
            chrome_option = webdriver.ChromeOptions()
            chrome_option.add_argument('--no-sandbox')
            chrome_option.add_argument('--disable-dev-shm-usage')
            chrome_option.add_argument('--ignore-certificate-errors')
            chrome_option.add_argument("--disable-blink-features=AutomationControlled")
            chrome_option.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                'Chrome/80.0.3987.132 Safari/537.36')
            chrome_option.add_argument('--headless')

            driver = webdriver.Chrome('/usr/local/bin/chromedriver', options = chrome_option)
            return driver
        except:
            print(traceback.print_exc())

    # main function
    def start(self):
        try:
            self.driver = self.set_driver()
            self.driver.get("https://finance.yahoo.com/quote/SNOW/options?p=SNOW&guccounter=1")
            WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_xpath("//div[@id='app']"))

            res_content = self.driver.page_source
            res_content = res_content.split("root.App.main =", 1)[1].strip().split("(this));", 1)[0].rsplit(";", 1)[0]

            # get full json data from page source
            full_data = json.loads(res_content)

            # get displayed calls data from full data
            calls_data = full_data["context"]["dispatcher"]["stores"]["OptionContractsStore"]["contracts"]["displayed"]["calls"]["contracts"]

            # get displayed puts data from full data
            puts_data = full_data["context"]["dispatcher"]["stores"]["OptionContractsStore"]["contracts"]["displayed"]["puts"]["contracts"]

            baseItem = {
                "Contract Name": "",
                "Last Trade Date": "",
                "Strike": "",
                "Last Price": "",
                "Bid": "",
                "Ask": "",
                "Change": "",
                "percentChange": "",
                "Volume": "",
                "OpenInterest": "",
                "ImpliedVolatility": "",
            }

            calls_final_data = list()

            for item in calls_data:
                item_result = baseItem.copy()
                try:
                    item_result["Contract Name"] = item["contractSymbol"]
                except:
                    pass
                try:
                    item_result["Last Trade Date"] = item["lastTradeDate"]["longFmt"]
                except:
                    pass
                try:
                    item_result["Strike"] = item["strike"]["fmt"]
                except:
                    pass
                try:
                    item_result["Last Price"] = item["lastPrice"]["fmt"]
                except:
                    pass
                try:
                    item_result["Bid"] = item["bid"]["fmt"]
                except:
                    pass
                try:
                    item_result["Ask"] = item["ask"]["fmt"]
                except:
                    pass
                try:
                    item_result["Change"] = item["change"]["fmt"]
                except:
                    pass
                try:
                    item_result["percentChange"] = item["percentChange"]["fmt"]
                except:
                    pass
                try:
                    item_result["Volume"] = item["volume"]["fmt"]
                except:
                    pass
                try:
                    item_result["OpenInterest"] = item["openInterest"]["fmt"]
                except:
                    pass
                try:
                    item_result["ImpliedVolatility"] = item["impliedVolatility"]["fmt"]
                except:
                    pass
                
                calls_final_data.append(item_result)

            # save calls data as json file
            with open(calls_json_f, "w") as calls_json:
                calls_json.write(json.dumps(calls_final_data, indent=2))

            puts_final_data = list()
            for item in puts_data:
                item_result = baseItem.copy()
                try:
                    item_result["Contract Name"] = item["contractSymbol"]
                except:
                    pass
                try:
                    item_result["Last Trade Date"] = item["lastTradeDate"]["longFmt"]
                except:
                    pass
                try:
                    item_result["Strike"] = item["strike"]["fmt"]
                except:
                    pass
                try:
                    item_result["Last Price"] = item["lastPrice"]["fmt"]
                except:
                    pass
                try:
                    item_result["Bid"] = item["bid"]["fmt"]
                except:
                    pass
                try:
                    item_result["Ask"] = item["ask"]["fmt"]
                except:
                    pass
                try:
                    item_result["Change"] = item["change"]["fmt"]
                except:
                    pass
                try:
                    item_result["percentChange"] = item["percentChange"]["fmt"]
                except:
                    pass
                try:
                    item_result["Volume"] = item["volume"]["fmt"]
                except:
                    pass
                try:
                    item_result["OpenInterest"] = item["openInterest"]["fmt"]
                except:
                    pass
                try:
                    item_result["ImpliedVolatility"] = item["impliedVolatility"]["fmt"]
                except:
                    pass
                
                puts_final_data.append(item_result)
            
            # save puts data as json file
            with open(puts_json_f, "w") as puts_json:
                puts_json.write(json.dumps(puts_final_data, indent=2))

        except:
            time.sleep(60)
            print(traceback.print_exc())
        finally:
            if self.driver is not None:
                self.driver.quit()
                self.driver = None

if __name__ == "__main__":

    yahooSpider = YahooSpider()
    yahooSpider.start()
    
    
