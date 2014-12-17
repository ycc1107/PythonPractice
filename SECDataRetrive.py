__author__ = 'cheng'
from bs4 import BeautifulSoup
import urllib2
import csv

def processAnswer(soup):
    counter,output,data = 0,[],[]
    spanClass,imgAlt = "PrintHistRed","selected"
    for item in soup.find_all(["img","span"]):
        tempOutput = item.get_text(strip=True)
        if "class" in item.attrs and spanClass in item["class"] and len(tempOutput):
            output.append(tempOutput)
        elif "alt" in item.attrs and imgAlt in item["alt"]:
            counter += 1
            if not len(tempOutput):
                if not ("not" in item["alt"]):
                    tempOutput = "Yes" if counter%2 == 1 else "No"
                else:
                    continue
            elif "not" in item["alt"]:
                continue
            output.append(tempOutput)
    for index in range(len(output)):
        data.append([index+1,output[index]])
    return data

def getSoupContain():
    link = "http://www.adviserinfo.sec.gov/iapd/content/" \
           "viewform/adv/sections/" \
           "iapd_AdvIdentifyingInfoSection.aspx?ORG_PK=107715&RGLTR_PK=50000&STATE_CD=&" \
           "FLNG_PK=003E31180008017703BE8EA0051BBD79056C8CC0"
    htemlContent = urllib2.urlopen(link)
    soup = BeautifulSoup(htemlContent)
    return soup

def dataWrite(data):
    with open("output.csv","w") as f:
        fileWriter = csv.writer(f, delimiter=',')
        fileWriter.writerows(data)

def main():
    soup = getSoupContain()
    data = processAnswer(soup)
    dataWrite(data)


if __name__ == "__main__": main()
