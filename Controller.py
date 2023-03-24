from ChessUI.ChessUI import ChessUI

if __name__ == "__main__":

    state = [[0 for j in range(0, 10)] for i in range(0, 5)]
    ui = ChessUI(5, 10)

    while True:
        i, j = ui.GetAction()
        state[i][j] += 1
        if state[i][j] == 5:
            state[i][j] = 0
        ui.SetState(state)
