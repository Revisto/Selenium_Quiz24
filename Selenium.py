

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time
import random
URLs={
    "903":"https://www.quiz24.ir/home/JoinToClass?code=holding-244129397",
    "902":"https://www.quiz24.ir/home/JoinToClass?code=holding-329929818",
    "901":"https://www.quiz24.ir/home/JoinToClass?code=holding-431666409"}
Students=[
    "امین الماسی راد",
    "پارسا طالبی",
    "ماهان رضایی وارسته","ماهان رضایی وارسته","ماهان رضایی وارسته","ماهان رضایی وارسته","ماهان رضایی وارسته"
    "مهدی بدخشان",
    "حسام صادقپور","حسام صادقپور","حسام صادقپور","حسام صادقپور","حسام صادقپور",
    "ایلیا بقایی",
    "آرمین قیدی",
    "محمد خداکرمی",
    "مهرشاد رضایی",
    "شایان موسوی","محمد جعفر پور",
    "محمد رضا رشادتی","محمد رضا رشادتی","محمد رضا رشادتی","محمد رضا رشادتی","محمد رضا رشادتی",
    "ماهان بیداروند",
    "محسن داداشزاده",
    "محمد نوعی",
    "محمد رضایی",
    "سام صالحی","سام صالحی","سام صالحی","سام صالحی","سام صالحی","سام صالحی",
    "دایان کر",
    "آرین جعفرپور",
    "دانیال معتمد",
    "فراز صالحیان",
    "محمد رضا واشقیانی",
    "امیر اشکان اسماعیلی",
    "آرمین رستمیان","آرمین رستمیان","آرمین رستمیان","آرمین رستمیان","آرمین رستمیان",
    "عباس خراج",
    "علیرضا مجریان",
    "رضا تقی زاده","رضا تقی زاده","رضا تقی زاده","رضا تقی زاده",
    "علیرضا نیک منش",
    "کیان حجازی",
    "ماهان معصوم زاده",
    "پویا زندیان",
    "مهدی عباسی",
    "کاویان گشتاسبی","کاویان گشتاسبی","کاویان گشتاسبی","کاویان گشتاسبی",
    "پارسا سعیدنیا",
    "محمد حسین سلیمانی",
    "ماهان فروزنده دوست","ماهان فروزنده دوست","ماهان فروزنده دوست","ماهان فروزنده دوست","ماهان فروزنده دوست","ماهان فروزنده دوست","ماهان فروزنده دوست","ماهان فروزنده دوست",
    "علی باطبی",
    "شایان شیرخوانی",
    "آرمین آقازاده",
    "حسین دلاور",
    "مهدی بدخشان",
    "عرفان بزرگی",
    "علی عزیزمحمدی",
    "عرشیا خدامرادی",
    "آرین فرتاش","آرین فرتاش","آرین فرتاش","آرین فرتاش","آرین فرتاش","آرین فرتاش",
    "محسن ابراهیمی",
    "محمد سحری",
    "آرمین",
    "آرین جعفرپور",
    "علیرضا امیرخانی",
    "دانیال پیغمبرزاده","دانیال پیغمبرزاده","دانیال پیغمبرزاده","دانیال پیغمبرزاده","دانیال پیغمبرزاده",
    "بنیامین شفیعی",
    "سعید صباقیان","سعید صباقیان","سعید صباقیان",
    "شهروز یوسفی","شهروز یوسفی","شهروز یوسفی"]

def WhatsYourDestiny(URLs):
    Num=input("""which Class Do You Wanna Atack 
    901
    or 
    902
    or
    903
    Class : """)
    if Num in URLs:
        print (URLs[Num])
        return URLs[Num]
    else:
        return WhatsYourDestiny(URLs)
Texts=[
    "ساعت چنده",
    'درس چندیم؟',
    'اینجا چه کلاسی؟',
    'شما؟',
    'کی هستی؟',
    'تو کی هستی؟',
    'ببخشید شما؟',
    'شما معلم چه درسی بودید؟',
    'یادم نمیاد . شما؟',
    'یاالله',
    'اینجا کجاست',
    'من کیم',
    'چی شده',
    'اونجا ساعت چنده',
    'شما تهران هستید',
    'اگه دیروز سه شنبه بود , امروز چند شنبست؟',
    'خسته نباشید',
    'خسته نبااااشید',
    'کلاس کی تموم میشه',
    'وای من یادم رفت صبحونه بخورم',
    'من برم ناهار',
    'صبح بخیر',
    'من برم صبحونه',
    'استاد صبونه چی خوردید',
    'ناهار چی بخورم',
    'این یعنی چی؟',
    'چی گفتید استاد . صداتون قطع شد',
    'صفحه مشکل داره',
    'چیزی پخش نمیشه',
    'صدا نییییست',
    'استاد چرا صحبت نمیکنید؟',
    'تصویر ندارم',
    'چرا سیاه شد تصویر؟',
    'استاد کلاس تموم شد',
    'صدا قطع شده',
    'استاد صحبت نمیکنید؟',
    'درس تموم شد؟',
    'قضیه چیه؟',
    'موضوع چیه؟',
    'ما کجاااااییم؟'
    'تشکر استاد',
    'امیدوارم همیشه سلامت باشید',
    'من فقط به عشق استاد از خواب پامیشم',
    'من تازه پاشدم   اینجا چه خبره',
    'چه درسی داریم؟',
    'بچه ها کی داره حرف میزنه',
    'استادمون عوض شده',
    "چرا صداش اینجوریه؟",
    "این دیکه کیه؟",
    "درس خیلی پیچیدست",
    'من نمیفهمم',
    'متوجه نمیشم']

def ReTurnMessage(Texts):
    Word=random.choice(Texts)
    print (Word)
    a=input("'y' for yes , 'n' for no    which:  ")
    if a=="y" or a=="Y":
        return Word
    else:
        return ReTurnMessage(Texts)
def ReturnStudent(Texts):
    Word=random.choice(Texts)
    print (Word)
    a=input("'y' for yes , 'n' for no    which:  ")
    if a=="y" or a=="Y":
        return Word
    else:
        return ReTurnMessage(Texts)

ListDrives=[]
if True:
    Url=WhatsYourDestiny(URLs)
    
    for i in range (int(input("How Many Tabs Do You Want To Open : "))):
        Path="/usr/lib/chromium-browser/chromedriver"
        Drive = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        print (Url)
        Drive.get(Url)
        
        time.sleep(5)
    

        SearchBox = Drive.find_elements_by_class_name("form-control")
        Name=ReturnStudent(Students)
        SearchBox[0].send_keys(Name)
        SearchBox[0].send_keys(Keys.ENTER) 

        SearchBox[1].send_keys("0912"+str(random.randint(1000000,9999999)))
        SearchBox[1].send_keys(Keys.ENTER)



        SearchBox[2].send_keys("1234567")
        SearchBox[2].send_keys(Keys.ENTER)

        time.sleep(5)
        try:
            Drive.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]").click()
        except:
            None
        a=input("WAit")
        
        ListDrives.append(Drive)

while True:
    Sentense=ReTurnMessage(Texts)
    DriveRandom=random.choice(ListDrives)
    Chat=DriveRandom.find_element_by_id("message-input")
    try:
        Chat.send_keys(Sentense)
        Chat.send_keys(Keys.ENTER)
    except:
        None