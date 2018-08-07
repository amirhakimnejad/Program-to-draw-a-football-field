# Program-to-draw-a-football-field
A python program that accepts field width and height, penalty area length, penalty area width, penalty cross distance, center circle diameter as input and draws the field automatically.

The reason that the program gets these inputs is the differences between different football fields's dimensions ratio.
For the purpose of this program that is related to my duty in @mrlspl as a localizer guy(if such thing exists :D), the default inputs are the dimensions of Robocup Standard Platform League's field (you can see the dimensions in SPL rule's book, I did put a screenshut of it) but you can put any other logical dimensions.


![Alt text](readmePics/SPLField.jpg?raw=true "SPL Field")

 Here is the visual Output

![Alt text](readmePics/beautifiedField.jpg?raw=true "Beautified Field")

The real output that i'm gonna use for my work is this.
![Alt text](readmePics/realField.jpg?raw=true "Real Field")

'W's are white and 'B's are black.
That's because i want to give it to my lost robot and localize it using different bayesian methods like 
[this repo](https://github.com/amirhakimnejad/Histogram-filter-for-robot-localization) of mine.


And to have a little bit of fun let's add a little color to our field. You can change prints in line 54, 56 and 61 and add a few background color to them like this:
```Python
if isEdge(i, j, B, A) or isMidLine(j, A) or isLeftPenaltyBox(i, j, B, E, F) or isRightPenaltyBox(i, j, A, B, E, F) or isPenaltySpot(i, j, A, B, G) or isCircle(i, j, A, B, H) or isCenterSpot(i, j, A, B):
    print ('\033[107m  ', end='')
else:
    print ('\033[42m  ', end='')

for i in range(B):
for j in range(A):
    draw(i, j, A, B, E, F, G, H)
print ('\033[0m\n', end='')
```
![Alt text](readmePics/graphicalField.png?raw=true "Graphical Field")

Feel free to ask questions or anything else.
