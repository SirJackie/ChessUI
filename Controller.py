from ChessUI.ChessUI import ChessUI

if __name__ == "__main__":

    iMax = 200
    jMax = 200

    state = [[0 for j in range(0, jMax)] for i in range(0, iMax)]
    ui = ChessUI(iMax, jMax)

    while True:
        i, j = ui.GetAction()
        state[i][j] += 1
        if state[i][j] == 5:
            state[i][j] = 0
        ui.SetState(state)
