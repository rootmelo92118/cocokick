# -*- coding: utf-8 -*-
from linepy import *
from time import sleep
import time
#cl = LINE()
cl = LINE('coco91062712@gmail.com','Apple234')
#cl = LINE('coco91062710@gmail.com','Apple234')
#cl = LINE('coco91062709@gmail.com','Apple234')
#cl = LINE('EtTT4PClrV6uYfvMRyF9.CYc5MdGPpQyxab794ESzAq.9NGvTozjm3ilraVRb8aBn9Htr3xpNN570KT8vHgxYgQ=')
cl.log("Auth Token : " + str(cl.authToken))
admin=['u28d781fa3ba9783fd5144390352b0c24','u993f768f416ab5abbb551153ff8ac38e','u17dd300568da75eef185af17397d175b','u9545690c9ce38c5c0dde40d6e8085ba1','u0f26401bbba4a99eff1412a1ac27b213','u00d0e3684d203a77d15f2d5489f9df41','u53166daf2aa18068111cc1d0cb1553d8','u4c10b3d699545a706d87eb8002ac49c5','u471d64ce29a82b8a0e5c0f4d5e1c6ef3','u67c43239c865dfce6addb41c6b3c0edd','u4923457f86af7435f3d8ad76a2a2dd52','u38f9f54eb878169aff22659cb165eb4e','u1626a6c4203e1b26a1e2d1a31fdc8a6d','u7320b99838293ea617001efde1eb1969','ub0e7b4197282f8db33c334f6656d7b90','u798fdd1bec45ae87ced03440310140dc','u0dff86c5c86343099b6f42c8c36baaaf','u43dcb9b0efb47e4fa4b4da0bc468a043','u00d0e3684d203a77d15f2d5489f9df41','ua1eedada6ebaf44004caab3458da1026','u2b37602c4f9f8d54917de47b09749130']
tracer = OEPoll(cl)
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        if cl.profile.mid in op.param3:
            if op.param2 in admin:
                cl.log("[13] NOTIFIED_INVITE_INTO_GROUP")
                cl.acceptGroupInvitation(op.param1)
                cl.sendMessage(op.param1, "レム❄帝国主义の破壊")
                #cl.sendMessage(op.param1, "✿千本桜❀帝国の滅殺です(^^♪/レム❄帝国主义の破壊/末日に栄光あれ☆/天皇軍に栄光あれ/★天選に荣光あれ☆/꧁༻❦神一族に栄光あれฺฺ❦༺꧂/〘善席〙破壊降臨∆/❄バブル帝国が破壊する❄/‡夜杀团‡が降臨します...☆/九条騎士団∆...降臨☆/冥魔军に栄光あれ☆/邵家戦いチーム破壊は訪れま/送葬に栄光あれℜ/血盟に荣光あれ☆彡")
                group = cl.getGroup(op.param1)
                group.name = "レム❄帝国主义の破壊"
                cl.updateGroup(group)
                for g in group.members:
                    if g.mid in admin:
                        print('pass')
                    else:
                        cl.kickoutFromGroup(op.param1, [g.mid])
                        time.sleep(0.1)
    except Exception as e:
        cl.log("[訊息錯誤]" + str(e))
tracer.addOpInterrupt(13, NOTIFIED_INVITE_INTO_GROUP)
while True:
    tracer.trace()
