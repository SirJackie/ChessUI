import json
from JSock import JSock

jsock = JSock()
jsock.Connect("127.0.0.1", 16520)

jsock.SendStr("CloseServer")

# jsock.SendStr("SetState")
# jsock.SendStr(json.dumps(
#     [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ))

# jsock.SendStr("GetAction")
# print(jsock.RecvStr())
