# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,data,atexit
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()
cl = LINE("EtYdZFopDp6t05Mks8W1.LuvPdjZJJfWn3Kdw6aHBOq.UIyP7OxAhatg3G9OOrH4AJCOB4leV+pleOnYmBx2ODI=")
baime = LINE("EsaRYhfKPJerFvPsTZse.VJ7z0J4e/d5kiF5mT9U5FG.RhyadcN4iNnuIrlzUdDfmtYaeSbAjqQsg8J8Y8M8j0Y=")
orange = LINE("EtVhwdOnvlkqVVFQeRCe.Mt92J0fQTAU7vrft+4RdJG.SnTraOahLZeni4H64XwtvaPLJGmNlwCv7A/4mZiMLAw=")
#coi01 = LINE("EsgwGQo7wUDrhaPN50V9.WewaHX+5eCQCvBHMG2OfYq.lCsap5Co8RjtAQc7Ip75bUDXZSgr95sAHKslbvgMXl0=")
coi01 = cl
ghost01 = LINE("EsZjeSZLogbTGtvLsH4f.uifK08jVAVQUFFGPGWbhlW.ZrS08ZaUconLw6qsrKBPAMKOozfPUpO/cU9xbwVOelQ=")
ghost02 = LINE("EsdC1dWB564Dhdq5OIpb.0NUmZEsh6+Dhqa7uTfcJsW.pGU4yHnb2kc+StuBi8JlfDJIz9plq099dzbrEhG9tcE=")
kicker01 = LINE("EtMyh0mM1h8MeA8Py5k1.X/9n3an1J75BajgVvEY6eq.IJGAqEv0iRDL7OOZuPkYuZOHWpK4psOi7iimLCzUkQY=")
kicker02 = LINE("Esg7UDW6wSPm2Kyz1mZ0.VvcMElkI+oGtJgVyFHXxea.EIvQWsbZG2huRO+jzHhP67QbREM1LIIchZaBn1WGZhI=")
kicker03 = LINE("Ese5jloXXfD7JYxdv7pe.opN1tRH4fPR+iMwCSwxRtG.m9/CGhviks9g/DiK58qi0BJ4xc+AjZ/hhN0olRF8UrY=")
kicker04 = LINE("EsxKynuEZJ5gdCF2Erv6.5DosnUnAyvWEKXtHvj5wbG.16QTuhBlJ38TCxVoXOeuy09zjwYSTusXdZ4gfKGaazw=")
kicker05 = LINE("Etp22vMwaHaVbRlZAEkc.1nliY+fcMel8l2xN8erKFa.rQoD/NF8w5TqmsorOQPzG/a7hCNaeS/R9SblB4B3QqU=")
kicker06 = LINE("EskXeludd3GQHHetmAr2.wHI264N/gj4V/ahEyGooiG.aqYhlb8u+pUF6Y3d4xmWNaz2iehrWFdr6LZqlG6ux6U=")
kicker07 = LINE("EtADLMn2peI1dZoyWj08.7/1TD4h3gGX/VhsGVzUvMa.DWg8xwznLTiUPQTCDJlrtEDMt2+kbdj9B6tm5CE5ELI=")
kicker08 = LINE("EtIpYJdlx4QVOR4EFs57.zqLdC8TXR+RFywS1uE47zW.cIP6uWTCj0f/+59JuSg9WhsjBRWYMbr9LciOPLu7ME4=")
kicker09 = LINE("EtQcyp7nlHQq2MWCV0Ye.ZiheIROvDTnbhzPKPFPyZG.FWoS264D6L4ovmq3qgnFR7/vsgwNrpUxvE0j64u1ZY0=")
kicker10 = LINE("EtNwT2Rr0bCGoMPyRyvc.26tehiskzNeYEvtImOkYla.jCqVYioa96KVzHYH0XGVD7CE4Gt37vu3ogKMva0ZCkQ=")
print ("======登入成功=====")
#ghost01 = ghost02
#kicker05 = kicker01
#kicker07 = kicker02
#kicker08 = kicker03
#kicker09 = kicker04
#kicker10 = kicker06
#==============================================================================#
oepoll = OEPoll(cl)
#==============================================================================#
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
protectOpen = codecs.open("protect.json","r","utf-8")
creatorOpen = codecs.open("GroupCreater.json","r","utf-8")
blackOpen = codecs.open("blacklist.json","r","utf-8")
adminsOpen = codecs.open("creator.json","r","utf-8")
timeOpen = codecs.open("Time.json","r","utf-8")
cktOpen = codecs.open("cktext.json","r","utf-8")

read = json.load(readOpen)
settings = json.load(settingsOpen)
pro = json.load(protectOpen)
gcs= json.load(creatorOpen)
black = json.load(blackOpen)
admins = json.load(adminsOpen)
times = json.load(timeOpen)
ckt = json.load(cktOpen)

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
#==============================================================================#
lineSettings = cl.getSettings()
baimeSettings = baime.getSettings()
orangeSettings = orange.getSettings()
ghost01Settings = ghost01.getSettings()
ghost02Settings = ghost02.getSettings()
kicker01Settings = kicker01.getSettings()
kicker02Settings = kicker02.getSettings()
kicker03Settings = kicker03.getSettings()
kicker04Settings = kicker04.getSettings()
kicker05Settings = kicker05.getSettings()
kicker06Settings = kicker06.getSettings()
kicker07Settings = kicker07.getSettings()
kicker08Settings = kicker08.getSettings()
kicker09Settings = kicker09.getSettings()
kicker10settings = kicker10.getSettings()

#==============================================================================#
clProfile = cl.getProfile()
baimeProfile = baime.getProfile()
orangeProfile = orange.getProfile()
ghost01Profile = ghost01.getProfile()
ghost02Profile = ghost02.getProfile()
kicker01Profile = kicker01.getProfile()
kicker02Profile = kicker02.getProfile()
kicker03Profile = kicker03.getProfile()
kicker04Profile = kicker04.getProfile()
kicker05Profile = kicker05.getProfile()
kicker06Profile = kicker06.getProfile()
kicker07Profile = kicker07.getProfile()
kicker08Profile = kicker08.getProfile()
kicker09Profile = kicker09.getProfile()
kicker10Profile = kicker10.getProfile()

#==============================================================================#
clMID = cl.profile.mid
baimeMID=baime.profile.mid
orangeMID=orange.profile.mid
ghost01MID = ghost01.profile.mid
ghost02MID = ghost02.profile.mid
kicker01MID = kicker01.profile.mid
kicker02MID = kicker02.profile.mid
kicker03MID = kicker03.profile.mid
kicker04MID = kicker04.profile.mid
kicker05MID = kicker05.profile.mid
kicker06MID = kicker06.profile.mid
kicker07MID = kicker07.profile.mid
kicker08MID = kicker08.profile.mid
kicker09MID = kicker09.profile.mid
kicker10MID = kicker10.profile.mid

#==============================================================================#
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
#==============================================================================#
KAC = [kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10]
NK1 = [cl,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10]
NK2 = [cl,kicker01,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10]
NK3 = [cl,kicker01,kicker02,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10]
NK4 = [cl,kicker01,kicker02,kicker03,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10]
NK5 = [cl,kicker01,kicker02,kicker03,kicker04,kicker06,kicker07,kicker08,kicker09,kicker10]
NK6 = [cl,kicker01,kicker02,kicker03,kicker04,kicker05,kicker07,kicker08,kicker09,kicker10]
NK7 = [cl,kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker08,kicker09,kicker10]
NK8 = [cl,kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker09,kicker10]
NK9 = [cl,kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker10]
NK10 = [cl,kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09]
Bots = [clMID,baimeMID,orangeMID,kicker01,kicker02MID,kicker03MID,kicker04MID,kicker05MID,kicker06,kicker07MID,kicker08MID,kicker09MID,kicker10MID,ghost01MID,ghost02MID]
adbots = ["u67f1283db3cb9a8d694b2b0746cea56e","ue5c395168da59b2e0c46a2b6d0a5d0db","ubfd7f98515e5b1defb4594fe61362b29","u0a5bc9ffcbd7e75a1ee5c53684ed86c3","u35826ab2811a8474ef324f34a6f8a0ee","u2b37602c4f9f8d54917de47b09749130"]

#LV1 = ['u00d0e3684d203a77d15f2d5489f9df41','u0a5bc9ffcbd7e75a1ee5c53684ed86c3','u35826ab2811a8474ef324f34a6f8a0ee','u67f1283db3cb9a8d694b2b0746cea56e','u96597cb3a0934c93e0736c413cf28aa9','ubfd7f98515e5b1defb4594fe61362b29','ue5c395168da59b2e0c46a2b6d0a5d0db','uf5768dd477f04b109057d477bd029e8a','uf119b7da7209a75d0c0713019067f153',owner]
#==============================================================================#
setTime = {}
setTime = read['wait2']['setTime']
res = {
    'num':{},
    'us':{},
    'au':{},
}
#==============================================================================#
try:
    with open("Reread.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("讀取紀錄失敗")
bl = []
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
#==============================================================================#
def restartBot():
    print ("[ 訊息 ] 機器 重新啟動")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def omikuji():
    kuji = ["大吉だよ♪","吉だよ♪","中吉だよ♪","小吉だよ...","末吉だよ...","凶だよ..."]
    return random.choice(kuji)
    
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = pro
        f = codecs.open('protect.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = black
        f = codecs.open('blacklist.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = admins
        f = codecs.open('creator.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = gcs
        f = codecs.open('GroupCreater.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = times
        f = codecs.open('Time.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = ckt
        f = codecs.open('cktext.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#==============================================================================#
#==============================================================================#
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def logRead():
    try:
        with open("Reread.json","w",encoding='utf8') as f:
            json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    except Exception as error:
        logError(error)
        return False

def Tag(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@co \n'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def helpmessage():
    helpMessage = """
╔═══════════
♥ ✿ CoCo指令表 ✿ ♥
════✪〘 查看指令表 〙✪════
↪ 「Help」查看全部指令
↪ 「HelpTag」查看標註指令
↪ 「HelpKick」查看踢人指令
↪ 「HelpBot」查看機器指令
════✪〘 狀態 〙✪═══════
↪ 「Rebot」重新啟動機器
↪ 「Runtime」查看機器運行時間
↪ 「Speed」查看機器速度
↪ 「Set」查看設定
↪ 「About」查看自己的狀態
↪ 「Protect Info」查看群組保護狀態
════✪〘 設定 〙✪═══════
↪ 「Add On/Off」自動加入好友 打開/關閉
↪ 「Join On/Off」邀請自動進入群組 打開/關閉
↪ 「Leave On/Off」自動離開副本 打開/關閉
↪ 「Read On/Off」自動已讀 打開/關閉
↪ 「Sticker On/Off」檢查貼圖 打開/關閉
↪ 「AitoTag On/Off」標註提醒 打開/關閉
↪ 「Inviteprotect On/Off」邀請保護 打開/關閉
↪ 「Urljoin On/Off」網址自動進入群組 打開/關閉
↪ 「Reread On/Off」查看收回 打開/關閉
↪ 「kickerjoin On/Off」分機自動進入群組 打開/關閉
↪ 「Tag On/Off」標註全部人 打開/關閉
↪ 「Article On/Off」檢視文章詳情 打開/關閉
════✪〘 自己 〙✪═══════
↪ 「Me」丟出自己好友資料
↪ 「MyMid」查看自己系統識別碼
↪ 「MyName」查看自己名字
↪ 「MyBio」查看自己個簽
↪ 「MyPicture」查看自己頭貼網址
↪ 「MyVideoProfile」查看自己動態頭貼網址
↪ 「MyCover」查看自己封面網址
↪ 「Contact @」標註查看好友資料
↪ 「Mid @」標註查看系統識別碼
↪ 「Name @」標註查看名稱
↪ 「Bio @」標註查看狀態消息
↪ 「Picture @」標註查看頭貼
↪ 「VideoProfile @」標註查看動態頭貼
↪ 「Cover @」標注查看封面
↪ 「Copy @」標註複製配置文件
↪ 「Restore」恢復配置文件
════✪〘 群組 〙✪═══════
↪ 「Gowner」查看群組擁有者
↪ 「Gid」查看群組識別碼
↪ 「Gname」查看群組名稱
↪ 「GPicture」查看群組圖片網址
↪ 「Gurl」丟出群組網址
↪ 「O/Curl」打開/關閉群組網址
↪ 「Lg」查看所有群組
↪ 「Gb」查看群組成員
↪ 「Ginfo」查看群組狀態
↪ 「Ri @」標註來回機票
↪ 「Tk @」標注踢出成員(多踢)
↪ 「Mk @」標注踢出成員(單踢)
↪ 「Dk mid」使用定名踢出成員
↪ 「Nkn Name」踢出不含這個名字的成員
↪ 「Vk @」標註踢出並清除訊息
↪ 「Vk:mid」使用系統識別碼踢出並清除訊息
↪ 「Nk Name」使用名子踢出成員
↪ 「Uk mid」使用系統識別碼踢出成員
↪ 「NT Name」使用名子標註成員
↪ 「DT Name」使用定名標註成員
↪ 「NTN Name」標註不含這個名字的成員
↪ 「Zk」踢出0字元
↪ 「Zt」標註名字0字成員
↪ 「Zm」丟出0字成員的系統識別碼
↪ 「Zc」丟出0字成員好友資料
↪ 「Cancel」取消所有成員邀請
↪ 「Gcancel」取消所有群組邀請
↪ 「Gn Name」更改群組名稱
↪ 「Gc @」標註查看個人資料
↪ 「Inv mid」使用系統識別碼邀請進入群組
↪ 「Ban @」標註加入黑單
↪ 「Unban @」標註解除黑單
↪ 「Clear Ban」清空黑單
↪ 「Kill Ban」剔除黑單
↪ 「Zk」踢出名字0字成員
↪ 「Nkk Name」使用名子踢出成員
↪ 「Mkk @」標註踢出成員(單踢)
↪ 「Tkk @」標註踢出成員(多踢)
↪ 「Zkk」踢出名字0字成員
↪ 「Nkkn Name」踢出不含這個名字的成員
↪ 「Dkk mid」使用定名踢出成員
════✪〘 特別 〙✪═══════
↪ 「Mimic On/Off」模仿 打開/關閉
↪ 「MimicList」模仿列表
↪ 「MimicAdd @」標註增加模仿
↪ 「MimicDel @」標註刪除模仿
↪ 「Tagall」標註群組所有成員
↪ 「Sn」已讀點開啟
↪ 「Sf」已讀點關閉
↪ 「Rr」已讀點重置
↪ 「R」查看已讀
↪ 「F/Gbc」好友/群組廣播
↪「/invitemeto:」使用群組識別碼邀請至群組
════✪〘 群組 〙✪═══════
↪ 「ProtectList」查看群組保護狀態
↪ 「Ia」設定副群主
════✪〘 媒體 〙✪═══════
↪ 「Time」查看現在的時間
↪ 「CheckDate Date」
↪ 「InstagramInfo UserName」
↪ 「InstagramPost UserName」
↪ 「SearchYoutube Search」
↪ 「SearchMusic Search」
↪ 「SearchLyric Search」
↪ 「SearchImage Search」
↪ 「ScreenshootWebsite LinkUrl」
╚═〘 Credits By: ©CoCo™  〙
"""
    return helpMessage

def helpmessagetag():
    helpMessageTag ="""
╔══[ 標注指令 ]════════
↪ 「Ri @」標註來回機票
↪ 「Tk @」標注踢出成員(多踢)
↪ 「Mk @」標注踢出成員(單踢)
↪ 「Vk @」標註踢出並清除訊息
↪ 「Gc @」標註查看個人資料
↪ 「Mid @」標註查看系統識別碼
↪ 「Name @」標註查看名稱
↪ 「Bio @」標註查看狀態消息
↪ 「Picture @」標註查看頭貼
↪ 「VideoProfile @」標註查看動態頭貼
↪ 「Cover @」標注查看封面
↪ 「Copy @」標註複製配置文件
↪ 「MimicAdd @」標註增加模仿
↪ 「MimicDel @」標註刪除模仿
↪ 「Ban @」標註加入黑單
↪ 「Unban @」標註解除黑單
↪ 「Mkk @」標注踢出成員(單踢)
↪ 「Tkk @」標注踢出成員(多踢)
╚═〘 Credits By: ©CoCo™  〙
"""
    return helpMessageTag

def helpmessagekick():
    helpMessageKick ="""
╔══[ 踢人指令 ]════════
↪ 「Ri @」標註來回機票
↪ 「Tk @」標注踢出成員(多踢)
↪ 「Mk @」標注踢出成員(單踢)
↪ 「Vk @」標註踢出並清除訊息
↪ 「Vk:mid」使用系統識別碼踢出並清除訊息
↪ 「Nk Name」踢出不含這個名字的成員
↪ 「Uk mid」使用系統識別碼踢出成員
↪ 「Dk mid」使用定名踢出成員
↪ 「Nkn Name」踢除了這個名字以外的成員
↪ 「Kill ban」踢出黑單成員
↪ 「Zk」踢出名字0字成員
↪ 「Nkk Name」使用名子踢出成員
↪ 「Mkk @」標注踢出成員(單踢)
↪ 「Tkk @」標注踢出成員(多踢)
↪ 「Zkk」踢出名字0字成員
↪ 「Nkkn Name」踢出不含這個名字的成員
↪ 「Dkk mid」使用定名踢出成員
╚═〘 Credits By: ©CoCo™  〙
"""
    return helpMessageKick

def helpmessagebot():
    helpMessageBot ="""
╔══〘 設定 〙✪═══════
↪ 「Add On/Off」自動加入好友 打開/關閉
↪ 「Join On/Off」邀請自動進入群組 打開/關閉
↪ 「Leave On/Off」自動離開副本 打開/關閉
↪ 「Read On/Off」自動已讀 打開/關閉
↪ 「Sticker On/Off」檢查貼圖 打開/關閉
↪ 「Tag On/Off」標註提醒 打開/關閉
↪ 「Inviteprotect On/Off」邀請保護 打開/關閉
↪ 「Urljoin On/Off」網址自動進入群組 打開/關閉
↪ 「Reread On/Off」查看收回 打開/關閉
↪ 「kickerjoin On/Off」分機自動進入群組 打開/關閉
↪ 「Tag On/Off」標註全部人 打開/關閉
↪ 「Article On/Off」檢視文章詳情 打開/關閉
"""
    return helpMessageBot

def helpmessagelv1():
    helpMessageLv1 ="""╔══〘 權限等級1 〙✪═══════
↪ 「Mk @」標注踢出成員(單踢)
↪ 「Gn Name」更改群組名稱
↪ 「Gc @」標註查看個人資料
↪ 「Ginfo」查看群組狀態
↪ 「Protect Info」查看群組保護狀態
↪ 「SetRead」設定已讀點
↪ 「LookRead」查看已讀
↪ 「Runtime」查看機器運行時間
↪ 「Speed」查看機器速度
↪ 「!ckt_add 貼圖包ID_貼圖ID:文字」增加貼圖回覆
↪ 「!ckt_del 貼圖包ID_貼圖ID」刪除貼圖回覆
"""
    return helpMessageLv1
def errortext():
    ErrorText = """
        D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.CD.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.CD.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T..D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.A.C.D.T.
        """
    return ErrorText
adminlv1 = []
adminowner = []
#==============================================================================#
def lineBot(op):
    try:
        for owner in admins["Max"]:
            Owner = [clMID,baimeMID,orangeMID,kicker01,kicker02MID,kicker03MID,kicker04MID,kicker05MID,kicker06,kicker07MID,kicker08MID,kicker09MID,kicker10MID,ghost01MID,ghost02MID, owner]
        for lv1 in admins['lv1']:
            adminlv1.append(lv1)
        if adminlv1 == []:
            Lv1 = Owner
            admin = Owner + Bots
        else:
            Lv1 = adminlv1 + Owner
            admin = adminlv1 + Owner + Bots
        bots = Bots + adbots
        if op.type == 0:
            #    print ("[ 0 ] 操作結束")
            return
        if op.type == 5:
            contact = cl.getContact(op.param1)
            print ("[ 5 ] 通知添加好友 名字: " + contact.displayName)
            if settings["autoAdd"] == True:
                cl.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker01.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker02.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker03.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker04.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker05.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker06.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker07.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker08.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker09.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker10.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
        if op.type == 9:
            cl.leaveGroup(op.param1)
            kicker01.leaveGroup(op.param1)
            kicker02.leaveGroup(op.param1)
            kicker03.leaveGroup(op.param1)
            kicker04.leaveGroup(op.param1)
            kicker05.leaveGroup(op.param1)
            kicker06.leaveGroup(op.param1)
            kicker07.leaveGroup(op.param1)
            kicker08.leaveGroup(op.param1)
            kicker09.leaveGroup(op.param1)
            kicker10.leaveGroup(op.param1)
            coi01.leaveGroup(op.param1)
        if op.type == 11:
            try:
                """
                op.param3
                1がグループ名
                2がグループ画像
                3が
                4がurl
                """
                if op.param3 == "1":
                    if op.param1 in pro["Name"]:
                        creater_ = gcs['Creater'][op.param1]
                        if (op.param1 in pro['Name'] and op.param2 == creater_ ) or (op.param2 in admin) or (op.param2 in bots):
                            G =cl.getGroup(op.param1)
                            pro['Name'][op.param1] = G.name
                        else:
                            G = cl.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            G.name = pro["Name"][op.param1]
                            random.choice(KAC).updateGroup(G)
                            if op.param1 in pro['High']:
                                try:
                                    random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                                except:
                                    cl.kickoutFromGroup(op.param1, [op.param2])
                            else:
                                pass
                            if op.param2 in black["blacklist"]:
                                pass
                            else:
                                black["blacklist"][op.param2] = True
                        backupData()
                    else:
                        pass
                if op.param3 == "2":
                    if op.param1 in pro["Image"]:
                        if (op.param1 in pro['Image'] and op.param2 in gcs['Creater'][op.param1]) or (op.param2 in admin) or (op.param2 in bots):
                            pass
                        else:
                            try:
                                random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                            except:
                                cl.kickoutFromGroup(op.param1, [op.param2])
                            if op.param2 in black["blacklist"]:
                                pass
                            else:
                                black["blacklist"][op.param2] = True
                            backupData()
                    else:
                        pass
                if op.param3 == "4":
                    group = cl.getGroup(op.param1)
                    contact = cl.getContact(op.param2)
                    print ("[11]有人打開群組網址 群組名稱: " + str(group.name) + "\n" + op.param1 + "\n名字: " + contact.displayName)
                    if op.param1 in pro["Qr"]:
                        if (op.param1 in pro['Qr'] and op.param2 in gcs['Creater'][op.param1]) or (op.param2 in admin) or (op.param2 in bots):
                            pass
                        else:
                            gs = cl.getGroup(op.param1)
                            invsend = 0
                            try:
                                Ti = cl.reissueGroupTicket(op.param1)
                                ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                                ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                                ghost01.kickoutFromGroup(op.param1, [op.param2])
                                gs.preventJoinByTicket = True
                                try:
                                    ghost02.updateGroup(gs)
                                except:
                                    try:
                                        random.choice(KAC).updateGroup(gs)
                                    except:
                                        cl.updateGroup(gs)
                                ghost01.leaveGroup(op.param1)
                                ghost02.leaveGroup(op.param1)
                            except:
                                try:
                                    random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                                except:
                                    cl.kickoutFromGroup(op.param1, [op.param2])
                                    gs.preventJoinByTicket = True
                                try:
                                    random.choice(KAC).updateGroup(gs)
                                except:
                                    cl.updateGroup(gs)
            except Exception as e:
                print (e)
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            print ("[ 13 ] 通知邀請群組: " + str(group.name) + "\n邀請者: " + contact1.displayName + "\n被邀請者" + contact2.displayName)
            if settings["kickblackjoin"] == True:
                if op.param2 in admin:
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    invsend = 0
                    try:
                        random.choice(KAC).cancelGroupInvitation(op.param1, [op.param3])
                        try:
                            gs.preventJoinByTicket = false
                            try:
                                random.choice(KAC).updateGroup(gs)
                            except:
                                cl.updateGroup(gs)
                            Ti = cl.reissueGroupTicket(op.param1)
                            ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                            ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                            ghost01.kickoutFromGroup(op.param1,[op.param2])
                            gs.preventJoinByTicket = True
                            try:
                                ghost02.updateGroup(gs)
                            except:
                                try:
                                    random.choice(KAC).updateGroup(gs)
                                except:
                                    cl.updateGroup(gs)
                            ghost01.leaveGroup(op.param1)
                            ghost02.leaveGroup(op.param1)
                        except:
                            try:
                                random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                            except:
                                cl.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        cl.cancelGroupInvitation(op.param1,[op.param3])
                        try:
                            gs.preventJoinByTicket = false
                            try:
                                random.choice(KAC).updateGroup(gs)
                            except:
                                cl.updateGroup(gs)
                            Ti = cl.reissueGroupTicket(op.param1)
                            ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                            ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                            ghost01.kickoutFromGroup(op.param1, [op.param2])
                            gs.preventJoinByTicket = True
                            try:
                                ghost02.updateGroup(gs)
                            except:
                                try:
                                    random.choice(KAC).updateGroup(gs)
                                except:
                                    cl.updateGroup(gs)
                            ghost01.leaveGroup(op.param1)
                            ghost02.leaveGroup(op.param1)
                        except:
                            try:
                                random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                            except:
                                cl.kickoutFromGroup(op.param1, [op.param2])

            if op.param1 in pro["Invite"]:
                if (op.param1 in gcs['Creater'] and op.param2 in gcs['Creater'][op.param1]) or (op.param1 in gcs['Invite'] and op.param2 in gcs['Invite'][op.param1]) or (op.param1 in gcs['Inviteadmin'] and op.param2 in gcs['Inviteadmin'][op.param1]) or (op.param2 in admin) or (op.param2 in bots):
                    pass
                else:
                    if op.param1 in pro['High']:
                        try:
                            random.choice(KAC).cancelGroupInvitation(op.param1, [op.param3])
                        except:
                            cl.cancelGroupInvitation(op.param1,[op.param3])
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                        except:
                            cl.kickoutFromGroup(op.param1, [op.param2])
                    else:
                        try:
                            random.choice(KAC).cancelGroupInvitation(op.param1, [op.param3])
                        except:
                            cl.cancelGroupInvitation(op.param1,[op.param3])
            if clMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in admin:
                        print ("進入群組: " + str(group.name))
                        cl.acceptGroupInvitation(op.param1)
                        if settings["kickerjoin"] == True:
                            G = cl.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(op.param1)
                            baime.acceptGroupInvitationByTicket(op.param1, Ti)
                            orange.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
            if kicker01MID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in admin:
                        kicker01.acceptGroupInvitation(op.param1)
            if kicker02MID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in admin:
                        kicker02.acceptGroupInvitation(op.param1)
            if kicker03MID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in admin:
                        kicker03.acceptGroupInvitation(op.param1)
            if kicker04MID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in admin:
                        kicker04.acceptGroupInvitation(op.param1)
            if kicker05MID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in admin:
                        kicker05.acceptGroupInvitation(op.param1)
            if kicker06MID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in admin:
                        kicker06.acceptGroupInvitation(op.param1)
            if kicker07MID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in admin:
                        kicker07.acceptGroupInvitation(op.param1)
            if kicker08MID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in admin:
                        kicker08.acceptGroupInvitation(op.param1)
            if kicker09MID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in admin:
                        kicker09.acceptGroupInvitation(op.param1)
            if kicker10MID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in admin:
                        kicker10.acceptGroupInvitation(op.param1)
#==============================================================================#
        if op.type == 19:
            try:
                contact1 = cl.getContact(op.param2)
                group = cl.getGroup(op.param1)
                contact2 = cl.getContact(op.param3)
                if op.param2 in bots:
                    pass
                else:
                    print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n被踢者" + contact2.displayName + "\nMid:" + contact2.mid )
            except Exception as e:
                print(e)
#==============================================================================#
            if op.param1 in gcs["Lock"]:
                if op.param3 in gcs["Lock"][op.param1]:
                    if op.param2 in (gcs["Creater"][op.param1] or admin or bots):
                        pass
                    else:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                        except:
                            cl.kickoutFromGroup(op.param1, [op.param2])
                        for mi_d in gcs["Lock"][op.param1]:
                            try:
                                cl.findAndAddContactsByMid(mi_d)
                            except:
                                pass
                            cl.inviteIntoGroup(op.param1, [mi_d])
                        black["blacklist"][op.param2] = True
                        backupData()
            if op.param1 in pro["Kick"]:
                if (op.param1 in gcs['Creater'] and op.param2 in gcs['Creater'][op.param1]) or (op.param1 in gcs['Invite'] and op.param2 in gcs['Invite'][op.param1]) or (op.param2 in admin) or (op.param2 in bots):
                    pass
                else:
                    if op.param1 in pro['High']:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                        except:
                            cl.kickoutFromGroup(op.param1, [op.param2])
                    else:
                        if op.param1 in res['us']:
                            if op.param2 == res['us'][op.param1]:
                                res['num'][op.param1] += 1
                            else:
                                del res['num'][op.param1]
                                del res['us'][op.param1]
                                res['us'][op.param1] = op.param2
                                res['num'][op.param1] = 1
                        else:
                            res['us'][op.param1] = op.param2
                            res['num'][op.param1] = 1
                        if op.param1 in res['num']:
                            if res['num'][op.param1] >= 3:
                                if(op.param2 in admin) or (op.param2 in gcs['Creater'][op.param1]):
                                    del res['num'][op.param1]
                                    del res['us'][op.param1]
                                else:
                                    try:
                                        cl.kickoutFromGroup(op.param1, [op.param2])
                                    except:
                                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                                    cl.sendMessage(op.param1, "3回連続で退会させちゃったね(;´･ω･)")
                                if group.preventedJoinByTicket == False:
                                    group.preventedJoinByTicket = True
                                    random.choice(KAC).updateGroup(group)
                                else:
                                    pass
                                black["blacklist"][op.param2] = True
                                del res['num'][op.param1]
                                del res['us'][op.param1]
                                backupData()
            else:
                pass
#==============================================================================#
            if owner in op.param3:
                print("有人踢權限者")
                try:
                    random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                except:
                    cl.kickoutFromGroup(op.param1, [op.param2])
                try:
                    random.choice(KAC).inviteIntoGroup(op.param1, [owner])
                except:
                    cl.inviteIntoGroup(op.param1, [owner])
                black["blacklist"][op.param2] = True
                backupData()
            if clMID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n\n")
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    try:
                        random.choice(KAC).updateGroup(G)
                    except:
                        kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                    try:
                        try:
                            ghost01.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            ghost02.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                    baime.acceptGroupInvitationByTicket(op.param1, Ti)
                    orange.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    ghost02.updateGroup(G)
                    ghost01.leaveGroup(op.param1)
                    ghost02.leaveGroup(op.param1)
                    if op.param2 in black["blacklist"]:
                        pass
                    else:
                        black["blacklist"][op.param2] = True
                        backupData()
            if orangeMID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n\n")
                    G = cl.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    try:
                        random.choice(KAC).updateGroup(G)
                    except:
                        cl.updateGroup(G)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                    try:
                        try:
                            ghost01.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            ghost02.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                    baime.acceptGroupInvitationByTicket(op.param1, Ti)
                    orange.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    ghost02.updateGroup(G)
                    ghost01.leaveGroup(op.param1)
                    ghost02.leaveGroup(op.param1)
                    if op.param2 in black["blacklist"]:
                        pass
                    else:
                        black["blacklist"][op.param2] = True
                        backupData()
            if baimeMID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n\n")
                    G = cl.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    try:
                        random.choice(KAC).updateGroup(G)
                    except:
                        cl.updateGroup(G)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                    try:
                        try:
                            ghost01.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            ghost02.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                    baime.acceptGroupInvitationByTicket(op.param1, Ti)
                    orange.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    ghost02.updateGroup(G)
                    ghost01.leaveGroup(op.param1)
                    ghost02.leaveGroup(op.param1)
                    if op.param2 in black["blacklist"]:
                        pass
                    else:
                        black["blacklist"][op.param2] = True
                        backupData()
            if kicker01MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n\n")
                    G = kicker02.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    try:
                        random.choice(NK1).updateGroup(G)
                    except:
                        kicker02.updateGroup(G)
                    invsend = 0
                    Ti = kicker02.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                    try:
                        try:
                            ghost01.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            ghost02.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                    baime.acceptGroupInvitationByTicket(op.param1, Ti)
                    orange.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    ghost02.updateGroup(G)
                    ghost01.leaveGroup(op.param1)
                    ghost02.leaveGroup(op.param1)
                    if op.param2 in black["blacklist"]:
                        pass
                    else:
                        black["blacklist"][op.param2] = True
                        backupData()
            if kicker02MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n\n")
                    G = kicker02.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    try:
                        random.choice(NK2).updateGroup(G)
                    except:
                        kicker03.updateGroup(G)
                    invsend = 0
                    Ti = kicker03.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                    try:
                        try:
                            ghost01.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            ghost02.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                    baime.acceptGroupInvitationByTicket(op.param1, Ti)
                    orange.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    ghost02.updateGroup(G)
                    ghost01.leaveGroup(op.param1)
                    ghost02.leaveGroup(op.param1)
                    if op.param2 in black["blacklist"]:
                        pass
                    else:
                        black["blacklist"][op.param2] = True
                        backupData()
            if kicker03MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n\n")
                    G = kicker02.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    try:
                        random.choice(NK3).updateGroup
                    except:
                        kicker04.updateGroup(G)
                    invsend = 0
                    Ti = kicker04.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                    try:
                        try:
                            ghost01.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            ghost02.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                    baime.acceptGroupInvitationByTicket(op.param1, Ti)
                    orange.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    ghost02.updateGroup(G)
                    ghost01.leaveGroup(op.param1)
                    ghost02.leaveGroup(op.param1)
                    if op.param2 in black["blacklist"]:
                        pass
                    else:
                        black["blacklist"][op.param2] = True
                        backupData()
            if kicker04MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n\n")
                    G = kicker05.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    try:
                        random.choice(NK4).updateGroup(G)
                    except:
                        kicker05.updateGroup(G)
                    invsend = 0
                    Ti = kicker05.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                    try:
                        try:
                            ghost01.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            ghost02.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                    baime.acceptGroupInvitationByTicket(op.param1, Ti)
                    orange.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    ghost02.updateGroup(G)
                    ghost01.leaveGroup(op.param1)
                    ghost02.leaveGroup(op.param1)
                    if op.param2 in black["blacklist"]:
                        pass
                    else:
                        black["blacklist"][op.param2] = True
                        backupData()
            if kicker05MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n\n")
                    G = kicker06.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    try:
                        random.choice(NK5).updateGroup(G)
                    except:
                        kicker06.updateGroup(G)
                    invsend = 0
                    Ti = kicker06.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                    try:
                        try:
                            ghost01.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            ghost02.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                    baime.acceptGroupInvitationByTicket(op.param1, Ti)
                    orange.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    ghost02.updateGroup(G)
                    ghost01.leaveGroup(op.param1)
                    ghost02.leaveGroup(op.param1)
                    if op.param2 in black["blacklist"]:
                        pass
                    else:
                        black["blacklist"][op.param2] = True
                        backupData()
            if kicker06MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n\n")
                    G = kicker07.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    try:
                        random.choice(NK6).updateGroup(G)
                    except:
                        kicker07.updateGroup(G)
                    invsend = 0
                    Ti = kicker07.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                    try:
                        try:
                            ghost01.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            ghost02.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                    baime.acceptGroupInvitationByTicket(op.param1, Ti)
                    orange.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    ghost02.updateGroup(G)
                    ghost01.leaveGroup(op.param1)
                    ghost02.leaveGroup(op.param1)
                    if op.param2 in black["blacklist"]:
                        pass
                    else:
                        black["blacklist"][op.param2] = True
                        backupData()
            if kicker07MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n\n")
                    G = kicker08.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    try:
                        random.choice(NK7).updateGroup(G)
                    except:
                        kicker08.updateGroup(G)
                    invsend = 0
                    Ti = kicker08.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                    try:
                        try:
                            ghost01.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            ghost02.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                    baime.acceptGroupInvitationByTicket(op.param1, Ti)
                    orange.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    ghost02.updateGroup(G)
                    ghost01.leaveGroup(op.param1)
                    ghost02.leaveGroup(op.param1)
                    if op.param2 in black["blacklist"]:
                        pass
                    else:
                        black["blacklist"][op.param2] = True
                        backupData()
            if kicker08MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n\n")
                    G = kicker09.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    try:
                        random.choice(NK8).updateGroup(G)
                    except:
                        kicker09.updateGroup(G)
                    invsend = 0
                    Ti = kicker09.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                    try:
                        try:
                            ghost01.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            ghost02.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                    baime.acceptGroupInvitationByTicket(op.param1, Ti)
                    orange.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    ghost02.updateGroup(G)
                    ghost01.leaveGroup(op.param1)
                    ghost02.leaveGroup(op.param1)
                    if op.param2 in black["blacklist"]:
                        pass
                    else:
                        black["blacklist"][op.param2] = True
                        backupData()
            if kicker09MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n\n")
                    G = kicker10.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    try:
                        random.choice(NK9).updateGroup(G)
                    except:
                        kicker10.updateGroup(G)
                    invsend = 0
                    Ti = kicker10.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                    try:
                        try:
                            ghost01.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            ghost02.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                    baime.acceptGroupInvitationByTicket(op.param1, Ti)
                    orange.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    ghost02.updateGroup(G)
                    ghost01.leaveGroup(op.param1)
                    ghost02.leaveGroup(op.param1)
                    if op.param2 in black["blacklist"]:
                        pass
                    else:
                        black["blacklist"][op.param2] = True
                        backupData()
            if kicker10MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n\n")
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    try:
                        random.choice(NK10).updateGroup(G)
                    except:
                        kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost01.acceptGroupInvitationByTicket(op.param1, Ti)
                    ghost02.acceptGroupInvitationByTicket(op.param1, Ti)
                    try:
                        try:
                            ghost01.kickoutFromGroup(op.param1, [op.param2])
                        except:
                            ghost02.kickoutFromGroup(op.param1, [op.param2])
                    except:
                        print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                    baime.acceptGroupInvitationByTicket(op.param1, Ti)
                    orange.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    ghost02.updateGroup(G)
                    ghost01.leaveGroup(op.param1)
                    ghost02.leaveGroup(op.param1)
                    if op.param2 in black["blacklist"]:
                        pass
                    else:
                        black["blacklist"][op.param2] = True
                        backupData()
#==============================================================================#
        if op.type == 24:
            print ("[ 24 ] 通知離開副本")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
                baime.leaveRoom(op.param1)
                orange.leaveRoom(op.param1)
                kicker01.leaveRoom(op.param1)
                kicker02.leaveRoom(op.param1)
                kicker03.leaveRoom(op.param1)
                kicker04.leaveRoom(op.param1)
                kicker05.leaveRoom(op.param1)
                kicker06.leaveRoom(op.param1)
                kicker07.leaveRoom(op.param1)
                kicker08.leaveRoom(op.param1)
                kicker09.leaveRoom(op.param1)
                kicker10.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1]更新頭貼/個簽/名字")
        if op.type == 15:
            if op.param1 in settings["LeaveText"]:
                cmem = cl.getContact(op.param2)
                zx = ""
                zxc = ""
                zx2 = []
                xpesan = '我們的 '
                xjoin = ' 離開了群組'
                xname = str(cmem.displayName)
                pesan = ''
                pesan2 = pesan+"@c"
                xlen = str(len(zxc)+len(xpesan))
                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                zx = {'S':xlen, 'E':xlen2, 'M':cmem.mid}
                zx2.append(zx)
                zxc += pesan2
                text = xpesan + zxc + xjoin
                cl.sendMessage(op.param1, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
        if op.type == 17:
            if op.param1 in settings["JoinText"]:
                contact1 = cl.getContact(op.param2)
                group = cl.getGroup(op.param1)
                try:
                    arrData = ""
                    text = '%s'%("歡迎")
                    arr = []
                    mention = "@x"
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) -1)
                    arrData = {'S':slen,'E':elen,'M':op.param2}
                    arr.append(arrData)
                    text += mention + "進入{}".format(str(group.name))
                    cl.sendMessage(op.param1, text, {'MENTION':str('{"MENTIONS":' + json.dumps(arr) + '}')}, 0)
                except:
                    aa = '{"S":"0","E":"3","M":'+json.dumps(op.param2)+'}'
                    text = "歡迎進入" + group.name
                    mention = '@c \n'
                    text_ = mention + text
                    cl.sendMessage(op.param1, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)

        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in black["blacklist"]:
                        cl.sendMessage(to, "已經在黑名單了")
                        settings["wblack"] = False
                    else:
                        black["blacklist"][msg.contentMetadata["mid"]] = True
                        cl.sendMessage(to, "已加入黑名單")
                        settings["wblack"] = False
                    backupData()
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in black["blacklist"]:
                        del black["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(to, "已解除黑名單")
                        settings["dblack"] = False
                    else:
                        cl.sendMessage(to, "他不在黑名單")
                        settings["dblack"] = False
                    backupData()
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in black["pblack"]:
                        cl.sendMessage(to,"已經是永黑了")
                        settings["wblacklist"] = False
                    else:
                        black["pblack"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        cl.sendMessage(to,"已加入永黑")
                    backupData()
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in black["pblack"]:
                        del black["pblack"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"已刪除永黑")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        cl.sendMessage(to,"他不再永黑")
                    backupData()
                elif settings["convinv"] == True:
                    if sender in admins['Contect']:
                        gcs['Invite'][msg.to] = msg.contentMetadata["mid"]
                        settings["convinv"] = False
                        backupData()
                        mi_d = gcs['Invite'][msg.to]
                        name = cl.getContact(mi_d).displayName
                        aa = '{"S":"0","E":"3","M":'+json.dumps(mi_d)+'}'
                        cl.sendMessage(msg.to,"副群主已更改為: " + name)
                        try:
                            Tag(to, mi_d)
                        except:
                            pass
                        admins['Contect'] = {}
                    else:
                        pass
                elif settings["conadinv"] == True:
                    if sender in admins['Contect']:
                        gcs['Inviteadmin'][msg.to] = msg.contentMetadata["mid"]
                        settings["conadinv"] = False
                        backupData()
                        mi_d = gcs['Inviteadmin'][msg.to]
                        name = cl.getContact(mi_d).displayName
                        aa = '{"S":"0","E":"3","M":'+json.dumps(mi_d)+'}'
                        cl.sendMessage(msg.to,"邀請權限者已更改為: " + name)
                        try:
                            Tag(to, mi_d)
                        except:
                            pass
                        admins['Contect'] = {}
                    else:
                        pass
                elif settings["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ctime = int(round(contact.createdTime/1000))
                        ret_ = "[ 現在名稱 ]\n{}".format(msg.contentMetadata["displayName"])
                        ret_ += "\n\n[ 自訂名稱 ]\n{}".format(contact.displayNameOverridden)
                        ret_ += "\n\n[ 系統識別碼 ]\n{}".format(msg.contentMetadata["mid"])
                        ret_ += "\n\n[ 狀態消息 ]\n{}".format(contact.statusMessage)
                        ret_ += "\n\n[ 頭貼網址 ]\n{}".format("http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        ret_ += "\n\n[ 封面網址 ]\n{}".format(str(cu))
                        ret_ += "\n\n[ 建立日期 ]\n{}".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(ctime)))
                        cl.sendMessage(to, str(ret_))
                        #cl.sendMessage(to, "[顯示名稱]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[狀態消息]:\n" + contact.statusMessage + "\n[圖片網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        print(contact)
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        if contact.capableVoiceCall == False:
                            cocall = ""
                        else:
                            cocall = "語音通話中"
                        if contact.capableVideoCall == False:
                            cicall = ""
                        else:
                            cicall = "視訊通話中"
                        ctime = int(round(contact.createdTime/1000))
                        ret_ = "[ 現在名稱 ]\n{}".format(contact.displayName)
                        ret_ += "\n\n[ 自訂名稱 ]\n{}".format(contact.displayNameOverridden)
                        ret_ += "\n\n[ 系統識別碼 ]\n{}".format(msg.contentMetadata["mid"])
                        ret_ += "\n\n[ 狀態消息 ]\n{}".format(contact.statusMessage)
                        ret_ += "\n\n[ 頭貼網址 ]\n{}".format("http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        ret_ += "\n\n[ 封面網址 ]\n{}".format(str(cu))
                        ret_ += "\n\n[ 通話狀態 ]\n{}\n{}".format(str(cocall),str(cicall))
                        ret_ += "\n\n[ 建立日期 ]\n{}".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(ctime)))
                        cl.sendMessage(to, str(ret_))
                        #cl.sendMessage(msg.to,"[顯示名稱]\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[狀態消息]:\n" + contact.statusMessage + "\n[圖片網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
            if msg.contentType == 16:
                if settings["timeline"] == True:
                    if 'text' not in msg.contentMetadata:
                        if 'mediaOid' in msg.contentMetadata:
                            Object = msg.contentMetadata['mediaOid'].replace("svc=myhome|sid=h|","")
                            if msg.contentMetadata['mediaType'] == 'V':
                                if msg.contentMetadata['serviceType'] == 'GB':
                                    print("1")
                                    cl.sendMessage(msg.to, cl.getContact(sender).displayName + "把文章建立至記事本上\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&oid=" + msg.contentMetadata['mediaOid'] + "\n[媒體網址]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                                else:
                                    print("2")
                                    cl.sendMessage(msg.to, msg.contentMetadata['serviceName'] + "已分享了一篇文章\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&" + Object + "\n[媒體網址]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                            else:
                                if msg.contentMetadata['serviceType'] == 'GB':
                                    print("3")
                                    cl.sendMessage(msg.to, cl.getContact(sender).displayName + "把文章建立至記事本上\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                                else:
                                    print("4")
                                    cl.sendMessage(msg.to, cl.getContact(sender).displayName + "在群組相簿裡增加了圖片\n\n[相簿網址]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                        elif 'stickerId' in msg.contentMetadata:
                            if msg.contentMetadata['serviceType'] == 'GB':
                                print("5")
                                cl.sendMessage(msg.to, cl.getContact(sender).displayName + "把文章建立至記事本上\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                            else:
                                print("6")
                                cl.sendMessage(msg.to, msg.contentMetadata['serviceName'] + "已分享了一篇文章\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                        else:
                            if msg.contentMetadata['serviceType'] == 'GB':
                                print("7")
                                cl.sendMessage(msg.to, cl.getContact(sender).displayName + "把文章建立至記事本上\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl'])
                            else:
                                print("8")
                                cl.sendMessage(msg.to, msg.contentMetadata['serviceName'] + "已分享了一篇文章\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl'])
                    else:
                        if 'mediaOid' in msg.contentMetadata:
                            Object = msg.contentMetadata['mediaOid'].replace("svc=myhome|sid=h|","")
                            if msg.contentMetadata['mediaType'] == 'V':
                                if msg.contentMetadata['serviceType'] == 'GB':
                                    print("9")
                                    cl.sendMessage(msg.to, cl.getContact(sender).displayName + "把文章建立至記事本上\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl'] + "\n文章內容\n[僅提供100字內]" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&oid=" + msg.contentMetadata['mediaOid'] + "\n[媒體網址]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                                else:
                                    print("10")
                                    cl.sendMessage(msg.to, msg.contentMetadata['serviceName'] + "已分享了一篇文章\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl'] + "\n文章內容\n[僅提供100字內]" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&" + Object + "\n[媒體網址]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                            else:
                                print("11")
                                if msg.contentMetadata['serviceType'] == 'GB':
                                    cl.sendMessage(msg.to, cl.getContact(sender).displayName + "把文章建立至記事本上\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl']+ "\n文章內容\n[僅提供100字內]" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                                else:
                                    print("12")
                                    cl.sendMessage(msg.to, msg.contentMetadata['serviceName'] + "已分享了一篇文章\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl']+ "\n文章內容\n[僅提供100字內]" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                        elif 'stickerId' in msg.contentMetadata:
                            if msg.contentMetadata['serviceType'] == 'GB':
                                print("13")
                                cl.sendMessage(msg.to, cl.getContact(sender).displayName + "把文章建立至記事本上\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl'] + "\n文章內容\n[僅提供100字內]" + msg.contentMetadata['text'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                            else:
                                print("14")
                                cl.sendMessage(msg.to, msg.contentMetadata['serviceName'] + "已分享了一篇文章\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl'] + "\n文章內容\n[僅提供100字內]" + msg.contentMetadata['text'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                        else:
                            if msg.contentMetadata['serviceType'] == 'GB':
                                print("15")
                                cl.sendMessage(msg.to, cl.getContact(sender).displayName + "把文章建立至記事本上\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl'] + "\n文章內容\n[僅提供100字內]" + msg.contentMetadata['text'])
                            else:
                                print("16")
                                cl.sendMessage(msg.to, msg.contentMetadata['serviceName'] + "已分享了一篇文章\n\n[文章網址]\n" + msg.contentMetadata['postEndUrl'] + "\n文章內容\n[僅提供100字內]" + msg.contentMetadata['text'])
                            #msg.contentType = 0
                            #msg.text = "作者:\n" + cl.getContact(sender).displayName + "\n文章內容\n[僅提供100字內][僅提供100字內]\n" + msg.contentMetadata['text'] + "\n文章網址\n" + msg.contentMetadata['postEndUrl']
                            #cl.sendMessage(to, msg.text)
            if msg.contentType == 0:
              if sender in admin:
                if msg.text is None:
                    pass
#==============================================================================#
                elif text.lower() == 'help':
                    if sender in Owner:
                        helpMessage = helpmessage()
                        cl.sendMessage(to, str(helpMessage))
                        cl.sendContact(to, "u28d781fa3ba9783fd5144390352b0c24")
                    else:
                        helpMessageLv1 = helpmessagelv1()
                        cl.sendMessage(to, str(helpMessageLv1))
                        cl.sendContact(to, "u28d781fa3ba9783fd5144390352b0c24")
                elif text.lower() == 'helptag':
                    if sender in Owner:
                        helpMessageTag = helpmessagetag()
                        cl.sendMessage(to, str(helpMessageTag))
                elif text.lower() == 'helpkick':
                    if sender in Owner:
                        helpMessageKick = helpmessagekick()
                        cl.sendMessage(to, str(helpMessageKick))
                elif text.lower() == 'helpbot':
                    if sender in Owner:
                        helpMessageBot = helpmessagebot()
                        cl.sendMessage(to, str(helpMessageBot))
                elif text.lower() == 'Error':
                    if sender in Owner:
                        ErrorText = errortext()
                        cl.sendMessage(to, str(ErrorText))
#==============================================================================#
                elif "clFbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("clFbc:","")
                        t = cl.getAllContactIds()
                        try:
                            for manusia in t:
                                cl.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K1Fbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K1Fbc:","")
                        t = kicker01.getAllContactIds()
                        try:
                            for manusia in t:
                                kicker01.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K2Fbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K2Fbc:","")
                        t = kicker02.getAllContactIds()
                        try:
                            for manusia in t:
                                kicker02.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K3Fbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K3Fbc:","")
                        t = kicker03.getAllContactIds()
                        try:
                            for manusia in t:
                                kicker03.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K4Fbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K4Fbc:","")
                        t = kicker04.getAllContactIds()
                        try:
                            for manusia in t:
                                kicker04.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K5Fbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K5Fbc:","")
                        t = kicker05.getAllContactIds()
                        try:
                            for manusia in t:
                                kicker05.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K6Fbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K6Fbc:","")
                        t = kicker06.getAllContactIds()
                        try:
                            for manusia in t:
                                kicker06.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K7Fbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K7Fbc:","")
                        t = kicker07.getAllContactIds()
                        try:
                            for manusia in t:
                                kicker07.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K8Fbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K8Fbc:","")
                        t = kicker08.getAllContactIds()
                        try:
                            for manusia in t:
                                kicker08.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K9Fbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K9Fbc:","")
                        t = kicker09.getAllContactIds()
                        try:
                            for manusia in t:
                                kicker09.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K10Fbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K10Fbc:","")
                        t = kicker10.getAllContactIds()
                        try:
                            for manusia in t:
                                kicker10.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
#==============================================================================#
                elif "clGbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("clGbc:","")
                        n = cl.getGroupIdsJoined()
                        try:
                            for manusia in n:
                                cl.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K1Gbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K1Gbc:","")
                        n = kicker01.getGroupIdsJoined()
                        try:
                            for manusia in n:
                                kicker01.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K2Gbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K2Gbc:","")
                        n = kicker02.getGroupIdsJoined()
                        try:
                            for manusia in n:
                                kicker02.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K3Gbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K3Gbc:","")
                        n = kicker03.getGroupIdsJoined()
                        try:
                            for manusia in n:
                                kicker03.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K4Gbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K4Gbc:","")
                        n = kicker04.getGroupIdsJoined()
                        try:
                            for manusia in n:
                                kicker04.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K5Gbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K5Gbc:","")
                        n = kicker05.getGroupIdsJoined()
                        try:
                            for manusia in n:
                                kicker05.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K6Gbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K6Gbc:","")
                        n = kicker06.getGroupIdsJoined()
                        try:
                            for manusia in n:
                                kicker06.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K7Gbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K7Gbc:","")
                        n = kicker07.getGroupIdsJoined()
                        try:
                            for manusia in n:
                                kicker07.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K8Gbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K8Gbc:","")
                        n = kicker08.getGroupIdsJoined()
                        try:
                            for manusia in n:
                                kicker08.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K9Gbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K9Gbc:","")
                        n = kicker09.getGroupIdsJoined()
                        try:
                            for manusia in n:
                                kicker09.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
                elif "K10Gbc:" in msg.text:
                    if sender in Owner:
                        bctxt = text.replace("K10Gbc:","")
                        n = kicker10.getGroupIdsJoined()
                        try:
                            for manusia in n:
                                kicker10.sendMessage(manusia,(bctxt))
                        except Exception as e:
                            print(e)
#==============================================================================#
                elif 'alljoin' in text.lower():
                    if sender in Owner:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == False:
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                baime.acceptGroupInvitationByTicket(to, Ti)
                                orange.acceptGroupInvitationByTicket(to, Ti)
                                kicker01.acceptGroupInvitationByTicket(to, Ti)
                                kicker02.acceptGroupInvitationByTicket(to, Ti)
                                kicker03.acceptGroupInvitationByTicket(to, Ti)
                                kicker04.acceptGroupInvitationByTicket(to, Ti)
                                kicker05.acceptGroupInvitationByTicket(to, Ti)
                                kicker06.acceptGroupInvitationByTicket(to, Ti)
                                kicker07.acceptGroupInvitationByTicket(to, Ti)
                                kicker08.acceptGroupInvitationByTicket(to, Ti)
                                kicker09.acceptGroupInvitationByTicket(to, Ti)
                                kicker10.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                baime.acceptGroupInvitationByTicket(to,Ti)
                                orange.acceptGroupInvitationByTicket(to, Ti)
                                kicker01.acceptGroupInvitationByTicket(to, Ti)
                                kicker02.acceptGroupInvitationByTicket(to, Ti)
                                kicker03.acceptGroupInvitationByTicket(to, Ti)
                                kicker04.acceptGroupInvitationByTicket(to, Ti)
                                kicker05.acceptGroupInvitationByTicket(to, Ti)
                                kicker06.acceptGroupInvitationByTicket(to, Ti)
                                kicker07.acceptGroupInvitationByTicket(to, Ti)
                                kicker08.acceptGroupInvitationByTicket(to, Ti)
                                kicker09.acceptGroupInvitationByTicket(to, Ti)
                                kicker10.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                elif '1join' in text.lower():
                    if sender in Owner:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == False:
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker01.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker01.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                elif '2join' in text.lower():
                    if sender in Owner:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == False:
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker02.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker02.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                elif '3join' in text.lower():
                    if sender in Owner:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == False:
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker03.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker03.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                elif '4join' in text.lower():
                    if sender in Owner:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == False:
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker04.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker04.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                elif '5join' in text.lower():
                    if sender in Owner:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == False:
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker05.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker05.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                elif '6join' in text.lower():
                    if sender in Owner:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == False:
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker06.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker06.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                elif '7join' in text.lower():
                    if sender in Owner:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == False:
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker07.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker07.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                elif '8join' in text.lower():
                    if sender in Owner:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == False:
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker04.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker08.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                elif '9join' in text.lower():
                    if sender in Owner:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == False:
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker09.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker09.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                elif '10join' in text.lower():
                    if sender in Owner:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == False:
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker10.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ti = cl.reissueGroupTicket(to)
                                kicker10.acceptGroupInvitationByTicket(to, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                elif text.lower() == 'all bye':
                    if sender in Owner:
                        if msg.toType == 2:
                            ginfo = cl.getGroup(to)
                            try:
                                orange.leaveGroup(to)
                                baime.leaveGroup(to)
                                kicker01.leaveGroup(to)
                                kicker02.leaveGroup(to)
                                kicker03.leaveGroup(to)
                                kicker04.leaveGroup(to)
                                kicker05.leaveGroup(to)
                                kicker06.leaveGroup(to)
                                kicker07.leaveGroup(to)
                                kicker08.leaveGroup(to)
                                kicker09.leaveGroup(to)
                                kicker10.leaveGroup(to)
                                cl.leaveGroup(to)
                            except:
                                pass
                elif text.lower() == 'bye bye':
                    if sender in Owner:
                        if msg.toType == 2:
                            ginfo = cl.getGroup(to)
                            try:
                                orange.leaveGroup(to)
                                baime.leaveGroup(to)
                            except:
                                pass
                elif text.lower() == 'bot bye':
                    if sender in Owner:
                        if msg.toType == 2:
                            ginfo = cl.getGroup(to)
                            try:
                                kicker01.leaveGroup(to)
                                kicker02.leaveGroup(to)
                                kicker03.leaveGroup(to)
                                kicker04.leaveGroup(to)
                                kicker05.leaveGroup(to)
                                kicker06.leaveGroup(to)
                                kicker07.leaveGroup(to)
                                kicker08.leaveGroup(to)
                                kicker09.leaveGroup(to)
                                kicker10.leaveGroup(to)
                            except:
                                pass
                elif text.lower() == 'leave':
                    if sender in Owner:
                        kicker01.leaveRoom(to)
                        kicker02.leaveRoom(to)
                        kicker03.leaveRoom(to)
                        kicker04.leaveRoom(to)
                        kicker05.leaveRoom(to)
                        kicker06.leaveRoom(to)
                        kicker07.leaveRoom(to)
                        kicker08.leaveRoom(to)
                        kicker09.leaveRoom(to)
                        kicker10.leaveRoom(to)

                elif text.lower() == 'test':
                    if sender in Owner:
                        time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=5000)
                        str1 = str(time0)
                        start = time.time()
                        cl.sendMessage(to,'處理速度\n' + str1 + '秒')
                        elapsed_time = time.time() - start
                        cl.sendMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒')
                        try:
                            baime.sendMessage(to, 'ok')
                        except:
                            pass
                        try:
                            orange.sendMessage(to, 'ok')
                        except:
                            pass
                        try:
                            kicker01.sendMessage(to, 'ok')
                        except:
                            pass
                        try:
                            kicker02.sendMessage(to, 'ok')
                        except:
                            pass
                        try:
                            kicker03.sendMessage(to, 'ok')
                        except:
                            pass
                        try:
                            kicker04.sendMessage(to, 'ok')
                        except:
                            pass
                        try:
                            kicker05.sendMessage(to, 'ok')
                        except:
                            pass
                        try:
                            kicker06.sendMessage(to, 'ok')
                        except:
                            pass
                        try:
                            kicker07.sendMessage(to, 'ok')
                        except:
                            pass
                        try:
                            kicker08.sendMessage(to, 'ok')
                        except:
                            pass
                        try:
                            kicker09.sendMessage(to, 'ok')
                        except:
                            pass
                        try:
                            kicker10.sendMessage(to, 'ok')
                        except:
                            pass
                    #elif 'invitebot' in text.lower():
                    #if sender in Owner:
                    #if msg.toType == 2:
                    #    group = cl.getGroup(to)
                    #    try:
                    #        group.preventedJoinByTicket = False
                    #        cl.updateGroup(group)
                    #        str1 = cl.reissueGroupTicket(to)
                    #    except Exception as e:
                    #        print(e)
                    #    cl.sendMessage(mid2, "/jgurlx gid: " + msg.to + " gid " + "url: http://line.me/R/ti/g/" + str1 + " url")
                    #    cl.sendMessage(mid3, "/jgurlx gid: " + msg.to + " gid " + "url: http://line.me/R/ti/g/" + str1 + " url")
                    #    cl.sendMessage(mid4, "/jgurlx gid: " + msg.to + " gid " + "url: http://line.me/R/ti/g/" + str1 + " url")
                    #    cl.sendMessage(mid5, "/jgurlx gid: " + msg.to + " gid " + "url: http://line.me/R/ti/g/" + str1 + " url")
                    #    cl.sendMessage(mid6, "/jgurlx gid: " + msg.to + " gid " + "url: http://line.me/R/ti/g/" + str1 + " url")
                elif text.startswith("/jgurlx"):
                    str1 = find_between_r(msg.text, "gid: ", " gid")
                    str2 = find_between_r(msg.text, "url: http://line.me/R/ti/g/", " url")
                    cl.acceptGroupInvitationByTicket(str1, str2)
                    JoinedGroups.append(str1)
                    group = cl.getGroup(str1)
                    try:
                        cl.reissueGroupTicket(str1)
                        group.preventedJoinByTicket = True
                        cl.updateGroup(group)
                    except Exception as e:
                        print(e)

                elif text.lower() == 'gj':
                    if sender in Owner:
                        if msg.toType == 2:
                            G = cl.getGroup(msg.to)
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(msg.to)
                            ghost01.acceptGroupInvitationByTicket(to, Ti)
                            ghost02.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            try:
                                ghost02.updateGroup(G)
                            except:
                                try:
                                    random.choice(KAC).updateGroup(G)
                                except:
                                    cl.updateGroup(G)
    
                elif text.lower() == 'gbye':
                    if sender in Owner:
                        if msg.toType == 2:
                            ginfo = cl.getGroup(to)
                            try:
                                ghost01.leaveGroup(to)
                            except:
                                pass
                            try:
                                ghost02.leaveGroup(to)
                            except:
                                pass
#==============================================================================#
                elif text.lower() == 'conac':
                    if sender in Owner:
                        admins["Mids"] = {}
                        group = cl.getGroups([to])
                        Mids = [contact.mid for contact in group[0].members]
                        for mmid in Mids:
                            admins["Mids"][mmid] = True
                        backupData()
                elif text.lower() == 'conv':
                    if sender in Owner:
                        if admins["Mids"] == {}:
                            pass
                        else:
                            Mids = []
                            for mi_d in admins["Mids"]:
                                Mids.append(mi_d)
                                try:
                                    cl.findAndAddContactsByMid(mi_d)
                                except:
                                    pass
                            mids = Mids[:33]
                            try:
                                cl.inviteIntoGroup(to, mids)
                            except Exception as e:
                                print(e)
#==============================================================================#
                elif "Ri " in msg.text:
                    if sender in Owner:
                        Ri0 = text.replace("Ri ","")
                        Ri1 = Ri0.rstrip()
                        Ri2 = Ri1.replace("@","")
                        Ri3 = Ri2.rstrip()
                        _name = Ri3
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                if target in admin:
                                    pass
                                else:
                                    try:
                                        cl.kickoutFromGroup(to,[target])
                                        cl.findAndAddContactsByMid(target)
                                        cl.inviteIntoGroup(to,[target])
                                    except:
                                        pass
                elif "Claguk:" in msg.text:
                    if sender in Owner:
                        midd = text.replace("Claguk:","")
                        n = cl.getGroupIdsJoined()
                        try:
                            for manusia in n:
                                try:
                                    cl.kickoutFromGroup(manusia, [midd])
                                    print(manusia + "\n" + midd + "\n")
                                except:
                                    print(manusia)
                            cl.sendMessage(to, "已針對全群踢除")
                        except Exception as e:
                            print(e)
                elif "Uk " in msg.text:
                    if sender in Owner:
                        midd = text.replace("Uk ","")
                        cl.kickoutFromGroup(to,[midd])
                elif "Tk " in msg.text:
                    if sender in Owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Tkk " in msg.text:
                    if sender in Owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    klist = [kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10]
                                    kickers = random.choice(klist)
                                    kickers.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Mk " in msg.text:
                    if sender in Lv1:
                        Mk0 = text.replace("Mk ","")
                        Mk1 = Mk0.rstrip()
                        Mk2 = Mk1.replace("@","")
                        Mk3 = Mk2.rstrip()
                        _name = Mk3
                        gs = cl.getGroup(to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                if target in admin:
                                    pass
                                else:
                                    try:
                                        cl.kickoutFromGroup(to,[target])
                                    except:
                                        pass
                elif "Mkk " in msg.text:
                    if sender in Owner:
                        Mkk0 = text.replace("Mkk ","")
                        Mkk1 = Mkk0.rstrip()
                        Mkk2 = Mkk1.replace("@","")
                        Mkk3 = Mkk2.rstrip()
                        _name = Mkk3
                        gs = cl.getGroup(to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                if target in admin:
                                    pass
                                else:
                                    try:
                                        klist = [kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10]
                                        kickers = random.choice(klist)
                                        kickers.kickoutFromGroup(to,[target])
                                    except:
                                        pass
                elif "Nk " in msg.text:
                    if sender in Owner:
                        _name = text.replace("Nk ","")
                        gs = cl.getGroup(to)
                        targets = []
                        try:
                            cl.unsendMessage(msg_id)
                        except:
                            pass
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                if target in admin:
                                    pass
                                else:
                                    try:
                                        cl.kickoutFromGroup(to,[target])
                                    except:
                                        pass
                elif "Nkk " in msg.text:
                    if sender in Owner:
                        _name = text.replace("Nkk ","")
                        gs = cl.getGroup(to)
                        try:
                            cl.unsendMessage(msg_id)
                        except:
                            pass
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                if target in admin:
                                    pass
                                else:
                                    try:
                                        klist = [kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10]
                                        kickers = random.choice(klist)
                                        kickers.kickoutFromGroup(to,[target])
                                    except:
                                        pass
                elif "Zk" in msg.text:
                    if sender in Owner:
                        gs = cl.getGroup(to)
                        targets = []
                        for g in gs.members:
                            if g.displayName in "":
                                targets.append(g.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                if target in admin:
                                    pass
                                else:
                                    try:
                                        cl.kickoutFromGroup(to,[target])
                                    except:
                                        pass
                elif "Zkk" in msg.text:
                    if sender in Owner:
                        gs = cl.getGroup(to)
                        targets = []
                        for g in gs.members:
                            if g.displayName in "":
                                targets.append(g.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                if target in admin:
                                    pass
                                else:
                                    try:
                                        klist = [kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10]
                                        kickers = random.choice(klist)
                                        kickers.kickoutFromGroup(to,[target])
                                    except:
                                        pass
                elif "Nkn " in msg.text:
                    if sender in Owner:
                        _name = text.replace("Nkn ","")
                        gs = cl.getGroup(to)
                        targets = []
                        try:
                            cl.unsendMessage(msg_id)
                        except:
                            pass
                        for g in gs.members:
                            if _name in g.displayName:
                                pass
                            else:
                                targets.append(g.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                if target in admin:
                                    pass
                                else:
                                    try:
                                        cl.kickoutFromGroup(to,[target])
                                    except:
                                        pass
                elif "Nkkn " in msg.text:
                    if sender in Owner:
                        _name = text.replace("Nkkn ","")
                        gs = cl.getGroup(to)
                        targets = []
                        try:
                            cl.unsendMessage(msg_id)
                        except:
                            pass
                        for g in gs.members:
                            if _name in g.displayName:
                                pass
                            else:
                                targets.append(g.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                if target in admin:
                                    pass
                                else:
                                    try:
                                        klist = [kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10]
                                        kickers = random.choice(klist)
                                        kickers.kickoutFromGroup(to,[target])
                                    except:
                                        pass
                elif "Dk " in msg.text:
                    if sender in Owner:
                        _name = text.replace("Dk ","")
                        gs = cl.getGroup(to)
                        targets = []
                        try:
                            cl.unsendMessage(msg_id)
                        except:
                            pass
                        for g in gs.members:
                            try:
                                contact = cl.getContact(g.mid)
                                if _name in contact.displayNameOverridden:
                                    targets.append(g.mid)
                            except:
                                pass
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                if target in admin:
                                    pass
                                else:
                                    try:
                                        cl.kickoutFromGroup(to,[target])
                                    except:
                                        pass
                elif "Dkk " in msg.text:
                    if sender in Owner:
                        _name = text.replace("Dkk ","")
                        gs = cl.getGroup(to)
                        targets = []
                        try:
                            cl.unsendMessage(msg_id)
                        except:
                            pass
                        for g in gs.members:
                            try:
                                contact = cl.getContact(g.mid)
                                if _name in contact.displayNameOverridden:
                                    targets.append(g.mid)
                            except:
                                pass
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                if target in admin:
                                    pass
                                else:
                                    try:
                                        klist = [kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10]
                                        kickers = random.choice(klist)
                                        kickers.kickoutFromGroup(to,[target])
                                    except:
                                        pass
                elif "Vk:" in text:
                    if sender in Owner:
                        midd = msg.text.replace("Vk:","")
                        cl.kickoutFromGroup(msg.to,[midd])
                        cl.findAndAddContactsByMid(midd)
                        cl.inviteIntoGroup(msg.to,[midd])
                        cl.cancelGroupInvitation(msg.to,[midd])
                elif "Vk " in msg.text:
                    if sender in Owner:
                        vkick0 = msg.text.replace("Vk ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(msg.to,[target])
                                    cl.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass
                elif "Ulti " in msg.text:
                    if sender in Owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        G = cl.getGroup(msg.to)
                        G.preventedJoinByTicket = False
                        try:
                            random.choice(KAC).updateGroup(G)
                        except:
                            cl.updateGroup(G)
                        invsend = 0
                        Ti = cl.reissueGroupTicket(msg.to)
                        ghost01.acceptGroupInvitationByTicket(to, Ti)
                        ghost02.acceptGroupInvitationByTicket(to, Ti)
                        time.sleep(0.2)
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        else:
                            for target in targets:
                                try:
                                    ghost01.kickoutFromGroup(to, [target])
                                except:
                                    pass
                        G.preventedJoinByTicket = True
                        try:
                            ghost02.updateGroup(G)
                        except:
                            try:
                                random.choice(KAC).updateGroup(G)
                            except:
                                cl.updateGroup(G)
                        ghost01.leaveGroup(to)
                        ghost02.leaveGroup(to)
#==============================================================================#
                elif "NT " in msg.text:
                    if sender in Owner:
                        _name = text.replace("NT ","")
                        gs = cl.getGroup(to)
                        txt = u''
                        s=0
                        b=[]
                        for g in gs.members:
                            if _name in g.displayName:
                                b.append({"S":str(s), "E" :str(s+6), "M":g.mid})
                                s += 7
                                txt += u'@CoCo \n'
                        if b == []:
                            cl.sendMessage(to, "這個群組沒有這個人")
                        else:
                            cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                elif text.lower() == 'zt':
                    if sender in Owner:
                        gs = cl.getGroup(to)
                        txt = u''
                        s=0
                        b=[]
                        for g in gs.members:
                            if g.displayName in "":
                                b.append({"S":str(s), "E" :str(s+6), "M":g.mid})
                                s += 7
                                txt += u'@CoCo \n'
                        if b == []:
                            cl.sendMessage(to, "這個群組沒有名字0字的人")
                        else:
                            cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                elif "NTN " in msg.text:
                    if sender in Owner:
                        _name = text.replace("NTN ","")
                        gs = cl.getGroup(to)
                        txt = u''
                        s=0
                        b=[]
                        for g in gs.members:
                            if _name in g.displayName:
                                pass
                            else:
                                b.append({"S":str(s), "E" :str(s+6), "M":g.mid})
                                s += 7
                                txt += u'@CoCo \n'
                        if b == []:
                            cl.sendMessage(to, "這個群組沒有這個人")
                        else:
                            cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                elif "DT " in msg.text:
                    if sender in Owner:
                        _name = text.replace("DT ","")
                        gs = cl.getGroup(to)
                        txt = u''
                        s=0
                        b=[]
                        for g in gs.members:
                            try:
                                contact = cl.getContact(g.mid)
                                if _name in contact.displayNameOverridden:
                                    b.append({"S":str(s), "E" :str(s+6), "M":g.mid})
                                    s += 7
                                    txt += u'@CoCo \n'
                            except:
                                pass
                        if b == []:
                            cl.sendMessage(to, "這個群組沒有這個人")
                        else:
                            cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
#==============================================================================#
                elif text.lower() == 'zm':
                    if sender in Owner:
                        gs = cl.getGroup(to)
                        lists = []
                        for g in gs.members:
                            if g.displayName in "":
                                lists.append(g.mid)
                        if lists == []:
                            cl.sendMessage(to, "這個群組沒有名字0字的人")
                        else:
                            mc = ""
                            for mi_d in lists:
                                mc += "->" + mi_d + "\n"
                            cl.sendMessage(to,mc)
                elif text.lower() == 'zc':
                    if sender in Owner:
                        gs = cl.getGroup(to)
                        lists = []
                        for g in gs.members:
                            if g.displayName in "":
                                lists.append(g.mid)
                        if lists == []:
                            cl.sendMessage(to, "這個群組沒有名字0字的人")
                        else:
                            for ls in lists:
                                contact = cl.getContact(ls)
                                mi_d = contact.mid
                                cl.sendContact(to, mi_d)
#==============================================================================#
                elif "Mc " in msg.text:
                    if sender in Owner:
                        mmid = msg.text.replace("Mc ","")
                        cl.sendContact(to, mmid)
                elif "Sc " in msg.text:
                    if sender in Owner:
                        ggid = msg.text.replace("Sc ","")
                        group = cl.getGroup(ggid)
                        try:
                            gtime = group.createdTime
                            gtimee = int(round(gtime/1000))
                        except Exception as e:
                            cl.sendMessage(msg.to,str(e))
                        if ggid in gcs["Creater"]:
                            try:
                                mi_d = gcs["Creater"][ggid]
                                gCreator = cl.getContact(mi_d).displayName
                            except:
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "未找到"
                        else:
                            try:
                                gCreator = group.creator.displayName
                            except:
                                gCreator = "未找到"
                        if group.invitee is None:
                            gPending = "0"
                        else:
                            gPending = str(len(group.invitee))
                        if group.preventedJoinByTicket == True:
                            gQr = "關閉"
                            gTicket = "沒有"
                        else:
                            gQr = "開啟"
                            gTicket = "https://cl.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                        path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                        ret_ = "╔══[ 群組資料 ]"
                        ret_ += "\n╠ 顯示名稱 : {}".format(str(group.name))
                        ret_ += "\n╠ 群組ＩＤ : {}".format(group.id)
                        ret_ += "\n╠ 群組作者 : {}".format(str(gCreator))
                        ret_ += "\n╠ 成員數量 : {}".format(str(len(group.members)))
                        ret_ += "\n╠ 邀請數量 : {}".format(gPending)
                        ret_ += "\n╠ 群組網址 : {}".format(gQr)
                        ret_ += "\n╠ 群組網址 : {}".format(gTicket)
                        ret_ += "\n╠ 群組建立時間 : {}".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(gtimee)))
                        ret_ += "\n╚══[ 完 ]"
                        cl.sendMessage(to, str(ret_))
                        try:
                            cl.sendImageWithURL(to, path)
                        except:
                            cl.sendMessage(to, "這個群組沒有頭貼喔")
#==============================================================================#
                elif msg.text in ["c","C","cancel","Cancel"]:
                    if sender in Owner:
                        if msg.toType == 2:
                            X = cl.getGroup(msg.to)
                            if X.invitee is not None:
                                gInviMids = (contact.mid for contact in X.invitee)
                                ginfo = cl.getGroup(msg.to)
                                sinvitee = str(len(ginfo.invitee))
                                start = time.time()
                                for cancelmod in gInviMids:
                                    cl.cancelGroupInvitation(to, [cancelmod])
                                elapsed_time = time.time() - start
                                cl.sendMessage(to, "已取消完成\n取消時間: %s秒" % (elapsed_time))
                                cl.sendMessage(to, "取消人數:" + sinvitee)
                        else:
                            cl.sendMessage(to, "沒有任何人在邀請中！！")
                elif "C:" in msg.text:
                    if sender in Owner:
                        if msg.toType == 2:
                            mmid = text.replace("C:","")
                            try:
                                cl.cancelGroupInvitation(to, [mmid])
                            except:
                                cl.sendMessage(to, "他不在邀請中！！")
                elif text.lower() == 'gcancel':
                    if sender in Owner:
                        gid = cl.getGroupIdsInvited()
                        start = time.time()
                        for i in gid:
                            cl.rejectGroupInvitation(i)
                        elapsed_time = time.time() - start
                        cl.sendMessage(to, "全部群組邀請已取消")
                        cl.sendMessage(to, "取消時間: %s秒" % (elapsed_time))
#==============================================================================#
                elif "Gn " in msg.text:
                    if sender in Lv1:
                        if msg.toType == 2:
                            X = cl.getGroup(msg.to)
                            X.name = msg.text.replace("Gn ","")
                            cl.updateGroup(X)
                        else:
                            cl.sendMessage(msg.to,"無法使用在群組外")

                elif "Gc" in msg.text:
                    if sender in Lv1:
                        if msg.toType == 2:
                            key = eval(msg.contentMetadata["MENTION"])
                            u = key["MENTIONEES"][0]["M"]
                            contact = cl.getContact(u)
                            cu = cl.getProfileCoverURL(mid=u)
                            try:
                                cu = cl.getProfileCoverURL(content.mid)
                            except:
                                cu = ""
                            try:
                                ctime = int(round(contact.createdTime/1000))
                                ret_ = "[ 現在名稱 ]\n{}".format(contact.displayName)
                                ret_ += "\n\n[ 自訂名稱 ]\n{}".format(contact.displayNameOverridden)
                                ret_ += "\n\n[ 系統識別碼 ]\n{}".format(contact.mid)
                                ret_ += "\n\n[ 狀態消息 ]\n{}".format(contact.statusMessage)
                                ret_ += "\n\n[ 頭貼網址 ]\n{}".format("http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                                ret_ += "\n\n[ 封面網址 ]\n{}".format(str(cu))
                                ret_ += "\n\n[ 建立日期 ]\n{}".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(ctime)))
                            except:
                                ctime = int(round(contact.createdTime/1000))
                                ret_ = "[ 現在名稱 ]\n{}".format(contact.displayName)
                                ret_ += "\n\n[ 自訂名稱 ]\n{}".format(contact.displayNameOverridden)
                                ret_ += "\n\n[ 系統識別碼 ]\n{}".format(contact.mid)
                                ret_ += "\n\n[ 狀態消息 ]\n{}".format(contact.statusMessage)
                                ret_ += "\n\n[ 封面網址 ]\n{}".format(str(cu))
                                ret_ += "\n\n[ 建立日期 ]\n{}".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(ctime)))
                            cl.sendMessage(to, str(ret_))
                elif "Inv " in msg.text:
                    if sender in Owner:
                        try:
                            midd = msg.text.replace("Inv ","")
                            cl.findAndAddContactsByMid(midd)
                            cl.inviteIntoGroup(msg.to,[midd])
                        except:
                            cl.sendMessage(to, "Mid錯誤")
#==============================================================================#
                elif msg.text in ["Ban"]:
                    if sender in Owner:
                        settings["wblack"] = True
                        backupData()
                        cl.sendMessage(msg.to,"請丟出好友資料")
                elif msg.text in ["Unban"]:
                    if sender in Owner:
                        settings["dblack"] = True
                        backupData()
                        cl.sendMessage(msg.to,"請丟出好友資料")
                elif "Ban:" in msg.text:
                    if sender in Owner:
                        midd = msg.text.replace("Ban:","")
                        try:
                            black["blacklist"][midd] = True
                            backupData()
                            cl.sendMessage(to, "已加入黑名單")
                        except:
                            pass
                elif "Unban:" in msg.text:
                    if sender in Owner:
                        midd = msg.text.replace("Unban:","")
                        try:
                            del black["blacklist"][midd]
                            backupData()
                            cl.sendMessage(to, "已解除黑名單")
                        except:
                            pass
                elif "Ban " in msg.text:
                    if sender in Owner:
                        if msg.toType == 2:
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    try:
                                        black["blacklist"][target] = True
                                        backupData()
                                        cl.sendMessage(to, "已加入黑名單")
                                    except:
                                        pass
                elif "Unban " in msg.text:
                    if sender in Owner:
                        if msg.toType == 2:
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    try:
                                        del black["blacklist"][target]
                                        backupData()
                                        cl.sendMessage(to, "已解除黑名單")
                                    except:
                                            pass
                elif text.lower() == 'clear ban':
                    if sender in Owner:
                        for mi_d in black["blacklist"]:
                            black["blacklist"] = {}
                        cl.sendMessage(to, "已清空黑名單")
                elif text.lower() == 'banlist':
                    if sender in Owner:
                        if black["blacklist"] == {}:
                            cl.sendMessage(to, "沒有黑名單")
                        else:
                            cl.sendMessage(to, "以下是黑名單")
                            mc = ""
                            for mi_d in black["blacklist"]:
                                mc += "->" + cl.getContact(mi_d).displayName + "\n"
                            cl.sendMessage(to, mc)
                            cl.sendMessage(to, "總共 {} 個黑名單".format(str(len(black["blacklist"]))))
                elif text.lower() == 'banmid':
                    if sender in Owner:
                        if black["blacklist"] == {}:
                            cl.sendMessage(to, "沒有黑名單")
                        else:
                            cl.sendMessage(to, "以下是黑名單")
                            mc = ""
                            for mi_d in black["blacklist"]:
                                mc += "->" + cl.getContact(mi_d).displayName + "\n" + cl.getContact(mi_d).mid + "\n"
                            cl.sendMessage(to, mc)
                            cl.sendMessage(to, "總共 {} 個黑名單".format(str(len(black["blacklist"]))))
                elif text.lower() == 'kill ban':
                    if sender in Owner:
                        if msg.toType == 2:
                            group = cl.getGroup(to)
                            gMembMids = [contact.mid for contact in group.members]
                            matched_list = []
                            for tag in black["blacklist"]:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            if matched_list == []:
                                cl.sendMessage(to, "沒有黑名單")
                            else:
                                klist = [kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10]
                                kickers = random.choice(klist)
                                for jj in matched_list:
                                    try:
                                        kickers.kickoutFromGroup(to, [jj])
                                    except:
                                        cl.kickoutFromGroup(to, [jj])
                                cl.sendMessage(to, "黑名單以踢除")
                elif text.lower() == 'kill all group ban':
                    if sender in Owner:
                        groups = cl.groups
                        for gid in groups:
                            group = cl.getGroup(gid)
                            gMembMids = [contact.mid for contact in group.members]
                            matched_list = []
                            for tag in black["blacklist"]:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            if matched_list == []:
                                pass
                            else:
                                klist = [kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10]
                                kickers = random.choice(klist)
                                try:
                                    for jj in matched_list:
                                        try:
                                            kickers.kickoutFromGroup(gid, [jj])
                                        except:
                                            cl.kickoutFromGroup(gid, [jj])
                                    cl.sendMessage(gid, "已針對全群黑單進行剔除")
                                        #cl.sendMessage(to, cl.getGroup(gid).name + "\n" +cl.getContact(jj).displayName)
                                except Exception as error:
                                    print (error)
                                cl.sendMessage(to, "黑名單以踢除")
                elif text.lower() == 'tagban':
                    if sender in Owner:
                        if msg.toType == 2:
                            gs = cl.getGroup(to)
                            txt = u''
                            s=0
                            b=[]
                            for g in gs.members:
                                if g.mid in black["blacklist"]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":g.mid})
                                    s += 7
                                    txt += u'@CoCo \n'
                            if b == []:
                                cl.sendMessage(to, "沒有黑名單")
                            else:
                                cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
#==============================================================================#
                elif "Admin Lv1 Del " in msg.text:
                    if sender in Owner:
                        if msg.toType == 2:
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    try:
                                        del admins["lv1"][target]
                                        backupData()
                                        lv1c = cl.getContact(target).displayName
                                        cl.sendMessage(to , "已將 " + lv1c + "\n的等級1使用權移除")
                                    except:
                                        pass
                                return
                elif "Bl Add " in msg.text:
                    if sender in Owner:
                        if msg.toType == 2:
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    try:
                                        bl[target] = True
                                        bln = cl.getContact(target).displayName
                                        cl.sendMessage(to , "已將 " + bln + "\n加入BL名單")
                                    except:
                                        pass
                elif "Admin Lv1 Add " in msg.text:
                    if sender in Owner:
                        if msg.toType == 2:
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    try:
                                        admins["lv1"][target] = True
                                        backupData()
                                        lv1c = cl.getContact(target).displayName
                                        cl.sendMessage(to , "已將 " + lv1c + "\n更改為權限1使用者")
                                    except:
                                        pass
                                return
                elif text.lower() == 'adminlist':
                    if sender in Owner:
                        ret_ = "╔══[ 管理員列表 ]\n"
                        if admins["lv1"] == {}:
                            ret_ += "╠\n╠══[ 權限等級一 ]\n"
                            ret_ += "╠══ 沒有\n"
                        else:
                            ret_ += "╠\n╠══[ 權限等級一 ]\n"
                            for level1 in admins["lv1"]:
                                ret_ += "╠══ " + cl.getContact(level1).displayName + "\n"
                        if admins["lv2"] == {}:
                            ret_ += "╠\n╠══[ 權限等級二 ]\n"
                            ret_ += "╠══ 沒有\n"
                        else:
                            ret_ += "╠\n╠══[ 權限等級二 ]\n"
                            for level2 in admins["lv2"]:
                                ret_ += "╠══ " + cl.getContact(level2).displayName + "\n"
                        if admins["Max"] == {}:
                            ret_ += "╠\n╠══[ 權限等級最高 ]\n"
                            ret_ += "╠══ 沒有\n"
                        else:
                            ret_ += "╠\n╠══[ 權限等級最高 ]\n"
                            for levelMax in admins["Max"]:
                                ret_ += "╠══ " + cl.getContact(levelMax).displayName + "\n"
                        ret_ += "╚══[ 管理員列表 ]"
                        cl.sendMessage(to, str(ret_))
#==============================================================================#
                elif "Addfriend:" in msg.text:
                    if sender in Owner:
                        midd = msg.text.replace("Addfriend:","")
                        cl.findAndAddContactsByMid(midd)
                        kicker01.findAndAddContactsByMid(midd)
                        kicker02.findAndAddContactsByMid(midd)
                        kicker03.findAndAddContactsByMid(midd)
                        kicker04.findAndAddContactsByMid(midd)
                        kicker05.findAndAddContactsByMid(midd)
                        kicker06.findAndAddContactsByMid(midd)
                        kicker07.findAndAddContactsByMid(midd)
                        kicker08.findAndAddContactsByMid(midd)
                        kicker09.findAndAddContactsByMid(midd)
                        kicker10.findAndAddContactsByMid(midd)
                        cl.sendMessage(to, "ok")
                elif "Addfriend " in msg.text:
                    if sender in Owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            cl.findAndAddContactsByMid(target)
                            kicker01.findAndAddContactsByMid(target)
                            kicker02.findAndAddContactsByMid(target)
                            kicker03.findAndAddContactsByMid(target)
                            kicker04.findAndAddContactsByMid(target)
                            kicker05.findAndAddContactsByMid(target)
                            kicker06.findAndAddContactsByMid(target)
                            kicker07.findAndAddContactsByMid(target)
                            kicker08.findAndAddContactsByMid(target)
                            kicker09.findAndAddContactsByMid(target)
                            kicker10.findAndAddContactsByMid(target)
                            cl.sendMessage(to, "ok")
                elif "random:" in msg.text:
                    if sender in Owner:
                        strnum = msg.text.replace("random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in range(20)])
                                time.sleep(0.01)
                                group.name = name
                                cl.updateGroup(group)
                        except Exception as e:
                            cl.sendMessage(msg.to,str(e))
                elif "邀機:" in msg.text:
                    if sender in Owner:
                        midd = find_between_r(msg.text, "邀機:", "_")
                        strnum = find_between_r(msg.text, "_", "")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            try:
                                coi01.findAndAddContactsByMid(midd)
                            except:
                                pass
                            num = int(strnum)
                            for i in range(0, num):
                                name = "".join([random.choice(source_str) for x in range(20)])
                                coi01.createGroup(name, [midd])
                                time.sleep(3)
                            print("成功邀機:" + cl.getContact(midd).displayName + "\nMid\n" + midd)
                            cl.sendMessage(to, 'ok')
                        except Exception as e:
                            cl.sendMessage(msg.to,str(e))
                elif "邀機 " in msg.text:
                    if sender in Owner:
                        print ("邀機執行")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        num = 1
                        for var in range(0,num):
                            for target in targets:
                                name = "".join([random.choice(source_str) for x in range(20)])
                                cl.createGroup(name, [target])
                                time.sleep(0.5)
                                name1 = "".join([random.choice(source_str) for x in range(20)])
                                kicker01.createGroup(name1, [target])
                                time.sleep(0.5)
                                name2 = "".join([random.choice(source_str) for x in range(20)])
                                kicker02.createGroup(name2, [target])
                                time.sleep(0.5)
                                name3 = "".join([random.choice(source_str) for x in range(20)])
                                kicker03.createGroup(name3, [target])
                                time.sleep(0.5)
                                name4 = "".join([random.choice(source_str) for x in range(20)])
                                kicker04.createGroup(name4, [target])
                                time.sleep(0.5)
                                name5 = "".join([random.choice(source_str) for x in range(20)])
                                kicker05.createGroup(name5, [target])
                                time.sleep(0.5)
                                name6 = "".join([random.choice(source_str) for x in range(20)])
                                kicker06.createGroup(name6, [target])
                                time.sleep(0.5)
                                name7 = "".join([random.choice(source_str) for x in range(20)])
                                kicker07.createGroup(name7, [target])
                                time.sleep(0.5)
                                name8 = "".join([random.choice(source_str) for x in range(20)])
                                kicker08.createGroup(name8, [target])
                                time.sleep(0.5)
                                name9 = "".join([random.choice(source_str) for x in range(20)])
                                kicker09.createGroup(name9, [target])
                                time.sleep(0.5)
                                name10 = "".join([random.choice(source_str) for x in range(20)])
                                kicker10.createGroup(name10, [target])
                                time.sleep(0.5)
                        cl.sendMessage(to, 'ok')
#==============================================================================#
                elif "洗頻:" in msg.text:
                    if sender in Owner:
                        text = find_between_r(msg.text, "洗頻:", "_:")
                        strnum = find_between_r(msg.text, "_:", "")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            cl.unsendMessage(msg_id)
                        except:
                            pass
                        try:
                            num = int(strnum)
                            for i in range(0, num):
                                cl.sendMessage(to, text)
                        except Exception as e:
                            cl.sendMessage(msg.to,str(e))
#==============================================================================#
                elif "/invitemeto:" in msg.text:
                    if sender in Owner:
                        gid = msg.text.replace("/invitemeto:","")
                        if gid == "":
                            cl.sendMessage(to,"請輸入群組ID")
                        else:
                            try:
                                cl.findAndAddContactsByMid(sender)
                                cl.inviteIntoGroup(gid,[sender])
                            except:
                                cl.sendMessage(to,"我不在那個群組裡")
#==============================================================================#
                elif "Kickall" in msg.text:
                    if sender in Owner:
                        if settings["kickmeber"] == True:
                            if msg.toType == 2:
                                print ("翻群")
                                gs = cl.getGroup(to)
                                cl.sendMessage(to,"レム❄帝国主义の破壊")
                                group.name = "レム❄帝国主义の破壊"
                                cl.updateGroup(group)
                                targets = []
                                for g in gs.members:
                                        targets.append(g.mid)
                                for target in targets:
                                    if target in admin:
                                        pass
                                    else:
                                        try:
                                            klist=[cl,kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(to, [target])
                                        except:
                                            pass
#==============================================================================#
#elif "Dn " in msg.text:
#                   if sender in Owner:
#                       dname = msg.text.replace("Dn ","")
#                       key = eval(msg.contentMetadata["MENTION"])
#                       key["MENTIONEES"][0]["M"]
#                       targets = []
#                       for x in key["MENTIONEES"]:
#                           targets.append(x["M"])
#                       if targets == []:
#                           pass
#                       else:
#                           for target in targets:
#                               target.displayNameOverridden = dname
#                               cl.sendMessage(msg.to,"更新名字成功 : " + dname + "")
#==============================================================================#
                elif "clRn:" in msg.text:
                    if sender in Owner:
                        string = msg.text.replace("clRn:","")
                        clProfile.displayName = string
                        cl.updateProfile(clProfile)
                        cl.sendMessage(msg.to,"更新名字成功 : " + string + "")
#==============================================================================#
                elif "!ckt_add " in msg.text:
                    if sender in Lv1:
                        pkg_id = find_between_r(msg.text, "!ckt_add ", "_")
                        stk_id = find_between_r(msg.text, "_", ":")
                        ctext = find_between_r(msg.text, ":","")
                        if ctext is None:
                            cl.sendMessage(to, "請輸入回覆文字")
                        else:
                            if pkg_id in ckt['ck']:
                                pass
                            else:
                                ckt['ck'][pkg_id] = {}
                            if ckt['ck'][pkg_id] == {}:
                                ckt['ck'][pkg_id][stk_id] = ctext
                            else:
                                ckt['ck'][pkg_id] == {}
                                ckt['ck'][pkg_id][stk_id] = ctext
                            backupData()
                            cl.sendMessage(to, "已增加關鍵字回覆！\n" + ctext)
                elif "!ckt_del " in msg.text:
                    if sender in Owner:
                        pkg_id = find_between_r(msg.text, "!ckt_del ", "_")
                        stk_id = find_between_r(msg.text, "_", "")
                        try:
                            del ckt['ck'][pkg_id][stk_id]
                            backupData()
                            cl.sendMessage(to, "已刪除關鍵字回覆！")
                        except:
                            cl.sendMessage(to, "沒有這個關鍵字回覆呢...")
#==============================================================================#
                elif "拒絕:群組邀請" in msg.text or "拒絕：群組邀請" in msg.text:
                    if sender in Owner:
                        gid = cl.getGroupIdsInvited()
                        for i in gid:
                            cl.acceptGroupInvitation(i)
                            time.sleep(0.5)
                            try:
                                cl.leaveGroup(i)
                            except:
                                pass
                        cl.sendMessage(to, "已拒絕所有群組邀請！\n群組數量：{}".format(str(len(gid))))
                elif "同意:群組邀請" in msg.text or "同意：群組邀請" in msg.text:
                    if sender in Owner:
                        gid = cl.getGroupIdsInvited()
                        for i in gid:
                            cl.acceptGroupInvitation(i)
                            time.sleep(0.5)
                            try:
                                cl.sendMessage(i, "天選の多功能防翻★降臨☆\n\n要防翻功能請找機器作者\nline.me/ti/p/1MRX_Gjbmv")
                            except:
                                pass
                        cl.sendMessage(to, "已進入邀請中的群組！\n群組數量：{}".format(str(len(gid))))
                elif "設定:取消邀請" in msg.text or "設定：取消邀請" in msg.text:
                    if sender in Owner:
                        from gcancel import LineGroupCancel
                        cl.sendMessage(to, LineGroupCancel())
#cl.sendMessage(to, text=None, contentMetadata['GC_IGNORE_ON_FAILBACK']["False"], contentType=6)
#==============================================================================#
                elif msg.text in ["主機離開全部群組"]:
                    if sender in Owner:
                        gid = cl.getGroupIdsJoined()
                        for i in gid:
                            cl.leaveGroup(i)
                elif msg.text in ["K1離開全部群組"]:
                    if sender in Owner:
                        gid = kicker01.getGroupIdsJoined()
                        for i in gid:
                            kicker01.leaveGroup(i)
                elif msg.text in ["K2離開全部群組"]:
                    if sender in Owner:
                        gid = kicker02.getGroupIdsJoined()
                        for i in gid:
                            kicker02.leaveGroup(i)
                elif msg.text in ["K3離開全部群組"]:
                    if sender in Owner:
                        gid = kicker03.getGroupIdsJoined()
                        for i in gid:
                            kicker03.leaveGroup(i)
                elif msg.text in ["K4離開全部群組"]:
                    if sender in Owner:
                        gid = kicker04.getGroupIdsJoined()
                        for i in gid:
                            kicker04.leaveGroup(i)
                elif msg.text in ["K5離開全部群組"]:
                    if sender in Owner:
                        gid = kicker05.getGroupIdsJoined()
                        for i in gid:
                            kicker05.leaveGroup(i)
                elif msg.text in ["K6離開全部群組"]:
                    if sender in Owner:
                        gid = kicker06.getGroupIdsJoined()
                        for i in gid:
                            kicker06.leaveGroup(i)
                elif msg.text in ["K7離開全部群組"]:
                    if sender in Owner:
                        gid = kicker07.getGroupIdsJoined()
                        for i in gid:
                            kicker07.leaveGroup(i)
                elif msg.text in ["K8離開全部群組"]:
                    if sender in Owner:
                        gid = kicker08.getGroupIdsJoined()
                        for i in gid:
                            kicker08.leaveGroup(i)
                elif msg.text in ["K9離開全部群組"]:
                    if sender in Owner:
                        gid = kicker09.getGroupIdsJoined()
                        for i in gid:
                            kicker09.leaveGroup(i)
                elif msg.text in ["K10離開全部群組"]:
                    if sender in Owner:
                        gid = kicker01.getGroupIdsJoined()
                        for i in gid:
                            kicker10.leaveGroup(i)
#==============================================================================#
                elif msg.text in ["SR","Setread"]:
                    if sender in Lv1:
                        cl.sendMessage(msg.to, "設置已讀點")
                        try:
                            del read['wait2']['readPoint'][msg.to]
                            del read['wait2']['readMember'][msg.to]
                        except:
                            pass
                        now2 = datetime.now()
                        read['wait2']['readPoint'][msg.to] = msg.id
                        read['wait2']['readMember'][msg.to] = ""
                        read['wait2']['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                        read['wait2']['ROM'][msg.to] = {}
                        print ("設置已讀點")
                        backupData()
                elif msg.text in ["LR","Lookread"]:
                    if sender in Lv1:
                        if msg.to in read['wait2']['readPoint']:
                            print ("查詢已讀")
                            if read['wait2']["ROM"][msg.to].items() == []:
                                chiya = ""
                            else:
                                chiya = ""
                                for rom in read['wait2']["ROM"][msg.to].items():
                                    chiya += rom[1] + "\n"
                                cl.sendMessage(msg.to, "||已讀順序||%s\n\n%s\n[%s]" % (read['wait2']['readMember'][msg.to],chiya,setTime[msg.to]))
                        else:
                            cl.sendMessage(msg.to, "請輸入SR設置已讀點")
                        backupData()
                elif text.lower() == '030wwwww':
                    if sender in Owner:
                        try:
                            del read['Read']['readPoint'][msg.to]
                            del read['Read']['readMember'][msg.to]
                        except:
                            pass
                        now2 = datetime.now()
                        read['Read']['Point'][msg.to] = msg.id
                        read['Read']['Member'][msg.to] = ""
                        read['Read']['Time'][msg.to] = datetime.strftime(now2,"%H:%M")
                        read['Read']['ROM'][msg.to] = {}
                        cl.sendMessage(to, "笑")
                        backupData()
                elif text.lower() == 'offread':
                    if sender in Owner:
                        if msg.to in read['Read']['Point']:
                            if read['Read']["ROM"][msg.to].items() == []:
                                chiya = ""
                            else:
                                chiya = ""
                                for rom in read['Read']["ROM"][msg.to].items():
                                    chiya += rom[1] + "\n"
                                cl.sendMessage(msg.to, "已讀者\n" + chiya)
                            del read['Read']['Point'][msg.to]
                            del read['Read']['Member'][msg.to]
                            del read['Read']['ROM'][msg.to]
                            del read['Read']['Time'][msg.to]
                        else:
                            cl.sendMessage(to, "已讀點未設定")
                        backupData()
#==============================================================================#
                elif msg.text in ["Friendlist"]:
                    if sender in Owner:
                        anl = cl.getAllContactIds()
                        ap = ""
                        for q in anl:
                            ap += "• "+cl.getContact(q).displayName + "\n"
                        cl.sendMessage(msg.to,"「 朋友列表 」\n"+ap+"人數 : "+str(len(anl)))
#==============================================================================#
                elif msg.text in ["運勢"]:
                    if sender in admin:
                        cl.sendMessage(msg.to, text="["+omikuji()+"]", contentMetadata={'subText': 'おみくじですよー','previewUrl': 'http://illustrain.com/img/work/2013/illustrain03-oshougatu18.png','type': 'mt'}, contentType=19)
#==============================================================================#
                elif text.lower() == 'speed' or text.lower() == 'sp':
                    if sender in Lv1:
                        curTime = time.time()
                        cl.sendMessage(to, "請稍等...")
                        rtime = time.time()
                        xtime = rtime - curTime
                        cl.sendMessage(to,'處理速度\n' + format(str(xtime)) + '秒')
                        time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=5000)
                        str1 = str(time0)
                        cl.sendMessage(to,'反應時間\n' + str1 + '秒')
                elif text.lower() == 'rebot':
                    if sender in Owner:
                        cl.sendMessage(to, "重新啟動")
                        restartBot()
                elif text.lower() == 'runtime':
                    if sender in Lv1:
                        timeNow = time.time()
                        runtime = timeNow - botStart
                        runtime = format_timespan(runtime)
                        cl.sendMessage(to, "機器運行時間 {}".format(str(runtime)))
                elif text.lower() == 'about':
                    if sender in Owner:
                        try:
                            arr = []
                            owner = "u28d781fa3ba9783fd5144390352b0c24"
                            creator = cl.getContact(owner)
                            contact = cl.getContact(clMID)
                            grouplist = cl.getGroupIdsJoined()
                            contactlist = cl.getAllContactIds()
                            blockedlist = cl.getBlockedContactIds()
                            groupinvite = cl.getGroupIdsInvited()
                            ret_ = "╔══[ 關於自己 ]"
                            ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                            ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                            ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                            ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                            ret_ += "\n╠ 邀請 : {}".format(str(len(groupinvite)))
                            ret_ += "\n╠══[ 關於機器 ]"
                            ret_ += "\n╠ 版本 : Bate測試版"
                            ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                            ret_ += "\n╚══[ 未經許可禁止重製 ]"
                            cl.sendMessage(to, str(ret_))
                        except Exception as e:
                            cl.sendMessage(msg.to, str(e))

#==============================================================================#
                elif text.lower() == 'set':
                    if sender in Lv1:
                        try:
                            ret_ = "╔══[ 設定 ]"
                            if settings["autoAdd"] == True: ret_ += "\n╠ 自動加入好友 ✅"
                            else: ret_ += "\n╠ 自動加入好友 ❌"
                            if settings["autoJoin"] == True: ret_ += "\n╠ 自動加入群組 ✅"
                            else: ret_ += "\n╠ 自動加入群組 ❌"
                            if settings["kickerjoin"] == True: ret_ += "\n╠ Kicker自動加入群組 ✅"
                            else: ret_ += "\n╠ Kicker自動加入群組 ❌"
                            if settings["autoJoinTicket"] == True: ret_ += "\n╠ 網址自動入群 ✅"
                            else: ret_ += "\n╠ 網址自動入群 ❌"
                            if settings["autoLeave"] == True: ret_ += "\n╠ 自動離開副本 ✅"
                            else: ret_ += "\n╠ 自動離開副本 ❌"
                            if settings["autoRead"] == True: ret_ += "\n╠ 自動已讀 ✅"
                            else: ret_ += "\n╠ 自動已讀 ❌"
                            if settings["checkSticker"] == True: ret_ += "\n╠ 檢查貼圖訊息 ✅"
                            else: ret_ += "\n╠ 檢查貼圖訊息 ❌"
                            if settings["detectMention"] == True: ret_ += "\n╠ 標註提醒 ✅"
                            else: ret_ += "\n╠ 標註提醒 ❌"
                            if settings["targets"] == True: ret_ += "\n╠ 標註全部人 ✅"
                            else: ret_ += "\n╠ 標註全部人 ❌"
                            if settings["contact"] == True: ret_ += "\n╠ 詳細資料 ✅"
                            else: ret_ += "\n╠ 詳細資料 ❌"
                            if settings["contact"] == True: ret_ += "\n╠ 詳細文章 ✅"
                            else: ret_ += "\n╠ 詳細文章 ❌"
                            if settings["kickmeber"] == True: ret_ += "\n╠ 翻群開關 ✅"
                            else: ret_ += "\n╠ 翻群開關 ❌"
                            if settings["reread"] == True: ret_ += "\n╠ 查詢收回開啟 ✅"
                            else: ret_ += "\n╠ 查詢收回關閉 ❌"
                            if settings["reck"] == True: ret_ += "\n╠ 查詢貼圖收回開啟 ✅"
                            else: ret_ += "\n╠ 查詢貼圖收回關閉 ❌"
                            if msg.to in settings["JoinText"]: ret_ += "\n╠ 進群回覆 ✅"
                            else: ret_ += "\n╠ 進群回覆 ❌"
                            if msg.to in settings["LeaveText"]: ret_ += "\n╠ 退群回覆 ✅"
                            else: ret_ += "\n╠ 退群回覆 ❌"
                            ret_ += "\n╚══[ 設定 ]"
                            cl.sendMessage(to, str(ret_))
                        except Exception as e:
                            cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'add on':
                    if sender in Owner:
                        settings["autoAdd"] = True
                        backupData()
                        cl.sendMessage(to, "自動加入好友已開啟")
                elif text.lower() == 'add off':
                    if sender in Owner:
                        settings["autoAdd"] = False
                        backupData()
                        cl.sendMessage(to, "自動加入好友已關閉")
                elif text.lower() == 'join on':
                    if sender in Owner:
                        settings["autoJoin"] = True
                        backupData()
                        cl.sendMessage(to, "自動加入群組已開啟")
                elif text.lower() == 'join off':
                    if sender in Owner:
                        settings["autoJoin"] = False
                        backupData()
                        cl.sendMessage(to, "自動加入群組已關閉")
                elif text.lower() == 'leave on':
                    if sender in Owner:
                        settings["autoLeave"] = True
                        backupData()
                        cl.sendMessage(to, "自動離開副本已開啟")
                elif text.lower() == 'leave off':
                    if sender in Owner:
                        settings["autoLeave"] = False
                        backupData()
                        cl.sendMessage(to, "自動離開副本已關閉")
                elif text.lower() == 'read on':
                    if sender in Owner:
                        settings["autoRead"] = True
                        backupData()
                        cl.sendMessage(to, "自動已讀已開啟")
                elif text.lower() == 'read off':
                    if sender in Owner:
                        settings["autoRead"] = False
                        backupData()
                        cl.sendMessage(to, "自動已讀已關閉")
                elif text.lower() == 'ck on':
                    if sender in Owner:
                        settings["checkSticker"] = True
                        backupData()
                        cl.sendMessage(to, "檢查貼圖已開啟")
                elif text.lower() == 'ck off':
                    if sender in Owner:
                        settings["checkSticker"] = False
                        backupData()
                        cl.sendMessage(to, "檢查貼圖已關閉")
                elif text.lower() == 'autotag on':
                    if sender in Owner:
                        settings["detectMention"] = True
                        backupData()
                        cl.sendMessage(to, "標註提醒已開啟")
                elif text.lower() == 'autotag off':
                    if sender in Owner:
                        settings["detectMention"] = False
                        backupData()
                        cl.sendMessage(to, "標註提醒已關閉")
                elif text.lower() == 'clonecontact':
                    if sender in Owner:
                        settings["copy"] = True
                        backupData()
                        cl.sendMessage(to, "請丟出好友資料以便複製")
                elif text.lower() == 'contact on':
                    if sender in Owner:
                        settings["contact"] = True
                        backupData()
                        cl.sendMessage(to, "查看好友資料詳情開啟")
                elif text.lower() == 'contact off':
                    if sender in Owner:
                        settings["contact"] = False
                        backupData()
                        cl.sendMessage(to, "查看好友資料詳情關閉")
                elif text.lower() == 'urljoin on':
                    if sender in Owner:
                        settings["autoJoinTicket"] = True
                        backupData()
                        cl.sendMessage(to, "網址自動加入群組已開啟")
                elif text.lower() == 'urljoin off':
                    if sender in Owner:
                        settings["autoJoinTicket"] = False
                        backupData()
                        cl.sendMessage(to, "網址自動加入群組已關閉")
                elif text.lower() == 'kb on':
                    if sender in Owner:
                        settings["kickblackjoin"] = True
                        backupData()
                        cl.sendMessage(to, "剔除黑單進群已開啟")
                elif text.lower() == 'kb off':
                    if sender in Owner:
                        settings["kickblackjoin"] = False
                        backupData()
                        cl.sendMessage(to, "踢除黑單進群已關閉")
                elif text.lower() == 'jt on' or "設定:進群回覆" in msg.text or "設定：進群回覆" in msg.text:
                    if sender in Owner:
                        group = cl.getGroup(to)
                        settings["JoinText"][msg.to] = True
                        backupData()
                        cl.sendMessage(to, "進群回覆已開啟")
                elif text.lower() == 'jt off' or "關閉:進群回覆" in msg.text or "關閉：進群回覆" in msg.text:
                    if sender in Owner:
                        group = cl.getGroup(to)
                        del ["JoinText"][msg.to]
                        backupData()
                        cl.sendMessage(to, "進群回覆已關閉")
                elif text.lower() == 'bt on' or "設定:退群回覆" in msg.text or "設定：退群回覆" in msg.text:
                    if sender in Owner:
                        group = cl.getGroup(to)
                        settings["LeaveText"][msg.to] = True
                        backupData()
                        cl.sendMessage(to, "退群回覆已開啟")
                elif text.lower() == 'bt off' or "關閉:退群回覆" in msg.text or "關閉：退群回覆" in msg.text:
                    if sender in Owner:
                        group = cl.getGroup(to)
                        del ["LeaveText"][msg.to]
                        backupData()
                        cl.sendMessage(to, "退群回覆已關閉")
                elif text.lower() == 'inviteprotect on' or "設定:邀請保護" in msg.text or "設定：邀請保護" in msg.text:
                    if sender in Owner:
                        group = cl.getGroup(to)
                        pro["Invite"][msg.to] = True
                        if msg.to in gcs['Creater']:
                            pass
                        else:
                            try:
                                gcs['Creater'][msg.to] = group.creator.mid
                            except:
                                pass
                        backupData()
                        cl.sendMessage(to, "群組邀請保護已開啟")
                elif text.lower() == 'inviteprotect off' or "關閉:邀請保護" in msg.text or "關閉：邀請保護" in msg.text:
                    if sender in Owner:
                        group = cl.getGroup(to)
                        del pro["Invite"][msg.to]
                        backupData()
                        cl.sendMessage(to, "群組邀請保護已關閉")
                elif  text.lower() == 'inviteprotect list' or "查詢:邀請保護" in msg.text or "查詢：邀請保護" in msg.text:
                    if sender in Owner:
                        if pro["Invite"] == {}:
                            cl.sendMessage(to, "沒有網址保護中的群組")
                        else:
                            cl.sendMessage(to, "以下是網址保護中的群組")
                            mc = ""
                            for gi_d in pro["Invite"]:
                                mc += "->" + cl.getGroup(gi_d).name + "\n"
                            cl.sendMessage(to, mc)
                elif text.lower() == 'qr on' or "設定:網址保護" in msg.text or "設定：網址保護" in msg.text or "設定：網址保護" in msg.text:
                    if sender in Owner:
                        group = cl.getGroup(to)
                        try:
                            pro["Qr"][msg.to] = True
                            if msg.to in gcs['Creater']:
                                pass
                            else:
                                try:
                                    gcs['Creater'][msg.to] = group.creator.mid
                                except:
                                    cl.sendMessage(to, "未找到群組作者, 開網址請找管理員")
                            backupData()
                            cl.sendMessage(to, "群組網址保護已開啟")
                        except:
                            pass
                elif text.lower() == 'qr off' or "關閉:網址保護" in msg.text or "關閉：網址保護" in msg.text:
                    if sender in Owner:
                        group = cl.getGroup(to)
                        try:
                            del pro["Qr"][msg.to]
                        except:
                            pass
                        backupData()
                        cl.sendMessage(to, "群組網址保護已關閉")
                elif  text.lower() == 'qr list' or "查詢:網址保護" in msg.text or "查詢：網址保護" in msg.text:
                    if sender in Owner:
                        if pro["Qr"] == {}:
                            cl.sendMessage(to, "沒有網址保護中的群組")
                        else:
                            cl.sendMessage(to, "以下是網址保護中的群組")
                            mc = ""
                            for gi_d in pro["Qr"]:
                                try:
                                    mc += "->" + cl.getGroup(gi_d).name + "\n"
                                except:
                                    del pro["Qr"][gi_d]
                            cl.sendMessage(to, mc)
                elif text.lower() == 'image on' or "開啟:群圖保護" in msg.text or "開啟：群圖保護" in msg.text:
                    if sender in Owner:
                        group = cl.getGroup(to)
                        try:
                            pro["Image"][msg.to] = True
                        except:
                            pass
                        backupData()
                        cl.sendMessage(to, "群組圖片保護已開啟")
                elif text.lower() == 'image off' or "關閉:群圖保護" in msg.text or "關閉：群圖保護" in msg.text:
                    if sender in Owner:
                        group = cl.getGroup(to)
                        try:
                            del pro["Image"][msg.to]
                        except:
                            pass
                        backupData()
                        cl.sendMessage(to, "群組圖片保護已關閉")
                elif text.lower() == 'allprotect on' or "設定:全部保護" in msg.text or "設定：全部保護" in msg.text:
                    if sender in Owner:
                        group = cl.getGroup(to)
                        try:
                            pro["Qr"][msg.to] = True
                        except:
                            pass
                        try:
                            pro["Kick"][msg.to] = True
                        except:
                            pass
                        try:
                            pro["Image"][msg.to] = True
                        except:
                            pass
                        try:
                            pro["Invite"][msg.to] = True
                        except:
                            pass
                        try:
                            pro["Name"][msg.to] = cl.getGroup(msg.to).name
                        except:
                            pass
                        if msg.to in gcs['Creater']:
                            pass
                        else:
                            try:
                                gcs['Creater'][msg.to] = group.creator.mid
                            except:
                                cl.sendMessage(to, "未找到群組作者, 開網址/踢人請找管理員")
                        backupData()
                        cl.sendMessage(to, "這群已經開啟全部保護")
                elif text.lower() == 'allprotect off' or "關閉:保護" in msg.text or "關閉：保護" in msg.text:
                    if sender in Owner:
                        group = cl.getGroup(to)
                        try:
                            del pro["Qr"][msg.to]
                        except:
                            pass
                        try:
                            del pro["Kick"][msg.to]
                        except:
                            pass
                        try:
                            del pro["Image"][msg.to]
                        except:
                            pass
                        try:
                            del pro["Invite"][msg.to]
                        except:
                            pass
                        try:
                            del pro["Name"][msg.to]
                        except:
                            pass
                        backupData()
                        cl.sendMessage(to, "這群已經關閉全部保護")
                elif text.lower() == 'protect on' or "設定:踢人保護" in msg.text or "設定：踢人保護" in msg.text:
                    if sender in Owner:
                        group = cl.getGroup(to)
                        try:
                            pro['Kick'][msg.to] = True
                        except:
                            pass
                        try:
                            if msg.to in gcs['Creater']:
                                pass
                            else:
                                try:
                                    gcs['Creater'][msg.to] = group.creator.mid
                                except:
                                    cl.sendMessage(to, "未找到群組作者, 踢人請找管理員")
                        except:
                            pass
                        backupData()
                        cl.sendMessage(to, "群組保護已開啟")
                elif text.lower() == 'protect off' or "關閉:踢人保護" in msg.text:
                    if sender in Owner:
                        gid = msg.to
                        try:
                            del pro["Kick"][gid]
                        except:
                            pass
                        backupData()
                        cl.sendMessage(to, "群組保護已關閉")
                elif text.lower() == 'protectlist' or "查詢:踢人保護" in msg.text or "查詢：踢人保護" in msg.text:
                    if sender in Owner:
                        if pro["Kick"] == {}:
                            cl.sendMessage(to, "沒有保護中的群組")
                        else:
                            cl.sendMessage(to, "以下是保護中的群組")
                            mc = ""
                            for gi_d in pro["Kick"]:
                                mc += "->" + cl.getGroup(gi_d).name + "\n"
                            cl.sendMessage(to, mc)
                elif text.lower() == 'highprotect on' or "設定:高度保護" in msg.text or "設定：高度保護" in msg.text:
                    if sender in Owner:
                        try:
                            pro['High'][msg.to] = True
                        except:
                            pass
                        backupData()
                        cl.sendMessage(to, "這群已開啟高度保護")
                elif text.lower() == 'highprotect off' or "關閉:高度保護" in msg.text or "關閉：高度保護" in msg.text:
                    if sender in Owner:
                        try:
                            del pro['High'][msg.to]
                        except:
                            pass
                        backupData()
                        cl.sendMessage(to, "這群已關閉高度保護")
                elif text.lower() == 'gcl on' or "設定:作者鎖定" in msg.text or "設定：作者鎖定" in msg.text:
                    group = cl.getGroup(msg.to)
                    if sender in Owner:
                        try:
                            if msg.to in gcs['Creater']:
                                gcs['Lock'][msg.to] = True
                                cl.sendMessage(to, "這群已開啟作者鎖定")
                            else:
                                try:
                                    gcs['Creater'][msg.to] = group.creator.mid
                                    cl.sendMessage(to, "這群已開啟作者鎖定")
                                except:
                                    cl.sendMessage(to, "未找到群組作者, 作者鎖定失敗")
                            backupData()
                        except Exception as error:
                            print (error)
                elif text.lower() == 'gcl off' or "關閉:作者鎖定" in msg.text or "關閉：作者保護" in msg.text:
                    if sender in Owner:
                        gid = msg.to
                        try:
                            try:
                                del gcs['Lock'][msg.to]
                            except:
                                pass
                            backupData()
                            cl.sendMessage(to, "這群已關閉作者鎖定")
                        except Exception as error:
                            print (error)
                elif "設定:作者交換" in msg.text or "設定：作者交換" in msg.text:
                    if sender in Owner:
                        try:
                            group = cl.getGroup(msg.to)
                            Ga1 = [] #原群組作者
                            Ga2 = [] #原預備作者
                            if msg.to in gcs['Creater']:
                                if msg.to in gcs['Invite']:
                                    Ga1 = gcs['Creater'][msg.to]
                                    Ga2 = gcs['Invite'][msg.to]
                                    gcs['Creater'][msg.to] = Ga2
                                    gcs['Invite'][msg.to] = Ga1
                                    cl.sendMessage(to, "作者交換完畢")
                                else:
                                    Ga1 = gcs['Creater'][msg.to]
                                    gcs['Invite'][msg.to] = Ga1
                                    del gcs['Creater'][msg.to]
                                    cl.sendMessage(to, "群組作者交換完畢,無群組作者！")
                            else:
                                if group.creator is None :
                                    if msg.to in gcs['Invite']:
                                        Ga2 = gcs['Invite'][msg.to]
                                        gcs['Creater'][msg.to] = Ga2
                                        del gcs['Invite'][msg.to]
                                        cl.sendMessage(to, "群組作者交換完畢,無預備作者！")
                                    else:
                                        cl.sendMessage(to, "無群組作者！")
                                else:
                                    if msg.to in gcs['Invite']:
                                        Ga1 = group.creator.mid
                                        Ga2 = gcs['Invite'][msg.to]
                                        gcs['Creater'][msg.to] = Ga2
                                        gcs['Invite'][msg.to] = Ga1
                                        cl.sendMessage(to, "群組作者交換完畢！")
                                    else:
                                        gcs['Creater'][msg.to] = group.creator.mid
                                        cl.sendMessage(to, "群組作者交換完畢,無預備作者！")
                            backupData()
                        except Exception as error:
                            print (error)
                elif "清除:預備作者" in msg.text or "清除：預備作者" in msg.text:
                    try:
                        del gcs['Invite'][msg.to]
                        cl.sendMessage(to, "預備作者已清除")
                        backupData()
                    except:
                        cl.sendMessage(to, "沒有預備作者")
                elif text.lower() == 'va' or "設定:預備作者" in msg.text or "設定：預備作者" in msg.text:
                    if sender in Owner:
                        settings["convinv"] = True
                        admins['Contect'] = sender
                        cl.sendMessage(to, "請丟出好友資料")
                        backupData()
                elif "Va " in msg.text:
                    if sender in Owner:
                        im0 = text.replace("Va ","")
                        im1 = im0.rstrip()
                        im2 = im1.replace("@","")
                        im3 = im2.rstrip()
                        _name = im3
                        gs = cl.getGroup(to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    gcs['Invite'][msg.to] = target
                                    backupData()
                                    mi_d = gcs['Invite'][msg.to]
                                    name = cl.getContact(mi_d).displayName
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(mi_d)+'}'
                                    cl.sendMessage(to, "副群主已更改為: " + name)
                                    Tag(to, target)
                                except Exception as error:
                                    print (error)
                elif text.lower() == 'ia' or "設定:邀請權限" in msg.text or "設定：邀請權限" in msg.text:
                    if sender in Owner:
                        settings["conadinv"] = True
                        admins['Contect'] = sender
                        cl.sendMessage(to, "請丟出好友資料")
                        backupData()
                elif "Ia " in msg.text:
                    if sender in Owner:
                        im0 = text.replace("Ia ","")
                        im1 = im0.rstrip()
                        im2 = im1.replace("@","")
                        im3 = im2.rstrip()
                        _name = im3
                        gs = cl.getGroup(to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    gcs['Inviteadmin'][msg.to] = target
                                    backupData()
                                    mi_d = gcs['Inviteadmin'][msg.to]
                                    name = cl.getContact(mi_d).displayName
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(mi_d)+'}'
                                    cl.sendMessage(to, "邀請權限者已更改為: " + name)
                                    Tag(to, target)
                                except Exception as error:
                                    print (error)
                elif text.lower() == 'protectname on' or "設定:群名保護" in msg.text or "設定：群名保護" in msg.text:
                    if sender in Owner:
                        if msg.toType == 2:
                            try:
                                pro["Name"][msg.to] = cl.getGroup(to).name
                            except:
                                pass
                            backupData()
                            cl.sendMessage(to, "群名保護開啟")
                elif text.lower() == 'protectname off' or "關閉:群名保護" in msg.text or "關閉：群名保護" in msg.text:
                    if sender in Owner:
                        if msg.toType == 2:
                            try:
                                del pro["Name"][msg.to]
                            except:
                                pass
                            backupData()
                            cl.sendMessage(to, "群名保護關閉")
                elif text.lower() == 'protect info' or text.lower() == 'pi' or "設定:確認" in msg.text or "設定：確認" in msg.text:
                    if sender in Lv1:
                        group = cl.getGroup(to)
                        try:
                            if msg.to in gcs['Invite']:
                                mi_d = gcs['Invite'][msg.to]
                                vgc = cl.getContact(mi_d).displayName
                            else:
                                vgc = "未設定"
                        except:
                            vgc = "未設定"
                        try:
                            if msg.to in gcs['Inviteadmin']:
                                try:
                                    mi_d = gcs['Inviteadmin'][msg.to]
                                    ginvite = cl.getContact(mi_d).displayName
                                except:
                                    del gcs['Inviteadmin'][msg.to]
                                    ginvite = "未設定"
                            else:
                                ginvite = "未設定"
                        except:
                            ginvite = "未設定"
                        if msg.to in gcs["Creater"]:
                            try:
                                mi_d = gcs["Creater"][msg.to]
                                gCreator = cl.getContact(mi_d).displayName
                            except:
                                try:
                                    gcs['Creater'][msg.to] = group.creator.mid
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "未找到"
                        else:
                            try:
                                gcs['Creater'][msg.to] = group.creator.mid
                                gCreator = group.creator.displayName
                            except:
                                gCreator = "未找到"
                        if group.invitee is None:
                            gPending = "0"
                        else:
                            gPending = str(len(group.invitee))
                        ret_ = "╔══[ 保護狀態 ]"
                        gid = msg.to
                        if gid in pro["Kick"]: ret_ += "\n╠ 群組保護 ✅"
                        else: ret_ += "\n╠ 群組保護 ❌"
                        if gid in pro["Name"]: ret_ += "\n╠ 群名保護 ✅"
                        else: ret_ += "\n╠ 群名保護 ❌"
                        if gid in pro["Qr"]: ret_ += "\n╠ 網址保護 ✅"
                        else: ret_ += "\n╠ 網址保護 ❌"
                        if gid in pro["Invite"]: ret_ += "\n╠ 邀請保護 ✅"
                        else: ret_ += "\n╠ 邀請保護 ❌"
                        if gid in pro["Image"]: ret_ += "\n╠ 群圖保護 ✅"
                        else: ret_ += "\n╠ 群圖保護 ❌"
                        if gid in pro["High"]: ret_ += "\n╠ 高度保護 ✅"
                        else: ret_ += "\n╠ 高度保護 ❌"
                        if gid in gcs["Lock"]: ret_ += "\n╠ 作者鎖定 ✅"
                        else: ret_ += "\n╠ 作者鎖定 ❌"
                        ret_ += "\n╠ 群組作者 : {}".format(str(gCreator))
                        ret_ += "\n╠ 成員數量 : {}".format(str(len(group.members)))
                        ret_ += "\n╠ 預備作者 : {}".format(str(vgc))
                        ret_ += "\n╠ 可邀人者  : {}".format(str(ginvite))
                        ret_ += "\n╠ 邀請中的成員數量 : {}".format(gPending)
                        ret_ += "\n╚══[ 這個群組 ]"
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'kick on':
                    if sender in Owner:
                        settings["kickmeber"] = True
                        backupData()
                        cl.sendMessage(to, "Kick:0")
                elif text.lower() == 'kick off':
                    if sender in Owner:
                        settings["kickmeber"] = False
                        backupData()
                        cl.sendMessage(to, "Kick:1")
                elif text.lower() == 'reread on':
                    if sender in Owner:
                        settings["reread"] = True
                        backupData()
                        cl.sendMessage(to, "查詢收回開啟")
                elif text.lower() == 'reread off':
                    if sender in Owner:
                        settings["reread"] = False
                        backupData()
                        cl.sendMessage(to, "查詢收回關閉")
                elif text.lower() == 'rec on':
                    if sender in Owner:
                        settings["reck"] = True
                        backupData()
                        cl.sendMessage(to, "查詢收回開啟")
                elif text.lower() == 'rec off':
                    if sender in Owner:
                        settings["reck"] = False
                        backupData()
                        cl.sendMessage(to, "查詢收回關閉")
                elif text.lower() == 'kickerjoin on':
                    if sender in Owner:
                        settings["kickerjoin"] = True
                        backupData()
                        cl.sendMessage(to, "自動加入群組已開啟")
                elif text.lower() == 'kickerjoin off':
                    if sender in Owner:
                        settings["kickerjoin"] = False
                        backupData()
                        cl.sendMessage(to, "自動加入群組已關閉")
                elif text.lower() == 'tag on':
                    if sender in Owner:
                        settings["targets"] = True
                        cl.sendMessage(to, "標註開啟")
                elif text.lower() == 'tag off':
                    if sender in Owner:
                        settings["targets"] = False
                        cl.sendMessage(to, "標註關閉")
                elif text.lower() == 'article on':
                    if sender in Owner:
                        settings["timeline"] = True
                        cl.sendMessage(to, "文章詳情開啟")
                        backupData()
                elif text.lower() == 'article off':
                    if sender in Owner:
                        settings["timeline"] = False
                        cl.sendMessage(to, "文章詳情關閉")
                        backupData()
#==============================================================================#
                elif text.lower() == 'me':
                    if sender in Owner:
                        Tag(to, sender)
                        cl.sendContact(to, sender)
                elif text.lower() == 'mymid':
                    if sender in Owner:
                        cl.sendMessage(msg.to,"[MID]\n" +  sender)
                elif text.lower() == 'myname':
                    if sender in Owner:
                        me = cl.getContact(sender)
                        cl.sendMessage(msg.to,"[顯示名稱]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    if sender in Owner:
                        me = cl.getContact(sender)
                        cl.sendMessage(msg.to,"[狀態消息]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    if sender in Owner:
                        me = cl.getContact(sender)
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    if sender in Owner:
                        me = cl.getContact(sender)
                        cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    if sender in Owner:
                        me = cl.getContact(sender)
                        cover = cl.getProfileCoverURL(sender)
                        cl.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("contact "):
                    if sender in Owner:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                contact = cl.getContact(ls)
                                mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if sender in Owner:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            ret_ = ""
                            for ls in lists:
                                ret_ += "" + ls
                            cl.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("name "):
                    if sender in Owner:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                contact = cl.getContact(ls)
                                cl.sendMessage(msg.to, "[ 顯示名稱 ]\n" + contact.displayName)
                elif msg.text.lower().startswith("bio "):
                    if sender in Owner:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                contact = cl.getContact(ls)
                                cl.sendMessage(msg.to, "[ 狀態消息 ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("picture "):
                    if sender in Owner:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                                cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("videoprofile "):
                    if sender in Owner:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus + "/vp"
                                cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cover "):
                    if sender in Owner:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = cl.getProfileCoverURL(ls)
                                    cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("copy "):
                    if sender in Owner:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                contact = mention["M"]
                                break
                            try:
                                cl.cloneContactProfile(contact)
                                cl.sendMessage(msg.to, "成功複製成員，請稍等片刻，直到配置文件更改")
                            except:
                                cl.sendMessage(msg.to, "無法複製成員")
                            
                elif text.lower() == 'restore':
                    if sender in Owner:
                        try:
                            clProfile.displayName = str(myProfile["displayName"])
                            clProfile.statusMessage = str(myProfile["statusMessage"])
                            clProfile.pictureStatus = str(myProfile["pictureStatus"])
                            cl.updateProfileAttribute(8, clProfile.pictureStatus)
                            cl.updateProfile(clProfile)
                            cl.sendMessage(msg.to, "成功恢復配置文件，請稍等片刻，直到配置文件更改")
                        except:
                            cl.sendMessage(msg.to, "恢復失敗")
                        
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    if sender in Owner:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                settings["mimic"]["target"][target] = True
                                cl.sendMessage(msg.to,"目標已添加！")
                                break
                            except:
                                cl.sendMessage(msg.to,"增加目標失敗！")
                                break
                elif msg.text.lower().startswith("mimicdel "):
                    if sender in Owner:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del settings["mimic"]["target"][target]
                                cl.sendMessage(msg.to,"目標廢除！")
                                break
                            except:
                                cl.sendMessage(msg.to,"目標廢除失敗！")
                                break
                elif text.lower() == 'mimiclist':
                    if sender in Owner:
                        if settings["mimic"]["target"] == {}:
                            cl.sendMessage(msg.to,"沒有目標")
                        else:
                            mc = "╔══[ 複製列表 ]"
                            for mi_d in settings["mimic"]["target"]:
                                mc += "\n╠ "+cl.getContact(mi_d).displayName
                            cl.sendMessage(msg.to,mc + "\n╚══[ 完 ]")
                    
                elif "mimic" in msg.text.lower():
                    if sender in Owner:
                        sep = text.split(" ")
                        mic = text.replace(sep[0] + " ","")
                        if mic == "on":
                            if settings["mimic"]["status"] == False:
                                settings["mimic"]["status"] = True
                                cl.sendMessage(msg.to,"回复消息開啟")
                    elif mic == "off":
                        if sender in Owner:
                            if settings["mimic"]["status"] == True:
                                settings["mimic"]["status"] = False
                                cl.sendMessage(msg.to,"回复消息關閉")
#==============================================================================#
                elif text.lower() == 'gowner':
                    if sender in Owner:
                        group = cl.getGroup(to)
                        GS = group.creator.mid
                        cl.sendContact(to, GS)
                elif text.lower() == 'gid':
                    if sender in Owner:
                        gid = cl.getGroup(to)
                        cl.sendMessage(to, "[群組ID : ]\n" + gid.id)
                elif text.lower() == 'gpicture':
                    if sender in Owner:
                        group = cl.getGroup(to)
                        path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                        cl.sendImageWithURL(to, path)
                elif text.lower() == 'gname':
                    if sender in Owner:
                        gid = cl.getGroup(to)
                        cl.sendMessage(to, "[群組名稱 : ]\n" + gid.name)
                elif text.lower() == 'gurl':
                    if sender in Owner:
                        if msg.toType == 2:
                            group = cl.getGroup(to)
                            if group.preventedJoinByTicket == False:
                                ticket = cl.reissueGroupTicket(to)
                                cl.sendMessage(to, "[ 群組網址 ]\nhttps://cl.me/R/ti/g/{}".format(str(ticket)))
                            else:
                                cl.sendMessage(to, "群組網址未開啟，請用Ourl先開啟".format(str(settings["keyCommand"])))
                elif text.lower() == 'ourl':
                    if sender in Owner:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == False:
                                cl.sendMessage(to, "群組網址已開啟")
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                cl.sendMessage(to, "成功開啟群組網址")
                elif text.lower() == 'curl':
                    if sender in Owner:
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == True:
                                cl.sendMessage(to, "群組網址已關閉")
                            else:
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                cl.sendMessage(to, "成功關閉群組網址")
                elif text.lower() == 'ginfo':
                    if sender in Lv1:
                        group = cl.getGroup(to)
                        try:
                            gtime = group.createdTime
                            gtimee = int(round(gtime/1000))
                        except Exception as e:
                            cl.sendMessage(msg.to,str(e))
                        try:
                            gCreator = group.creator.displayName
                        except:
                            gCreator = "未找到"
                        if group.invitee is None:
                            gPending = "0"
                        else:
                            gPending = str(len(group.invitee))
                        if group.preventedJoinByTicket == True:
                            gQr = "關閉"
                            gTicket = "沒有"
                        else:
                            gQr = "開啟"
                            gTicket = "https://cl.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                        try:
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                        except:
                            pass
                        ret_ = "╔══[ 群組資料 ]"
                        ret_ += "\n╠ 顯示名稱 : {}".format(str(group.name))
                        ret_ += "\n╠ 群組ＩＤ : {}".format(group.id)
                        ret_ += "\n╠ 群組作者 : {}".format(str(gCreator))
                        ret_ += "\n╠ 成員數量 : {}".format(str(len(group.members)))
                        ret_ += "\n╠ 邀請數量 : {}".format(gPending)
                        ret_ += "\n╠ 群組網址 : {}".format(gQr)
                        ret_ += "\n╠ 群組網址 : {}".format(gTicket)
                        ret_ += "\n╠ 群組建立時間 : {}".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(gtimee)))
                        ret_ += "\n╚══[ 完 ]"
                        cl.sendMessage(to, str(ret_))
                        try:
                            cl.sendImageWithURL(to, path)
                        except:
                            pass
                elif text.lower() == 'gb':
                    if sender in Owner:
                        if msg.toType == 2:
                            group = cl.getGroup(to)
                            ret_ = "╔══[ 成員列表 ]"
                            no = 0 + 1
                            for mem in group.members:
                                ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                                no += 1
                            ret_ += "\n╚══[ 總共： {} ]".format(str(len(group.members)))
                            cl.sendMessage(to, str(ret_))
                elif text.lower() == 'lg':
                    if sender in Owner:
                        groups = kicker01.groups
                        ret_ = "╔══[ 群組列表 ]"
                        no = 0 + 1
                        k = len(groups)//50
                        for a in range(k+1):
                            for gid in groups:
                                try:
                                    group = kicker01.getGroup(gid)
                                    ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                    no += 1
                                    print(ret_)
                                except Exception as e:
                                    print(e)
                            ret_ += "\n╚══[ 總共 {} 個群組 ]".format(str(len(groups)))
                            cl.sendMessage(to, str(ret_))
#==============================================================================#          
                elif text.lower() == 'tagall':
                    if sender in Owner:
                        if msg.toType == 2:
                            if settings["targets"] == True:
                                group = cl.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//100
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*100 : (a+1)*100]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@CoCo \n'
                                    cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    cl.sendMessage(to, "總共 {} 個成員".format(str(len(nama))))
                            else:
                                cl.sendMessage(to, "標註未開啟")
                elif text.lower() == 'sn':
                    if sender in Owner:
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                            if bln == str(k): bln = bulan[k-1]
                        readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                        if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                cl.sendMessage(msg.to,"已讀點已開始")
                        else:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                cl.sendMessage(msg.to, "設定已讀點:\n" + readTime)
                        backupData()
                            
                elif text.lower() == 'sf':
                    if sender in Owner:
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                            if bln == str(k): bln = bulan[k-1]
                        readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                        if msg.to not in read['readPoint']:
                            cl.sendMessage(msg.to,"已讀點已經關閉")
                        else:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            cl.sendMessage(msg.to, "刪除已讀點:\n" + readTime)
                        backupData()
    
                elif text.lower() == 'rr':
                    if sender in Owner:
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                            if bln == str(k): bln = bulan[k-1]
                        readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                        if msg.to in read["readPoint"]:
                            try:
                                del read["readPoint"][msg.to]
                                del read["readMember"][msg.to]
                                del read["readTime"][msg.to]
                            except:
                                pass
                            cl.sendMessage(msg.to, "重置已讀點:\n" + readTime)
                        else:
                            cl.sendMessage(msg.to, "已讀點未設定")
                        backupData()
                        
                elif text.lower() == 'r':
                    if sender in Owner:
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                            if bln == str(k): bln = bulan[k-1]
                        readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                        if receiver in read['readPoint']:
                            if read["ROM"][receiver].items() == []:
                                cl.sendMessage(receiver,"[ 已讀者 ]:\n沒有")
                            else:
                                chiya = []
                                for rom in read["ROM"][receiver].items():
                                    chiya.append(rom[1])
                                cmem = cl.getContacts(chiya)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = '[ 已讀者 ]:\n'
                            for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@c\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                            text = xpesan+ zxc + "\n[ 已讀時間 ]: \n" + readTime
                            try:
                                cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except Exception as error:
                                print (error)
                            pass
                        else:
                            cl.sendMessage(receiver,"已讀點未設定")
                        backupData()
#==============================================================================#

#==============================================================================#
                elif "嬌喘" in msg.text:
                    if sender in Owner:
                        word = "あｯ…あぁいｯいｯ..痛いよぉ…ふぇ..強いのぉ……なっ…なかに出してぇ…あｯ…あうぅ…//(ﾄﾞﾛﾄﾞﾛｼﾞｭﾋﾞｨ~)","あｯ…あぁもっと大きいの…ふぇ..もっともっと……なっ…なかに出してぇ…あｯ…あうぅ…//(ﾄﾞﾛﾄﾞﾛｼﾞｭﾋﾞｨ~)","ヵッォ､､､ぉっゅ､､､ぅぅぅ///","ひゃうん！はぅんあっやっ、もうだめもうやめて！これ以上されたら、おか、おかしくなるぅううう！","あ…あぁっ…!!いっだめぇっ……///\nイッ…イクゥっ!!!イッちゃうぅぅぅあぁぁあああっっ!!!(ﾄﾞﾋﾞｭｯｼｰ","オォゥ…ベリベリビッグペニス…オゥグゥッド…オウイエェス","ぁあああ あぉん///イっくぅぅふぅんっ"
                        cl.sendMessage(msg.to, random.choice(word))
                elif "喘" in msg.text:
                    if sender in Owner:
                        cl.sendMessage(to, "唔嗯…啊…想…想要主人唔嗯…好…好想要呀…不…不可以喝…嗯啊…好…好髒哈啊…唔嗯…啊…主…主人…哈啊…給…給人家唔嗯…好…好難受哼嗯…啊…好…好想要…唔啊…求求主人哈啊…用主人嗯哼…哈啊…的大肉棒呀…幹壞…哈啊…幹壞人家…人家淫蕩的…唔嗯…的小穴…哼嗯…啊…唔嗯…啊！哈啊…唔嗯…好…好舒服…嗯哈…好…好大呀…好滿…嗯哈…呀…還…還想要更多…唔嗯…啊哈…唔嗯…啊！別…嗯啊…尾…尾巴哈啊…跟…跟耳朵哼嗯…呀…會…壞掉的…嗯哼…唔嗯…主…主人…哈啊…請…請用你的哈啊…大肉棒唔嗯…幹壞人家哈啊…這隻…小騷貓…嗯啊…唔嗯…哈啊…好…好棒…呀…主…主人的嗯啊…好大呀…人家…人家的小騷穴好…嗯哈…好癢啊哈…好難受…嗯哼…呀…想…想要主人唔嗯…主人的大雞巴幹…幹壞…唔嗯…人家的騷穴…唔嗯…呀…好…好舒服唔嗯…哈啊…好棒…好舒服…主…主人好棒…啊…要…要壞了…唔嗯…主…主人哈啊…好…好舒服…")

#==============================================================================#   
                elif text.lower() == 'time':
                    if sender in Owner:
                        tz = pytz.timezone("Asia/Makassar")
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                            if bln == str(k): bln = bulan[k-1]
                        readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                        cl.sendMessage(msg.to, readTime)
                elif "checkdate" in msg.text.lower():
                    if sender in Owner:
                        sep = msg.text.split(" ")
                        tanggal = msg.text.replace(sep[0] + " ","")
                        r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                        data=r.text
                        data=json.loads(data)
                        ret_ = "╔══[ 日期 ]"
                        ret_ += "\n╠ 出生日期 : {}".format(str(data["data"]["lahir"]))
                        ret_ += "\n╠ 年齡 : {}".format(str(data["data"]["usia"]))
                        ret_ += "\n╠ 生日 : {}".format(str(data["data"]["ultah"]))
                        ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                        ret_ += "\n╚══[ 完成 ]"
                        cl.sendMessage(to, str(ret_))
                elif "searchimage" in msg.text.lower():
                    if sender in Owner:
                        separate = msg.text.split(" ")
                        search = msg.text.replace(separate[0] + " ","")
                        with requests.session() as web:
                            web.headers["User-Agent"] = random.choice(settings["userAgent"])
                            r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                            data = r.text
                            data = json.loads(data)
                            if data["result"] != []:
                                items = data["result"]
                                path = random.choice(items)
                                a = items.index(path)
                                b = len(items)
                                cl.sendImageWithURL(to, str(path))
                elif "searchyoutube" in msg.text.lower():
                    if sender in Owner:
                        sep = text.split(" ")
                        search = text.replace(sep[0] + " ","")
                        params = {"search_query": search}
                        with requests.session() as web:
                            web.headers["User-Agent"] = random.choice(settings["userAgent"])
                            r = web.get("https://www.youtube.com/results", params = params)
                            soup = BeautifulSoup(r.content, "html5lib")
                            ret_ = "╔══[ Youtube 結果 ]"
                            datas = []
                            for data in soup.select(".yt-lockup-title > a[title]"):
                                if "&lists" not in data["href"]:
                                    datas.append(data)
                            for data in datas:
                                ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                                ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                            ret_ += "\n╚══[ 總共 {} ]".format(len(datas))
                            cl.sendMessage(to, str(ret_))
            elif msg.contentType == 6:
                tz = pytz.timezone("Asia/Makassar")
                timeNow = datetime.now(tz=tz)
                if msg.contentMetadata['GC_IGNORE_ON_FAILBACK'] == "false":
                    try:
                        del times['Time'][op.param1]
                    except:
                        pass
                    if msg.toType == 2:
                        if msg.contentMetadata['GC_MEDIA_TYPE'] == 'AUDIO':
                            Stnn = cl.getContact(sender)
                            aa = '{"S":"0","E":"3","M":'+json.dumps(Stnn.mid)+'}'
                            cl.sendMessage(to, '@Co \n開始了群組通話\n開始時間\n' + timeNow.strftime('%H:%M:%S'), contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                        else:
                            Stnn = cl.getContact(sender)
                            aa = '{"S":"0","E":"3","M":'+json.dumps(Stnn.mid)+'}'
                            cl.sendMessage(to, '@Co \n開始了視訊通話\n開始時間\n' + timeNow.strftime('%H:%M:%S'), contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                else:
                    cl.sendMessage(msg.to,"通話結束\n" + timeNow.strftime('%H:%M:%S'))
#==============================================================================#
            elif msg.contentType == 7:
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                if settings["checkSticker"] == True:
                    ret_ = "╔══[ 貼圖訊息 ]"
                    ret_ += "\n╠ 貼圖ID : {}".format(stk_id)
                    ret_ += "\n╠ 貼圖包ID : {}".format(pkg_id)
                    ret_ += "\n╠ 貼圖版本 : {}".format(stk_ver)
                    ret_ += "\n╠ 貼圖網址L : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ 完 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + stk_id + '/ANDROID/sticker.png')
                if pkg_id in ckt['ck'] and stk_id in ckt['ck'][pkg_id]:
                    ctext = ckt['ck'][pkg_id][stk_id]
                    cl.sendMessage(to, ctext)
#==============================================================================#
            elif msg.contentType == 13:
                if settings['mimic']["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Copy")
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        cl.sendMessage(msg.to, "未找到...")
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.cloneContactProfile(target)
                                cl.sendMessage(msg.to, "成功複製成員,請稍等,直到更新資料")
                                settings['mimic']['copy'] = False
                                break
                            except:
                                msg.contentMetadata = {'mid': target}
                                settings['micic']["copy"] = False
                                break
#==============================================================================#
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.contentType == 0:
                        if msg.toType == 0:
                            cl.log("[%s]"%(msg._from)+msg.text)
                        else:
                            cl.log("[%s]"%(msg.to)+msg.text)
                        if msg.contentType == 0:
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                    if len(msg_dict) > 100:
                        del msg_dict[min(list(msg_dict.keys()))]
                    logRead()
                if settings["reck"] == True:
                    if msg.contentType == 7:
                        stk_id = msg.contentMetadata['STKID']
                        if msg.toType == 0:
                            cl.log("[%s]"%(msg._from) + stk_id)
                        else:
                            cl.log("[%s]"%(msg.to) + stk_id)
                        if msg.contentType == 7:
                            msg_dict[msg.id] = {"id":stk_id,"from":msg._from,"createdTime":msg.createdTime}
                    if len(msg_dict) > 100:
                        del msg_dict[min(list(msg_dict.keys()))]
                    logRead()
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                msg = op.message
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            rereadtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(round(msg_dict[msg_id]["createdTime"]/1000))))
                            newtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(round(time.time()))))
                            try:
                                mi_d = msg_dict[msg_id]["from"]
                                cmem = cl.getContact(mi_d)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = '[ 收回者 ]\n'
                                xretext = '[ 收回訊息 ]\n'
                                xname = str(cmem.displayName)
                                pesan = ''
                                pesan2 = pesan+"@c\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                retext = msg_dict[msg_id]["text"]
                                text = xpesan + zxc + xretext + retext + "\n[ 發送時間 ]\n" + rereadtime + "\n[ 收回時間 ]: \n" + newtime
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                txr = '[收回了一個貼圖]\n\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                pesan = '@c \n'
                                text_ =  pesan + txr
                                cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                cl.sendImageWithURL(at, 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/ANDROID/sticker.png')
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 26:
            # print ("[ 26 ] 接收消息")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                   text = msg.text
                   if text is not None:
                       cl.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = cl.getContact(sender)
                                    cl.sendMessage(to, "標我幹嘛?")
                                    Tag(to, contact.mid)
                                break
#==============================================================================#
        if op.type == 25 or op.type == 26:
            msg = op.message
            if msg.contentType == 0:
              if msg.text.lower() == '/ti/g/':
                if settings["autoJoinTicket"] == True:
                    n_link = text.replace('/ti/g/','')
                    for ticket_id in n_links:
                        try:
                            group = cl.findGroupByTicket(ticket_id)
                            cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                            baime.acceptGroupInvitationByTicket(group.id, ticket_id)
                            orange.acceptGroupInvitationByTicket(group.id, ticket_id)
                            kicker01.acceptGroupInvitationByTicket(group.id, ticket_id)
                            kicker02.acceptGroupInvitationByTicket(group.id, ticket_id)
                            kicker03.acceptGroupInvitationByTicket(group.id, ticket_id)
                            kicker04.acceptGroupInvitationByTicket(group.id, ticket_id)
                            kicker05.acceptGroupInvitationByTicket(group.id, ticket_id)
                            kicker06.acceptGroupInvitationByTicket(group.id, ticket_id)
                            kicker07.acceptGroupInvitationByTicket(group.id, ticket_id)
                            kicker08.acceptGroupInvitationByTicket(group.id, ticket_id)
                            kicker09.acceptGroupInvitationByTicket(group.id, ticket_id)
                            kicker10.acceptGroupInvitationByTicket(group.id, ticket_id)
                        except Exception as e:
                            logError(e)
#==============================================================================#
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in read['wait2']['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in read['wait2']['readMember'][op.param1]:
                        pass
                    else:
                        read['wait2']['readMember'][op.param1] += "\n[•]" + Name
                        read['wait2']['ROM'][op.param1][op.param2] = "[•]" + Name
                        print (Name)
                else:
                    pass
            except:
                pass
            try:
                if op.param1 in read['Read']['Point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in read['Read']['Member'][op.param1]:
                        pass
                    else:
                        read['Read']['Member'][op.param1] += "\n[•]" + Name
                        read['Read']['ROM'][op.param1][op.param2] = "[•]" + Name
                        print(Name)
                            #aa = '{"S":"0","E":"3","M":'+json.dumps(op.param2)+'}'
                            #cl.sendMessage(op.param1, '@Co \n已讀ㄌ訊息',  contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                            #cl.sendMessage(op.param1, op.param2)
                else:
                    pass
            except:
                pass
            backupData()

    except Exception as error:
        logError(error)
#==============================================================================#
def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
