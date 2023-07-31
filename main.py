from parsel import Selector
import requests
import json


HTMLFile = open("./bcv.html", "r")
index = HTMLFile.read()

Web = requests.get('https://www.bcv.org.ve/')
index = Web.text

#html_selector = Selector(text=index)
#usd = html_selector.xpath('//div[@id="dolar"]/div/div/div/strong/text()').get()


usd = usd.strip()
usd = float(usd.replace(',', '.'))


print(usd)

#save to json file
aList = [{"USD":usd}]
jsonString = json.dumps(aList)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

