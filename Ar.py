# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,atexit
from gtts import gTTS
from googletrans import Translator
#di larang untuk merubah bagian ini untuk menghargai saya yang membuat created : Araragi kanega
# thank for :
# Agy pascha (nvstarbot) 
# Hanavi koplaxs
# NadyaTjia
#dan teman teman lainya yang sudah membantu dan memberi saya sc segaligus saran
#gunakan bot ini dengan bijak.  Jangan berharap lebih, scrib ini masih mau di revisi dan belom sempurna
#jika memerlukan atau ada yang ingin di tanyakan hubungi ➡ id line : araragi.  (pakai titik)  ◀ 

botStart = time.time()
araragi = LINE('EtsPaEG8q1jtyQPHVsBe.NnWPYXrsfOYTRMjXCBEM7G.ew2jSbEMc29uB0HpYt9ZEQu0YgvhBmElWyodYWN6wa4=')
araragi.log("Auth Token : " + str(araragi.authToken))


oepoll = OEPoll(araragi)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
lineSettings = araragi.getSettings()
araragiProfile = araragi.getProfile()
araragiMID = araragi.profile.mid
myProfile["displayName"] = araragiProfile.displayName
myProfile["statusMessage"] = araragiProfile.statusMessage
myProfile["pictureStatus"] = araragiProfile.pictureStatus
admin=['ua5f2cbc325816777be5ef529eb920c50','u529ed08e968ba9d107784186eb66b76a',araragiMID]
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
    print ("[ Info ] Bot reset")
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
    araragi.log("[ Eror ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        araragi.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """╔════════════════
║ Araragi Kanega 👑 Ay 
║╔═══════════════
║╠⎆ ༼ Araragi Bot ༽
║╠═══════════════
║╠࿐【Helpkick/tag
║╠࿐【Self:rebot
║╠࿐【Runtime
║╠࿐【Speed
║╠࿐【Set
║╠࿐【About
║╠࿐【Creator
║╠═══════════════
║╠⎆ ༼ Araragi Setting ༽
║╠═══════════════
║╠࿐【Add 
║╠࿐【Join 
║╠࿐【Leave 
║╠࿐【Read 
║╠࿐【Inviteprotect 
║╠࿐【Reread 
║╠࿐【Qr 
║╠࿐【Qrjoin 
║╠࿐【Ck 
║╠࿐【Groupprotect 
║╠࿐【Kc 
║╠࿐【Ptt 
║╠࿐Tag 
║╠═══════════════
║╠⎆ ༼ Araragi  Self  ༽
║╠═══════════════
║╠࿐【Me
║╠࿐【MyMid
║╠࿐【MyName
║╠࿐【MyBio
║╠࿐【MyPicture
║╠࿐【MyCover
║╠࿐【Contact @
║╠࿐【Friendlist
║╠═══════════════
║╠⎆ ༼ Araragi Group ༽
║╠═══════════════
║╠࿐【Gowner
║╠࿐【Gurl
║╠࿐【O/Curl
║╠࿐【Lg
║╠࿐【Gb
║╠࿐【Ginfo
║╠࿐【Vk:mid
║╠࿐【Nk Name
║╠࿐【Kickall
║╠࿐【Uk mid
║╠࿐【NT Name
║╠࿐【Zk, Zt, Zm
║╠࿐【Cancel
║╠࿐【Gcancel
║╠࿐【Gn Name
║╠࿐【Gc @
║╠࿐【Inv mid
║╠࿐【Mb:mid
║╠࿐【Mub:mid
║╠࿐【Clear Ban
║╠࿐【Kill Ban
║╠࿐【Killbanall
║╠࿐【banlist
║╠࿐【Sc gid
║╠࿐【Mc mid
║╠═══════════════
║╠⎆ ༼ Araragi Khusus ༽
║╠═══════════════
║╠࿐【Tagall
║╠࿐【SR/DR
║╠࿐【LR
║╠࿐【F/Gbc
║╠࿐【/invitemeto:
║╠࿐【Op @
║╠࿐【Deop @
║╠࿐【mop:mid
║╠࿐【mdp:mid
║╠࿐【Opmid
║╠࿐【Oplist
║╚═══════════════
║ Araragi Kanega 👑 Ay 
╚════════════════
"""
    return helpMessage
def helpmessagetag():
    helpMessageTag ="""╔══════════════
║ Araragi Kanega 👑 Ay 
║╔═════════════
║╠࿐〘Help Tag
║╠࿐【Ri @
║╠࿐【Tk @
║╠࿐【Mk @
║╠࿐【Vk @
║╠࿐【Gc @
║╠࿐【Mid @
║╠࿐【Name @
║╠࿐【Bio @
║╠࿐【Picture @
║╠࿐【Cover @
║╠࿐【Ban @
║╠࿐【Unban @
║╚═════════════
║Araragi Kanega 👑 Ay 
╚══════════════
"""
    return helpMessageTag
def helpmessagekick():
    helpMessageKick ="""╔════════════
║   Araragi Kanega 👑 Ay 
║╔═══════════
║╠࿐〘Help Kick〙
║╠࿐【Ri @
║╠࿐【Tk @
║╠࿐【Mk @
║╠࿐【Vk @
║╠࿐【Vk:mid
║╠࿐【Nk Name
║╠࿐【Uk mid
║╠࿐【Kill ban
║╠࿐【Zk
║════════════
║Araragi Kanega 👑 Ay 
╚════════════
"""
    return helpMessageKick
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = araragi.getContact(op.param1)
            print ("[ 5 ] Notice Add Contact : " + contact.displayName)
            if settings["autoAdd"] == True:
                araragi.findAndAddContactsByMid(op.param1)
                araragi.sendMessage(op.param1, "Terimakasih Telah Invite 👌😳".format(str(contact.displayName)))
                araragi.sendMessage(op.param1, "Jangan Nakalin dedek,  Achu Masih polos kakak 😳^^")
        if op.type == 11:
            group = araragi.getGroup(op.param1)
            contact = araragi.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    gs = araragi.getGroup(op.param1)
                    gs.preventJoinByTicket = True
                    araragi.updateGroup(gs)
                    invsend = 0
                    araragi.sendMessage(op.param1,araragi.getContact(op.param2).displayName + "Heh kutil babi jangan buka qr ！")
                    araragi.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 13:
            contact1 = araragi.getContact(op.param2)
            contact2 = araragi.getContact(op.param3)
            group = araragi.getGroup(op.param1)
            if settings["inviteprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    araragi.cancelGroupInvitation(op.param1,[op.param3])
                    time.sleep(0.15)
                    araragi.kickoutFromGroup(op.param1,[op.param3])
                    time.sleep(0.15)
                    araragi.kickoutFromGroup(op.param1,[op.param2])
            if araragiMID in op.param3:
                if settings["autoJoin"] == True:
                    try:
                        arrData = ""
                        text = "%s "%('[on]')
                        arr = []
                        mention = "@x "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention + "\nAssalamualaikum.. "
                        araragi.acceptGroupInvitation(op.param1)
                        araragi.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        araragi.sendMessage(op.param1, "Created ：")
                        araragi.sendContact(op.param1, "u9cdc29cb1452168cadae627171b7a6ee")
                    except Exception as error:
                        print(error)
            if araragiMID in op.param3:
                if settings["autoPtt"] == True:
                    araragi.acceptGroupInvitation(op.param1)
                    araragi.sendMessage(op.param1, "SeeYou...")
                    araragi.leaveGroup(op.param1)
        if op.type == 15:
            contact1 = araragi.getContact(op.param2)
            group = araragi.getGroup(op.param1)
            if settings["seeLeave"] == True:
                try:
                    arrData = ""
                    text = "%s "%('[Hallo.. ]')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "Good Bye Kakak Semoga Amal ibadah mu cukup 😳{} ！".format(str(group.name))
                    araragi.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 17:
            contact1 = araragi.getContact(op.param2)
            group = araragi.getGroup(op.param1)
            if settings["seeJoin"] == True:
                try:
                    arrData = ""
                    text = "%s "%('Halo')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "Cek note ya kakak Baca Rules nya！".format(str(group.name))
                    araragi.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 19:
            contact1 = araragi.getContact(op.param2)
            group = araragi.getGroup(op.param1)
            contact2 = araragi.getContact(op.param3)
            print ("[19] Notice Kick Out From Group: " + str(group.name) + "\n" + op.param1 +"\nNama: " + contact1.displayName + "\nMid:" + contact1.mid + "\nNama: " + contact2.displayName + "\nMid:" + contact2.mid )
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        araragi.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
                        araragi.sendMessage(op.param1, "[Dangger] %s Kick %s"%(contact1.displayName,contact2.displayName))
                        araragi.sendMessage(op.param1, "Kick：")
                        sendMessageWithMention(op.param1, contact1.mid)
                        araragi.sendMessage(op.param1, " Kicker：")
                        sendMessageWithMention(op.param1, contact2.mid)
                    else:
                        araragi.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
            else:
                if settings["kickContact"] == True:
                    araragi.sendMessage(op.param1, "[Dangger] %s  Kick%s"%(contact1.displayName,contact2.displayName))
                    araragi.sendMessage(op.param1, " kick：")
                    sendMessageWithMention(op.param1, contact1.mid)
                    araragi.sendMessage(op.param1, "Kicker：")
                    sendMessageWithMention(op.param1, contact2.mid)
                else:
                    pass
        if op.type == 22:
            print ("[ 22 ] Notice Leave Group")
            if settings["autoLeave"] == True:
                araragi.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1] NOTICED File Konfigurasi ")
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != araragi.profile.mid:
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
                    ret_ = "[ Info ]"
                    ret_ += "\nID       : {}".format(stk_id)
                    ret_ += "\nID       : {}".format(pkg_id)
                    ret_ += "\nUrl     : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\nPicUrl：https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ += "\n[ By : Araragi Kanega 👑 Ay ]"
                    araragi.sendMessage(to, str(ret_))
                    araragi.sendImageWithURL(to, path)
            if msg.contentType == 13:
                if settings["contact"] == True:
                    #msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = araragi.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = araragi.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        araragi.sendMessage(msg.to,"[ Nama ]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[Check]:\n" + contact.statusMessage + "\n[ Url ]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[ Cover ]:\n" + str(cu))
                    else:
                        contact = araragi.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = araragi.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        araragi.sendMessage(msg.to,"[ Nama ]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[ Check ]:\n" + contact.statusMessage + "\n[ Url ]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[ Cover ]:\n" + str(cu))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    try:
                        msg.contentType = 0
                        f_mid = msg.contentMetadata["postEndUrl"].split("userMid=")
                        s_mid = f_mid[1].split("&")
                        mid = s_mid[0]
                        try:
                            arrData = ""
                            text = "%s\n%s\n"%("---[Post Share ]---","[ Created ]:")
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':mid}
                            arr.append(arrData)
                            text += mention + "\n[ Keterangan ]:\n" + msg.contentMetadata["text"] + "\n(by : AraragiKanega👑Ay )" + "\n[ Url ]:\n" + msg.contentMetadata["postEndUrl"]
                            araragi.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    except:
                        ret_ = "---[Artikel]---\n[Keterangan]:\n" + msg.contentMetadata["text"] + "\n(by : AraragiKanega👑Ay )"
                        ret_ += "\n[]:\n" + msg.contentMetadata["postEndUrl"]
                        araragi.sendMessage(msg.to, str(ret_))
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in admin:
                if msg.text in ["Helpe"]:
                    helpMessage = helpmessage()
                    araragi.sendMessage(to, str(helpMessage))
                elif text.lower() == 'helptag':
                    helpMessageTag = helpmessagetag()
                    araragi.sendMessage(to, str(helpMessageTag))
                elif text.lower() == 'helpkick':
                    helpMessageKick = helpmessagekick()
                    araragi.sendMessage(to, str(helpMessageKick))
                elif text.lower() == 'unsend me':
                    araragi.unsendMessage(msg_id)
                elif text.lower() == 'creator':
                    araragi.sendMessage(to, "My Creator:")
                    araragi.sendContact(to, "u9cdc29cb1452168cadae627171b7a6ee")
                elif "Fbc:" in msg.text:
                    bctxt = text.replace("Fbc:","")
                    t = araragi.getAllContactIds()
                    for manusia in t:
                        araragi.sendMessage(manusia,(bctxt))
                elif "Gbc:" in msg.text:
                    bctxt = text.replace("Gbc:","")
                    n = araragi.getGroupIdsJoined()
                    for manusia in n:
                        araragi.sendMessage(manusia,(bctxt))
                elif "Ri " in msg.text:
                    Ri0 = text.replace("Ri ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = araragi.getGroup(msg.to)
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
                                    araragi.kickoutFromGroup(to,[target])
                                    araragi.findAndAddContactsByMid(target)
                                    araragi.inviteIntoGroup(to,[target])
                                except:
                                    pass
                elif "Ri:" in msg.text:  # Jangan Sampe LUPA TAG TARGET.  Jika Lupa Akan Berubah Menjadi kick all 😂
                    midd = text.replace("Ri:","")
                    araragi.kickoutFromGroup(to,[midd])
                    araragi.findAndAddContactsByMid(midd) #kick target dan add
                elif "Uk " in msg.text:
                    midd = text.replace("Uk ","")
                    araragi.kickoutFromGroup(to,[midd])
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
                                araragi.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif "Mk " in msg.text:
                    Mk0 = text.replace("Mk ","")
                    Mk1 = Mk0.rstrip()
                    Mk2 = Mk1.replace("@","")
                    Mk3 = Mk2.rstrip()
                    _name = Mk3
                    gs = araragi.getGroup(to)
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
                                    araragi.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Nk " in msg.text:
                    _name = text.replace("Nk ","")
                    gs = araragi.getGroup(to)
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
                                    araragi.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Kickall" in msg.text:
                    if settings["kickmeber"] == True:
                        if msg.toType == 2:
                            _name = msg.text.replace("Kickall","")
                            gs = araragi.getGroup(to)
                            araragi.sendMessage(to, "Terdjang BosQ Jangan Benci Jangan baper yayayayaya 😳☆")
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
                                            araragi.kickoutFromGroup(to, [target])
                                        except:
                                            pass
                elif "Zk" in msg.text:
                    gs = araragi.getGroup(to)
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
                                    araragi.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Vk:" in text: # Untuk Menghikangkan Jejak dari target
                    midd = msg.text.replace("Vk:","")
                    araragi.kickoutFromGroup(msg.to,[midd])
                    araragi.findAndAddContactsByMid(midd)
                    araragi.inviteIntoGroup(msg.to,[midd])
                    araragi.cancelGroupInvitation(msg.to,[midd])
                elif "Vk " in msg.text:
                        vkick0 = msg.text.replace("Vk ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = araragi.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    araragi.kickoutFromGroup(msg.to,[target])
                                    araragi.findAndAddContactsByMid(target)
                                    araragi.inviteIntoGroup(msg.to,[target])
                                    araragi.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass
                elif "NT " in msg.text:
                    _name = text.replace("NT ","")
                    gs = araragi.getGroup(to)
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
                        araragi.sendMessage(to,mc)
                elif text.lower() == 'zt':
                    gs = araragi.getGroup(to)
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
                    gs = araragi.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        mc = "Mid："
                        for mi_d in targets:
                            mc += "\n->" + mi_d
                        araragi.sendMessage(to,mc)
                elif "Mc " in msg.text:
                    mmid = msg.text.replace("Mc ","")
                    araragi.sendContact(to, mmid)
                elif "Sc " in msg.text:
                    ggid = msg.text.replace("Sc ","")
                    group = araragi.getGroup(ggid)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak di kenal "
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Open "
                        gTicket = "https://line.me/R/ti/g/{}".format(str(araragi.reissueGroupTicket(group.id)))
                    else:
                        gQr = "Close" 
                        gTicket = "https://line.me/R/ti/g/{}".format(str(araragi.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "[Information ]"
                    ret_ += "\nNama        : {}".format(str(group.name))
                    ret_ += "\nＩＤ           : {}".format(group.id)
                    ret_ += "\nCreator    : {}".format(str(gCreator))
                    ret_ += "\nMember   : {}".format(str(len(group.members)))
                    ret_ += "\nPending    : {}".format(gPending)
                    ret_ += "\nQr               : {}".format(gQr)
                    ret_ += "\nUrl              : {}".format(gTicket)
                    ret_ += "\n[End Information ]"
                    araragi.sendMessage(to, str(ret_))
                    araragi.sendImageWithURL(to, path)
                elif msg.text in ["c","C","cancel","Cancel"]:
                  if msg.toType == 2:
                    X = araragi.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = araragi.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            araragi.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        araragi.sendMessage(to, "Batal\nBatal Time : %sSecond" % (elapsed_time))
                        araragi.sendMessage(to, "Suksez:" + sinvitee)
                    else:
                        araragi.sendMessage(to, " Tidak Ada pendingan sayangku 😂😳！！")
                elif text.lower() == 'gcancel':
                    gid = araragi.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        araragi.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    araragi.sendMessage(to, "Semua Undangan di batalkan ")
                    araragi.sendMessage(to, "Pembatalan: %s Seconds" % (elapsed_time))
                elif "Gn " in msg.text:
                    if msg.toType == 2:
                        X = araragi.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        araragi.updateGroup(X)
                    else:
                        araragi.sendMessage(msg.to,"Hanya di group")
                elif text.lower().startswith('op '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.append(str(inkey))
                        araragi.sendMessage(to, " Di Tambah kan ( ➕ ) ！")
                elif text.lower().startswith('deop '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.remove(str(inkey))
                        araragi.sendMessage(to, " Telah Di Hapus ( ➖ ) ！")
                elif text.lower().startswith('mop:'):
                        midd = msg.text.replace("mop:","")
                        admin.append(str(midd))
                        araragi.sendMessage(to, "Di Tambah kan ( ➕ ) ！") 
                        backupData()
                elif text.lower().startswith('mdp:'):
                        midd = msg.text.replace("mdp:","")
                        admin.remove(str(midd))
                        araragi.sendMessage(to, "Telah Di Hapus ( ➖ )！") 
                        backupData()
                elif text.lower() == 'opmid':
                    if admin == []:
                        araragi.sendMessage(to, " Di Tambah kan ( ➕ )  ")
                    else:
                        mc = " Daftar Izin ："
                        for mi_d in admin:
                            mc += "\n-> " + mi_d
                        araragi.sendMessage(to, mc)
                elif text.lower() == 'oplist':
                    if admin == []:
                        araragi.sendMessage(to, "")
                    else:
                        mc = " Daftar ："
                        for mi_d in admin:
                            mc += "\n◉ " + araragi.getContact(mi_d).displayName
                        araragi.sendMessage(to, mc)
                elif "Gc" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        u = key["MENTIONEES"][0]["M"]
                        contact = araragi.getContact(u)
                        cu = araragi.getProfileCoverURL(mid=u)
                        try:
                            araragi.sendMessage(msg.to,"Nama:\n" + contact.displayName + "\n\nMid:\n" + contact.mid + "\n\nStatus:\n" + contact.statusMessage + "\n\nUrl :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nSampul :\n" + str(cu))
                        except:
                            araragi.sendMessage(msg.to,"Nama:\n" + contact.displayName + "\n\nMid:\n" + contact.mid + "\n\nStatus:\n" + contact.statusMessage + "\n\nSampul:\n" + str(cu))
                elif "Inv " in msg.text:
                    midd = msg.text.replace("Inv ","")
                    araragi.findAndAddContactsByMid(midd)
                    araragi.inviteIntoGroup(msg.to,[midd])
                elif "Ban" in msg.text:
                    if msg.toType == 2:
                        print ("[Ban] Sukses ")
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
                                    araragi.sendMessage(to, "Di Tambah kan ( ➕ ) ")
                                except:
                                    pass
                elif "Unban" in msg.text:
                    if msg.toType == 2:
                        print ("[UnBan] Sukses")
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
                                    araragi.sendMessage(to, "Telah Di Hapus ( ➖ )")
                                except:
                                    pass
                elif "Mb:" in msg.text:
                    midd = msg.text.replace("Mb:","")
                    try:
                        settings["blacklist"][midd] = True
                        backupData()
                        araragi.sendMessage(to, "Blaclist")
                    except:
                        pass
                elif "Mub:" in msg.text:
                    midd = msg.text.replace("Mub:","")
                    try:
                        del settings["blacklist"][midd]
                        backupData()
                        araragi.sendMessage(to, "Blacklist")
                    except:
                        pass
                elif text.lower() == 'clear ban':
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                    araragi.sendMessage(to, "Telah Di Hapus ( ➖ )")
                elif text.lower() == 'banlist':
                    if settings["blacklist"] == {}:
                        araragi.sendMessage(to, "Tidak Ada")
                    else:
                        mc = "Blacklist："
                        for mi_d in settings["blacklist"]:
                            mc += "\n->" + araragi.getContact(mi_d).displayName
                        araragi.sendMessage(to, mc)
                elif text.lower() == 'banmid':
                    if settings["blacklist"] == {}:
                        araragi.sendMessage(to, "Berzih")
                    else:
                        mc = "Daftar Hitam："
                        for mi_d in settings["blacklist"]:
                            mc += "\n->" + mi_d
                        araragi.sendMessage(to, mc)
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = araragi.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            araragi.sendMessage(to, "Tidak Ada ")
                            return
                        for jj in matched_list:
                            araragi.kickoutFromGroup(to, [jj])
                            araragi.sendMessage(to, "Sukses")
                elif text.lower() == 'killbanall':
                    gid = araragi.getGroupIdsJoined()
                    group = araragi.getGroup(to)
                    gMembMids = [contact.mid for contact in group.members]
                    ban_list = []
                    for tag in settings["blacklist"]:
                        ban_list += filter(lambda str: str == tag, gMembMids)
                    if ban_list == []:
                        araragi.sendMessage(to, "Not found ")
                    else:
                        for i in gid:
                            for jj in ban_list:
                                araragi.kickoutFromGroup(i, [jj])
                            araragi.sendMessage(i, "AllCleanGroup！")
                elif "/invitemeto:" in msg.text:
                    gid = msg.text.replace("/invitemeto:","")
                    if gid == "":
                        araragi.sendMessage(to, "ID")
                    else:
                        try:
                            araragi.findAndAddContactsByMid(msg._from)
                            araragi.inviteIntoGroup(gid,[msg._from])
                        except:
                            araragi.sendMessage(to, "Nkt found ")
                elif msg.text in ["Friendlist"]:
                    anl = araragi.getAllContactIds()
                    ap = ""
                    for q in anl:
                        ap += "• "+araragi.getContact(q).displayName + "\n"
                    araragi.sendMessage(msg.to,"「 Daftar 」\n"+ap+"Numb : "+str(len(anl)))
                elif text.lower() == 'sp':
                    start = time.time()
                    araragi.sendMessage(to, "Progress.... ")
                    elapsed_time = (time.time() - start)/100
                    araragi.sendMessage(to,format(str(elapsed_time)) + " Second")
                elif text.lower() == 'speed':
                    start = time.time()
                    araragi.sendMessage(to, "Progress... ")
                    elapsed_time = (time.time() - start)/100
                    araragi.sendMessage(to,format(str(elapsed_time)) + " Second")
                elif text.lower() == '!speed':
                    start = time.time()
                    araragi.sendMessage(to, "Progress... ")
                    elapsed_time = (time.time() - start)/100
                    araragi.sendMessage(to,format(str(elapsed_time)) + " Second")
                elif text.lower() == 'self:rebot':
                    araragi.sendMessage(to, "Prosess... ")
                    time.sleep(5)
                    araragi.sendMessage(to, "Berhasil.... ！")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    araragi.sendMessage(to, "Ngesot Selama {}".format(str(runtime)))                    
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u9cdc29cb1452168cadae627171b7a6ee"
                        creator = araragi.getContact(owner)
                        contact = araragi.getContact(araragiMID)
                        grouplist = araragi.getGroupIdsJoined()
                        contactlist = araragi.getAllContactIds()
                        blockedlist = araragi.getBlockedContactIds()
                        ret_ = " Araragi Kanega 👑 Ay "
                        ret_ += "\nNama            : {}".format(contact.displayName)
                        ret_ += "\nGc                  : {}".format(str(len(grouplist)))
                        ret_ += "\nCont               : {}".format(str(len(contactlist)))
                        ret_ += "\nBlock             : {}".format(str(len(blockedlist)))
                        ret_ += "\n ➡ "
                        ret_ += "\nTentang        : Araragi Bot"
                        ret_ += "\nFormat          : {}".format(creator.displayName)
                        ret_ += "\n Araragi Kanega 👑 Ay "
                        araragi.sendMessage(to, str(ret_))
                    except Exception as e:
                        araragi.sendMessage(msg.to, str(e))
                elif text.lower() == 'set':
                    try:
                        ret_ = "[ Status ]"
                        if settings["autoAdd"] == True: ret_ += "\nAuto Add ✔"
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
                        araragi.sendMessage(to, str(ret_))
                    except Exception as e:
                        araragi.sendMessage(msg.to, str(e))
                elif text.lower() == 'add on':
                    settings["autoAdd"] = True
                    araragi.sendMessage(to, "Auto Add ✔")
                elif text.lower() == 'add off':
                    settings["autoAdd"] = False
                    araragi.sendMessage(to, "Auto Add ✘")
                elif text.lower() == 'join on':
                    settings["autoJoin"] = True
                    araragi.sendMessage(to, "Join ✔")
                elif text.lower() == 'join off':
                    settings["autoJoin"] = False
                    araragi.sendMessage(to, "Join ✘")
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    araragi.sendMessage(to, "Leave ✔")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    araragi.sendMessage(to, "Leave ✘")
                elif text.lower() == 'contact on':
                    settings["contact"] = True
                    araragi.sendMessage(to, "Contact ✔")
                elif text.lower() == 'contact off':
                    settings["contact"] = False
                    araragi.sendMessage(to, "Contact ✘")
                elif text.lower() == 'groupprotect on':
                    settings["protect"] = True
                    araragi.sendMessage(to, "Protect ✔")
                elif text.lower() == 'groupprotect off':
                    settings["protect"] = False
                    araragi.sendMessage(to, "Protect ✘")
                elif text.lower() == 'inviteprotect on':
                    settings["inviteprotect"] = True
                    araragi.sendMessage(to, "Invit Pro ✔")
                elif text.lower() == 'inviteprotect off':
                    settings["inviteprotect"] = False
                    araragi.sendMessage(to, "Invit Pro ✘")
                elif text.lower() == 'qr on':
                    settings["qrprotect"] = True
                    araragi.sendMessage(to, "Qr ✔")
                elif text.lower() == 'qr off':
                    settings["qrprotect"] = False
                    araragi.sendMessage(to, " Qr ✘")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    araragi.sendMessage(to, "ReRead ✔")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    araragi.sendMessage(to, "ReRead ✘")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    araragi.sendMessage(to, "Read ✔")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    araragi.sendMessage(to, "Read ✘")
                elif text.lower() == 'qrjoin on':
                    settings["autoJoinTicket"] = True
                    araragi.sendMessage(to, "Qr Join  ✔")
                elif text.lower() == 'qrjoin off':
                    settings["autoJoinTicket"] = False
                    araragi.sendMessage(to, "Qr join ✘")
                elif text.lower() == 'tag on':
                    settings["detectMention"] = False
                    araragi.sendMessage(to, "Tag ✔")
                elif text.lower() == 'tag off':
                    settings["detectMention"] = True
                    araragi.sendMessage(to, "Tag ✘")
                elif text.lower() == 'ck on':
                    settings["checkSticker"] = True
                    araragi.sendMessage(to, "Stickers ✔")
                elif text.lower() == 'ck off':
                    settings["checkSticker"] = False
                    araragi.sendMessage(to, "Stickers ✘")
                elif text.lower() == 'kc on':
                    settings["kickContact"] = True
                    araragi.sendMessage(to, "Kick Contact ✔")
                elif text.lower() == 'kc off':
                    settings["kickContact"] = False
                    araragi.sendMessage(to, "Kick Contact ✘")
                elif text.lower() == 'ptt on':
                    settings["autoPtt"] = True
                    araragi.sendMessage(to, "Ptt ✔")
                elif text.lower() == 'ptt off':
                    settings["autoPtt"] = False
                    araragi.sendMessage(to, "ptt ✘")
                elif text.lower() == 'me':
                    sendMessageWithMention(to, sender)
                    araragi.sendContact(to, sender)
                elif text.lower() == 'mymid':
                    araragi.sendMessage(msg.to,"[MID]\n" +  sender)
                elif text.lower() == 'myname':
                    me = araragi.getContact(sender)
                    araragi.sendMessage(msg.to,"[Tampilan]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = araragi.getContact(sender)
                    araragi.sendMessage(msg.to,"[Tampilan]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = araragi.getContact(sender)
                    araragi.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'mycover':
                    me = araragi.getContact(sender)
                    cover = araragi.getProfileCoverURL(sender)
                    araragi.sendImageWithURL(msg.to, cover)
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
                            contact = araragi.getContact(ls)
                            mi_d = contact.mid
                            araragi.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "îdsys："
                        for ls in lists:
                            ret_ += "\n" + ls
                        araragi.sendMessage(msg.to, str(ret_))
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
                            contact = araragi.getContact(ls)
                            araragi.sendMessage(msg.to, "[ nama ]\n" + contact.displayName)
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
                            contact = araragi.getContact(ls)
                            araragi.sendMessage(msg.to, "[ nama ]\n" + contact.statusMessage)
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
                            path = "http://dl.profile.line-cdn.net/" + araragi.getContact(ls).pictureStatus
                            araragi.sendImageWithURL(msg.to, str(path))
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
                            path = "http://dl.profile.line-cdn.net/" + araragi.getContact(ls).pictureStatus
                            araragi.sendVideoWithURL(msg.to, str(path))
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
                                path = araragi.getProfileCoverURL(ls)
                                araragi.sendImageWithURL(msg.to, str(path))
                elif text.lower() == 'gowner':
                    group = araragi.getGroup(to)
                    GS = group.creator.mid
                    araragi.sendContact(to, GS)
                elif text.lower() == 'gid':
                    gid = araragi.getGroup(to)
                    araragi.sendMessage(to, "[ID : ]\n" + gid.id)
                elif text.lower() == 'gurl':
                    if msg.toType == 2:
                        group = araragi.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = araragi.reissueGroupTicket(to)
                            araragi.sendMessage(to, "[ Url ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            araragi.sendMessage(to, "Url Off，Djancoeg 👺👺".format(str(settings["keyCommand"])))
                elif text.lower() == 'ourl':
                    if msg.toType == 2:
                        G = araragi.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            araragi.sendMessage(to, "Aktif")
                        else:
                            G.preventedJoinByTicket = False
                            araragi.updateGroup(G)
                            araragi.sendMessage(to, "Mati")
                elif text.lower() == 'curl':
                    if msg.toType == 2:
                        G = araragi.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            araragi.sendMessage(to, "Close ")
                        else:
                            G.preventedJoinByTicket = True
                            araragi.updateGroup(G)
                            araragi.sendMessage(to, "Open ")
                elif text.lower() == 'ginfo':
                    group = araragi.getGroup(to)
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
                        gTicket = "https://line.me/R/ti/g/{}".format(str(araragi.reissueGroupTicket(group.id)))
                    else:
                        gQr = "Open"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(araragi.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "《👺Araragi Kanega 👑 Ay 👺 》"
                    ret_ += "\nNama             : {}".format(str(group.name))
                    ret_ += "\nＩＤ                : {}".format(group.id)
                    ret_ += "\n Creator        : {}".format(str(gCreator))
                    ret_ += "\nMembers      : {}".format(str(len(group.members)))
                    ret_ += "\nPending        : {}".format(gPending)
                    ret_ += "\nQr                   : {}".format(gQr)
                    ret_ += "\nTickter           : {}".format(gTicket)
                    ret_ += "\n[ 👺Araragi Kanega 👑 Ay 👺 ]"
                    araragi.sendMessage(to, str(ret_))
                    araragi.sendImageWithURL(to, path)
                elif text.lower() == 'gb':
                    if msg.toType == 2:
                        group = araragi.getGroup(to)
                        ret_ = "[Daftar Anggota ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n[Total： {} ]".format(str(len(group.members)))
                        araragi.sendMessage(to, str(ret_))
                elif text.lower() == 'lg':
                        groups = araragi.groups
                        ret_ = "[Daftar Group]"
                        no = 0 + 1
                        for gid in groups:
                            group = araragi.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[Sebanyak {} Group]".format(str(len(groups)))
                        araragi.sendMessage(to, str(ret_))
                elif text.lower() == 'tagall':
                    group = araragi.getGroup(msg.to)
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
                        araragi.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        araragi.sendMessage(to, "Sebanyak {} Anggota".format(str(len(nama))))
                elif msg.text in ["SR","Setread"]:
                    araragi.sendMessage(msg.to, "Read ✔")
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
                    araragi.sendMessage(to, "Del Read ✘")
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
                        araragi.sendMessage(msg.to, "[Urutan]:%s\n\n[Read]:\n%s\nWaktu:[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        araragi.sendMessage(msg.to, "Belom Di set Weduss 👺👺")
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        araragi.log("[%s]"%(msg._from)+msg.text)
                    else:
                        araragi.log("[%s]"%(msg.to)+msg.text)
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
                            araragi.sendMessage(at,"[Pelaku nya nih ]\n%s\n[Unsend Messages ]\n%s"%(araragi.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
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
                if sender != araragi.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    araragi.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in araragiMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if araragiMID in mention["M"]:
                                if settings["detectMention"] == False:
                                    contact = araragi.getContact(sender)
                                    araragi.sendMessage(to, "Ihh kakak Genit Colek Colek adek Muluk.  Pc aja kak biar mesra 😘 😳 ") 
                                pass

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
                    Name = araragi.getContact(op.param2).displayName
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
        