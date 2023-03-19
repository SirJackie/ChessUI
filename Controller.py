from ChessUI.ChessUI import ChessUI

state = [[0 for j in range(0, 9)] for i in range(0, 9)]
ui = ChessUI(9, 9)

while True:
    i, j = ui.GetAction()
    state[i][j] += 1
    if state[i][j] == 5:
        state[i][j] = 0
    ui.SetState(state)
