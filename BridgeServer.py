from JSock import JSock
import _thread
import json
import time


state = None
hasNewState = False
action = None
hasNewAction = False

wannaClose = False
closeBridgeServer = False


def ControllerServer():
    global state, hasNewState, action, hasNewAction
    global closeBridgeServer, wannaClose

    jsock = JSock()
    jsock.StartServer(16520)

    while True:
        # noinspection PyBroadException
        try:
            while True:
                jsock.AcceptClient()

                while True:
                    msg = jsock.RecvStr()

                    if msg == "SetState":
                        state = json.loads(jsock.RecvStr())
                        hasNewState = True
                        print(state)

                    elif msg == "GetAction":
                        if hasNewAction:
                            jsock.SendStr(json.dumps(action))
                            hasNewAction = False
                        else:
                            jsock.SendStr("NoNewAction")

                    elif msg == "CloseServer":
                        jsock.Close()
                        raise SystemExit("Controller Client Closed Correctly")

        except SystemExit:
            # Exited Correctly, Close the Bridge Server
            print("Controller Client Closed Correctly, So the Bridge Server is Closing...")
            wannaClose = True
            print("Wanna Close")

        except BaseException:
            print("An Error Occurred in Controller Server")
            pass


def ControleeServer():
    global state, hasNewState, action, hasNewAction
    global closeBridgeServer, wannaClose

    jsock = JSock()
    jsock.StartServer(16521)

    while True:
        # noinspection PyBroadException
        try:
            while True:
                jsock.AcceptClient()

                # If the code runs till here ( AcceptClient() is a blocking function ),
                # The Tkinter Controlee Client may have been connected.

                while True:
                    msg = jsock.RecvStr()

                    if msg == "CloseOrNot":
                        if wannaClose is True:
                            jsock.SendStr("Yes")
                            closeBridgeServer = True
                        else:
                            jsock.SendStr("No")

                    elif msg == "GetState":
                        if hasNewState:
                            jsock.SendStr(json.dumps(state))
                            hasNewState = False
                        else:
                            jsock.SendStr("NoNewState")

                    elif msg == "SetAction":
                        action = json.loads(jsock.RecvStr())
                        hasNewAction = True
                        print(action)

        except BaseException:
            print("An Error Occurred in Controlee Server")
            pass


if __name__ == "__main__":

    # Start Server Threads
    _thread.start_new_thread(ControllerServer, ())
    _thread.start_new_thread(ControleeServer, ())

    # Main Loop
    while not closeBridgeServer:
        time.sleep(1)