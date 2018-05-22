# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
import time, datetime, random ,sys, re, string, os, json, codecs, timeit
cl = LINE()
cl.log("Auth Token : " + str(cl.authToken))
admin=['u28d781fa3ba9783fd5144390352b0c24','u17dd300568da75eef185af17397d175b','u9545690c9ce38c5c0dde40d6e8085ba1','u0f26401bbba4a99eff1412a1ac27b213','u00d0e3684d203a77d15f2d5489f9df41','u53166daf2aa18068111cc1d0cb1553d8','u4c10b3d699545a706d87eb8002ac49c5']
tracer = OEPoll(cl)
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        if cl.profile.mid in op.param3:
            if op.param2 in admin:
                print("[13] NOTIFIED_INVITE_INTO_GROUP")
                cl.acceptGroupInvitation(op.param1)
                cl.sendMessage(op.param1,"✿千本桜❀帝国の滅殺です(^^♪/レム❄帝国主义の破壊/末日に栄光あれ☆/天皇軍に栄光あれ/★天選に荣光あれ☆/꧁༻❦神一族に栄光あれฺฺ❦༺꧂/〘善席〙破壊降臨∆/❄バブル帝国が破壊する❄")
                group = cl.getGroup(op.param1)
                group.name = "レム❄帝国主义の破壊"
                cl.updateGroup(group)
                for g in group.members:
                    if g.mid in admin:
                        print('pass')
                    else:
                        cl.kickoutFromGroup(op.param1, [g.mid])
                        time.sleep(0.5)
    except Exception as e:
        cl.log("[訊息錯誤]" + str(e))
tracer.addOpInterrupt(13, NOTIFIED_INVITE_INTO_GROUP)
while True:
    tracer.trace()
