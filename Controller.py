import os
import json
from ChessUI.JSock import JSock
import time

os.system("start .\\ChessUI\\Launcher1.vbs")
os.system("start .\\ChessUI\\Launcher2.vbs")

jsock = JSock()
jsock.Connect("127.0.0.1", 16520)


def GetAction():
    result = None
    while True:
        jsock.SendStr("GetAction")
        result = jsock.RecvStr()
        if result == "NoNewAction":
            time.sleep(0.01)
        else:
            break
    return json.loads(result)


def SetState(state):
    jsock.SendStr("SetState")
    jsock.SendStr(json.dumps(
        state
    ))


jsock.SendStr("SetSize")
jsock.SendStr(json.dumps(
    [9, 9]
))

state = [[0 for j in range(0, 9)] for i in range(0, 9)]

while True:
    action = GetAction()
    state[action[0]][action[1]] += 1
    if state[action[0]][action[1]] == 5:
        state[action[0]][action[1]] = 0
    SetState(state)
