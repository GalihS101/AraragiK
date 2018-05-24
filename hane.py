# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,atexit
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
cl = LINE() 
cl.log("Auth Token : " + str(cl.authToken))
oepoll = OEPoll(cl)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
lineSettings = cl.getSettings()
clProfile = cl.getProfile()
clMID = cl.profile.mid
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
admin=['u529ed08e968ba9d107784186eb66b76a','ua5f2cbc325816777be5ef529eb920c50',clMID]
msg_dict = {}
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']
bl = [""]
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ EROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """╔═════════════════════════
║      Araragi Kanega 👑 Ay 
║╔═════════════════════════
║╠࿐【Self:help】
║╠࿐【HelpTag】
║╠࿐【HelpKick】
║╠⎆ ༼ Araragi Bot ༽══࿐
║╠࿐【Self:rebot】
║╠࿐【Runtime】
║╠࿐【Speed】
║╠࿐【Set】
║╠࿐【About】
║╠࿐【Creator】
║╠⎆ ༼ Araragi Setting ༽══࿐
║╠࿐【Add On/Off】
║╠࿐【Join On/Off】
║╠࿐【Leave On/Off】
║╠࿐【Read On/Off】
║╠࿐【Inviteprotect On/Off】
║╠࿐【Reread On/Off】
║╠࿐【Qr On/Off】
║╠࿐【Qrjoin On/Off】
║╠࿐【Ck On/Off】
║╠࿐【Groupprotect On/Off】
║╠࿐【Kc On/Off】
║╠࿐【Ptt On/Off】
║╠࿐Tag on/off
║╠⎆ ༼ Araragi  Self  ༽══࿐
║╠࿐【Me】
║╠࿐【MyMid】
║╠࿐【MyName】
║╠࿐【MyBio】
║╠࿐【MyPicture】
║╠࿐【MyCover】
║╠࿐【Contact @】
║╠࿐【Friendlist】
║╠⎆ ༼ Araragi Group ༽══࿐
║╠࿐【Gowner】
║╠࿐【Gurl】
║╠࿐【O/Curl】
║╠࿐【Lg】
║╠࿐【Gb】
║╠࿐【Ginfo】
║╠࿐【Vk:mid】
║╠࿐【Nk Name】
║╠࿐【Kickall】
║╠࿐【Uk mid】
║╠࿐【NT Name】
║╠࿐【Zk, Zt, Zm】
║╠࿐【Cancel】
║╠࿐【Gcancel】
║╠࿐【Gn Name】
║╠࿐【Gc @】
║╠࿐【Inv mid】
║╠࿐【Mb:mid】
║╠࿐【Mub:mid
║╠࿐【Clear Ban】
║╠࿐【Kill Ban】
║╠࿐【Killbanall】
║╠࿐【banlist
║╠࿐【Sc gid】
║╠࿐【Mc mid】
║╠⎆ ༼ Araragi Khusus ༽══࿐
║╠࿐【Tagall
║╠࿐【SR/DR】
║╠࿐【LR】
║╠࿐【F/Gbc】
║╠࿐【/invitemeto:】
║╠࿐【Op @】
║╠࿐【Deop @】
║╠࿐【mop:mid】
║╠࿐【mdp:mid】
║╠࿐【Opmid】
║╠࿐【Oplist
║╚═════════════════════════
║    Credits by : Araragi Kanega 👑 Ay 
╚══════════════════════════
"""
    return helpMessage
def helpmessagetag():
    helpMessageTag ="""╔═════════════════════════
║            Araragi Kanega 👑 Ay 
║╔═════════════════════════
║╠࿐〘Help Tag〙
║╠࿐【Ri @】
║╠࿐【Tk @
║╠࿐【Mk @
║╠࿐【Vk @】
║╠࿐【Gc @】
║╠࿐【Mid @】
║╠࿐【Name @】
║╠࿐【Bio @】
║╠࿐【Picture @】
║╠࿐【Cover @
║╠࿐【Ban @】
║╠࿐【Unban @】
║╚═════════════════════════
║ ࿐Credits By. Araragi Kanega 👑 Ay 
╚══════════════════════════
"""
    return helpMessageTag
def helpmessagekick():
    helpMessageKick ="""╔═════════════════════════
║   Araragi Kanega 👑 Ay 
║╔═════════════════════════
║╠࿐〘Help Kick〙
║╠࿐【Ri @】
║╠࿐【Tk @】
║╠࿐【Mk @
║╠࿐【Vk @】
║╠࿐【Vk:mid】
║╠࿐【Nk Name
║╠࿐【Uk mid】
║╠࿐【Kill ban】
║╠࿐【Zk】
║╚═════════════════════════
║ ࿐Credits By Araragi Kanega 👑 Ay 
╚══════════════════════════
"""
    return helpMessageKick
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(op.param1)
            print ("[ 5 ] NOTIFED ADD CONTACT: " + contact.displayName)
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1, "Halo Thanks Telah Invit 👺".format(str(contact.displayName)))
                cl.sendMessage(op.param1, "Jangan Lupa Gift 🎁 ")
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    gs.preventJoinByTicket = True
                    cl.updateGroup(gs)
                    invsend = 0
                    cl.sendMessage(op.param1,cl.getContact(op.param2).displayName + "perlindungan URL.... JANGAN DIBUKA！")
                    cl.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            if settings["inviteprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    time.sleep(0.15)
                    cl.kickoutFromGroup(op.param1,[op.param3])
                    time.sleep(0.15)
                    cl.kickoutFromGroup(op.param1,[op.param2])
            if clMID in op.param3:
                if settings["autoJoin"] == True:
                    try:
                        arrData = ""
                        text = "%s "%('[提示]')
                        arr = []
                        mention = "@x "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention + "Assalamualaikum... "
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        cl.sendMessage(op.param1, "Created ：")
                        cl.sendContact(op.param1, "u9cdc29cb1452168cadae627171b7a6ee")
                    except Exception as error:
                        print(error)
            if clMID in op.param3:
                if settings["autoPtt"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1, "Selamat Tinggal Kalian Semua 👺")
                    cl.leaveGroup(op.param1)
        if op.type == 15:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            if settings["seeLeave"] == True:
                try:
                    arrData = ""
                    text = "%s "%('[Hallo 👺]')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + " Semoga Tenang Di alam Sana 🔪{} ！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 17:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            if settings["seeJoin"] == True:
                try:
                    arrData = ""
                    text = "%s "%('Halo 👋 ')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "Cek Note.  Baca Rules, weeduz！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[19]NOTIFED KICKOUT FROM GROUP: " + str(group.name) + "\n" + op.param1 +"\nNama: " + contact1.displayName + "\nMid:" + contact1.mid + "\nNama: " + contact2.displayName + "\nMid:" + contact2.mid )
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
                        cl.sendMessage(op.param1, "[Peringatan ] %s TenDang%s"%(contact1.displayName,contact2.displayName))
                        cl.sendMessage(op.param1, "Kicker：")
                        sendMessageWithMention(op.param1, contact1.mid)
                        cl.sendMessage(op.param1, "Ditendang：")
                        sendMessageWithMention(op.param1, contact2.mid)
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
            else:
                if settings["kickContact"] == True:
                    cl.sendMessage(op.param1, "[Peringatan ] %s TenDang %s"%(contact1.displayName,contact2.displayName))
                    cl.sendMessage(op.param1, "Kicker ：")
                    sendMessageWithMention(op.param1, contact1.mid)
                    cl.sendMessage(op.param1, "Ditendang：")
                    sendMessageWithMention(op.param1, contact2.mid)
                else:
                    pass
        if op.type == 22:
            print ("[ 22 ] NOTIFED LEAVE GROUP")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1] NOTIFED FILE KONFIGURASION")
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
            if msg.contentType == 7:
               if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ = "[ Date ]"
                    ret_ += "\TextureID : {}".format(stk_id)
                    ret_ += "\nTagID : {}".format(pkg_id)
                    ret_ += "\nMap : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\nPicture：https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ += "\n[ end ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
            if msg.contentType == 13:
                if settings["contact"] == True:
                    #msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[Name]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[Check]:\n" + contact.statusMessage + "\n[Url]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[Cover]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[Name]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[Check]:\n" + contact.statusMessage + "\n[Url]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[Cover]:\n" + str(cu))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    try:
                        msg.contentType = 0
                        f_mid = msg.contentMetadata["postEndUrl"].split("userMid=")
                        s_mid = f_mid[1].split("&")
                        mid = s_mid[0]
                        try:
                            arrData = ""
                            text = "%s\n%s\n"%("---[Saham]---","[Created]:")
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':mid}
                            arr.append(arrData)
                            text += mention + "\n[Tinjau]:\n" + msg.contentMetadata["text"] + "\n(100 Only)" + "\n[Url]:\n" + msg.contentMetadata["postEndUrl"]
                            cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    except:
                        ret_ = "---[Tinjau Artikel]---\n[Tinjau]:\n" + msg.contentMetadata["text"] + "\n(100 Only)"
                        ret_ += "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                        cl.sendMessage(msg.to, str(ret_))
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in admin:
                if msg.text in ["Help"]:
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                    cl.sendMessage(to, "My Creator:")
                    cl.sendContact(to, "u9cdc29cb1452168cadae627171b7a6ee")
                elif text.lower() == 'helptag':
                    helpMessageTag = helpmessagetag()
                    cl.sendMessage(to, str(helpMessageTag))
                elif text.lower() == 'helpkick':
                    helpMessageKick = helpmessagekick()
                    cl.sendMessage(to, str(helpMessageKick))
                elif text.lower() == 'creator':
                    cl.sendMessage(to, "My Creator:")
                    cl.sendContact(to, "u9cdc29cb1452168cadae627171b7a6ee")
                elif "Fbc:" in msg.text:
                    bctxt = text.replace("Fbc:","")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,(bctxt))
                elif "Gbc:" in msg.text:
                    bctxt = text.replace("Gbc:","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,(bctxt))
                elif "Ri " in msg.text:
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
                                except:
                                    pass
                elif "Ri:" in msg.text:
                    midd = text.replace("Ri:","")
                    cl.kickoutFromGroup(to,[midd])
                    cl.findAndAddContactsByMid(midd)
                elif "Uk " in msg.text:
                    midd = text.replace("Uk ","")
                    cl.kickoutFromGroup(to,[midd])
                elif "Tk " in msg.text:
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
                elif "Mk " in msg.text:
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
                elif "Nk " in msg.text:
                    _name = text.replace("Nk ","")
                    gs = cl.getGroup(to)
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
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Kickall" in msg.text:
                    if settings["kickmeber"] == True:
                        if msg.toType == 2:
                            _name = msg.text.replace("Kickall","")
                            gs = cl.getGroup(to)
                            cl.sendMessage(to, "Terdjang Boskuh.....  👋👺👺👋")
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
                                            cl.kickoutFromGroup(to, [target])
                                        except:
                                            pass
                elif "Zk" in msg.text:
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
                elif "Vk:" in text: #Untuk Menghilangkan Jejak,  ( kikck -  invit - batal )  by : Araragi Kenega
                    midd = msg.text.replace("Vk:","")
                    cl.kickoutFromGroup(msg.to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    cl.cancelGroupInvitation(msg.to,[midd])
                elif "Vk " in msg.text:
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
                elif "NT " in msg.text:
                    _name = text.replace("NT ","")
                    gs = cl.getGroup(to)
                    targets = []
                    net_ = ""
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            mc = sendMessageWithMention(to,target) + "\n"
                        cl.sendMessage(to,mc)
                elif text.lower() == 'zt':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            sendMessageWithMention(to,target)
                elif text.lower() == 'zm':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        mc = "0Mid："
                        for mi_d in targets:
                            mc += "\n->" + mi_d
                        cl.sendMessage(to,mc)
                elif "Mc " in msg.text:
                    mmid = msg.text.replace("Mc ","")
                    cl.sendContact(to, mmid)
                elif "Sc " in msg.text:
                    ggid = msg.text.replace("Sc ","")
                    group = cl.getGroup(ggid)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tak Dikenal"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Open"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    else:
                        gQr = "Close"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "     [👺Araragi Kanega 👑 Ay 👺 ]"
                    ret_ += "\nNama         : {}".format(str(group.name))
                    ret_ += "\nＩＤ             : {}".format(group.id)
                    ret_ += "\nCreator      : {}".format(str(gCreator))
                    ret_ += "\nMember    : {}".format(str(len(group.members)))
                    ret_ += "\nPending     : {}".format(gPending)
                    ret_ += "\nQr                : {}".format(gQr)
                    ret_ += "\nUrl               : {}".format(gTicket)
                    ret_ += "\n[👺Araragi Kanega 👑 Ay 👺 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif msg.text in ["c","C","cancel","Cancel"]:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = cl.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            cl.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        cl.sendMessage(to, "Batal\nBatal Time: %s秒" % (elapsed_time))
                        cl.sendMessage(to, "Batal\nBatal Time: %s秒" % (elapsed_time))
                        cl.sendMessage(to, "Batal Numb:" + sinvitee)
                    else:
                        cl.sendMessage(to, "Tidak Ada undangan Weduzz！👺👺")
                elif text.lower() == 'gcancel':
                    gid = cl.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    cl.sendMessage(to, "Semua Undangan Di batalkan ndezz 👺👺")
                    cl.sendMessage(to, "Pembatalan: %s秒" % (elapsed_time))
                elif "Gn " in msg.text:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendMessage(msg.to,"Tidak Bekerja jika di luar group.  Weduzz 👺👺")
                elif text.lower().startswith('op '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.append(str(inkey))
                        cl.sendMessage(to, "Ditambahkan Boz ！")
                elif text.lower().startswith('deop '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.remove(str(inkey))
                        cl.sendMessage(to, "Telah Di Gajul 👺👺！")
                elif text.lower().startswith('mop:'):
                        midd = msg.text.replace("mop:","")
                        admin.append(str(midd))
                        cl.sendMessage(to, "Di ➕ Mbobs！") 
                        backupData()
                elif text.lower().startswith('mdp:'):
                        midd = msg.text.replace("mdp:","")
                        admin.remove(str(midd))
                        cl.sendMessage(to, "Di Hapus 👺👺！") 
                        backupData()
                elif text.lower() == 'opmid':
                    if admin == []:
                        cl.sendMessage(to, "Tanpa Izin")
                    else:
                        mc = "Daftar Izin nya Boz 🐌："
                        for mi_d in admin:
                            mc += "\n-> " + mi_d
                        cl.sendMessage(to, mc)
                elif text.lower() == 'oplist':
                    if admin == []:
                        cl.sendMessage(to, "Tanpa Izin")
                    else:
                        mc = "Daftar izin nya boz 🐌："
                        for mi_d in admin:
                            mc += "\n◉ " + cl.getContact(mi_d).displayName
                        cl.sendMessage(to, mc)
                elif "Gc" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        u = key["MENTIONEES"][0]["M"]
                        contact = cl.getContact(u)
                        cu = cl.getProfileCoverURL(mid=u)
                        try:
                            cl.sendMessage(msg.to,"Nama:\n" + contact.displayName + "\n\nMid:\n" + contact.mid + "\n\nStatus:\n" + contact.statusMessage + "\n\nUrl :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nSampul :\n" + str(cu))
                        except:
                            cl.sendMessage(msg.to,"Nama:\n" + contact.displayName + "\n\nMid:\n" + contact.mid + "\n\nStatus:\n" + contact.statusMessage + "\n\nSampul:\n" + str(cu))
                elif "Inv " in msg.text:
                    midd = msg.text.replace("Inv ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                elif "Ban" in msg.text:
                    if msg.toType == 2:
                        print ("[Ban] Sukzez")
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
                                    settings["blacklist"][target] = True
                                    cl.sendMessage(to, "Di Ceblozkan 👺👺")
                                except:
                                    pass
                elif "Unban" in msg.text:
                    if msg.toType == 2:
                        print ("[UnBan] Sukzes 👺")
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
                                    del settings["blacklist"][target]
                                    cl.sendMessage(to, "Telah Di tutup")
                                except:
                                    pass
                elif "Mb:" in msg.text:
                    midd = msg.text.replace("Mb:","")
                    try:
                        settings["blacklist"][midd] = True
                        backupData()
                        cl.sendMessage(to, "Tersangka 👋")
                    except:
                        pass
                elif "Mub:" in msg.text:
                    midd = msg.text.replace("Mub:","")
                    try:
                        del settings["blacklist"][midd]
                        backupData()
                        cl.sendMessage(to, "Yang Di tutup ")
                    except:
                        pass
                elif text.lower() == 'clear ban':
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                    cl.sendMessage(to, "Yang di hapus ")
                elif text.lower() == 'banlist':
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "Bersih 🐈")
                    else:
                        mc = "BlackList："
                        for mi_d in settings["blacklist"]:
                            mc += "\n->" + cl.getContact(mi_d).displayName
                        cl.sendMessage(to, mc)
                elif text.lower() == 'banmid':
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "Bersih")
                    else:
                        mc = "BlackList："
                        for mi_d in settings["blacklist"]:
                            mc += "\n->" + mi_d
                        cl.sendMessage(to, mc)
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            cl.sendMessage(to, "Ora Eneng Kambing 👺👺")
                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "Tersangka Berhasil Di Jebloskan 👺👺")
                elif text.lower() == 'killbanall':
                    gid = cl.getGroupIdsJoined()
                    group = cl.getGroup(to)
                    gMembMids = [contact.mid for contact in group.members]
                    ban_list = []
                    for tag in settings["blacklist"]:
                        ban_list += filter(lambda str: str == tag, gMembMids)
                    if ban_list == []:
                        cl.sendMessage(to, "Tidak Ada DAFTAR Hitam ")
                    else:
                        for i in gid:
                            for jj in ban_list:
                                cl.kickoutFromGroup(i, [jj])
                            cl.sendMessage(i, "All Black Group！")
                elif "/invitemeto:" in msg.text:
                    gid = msg.text.replace("/invitemeto:","")
                    if gid == "":
                        cl.sendMessage(to, "Masukan Id Dodol")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg._from)
                            cl.inviteIntoGroup(gid,[msg._from])
                        except:
                            cl.sendMessage(to, "Tidak Terdaftar 🐒 ")
                elif msg.text in ["Friendlist"]:
                    anl = cl.getAllContactIds()
                    ap = ""
                    for q in anl:
                        ap += "• "+cl.getContact(q).displayName + "\n"
                    cl.sendMessage(msg.to,"「 Daftar 」\n"+ap+"Numb : "+str(len(anl)))
                elif text.lower() == 'sp':
                    start = time.time()
                    cl.sendMessage(to, "Progress.... ")
                    elapsed_time = (time.time() - start)/100
                    cl.sendMessage(to,format(str(elapsed_time)) + "Second")
                elif text.lower() == 'speed':
                    start = time.time()
                    cl.sendMessage(to, "Progress... ")
                    elapsed_time = (time.time() - start)/100
                    cl.sendMessage(to,format(str(elapsed_time)) + "Second")
                elif text.lower() == 'self:rebot':
                    cl.sendMessage(to, "Prosess... ")
                    time.sleep(5)
                    cl.sendMessage(to, "Berhasil.... ！")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "Ngesot Selama {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u9cdc29cb1452168cadae627171b7a6ee"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "👺Araragi Kanega 👑 Ay 👺 "
                        ret_ += "\nNama            : {}".format(contact.displayName)
                        ret_ += "\nGc                  : {}".format(str(len(grouplist)))
                        ret_ += "\nCont               : {}".format(str(len(contactlist)))
                        ret_ += "\nBlock             : {}".format(str(len(blockedlist)))
                        ret_ += "\n 👺Araragi Kanega 👑 Ay 👺 "
                        ret_ += "\nTentang        : Araragi Bot"
                        ret_ += "\nFormat          : {}".format(creator.displayName)
                        ret_ += "\n(´・ω・｀)"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'set':
                    try:
                        ret_ = "[ Status ]"
                        if settings["autoAdd"] == True: ret_ += "\nAuto Add✔"
                        else: ret_ += "\nAuto Add ✘"
                        if settings["autoJoin"] == True: ret_ += "\nAuto Join ✔"
                        else: ret_ += "\nAuto Join ✘"
                        if settings["autoJoinTicket"] == True: ret_ += "\nAuto Join Tickets ✔"
                        else: ret_ += "\nAuto Join Tickets ✘"
                        if settings["autoLeave"] == True: ret_ += "\nAuto Leave ✔"
                        else: ret_ += "\nAuto Leave ✘"
                        if settings["autoRead"] == True: ret_ += "\nRead✔"
                        else: ret_ += "\nRead ✘"
                        if settings["protect"] == True: ret_ += "\nProtected ✔"
                        else: ret_ += "\nProtected ✘"
                        if settings["inviteprotect"] == True: ret_ += "\nInvit Pro ✔"
                        else: ret_ += "\nInvit Pro ✘"
                        if settings["qrprotect"] == True: ret_ += "\nQr pro ✔"
                        else: ret_ += "\nQr pro ✘"
                        if settings["contact"] == True: ret_ += "\nContact ✔"
                        else: ret_ += "\nContact ✘"
                        if settings["reread"] == True: ret_ += "\nReRead ✔"
                        else: ret_ += "\nReRead ✘"
                        if settings["detectMention"] == False: ret_ += "\nDetectMention ✔"
                        else: ret_ += "\nDetectMention ✘"
                        if settings["checkSticker"] == True: ret_ += "\nStiker ✔"
                        else: ret_ += "\nStiker ✘"
                        if settings["kickContact"] == True: ret_ += "\nKick Contact✔"
                        else: ret_ += "\nKick Contact ✘"
                        if settings["autoPtt"] == True: ret_ += "\nAuto Ptt ✔"
                        else: ret_ += "\nAuto Ptt ✘"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'add on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "Auto Add ✔")
                elif text.lower() == 'add off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "Auto Add ✘")
                elif text.lower() == 'join on':
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "Join ✔")
                elif text.lower() == 'join off':
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "Join ✘")
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "Leave ✔")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "Leave ✘")
                elif text.lower() == 'contact on':
                    settings["contact"] = True
                    cl.sendMessage(to, "Contact ✔")
                elif text.lower() == 'contact off':
                    settings["contact"] = False
                    cl.sendMessage(to, "Contact ✘")
                elif text.lower() == 'groupprotect on':
                    settings["protect"] = True
                    cl.sendMessage(to, "Protect ✔")
                elif text.lower() == 'groupprotect off':
                    settings["protect"] = False
                    cl.sendMessage(to, "Protect ✘")
                elif text.lower() == 'inviteprotect on':
                    settings["inviteprotect"] = True
                    cl.sendMessage(to, "Invit Pro ✔")
                elif text.lower() == 'inviteprotect off':
                    settings["inviteprotect"] = False
                    cl.sendMessage(to, "Invit Pro ✘")
                elif text.lower() == 'qr on':
                    settings["qrprotect"] = True
                    cl.sendMessage(to, "Qr ✔")
                elif text.lower() == 'qr off':
                    settings["qrprotect"] = False
                    cl.sendMessage(to, " Qr ✘")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    cl.sendMessage(to, "ReRead ✔")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    cl.sendMessage(to, "ReRead ✘")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "Read ✔")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "Read ✘")
                elif text.lower() == 'qrjoin on':
                    settings["autoJoinTicket"] = True
                    cl.sendMessage(to, "Qr Join  ✔")
                elif text.lower() == 'qrjoin off':
                    settings["autoJoinTicket"] = False
                    cl.sendMessage(to, "Qr join ✘")
                elif text.lower() == 'tag on':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "Tag ✔")
                elif text.lower() == 'tag off':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "Tag ✘")
                elif text.lower() == 'ck on':
                    settings["checkSticker"] = True
                    cl.sendMessage(to, "Stickers ✔")
                elif text.lower() == 'ck off':
                    settings["checkSticker"] = False
                    cl.sendMessage(to, "Stickers ✘")
                elif text.lower() == 'kc on':
                    settings["kickContact"] = True
                    cl.sendMessage(to, "Kick Contact ✔")
                elif text.lower() == 'kc off':
                    settings["kickContact"] = False
                    cl.sendMessage(to, "Kick Contact ✘")
                elif text.lower() == 'ptt on':
                    settings["autoPtt"] = True
                    cl.sendMessage(to, "Ptt ✔")
                elif text.lower() == 'ptt off':
                    settings["autoPtt"] = False
                    cl.sendMessage(to, "ptt ✘")
                elif text.lower() == 'me':
                    sendMessageWithMention(to, sender)
                    cl.sendContact(to, sender)
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                elif text.lower() == 'myname':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[Tamlpilan]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[Tampilan]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = cl.getContact(sender)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'mycover':
                    me = cl.getContact(sender)
                    cover = cl.getProfileCoverURL(sender)
                    cl.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("contact "):
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
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "Id Sys："
                        for ls in lists:
                            ret_ += "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("name "):
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
                            cl.sendMessage(msg.to, "[ Nama ]\n" + contact.displayName)
                elif msg.text.lower().startswith("bio "):
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
                            cl.sendMessage(msg.to, "[ Nama ]\n" + contact.statusMessage)
                elif msg.text.lower().startswith("picture "):
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
                elif msg.text.lower().startswith("mpicture "):
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
                            cl.sendVideoWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cover "):
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
                elif text.lower() == 'gowner':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif text.lower() == 'gid':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[ID : ]\n" + gid.id)
                elif text.lower() == 'gurl':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ Url ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "Url Off，Djancoeg 👺👺".format(str(settings["keyCommand"])))
                elif text.lower() == 'ourl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.sendMessage(to, "Aktif")
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            cl.sendMessage(to, "Mati")
                elif text.lower() == 'curl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            cl.sendMessage(to, "Close ")
                        else:
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.sendMessage(to, "Open ")
                elif text.lower() == 'ginfo':
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak Dikenal"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Close"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    else:
                        gQr = "Open"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "《👺Araragi Kanega 👑 Ay 👺 》"
                    ret_ += "\nNama : {}".format(str(group.name))
                    ret_ += "\nＩＤ : {}".format(group.id)
                    ret_ += "\n Creator: {}".format(str(gCreator))
                    ret_ += "\nMembers : {}".format(str(len(group.members)))
                    ret_ += "\nPending : {}".format(gPending)
                    ret_ += "\nQr : {}".format(gQr)
                    ret_ += "\nTickter : {}".format(gTicket)
                    ret_ += "\n[ 👺Araragi Kanega 👑 Ay 👺 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'gb':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "[Daftar Anggota ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n[Total： {} ]".format(str(len(group.members)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'lg':
                        groups = cl.groups
                        ret_ = "[Daftar Group]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[Sebanyak {} Group]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'tagall':
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
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "Sebanyak {} Anggota".format(str(len(nama))))
                elif msg.text in ["SR","Setread"]:
                    cl.sendMessage(msg.to, "Read ✔")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print ("Setting Lurking")
                elif msg.text in ["DR","Delread"]:
                    cl.sendMessage(to, "Del Read ✘")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                elif msg.text in ["LR","Lookread"]:
                    if msg.to in wait2['readPoint']:
                        print ("Read")
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "[Urutan]:%s\n\n[Read]:\n%s\nWaktu:[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "Belom Di set Weduss 👺👺")
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"[berguna ？]\n%s\n[Silahkan Di lakukan~]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            print ["Ingat Pesan"]
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 26:
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
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == False:
                                    contact = cl.getContact(sender)
                                    cl.sendMessage(to, "Kebanyakan Tag Lu weduzh.  Perlu apa??  Lu kurbel??  Genit amat 😡 ")
                                    sendMessageWithMention(to, contact.mid)
                                break
        if op.type == 55:
            print ("[ 55 ] NOTICED")
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
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[★]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[★]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
