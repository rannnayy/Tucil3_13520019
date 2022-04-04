from library import *

###################### MAIN PROGRAM #############################
welcome()
dict = {}
tempMat = initiate()
tempEmptyTile = [-1, -1]
isSolvable, tableKurang, Sigma, tempEmptyTile[0], tempEmptyTile[1] = checkSolvable(tempMat)

dict[str(toArray(tempMat))] = 0

# conditions if solvable and not
if (isSolvable):
    printMatrix(tempMat)
    printTableKurang(tableKurang)
    print("Sigma Kurang(i) from 1 to 16 + X = " + str(Sigma))
    solve(tempMat, dict, tempEmptyTile)
else:
    print("The puzzle is not solvable")
    printTableKurang(tableKurang)
    print("Sigma Kurang(i) from 1 to 16 + X = " + str(Sigma))