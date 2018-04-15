# -*- coding: utf-8 -*-
import scrapy
from usac.items import UsacItem

class UsacbasicSpider(scrapy.Spider):
    name = "usacbasic"
    allowed_domains = ["data.usac.org"]
    rotate_user_agent = True

    def start_requests(self):
        headers = {
                    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    'accept-encoding': "gzip, deflate, br",
                    'accept-language': "en-US,en;q=0.8",
                    'cache-control': "no-cache",
                    'content-type': "application/x-www-form-urlencoded",
                    'connection': "keep-alive",
                    'origin': "https://data.usac.org",
                    'host': "data.usac.org",
                    'referer': "https://data.usac.org/publicreports/FRN/Status/FundYear",
                    }
        url = "https://data.usac.org/publicreports/FRN/Status/FundYear"
        yield scrapy.Request(url=url, headers=headers,callback=self.parse_list)

    def parse_list(self,response):
        headers = {
                    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    'accept-encoding': "gzip, deflate, br",
                    'accept-language': "en-US,en;q=0.8",
                    'cache-control': "no-cache",
                    'content-type': "application/x-www-form-urlencoded",
                    'connection': "keep-alive",
                    'origin': "https://data.usac.org",
                    'host': "data.usac.org",
                    'referer': "https://data.usac.org/publicreports/FRN/Status/FundYear",
                    }
        count=0
        token = response.xpath("//input[@name='__RequestVerificationToken']/@value").extract_first() #Request token from the server !important
        for everystate in response.xpath("//select[@id='SelectedStateId']/option/@value").extract():# get value for All state
            count=count+1
            if count==1:#skip value for 'Select Field'
                continue
            payload = "__RequestVerificationToken="+str(token)+"" \
                      "&SelectedFundingYear=2018&SelectedStateId=" + str(everystate) + "&BilledEntityNumber=&CRN=&SPIN=&frnServiceType%5B0%5D.Id=1&frnServiceType%5B0%5D.ServiceName=Voice" \
                      "&frnServiceType%5B0%5D.IsSelected=true&frnServiceType%5B0%5D.IsSelected=false&frnServiceType%5B1%5D.Id=2&frnServiceType%5B1%5D.ServiceName=Data+Transmission+and" \
                      "%2For+Internet+Access&frnServiceType%5B1%5D.IsSelected=true&frnServiceType%5B1%5D.IsSelected=false&frnServiceType%5B2%5D.Id=3" \
                      "&frnServiceType%5B2%5D.ServiceName=Basic+Maintenance+of+Internal+Connections&frnServiceType%5B2%5D.IsSelected=true&frnServiceType%5B2%5D.IsSelected=false" \
                      "&frnServiceType%5B3%5D.Id=4&frnServiceType%5B3%5D.ServiceName=Internal+Connections&frnServiceType%5B3%5D.IsSelected=true&frnServiceType%5B3%5D.IsSelected=false" \
                      "&frnServiceType%5B4%5D.Id=5&frnServiceType%5B4%5D.ServiceName=Managed+Internal+Broadband+Services&frnServiceType%5B4%5D.IsSelected=true" \
                      "&frnServiceType%5B4%5D.IsSelected=false&frnEntityType%5B0%5D.Id=1&frnEntityType%5B0%5D.EntityName=School&frnEntityType%5B0%5D.IsSelected=true" \
                      "&frnEntityType%5B0%5D.IsSelected=false&frnEntityType%5B1%5D.Id=2&frnEntityType%5B1%5D.EntityName=School+District&frnEntityType%5B1%5D.IsSelected=true" \
                      "&frnEntityType%5B1%5D.IsSelected=false&frnEntityType%5B2%5D.Id=3&frnEntityType%5B2%5D.EntityName=Library&frnEntityType%5B2%5D.IsSelected=true" \
                      "&frnEntityType%5B2%5D.IsSelected=false&frnEntityType%5B3%5D.Id=4&frnEntityType%5B3%5D.EntityName=Library+System&frnEntityType%5B3%5D.IsSelected=true" \
                      "&frnEntityType%5B3%5D.IsSelected=false&frnEntityType%5B4%5D.Id=5&frnEntityType%5B4%5D.EntityName=Consortium&frnEntityType%5B4%5D.IsSelected=true" \
                      "&frnEntityType%5B4%5D.IsSelected=false&ApplicationNumber=&FRNNo=&WaveNumber=&AppealWaveNumber=&FormatOption=XML&hasDataPoint=true&hasDataPoint=false" \
                      "&selectAllDataPoint=true&selectAllDataPoint=false&frnSelectAllDataPointType%5B0%5D.ID=1&frnSelectAllDataPointType%5B0%5D.chkSelectedDataPoint=false" \
                      "&frnSelectAllDataPointType%5B1%5D.ID=2&frnSelectAllDataPointType%5B1%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B1%5D.chkSelectedDataPoint=false" \
                      "&frnSelectAllDataPointType%5B2%5D.ID=3&frnSelectAllDataPointType%5B2%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B2%5D.chkSelectedDataPoint=false" \
                      "&frnSelectAllDataPointType%5B3%5D.ID=4&frnSelectAllDataPointType%5B3%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B4%5D.ID=5" \
                      "&frnSelectAllDataPointType%5B4%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B4%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B5%5D.ID=6" \
                      "&frnSelectAllDataPointType%5B5%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B5%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B6%5D.ID=7" \
                      "&frnSelectAllDataPointType%5B6%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B6%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B7%5D.ID=8" \
                      "&frnSelectAllDataPointType%5B7%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B7%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B8%5D.ID=9" \
                      "&frnSelectAllDataPointType%5B8%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B8%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B9%5D.ID=10" \
                      "&frnSelectAllDataPointType%5B9%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B9%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B10%5D.ID=11" \
                      "&frnSelectAllDataPointType%5B10%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B10%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B11%5D.ID=12" \
                      "&frnSelectAllDataPointType%5B11%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B11%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B12%5D.ID=13" \
                      "&frnSelectAllDataPointType%5B12%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B12%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B13%5D.ID=14" \
                      "&frnSelectAllDataPointType%5B13%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B13%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B14%5D.ID=15" \
                      "&frnSelectAllDataPointType%5B14%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B14%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B15%5D.ID=16" \
                      "&frnSelectAllDataPointType%5B15%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B15%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B16%5D.ID=17" \
                      "&frnSelectAllDataPointType%5B16%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B16%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B17%5D.ID=18" \
                      "&frnSelectAllDataPointType%5B17%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B17%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B18%5D.ID=19" \
                      "&frnSelectAllDataPointType%5B18%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B18%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B19%5D.ID=20" \
                      "&frnSelectAllDataPointType%5B19%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B19%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B20%5D.ID=21" \
                      "&frnSelectAllDataPointType%5B20%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B20%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B21%5D.ID=22" \
                      "&frnSelectAllDataPointType%5B21%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B21%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B22%5D.ID=23" \
                      "&frnSelectAllDataPointType%5B22%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B22%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B23%5D.ID=24" \
                      "&frnSelectAllDataPointType%5B23%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B23%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B24%5D.ID=25" \
                      "&frnSelectAllDataPointType%5B24%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B24%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B25%5D.ID=26" \
                      "&frnSelectAllDataPointType%5B25%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B25%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B26%5D.ID=27" \
                      "&frnSelectAllDataPointType%5B26%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B26%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B27%5D.ID=28" \
                      "&frnSelectAllDataPointType%5B27%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B27%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B28%5D.ID=29" \
                      "&frnSelectAllDataPointType%5B28%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B28%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B29%5D.ID=30" \
                      "&frnSelectAllDataPointType%5B29%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B29%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B30%5D.ID=31" \
                      "&frnSelectAllDataPointType%5B30%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B30%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B31%5D.ID=32" \
                      "&frnSelectAllDataPointType%5B31%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B31%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B32%5D.ID=33" \
                      "&frnSelectAllDataPointType%5B32%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B32%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B33%5D.ID=34" \
                      "&frnSelectAllDataPointType%5B33%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B33%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B34%5D.ID=35" \
                      "&frnSelectAllDataPointType%5B34%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B34%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B35%5D.ID=36" \
                      "&frnSelectAllDataPointType%5B35%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B35%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B36%5D.ID=37" \
                      "&frnSelectAllDataPointType%5B36%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B36%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B37%5D.ID=38" \
                      "&frnSelectAllDataPointType%5B37%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B37%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B38%5D.ID=39" \
                      "&frnSelectAllDataPointType%5B38%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B38%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B39%5D.ID=40" \
                      "&frnSelectAllDataPointType%5B39%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B39%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B40%5D.ID=41" \
                      "&frnSelectAllDataPointType%5B40%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B40%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B42%5D.ID=43" \
                      "&frnSelectAllDataPointType%5B42%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B42%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B44%5D.ID=45" \
                      "&frnSelectAllDataPointType%5B44%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B44%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B46%5D.ID=47" \
                      "&frnSelectAllDataPointType%5B46%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B46%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B48%5D.ID=49" \
                      "&frnSelectAllDataPointType%5B48%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B48%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B41%5D.ID=42" \
                      "&frnSelectAllDataPointType%5B41%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B41%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B43%5D.ID=44" \
                      "&frnSelectAllDataPointType%5B43%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B43%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B45%5D.ID=46" \
                      "&frnSelectAllDataPointType%5B45%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B45%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B47%5D.ID=48" \
                      "&frnSelectAllDataPointType%5B47%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B47%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B49%5D.ID=50" \
                      "&frnSelectAllDataPointType%5B49%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B49%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B50%5D.ID=51" \
                      "&frnSelectAllDataPointType%5B50%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B50%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B52%5D.ID=53" \
                      "&frnSelectAllDataPointType%5B52%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B52%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B54%5D.ID=55" \
                      "&frnSelectAllDataPointType%5B54%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B54%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B51%5D.ID=52" \
                      "&frnSelectAllDataPointType%5B51%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B51%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B53%5D.ID=54" \
                      "&frnSelectAllDataPointType%5B53%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B53%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B55%5D.ID=56" \
                      "&frnSelectAllDataPointType%5B55%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B55%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B56%5D.ID=57" \
                      "&frnSelectAllDataPointType%5B56%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B56%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B58%5D.ID=59" \
                      "&frnSelectAllDataPointType%5B58%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B58%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B60%5D.ID=61" \
                      "&frnSelectAllDataPointType%5B60%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B60%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B57%5D.ID=58" \
                      "&frnSelectAllDataPointType%5B57%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B57%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B59%5D.ID=60" \
                      "&frnSelectAllDataPointType%5B59%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B59%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B61%5D.ID=62" \
                      "&frnSelectAllDataPointType%5B61%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B61%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B62%5D.ID=63" \
                      "&frnSelectAllDataPointType%5B62%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B62%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B64%5D.ID=65" \
                      "&frnSelectAllDataPointType%5B64%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B64%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B63%5D.ID=64" \
                      "&frnSelectAllDataPointType%5B63%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B63%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B65%5D.ID=66" \
                      "&frnSelectAllDataPointType%5B65%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B65%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B66%5D.ID=67" \
                      "&frnSelectAllDataPointType%5B66%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B66%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B67%5D.ID=68" \
                      "&frnSelectAllDataPointType%5B67%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B67%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B68%5D.ID=69" \
                      "&frnSelectAllDataPointType%5B68%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B68%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B69%5D.ID=70" \
                      "&frnSelectAllDataPointType%5B69%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B69%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B70%5D.ID=71" \
                      "&frnSelectAllDataPointType%5B70%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B70%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B71%5D.ID=72" \
                      "&frnSelectAllDataPointType%5B71%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B71%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B72%5D.ID=73" \
                      "&frnSelectAllDataPointType%5B72%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B72%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B73%5D.ID=74" \
                      "&frnSelectAllDataPointType%5B73%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B73%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B74%5D.ID=75" \
                      "&frnSelectAllDataPointType%5B74%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B74%5D.chkSelectedDataPoint=false&frnSelectAllDataPointType%5B75%5D.ID=76" \
                      "&frnSelectAllDataPointType%5B75%5D.chkSelectedDataPoint=true&frnSelectAllDataPointType%5B75%5D.chkSelectedDataPoint=false&CreateReport=Build+Data+File"
            url = "https://data.usac.org/publicreports/FRN/Status/FundYear"
            yield scrapy.Request(url=url, method = 'POST',headers=headers, body=payload,callback=self.parse)#request data file in XML document


    def parse(self, response):
        item = UsacItem()
        for everyreport in response.xpath("//NewDataSet/FRNDetailedReport"):
            if everyreport.xpath(".//FRNStatus/text()").extract_first() == "Denied":# Change this string to choose FRNstatus. Denied or Cancelled or Pending or Funded.
                #Collect all item field in data file
                item['FRN'] = everyreport.xpath(".//FRN/text()").extract_first()
                item['FRNNickname'] = everyreport.xpath(".//FRNNickname/text()").extract_first()
                item['FRNStatus'] = everyreport.xpath(".//FRNStatus/text()").extract_first()
                item['FourSeventyOneApplicationNumber'] = everyreport.xpath(".//FourSeventyOneApplicationNumber/text()").extract_first()
                item['FourSeventyOneNickName'] = everyreport.xpath(".//FourSeventyOneNickName/text()").extract_first()
                item['FourSeventyOneApplicationStatus'] = everyreport.xpath(".//FourSeventyOneApplicationStatus/text()").extract_first()
                item['FourSeventyOneReviewStatus'] = everyreport.xpath(".//FourSeventyOneReviewStatus/text()").extract_first()
                item['EstablishingFCCFormFourSeventyNumber'] = everyreport.xpath(".//EstablishingFCCFormFourSeventyNumber/text()").extract_first()
                item['EstablishingFCCFormFourSeventyStatus'] = everyreport.xpath(".//EstablishingFCCFormFourSeventyStatus/text()").extract_first()
                item['UserEnteredEstablishingFCCFormFourSeventyNumber'] = everyreport.xpath(".//UserEnteredEstablishingFCCFormFourSeventyNumber/text()").extract_first()
                item['BEN'] = everyreport.xpath(".//BEN/text()").extract_first()
                item['BilledEntityName'] = everyreport.xpath(".//BilledEntityName/text()").extract_first()
                item['ApplicantType'] = everyreport.xpath(".//ApplicantType/text()").extract_first()
                item['ApplicantStreetAddressOne'] = everyreport.xpath(".//ApplicantStreetAddressOne/text()").extract_first()
                item['ApplicantStreetAddressTwo'] = everyreport.xpath(".//ApplicantStreetAddressTwo/text()").extract_first()
                item['ApplicantCity'] = everyreport.xpath(".//ApplicantCity/text()").extract_first()
                item['ApplicantState'] = everyreport.xpath(".//ApplicantState/text()").extract_first()
                item['ApplicantZipCode'] = everyreport.xpath(".//ApplicantZipCode/text()").extract_first()
                item['FourSeventyOneContactName'] = everyreport.xpath(".//FourSeventyOneContactName/text()").extract_first()
                item['FourSeventyOneContactEmail'] = everyreport.xpath(".//FourSeventyOneContactEmail/text()").extract_first()
                item['BENUrbanRuralStatus'] = everyreport.xpath(".//BENUrbanRuralStatus/text()").extract_first()
                item['BENAccountAdministrator'] = everyreport.xpath(".//BENAccountAdministrator/text()").extract_first()
                item['BENAccountAdministratorEmail'] = everyreport.xpath(".//BENAccountAdministratorEmail/text()").extract_first()
                item['StateLEACode'] = everyreport.xpath(".//StateLEACode/text()").extract_first()
                item['StateSchoolCode'] = everyreport.xpath(".//StateSchoolCode/text()").extract_first()
                item['LibraryLocaleCode'] = everyreport.xpath(".//LibraryLocaleCode/text()").extract_first()
                item['LibraryFSCSKey'] = everyreport.xpath(".//LibraryFSCSKey/text()").extract_first()
                item['LibrarySquareFootage'] = everyreport.xpath(".//LibrarySquareFootage/text()").extract_first()
                item['LibraryFSCSSEQ'] = everyreport.xpath(".//LibraryFSCSSEQ/text()").extract_first()
                item['FourSeventyOneConsultantRegistrationNumber'] = everyreport.xpath(".//FourSeventyOneConsultantRegistrationNumber/text()").extract_first()
                item['FourSeventyOneConsultingFirmName'] = everyreport.xpath(".//FourSeventyOneConsultingFirmName/text()").extract_first()
                item['ServiceProviderName'] = everyreport.xpath(".//ServiceProviderName/text()").extract_first()
                item['SPIN'] = everyreport.xpath(".//SPIN/text()").extract_first()
                item['SPACFiled'] = everyreport.xpath(".//SPACFiled/text()").extract_first()
                item['FundYear'] = everyreport.xpath(".//FundYear/text()").extract_first()
                item['FourEightySixServiceStartDate'] = everyreport.xpath(".//FourEightySixServiceStartDate/text()").extract_first()
                item['ContractAwardDate']= everyreport.xpath(".//ContractAwardDate/text()").extract_first()
                item['ContractExpOrSvcEndDate'] = everyreport.xpath(".//ContractExpOrSvcEndDate/text()").extract_first()
                item['RemainingContractExtensions'] = everyreport.xpath(".//RemainingContractExtensions/text()").extract_first()
                item['LastDatetoInvoice'] = everyreport.xpath(".//LastDatetoInvoice/text()").extract_first()
                item['OrigRMonthlyCost'] = everyreport.xpath(".//OrigRMonthlyCost/text()").extract_first()
                item['CmtdRMonthlyCost'] = everyreport.xpath(".//CmtdRMonthlyCost/text()").extract_first()
                item['OrigRIneligibleCost'] = everyreport.xpath(".//OrigRIneligibleCost/text()").extract_first()
                item['CmtdRIneligibleCost'] = everyreport.xpath(".//CmtdRIneligibleCost/text()").extract_first()
                item['OrigREligibleCost'] = everyreport.xpath(".//OrigREligibleCost/text()").extract_first()
                item['CmtdREligibleCost'] = everyreport.xpath(".//CmtdREligibleCost/text()").extract_first()
                item['OrigRMonthsofService'] = everyreport.xpath(".//OrigRMonthsofService/text()").extract_first()
                item['CmtdRMonthsofService'] = everyreport.xpath(".//CmtdRMonthsofService/text()").extract_first()
                item['OrigRAnnualCost'] = everyreport.xpath(".//OrigRAnnualCost/text()").extract_first()
                item['CmtdRAnnualCost'] = everyreport.xpath(".//CmtdRAnnualCost/text()").extract_first()
                item['OrigNRCost'] = everyreport.xpath(".//OrigNRCost/text()").extract_first()
                item['CmtdNRCost'] = everyreport.xpath(".//CmtdNRCost/text()").extract_first()
                item['OrigNRIneligibleCost'] = everyreport.xpath(".//OrigNRIneligibleCost/text()").extract_first()
                item['CmtdNRIneligibleCost'] = everyreport.xpath(".//CmtdNRIneligibleCost/text()").extract_first()
                item['OrigNREligibleCost'] = everyreport.xpath(".//OrigNREligibleCost/text()").extract_first()
                item['CmtdNREligibleCost'] = everyreport.xpath(".//CmtdNREligibleCost/text()").extract_first()
                item['OrigTotalCost'] = everyreport.xpath(".//OrigTotalCost/text()").extract_first()
                item['CmtdTotalCost'] = everyreport.xpath(".//CmtdTotalCost/text()").extract_first()
                item['OrigDiscount'] = everyreport.xpath(".//OrigDiscount/text()").extract_first()
                item['CmtdDiscount'] = everyreport.xpath(".//CmtdDiscount/text()").extract_first()
                item['OrigFundingRequest'] = everyreport.xpath(".//OrigFundingRequest/text()").extract_first()
                item['CmtdFundingRequest'] = everyreport.xpath(".//CmtdFundingRequest/text()").extract_first()
                item['OrigFRNServiceType'] = everyreport.xpath(".//OrigFRNServiceType/text()").extract_first()
                item['CmtdFRNServiceType'] = everyreport.xpath(".//CmtdFRNServiceType/text()").extract_first()
                item['OrigFourSeventyOneSSD'] = everyreport.xpath(".//OrigFourSeventyOneSSD/text()").extract_first()
                item['CmtdFourSeventyOneSSD'] = everyreport.xpath(".//CmtdFourSeventyOneSSD/text()").extract_first()
                item['WaveNumber'] = everyreport.xpath(".//WaveNumber/text()").extract_first()
                item['FCDLDate'] = everyreport.xpath(".//FCDLDate/text()").extract_first()
                item['DateUserGeneratedFCDL'] = everyreport.xpath(".//DateUserGeneratedFCDL/text()").extract_first()
                item['FCDLCommentforFourSeventyOneApplication'] = everyreport.xpath(".//FCDLCommentforFourSeventyOneApplication/text()").extract_first()
                item['FCDLCommentforFRN'] = everyreport.xpath(".//FCDLCommentforFRN/text()").extract_first()
                item['AppealWaveNumber'] = everyreport.xpath(".//AppealWaveNumber/text()").extract_first()
                item['RevisedFCDLDate'] = everyreport.xpath(".//RevisedFCDLDate/text()").extract_first()
                item['FRNCommittedAmount'] = everyreport.xpath(".//FRNCommittedAmount/text()").extract_first()
                item['InvoicingMode'] = everyreport.xpath(".//InvoicingMode/text()").extract_first()
                item['TotalAuthorizedDisbursement'] = everyreport.xpath(".//TotalAuthorizedDisbursement/text()").extract_first()
                yield item
