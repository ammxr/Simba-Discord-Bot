tttWinningScenarios = [
  ['tile1', 'tile2', 'tile3'],
  ['tile4', 'tile5', 'tile6'],
  ['tile7', 'tile8', 'tile9'],
  
  ['tile1', 'tile4', 'tile7'],
  ['tile2', 'tile5', 'tile8'],
  ['tile3', 'tile6', 'tile9'],

  ['tile1', 'tile5', 'tile9'],
  ['tile3', 'tile5', 'tile7'],  
]

xTakenList = []
oTakenList = []

winner = False
tie = False
while winner==False and tie==False:
  x = input("What tile would you like to choose? ")
  xTakenList.append(x)
  if (len(xTakenList)+ (len(oTakenList)))==9:
    tie=True
  if tie==False:
    for i in range(len(tttWinningScenarios)):
      if (tttWinningScenarios[i][0] in xTakenList and tttWinningScenarios[i][1] in xTakenList and tttWinningScenarios[i][2] in xTakenList):
        print("Player 1 won")
        winner=True
      elif (tttWinningScenarios[i][0] in oTakenList and tttWinningScenarios[i][1] in oTakenList and tttWinningScenarios[i][2] in oTakenList):
        print("Player 2 won")