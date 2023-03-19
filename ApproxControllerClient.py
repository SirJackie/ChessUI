import json
from JSock import JSock
import time

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
    return result


# jsock.SendStr("CloseServer")

# jsock.SendStr("SetState")
# jsock.SendStr(json.dumps(
#     [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ))

print(GetAction())
