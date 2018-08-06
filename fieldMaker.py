'''
    File name: fieldMaker.py
    Author: Amirhossein Hakimnejad
    Date created: August 6, 2018
    Date last modified: August 6, 2018
    Python Version: 3.x
'''

# Field length
A = 90
# Field width
B = 60
# Penalty area length
E = 6
# Penalty area width
F = 22
# Penalty cross distance
G = 13
# Center circle diameter
H = 15

def draw(i, j, A, B, E, F, G, H):

    def isEdge(i, j, B, A):
        return i == 0 or i == B - 1 or j == 0 or j == A - 1

    def isMidLine(j, A):
        return j == int(round(A / 2))

    def isLeftPenaltyBox(i, j, B, E, F):
        lefBoxVerticLine = j == E - 1 and i > ((B - F) / 2)  and i < (B - F) / 2 + F - 1
        lefBoxHorizLine =  j < E and (i == int(round((B - F) / 2)) or i == int(round((B - F) / 2 + F) - 1))
        return lefBoxVerticLine or lefBoxHorizLine

    def isRightPenaltyBox(i, j, A, B, E, F):
        rightBoxVerticLine = j == A - E and i > (B - F) / 2 and i < (B - F) / 2 + F - 1
        rightBoxHorizLine = j >= A - E and (i == int(round((B - F) / 2)) or i == int(round((B - F) / 2 + F - 1)))
        return rightBoxVerticLine or rightBoxHorizLine

    def isPenaltySpot(i, j, A, B, G):
        leftPenaltySpot = j == G - 1 and i == int(round(B / 2 - 1))
        rightPenaltySpot = j == A - G and i == int(round(B / 2 - 1))
        return leftPenaltySpot or rightPenaltySpot

    def isCircle(i, j, A, B, H):
        mid = [A / 2, B / 2 - 1]
        return int(round(H/2)) == int(round(((j - mid[0])**2 + (i - mid[1])**2)**0.5))

    def isCenterSpot(i, j, A, B):
        mid = [A / 2, B / 2 - 1]
        return i == mid[1] and (j == mid[0] - 1 or j == mid[0] + 1)

    if isEdge(i, j, B, A) or isMidLine(j, A) or isLeftPenaltyBox(i, j, B, E, F) or isRightPenaltyBox(i, j, A, B, E, F) or isPenaltySpot(i, j, A, B, G) or isCircle(i, j, A, B, H) or isCenterSpot(i, j, A, B):
        print ('W', end='')
    else:
        print ('B', end='')

for i in range(B):
    for j in range(A):
        draw(i, j, A, B, E, F, G, H)
    print ('\n', end='')
