# pathFinding-Algorithms
Efficiency of Uninformed and informed search algorithms for path findings.

A python implementation for solving the path finding problems using uninformed and informed search strategy BFS (BREADTH-FIRST SEARCH), DFS (DEPTH-FIRST SEARCH), DFID (DEPTH-FIRST-ITERATIVE-DEEPNING SEARCH) and Heuristic search A*. The Goal is to search empirically compare strategies space and time complexities.

## For each strategy program collects and outputs the following information.
- Sequence of moves corresponding to the solution.
-	Total no of nodes expanded.
-	Total no of nodes generated.
-	Expanded children nodes.
-	Open list and closed list of expanded nodes.
-	Length of solution path.

## Expected output:

### BFS:
Expanding Caen
Children are (Calais Paris Rennes)
New children are (Calais Paris Rennes)
Open list is (Calais Paris Rennes)
Closed list is (Caen)

Expanding Calais
Children are (Caen Nancy Paris)
New children are (Nancy)
Open list is (Paris Rennes Nancy)
Closed list is (Caen Calais)

Expanding Paris
Children are (Caen Calais Dijon Limoges Nancy Rennes)
New children are (Dijon Limoges)
Open list is (Rennes Nancy Dijon Limoges)
Closed list is (Caen Calais Paris)

Expanding Rennes
Children are (Brest Caen Nantes Paris)
New children are (Brest Nantes)
Open list is (Nancy Dijon Limoges Brest Nantes)
Closed list is (Caen Calais Paris Rennes)

Expanding Nancy
Children are (Calais Dijon Paris Strasbourg)
New children are (Strasbourg)
Open list is (Dijon Limoges Brest Nantes Strasbourg)
Closed list is (Caen Calais Paris Rennes Nancy)

Expanding Dijon
Children are (Lyon Nancy Paris Strasbourg)
New children are (Lyon)
Open list is (Limoges Brest Nantes Strasbourg Lyon)
Closed list is (Caen Calais Paris Rennes Nancy Dijon)

Expanding Limoges
Children are (Bordeaux Lyon Nantes Paris Toulouse)
New children are (Bordeaux Toulouse)
Open list is (Brest Nantes Strasbourg Lyon Bordeaux Toulouse)
Closed list is (Caen Calais Paris Rennes Nancy Dijon Limoges)

Expanding Brest
Children are (Rennes)
New children are Nil
Open list is (Nantes Strasbourg Lyon Bordeaux Toulouse)
Closed list is (Caen Calais Paris Rennes Nancy Dijon Limoges Brest)

Expanding Nantes
Children are (Bordeaux Limoges Rennes)
New children are Nil
Open list is (Strasbourg Lyon Bordeaux Toulouse)
Closed list is (Caen Calais Paris Rennes Nancy Dijon Limoges Brest Nantes)

Expanding Strasbourg
Children are (Dijon Nancy)
New children are Nil
Open list is (Lyon Bordeaux Toulouse)
Closed list is (Caen Calais Paris Rennes Nancy Dijon Limoges Brest Nantes Strasbourg)

Expanding Lyon

Breadth-first search solution: (Caen Paris Dijon Lyon) .
10 nodes expanded.

### DFS:
Expanding Caen
Children are (Calais Paris Rennes)
New children are (Calais Paris Rennes)
Open list is (Calais Paris Rennes)
Closed list is (Caen)

Expanding Calais
Children are (Caen Nancy Paris)
New children are (Nancy)
Open list is (Nancy Paris Rennes)
Closed list is (Caen Calais)

Expanding Nancy
Children are (Calais Dijon Paris Strasbourg)
New children are (Dijon Strasbourg)
Open list is (Dijon Strasbourg Paris Rennes)
Closed list is (Caen Calais Nancy)

Expanding Dijon
Children are (Lyon Nancy Paris Strasbourg)
New children are (Lyon)
Open list is (Lyon Strasbourg Paris Rennes)
Closed list is (Caen Calais Nancy Dijon)

Expanding Lyon

Depth-first search solution:
 (Caen Calais Nancy Dijon Lyon) .
4 nodes expanded.

### A* WITH H=0 :

Expanding Caen f= 0 , g= 0 , h= 0
Children are (Calais Paris Rennes)
Open list is ((Calais 120) (Rennes 176) (Paris 241))
Closed list is ((Caen 0))

Expanding Calais f= 120 , g= 120 , h= 0
Children are (Caen Nancy Paris)
Open list is ((Rennes 176) (Paris 241) (Nancy 654))
Closed list is ((Caen 0) (Calais 120))

Expanding Rennes f= 176 , g= 176 , h= 0
Children are (Brest Caen Nantes Paris)
Open list is ((Paris 241) (Nantes 283) (Brest 420) (Nancy 654))
Closed list is ((Caen 0) (Calais 120) (Rennes 176))

Expanding Paris f= 241 , g= 241 , h= 0
Children are (Caen Calais Dijon Limoges Nancy Rennes)
***Revaluing open node Nancy from 654 to 613
Open list is ((Nantes 283) (Brest 420) (Dijon 554) (Nancy 613) (Limoges 637))
Closed list is ((Caen 0) (Calais 120) (Rennes 176) (Paris 241))

Expanding Nantes f= 283 , g= 283 , h= 0
Children are (Bordeaux Limoges Rennes)
***Revaluing open node Limoges from 637 to 612
Open list is ((Brest 420) (Dijon 554) (Bordeaux 612) (Limoges 612) (Nancy 613))
Closed list is ((Caen 0) (Calais 120) (Rennes 176) (Paris 241) (Nantes 283))

Expanding Brest f= 420 , g= 420 , h= 0
Children are (Rennes)
Open list is ((Dijon 554) (Bordeaux 612) (Limoges 612) (Nancy 613))
Closed list is ((Caen 0) (Calais 120) (Rennes 176) (Paris 241) (Nantes 283) (Brest 420))

Expanding Dijon f= 554 , g= 554 , h= 0
Children are (Lyon Nancy Paris Strasbourg)
Open list is ((Bordeaux 612) (Limoges 612) (Nancy 613) (Lyon 746) (Strasbourg 889))
Closed list is ((Caen 0) (Calais 120) (Rennes 176) (Paris 241) (Nantes 283) (Brest 420) (Dijon 554))

Expanding Bordeaux f= 612 , g= 612 , h= 0
Children are (Limoges Nantes Toulouse)
Open list is ((Limoges 612) (Nancy 613) (Lyon 746) (Toulouse 865) (Strasbourg 889))
Closed list is ((Caen 0) (Calais 120) (Rennes 176) (Paris 241) (Nantes 283) (Brest 420) (Dijon 554) (Bordeaux 612))

Expanding Limoges f= 612 , g= 612 , h= 0
Children are (Bordeaux Lyon Nantes Paris Toulouse)
Open list is ((Nancy 613) (Lyon 746) (Toulouse 865) (Strasbourg 889))
Closed list is ((Caen 0) (Calais 120) (Rennes 176) (Paris 241) (Nantes 283) (Brest 420) (Dijon 554) (Bordeaux 612) (Limoges 612))

Expanding Nancy f= 613 , g= 613 , h= 0
Children are (Calais Dijon Paris Strasbourg)
***Revaluing open node Strasbourg from 889 to 758
Open list is ((Lyon 746) (Strasbourg 758) (Toulouse 865))
Closed list is ((Caen 0) (Calais 120) (Rennes 176) (Paris 241) (Nantes 283) (Brest 420) (Dijon 554) (Bordeaux 612) (Limoges 612) (Nancy 613))

Expanding Lyon f= 746 , g= 746 , h= 0

A-star-search solution with H=0 : (Caen Paris Dijon Lyon) .
Path-length: 746 .
10 nodes expanded.

### A* WITH H=EAST-WEST DISTANCE :
Expanding Caen f= 416 , g= 0 , h= 416
Children are (Calais Paris Rennes)
Open list is ((Calais 360) (Paris 441) (Rennes 696))
Closed list is ((Caen 416))

Expanding Calais f= 360 , g= 120 , h= 240
Children are (Caen Nancy Paris)
Open list is ((Paris 441) (Rennes 696) (Nancy 766))
Closed list is ((Caen 416) (Calais 360))

Expanding Paris f= 441 , g= 241 , h= 200
Children are (Caen Calais Dijon Limoges Nancy Rennes)
***Revaluing open node Nancy from 766 to 725
Open list is ((Dijon 578) (Rennes 696) (Nancy 725) (Limoges 925))
Closed list is ((Caen 416) (Calais 360) (Paris 441))

Expanding Dijon f= 578 , g= 554 , h= 24
Children are (Lyon Nancy Paris Strasbourg)
Open list is ((Rennes 696) (Nancy 725) (Lyon 746) (Limoges 925) (Strasbourg 1121))
Closed list is ((Caen 416) (Calais 360) (Paris 441) (Dijon 578))

Expanding Rennes f= 696 , g= 176 , h= 520
Children are (Brest Caen Nantes Paris)
Open list is ((Nancy 725) (Lyon 746) (Nantes 795) (Limoges 925) (Strasbourg 1121) (Brest 1164))
Closed list is ((Caen 416) (Calais 360) (Paris 441) (Dijon 578) (Rennes 696))

Expanding Nancy f= 725 , g= 613 , h= 112
Children are (Calais Dijon Paris Strasbourg)
***Revaluing open node Strasbourg from 1121 to 990
Open list is ((Lyon 746) (Nantes 795) (Limoges 925) (Strasbourg 990) (Brest 1164))
Closed list is ((Caen 416) (Calais 360) (Paris 441) (Dijon 578) (Rennes 696) (Nancy 725))

Expanding Lyon f= 746 , g= 746 , h= 0


A-star-search solution with H=EAST-WEST DISTANCE : (Caen Paris Dijon Lyon) .
Path-length: 746 .
6 nodes expanded.


### DFID:
DFID LEVEL 0 :

Expanding Caen
Depth has been reached
Open list is Nil
Closed list is ((Caen 0))


DFID LEVEL 1 :

Expanding Caen
Children are ((Calais 1) (Paris 1) (Rennes 1))
New or revalued children are ((Calais 1) (Paris 1) (Rennes 1))
Open list is ((Calais 1) (Paris 1) (Rennes 1))
Closed list is ((Caen 0))

Expanding Calais
Depth has been reached
Open list is ((Paris 1) (Rennes 1))
Closed list is ((Caen 0) (Calais 1))

Expanding Paris
Depth has been reached
Open list is ((Rennes 1))
Closed list is ((Caen 0) (Calais 1) (Paris 1))

Expanding Rennes
Depth has been reached
Open list is Nil
Closed list is ((Caen 0) (Calais 1) (Paris 1) (Rennes 1))


DFID LEVEL 2 :

Expanding Caen
Children are ((Calais 1) (Paris 1) (Rennes 1))
New or revalued children are ((Calais 1) (Paris 1) (Rennes 1))
Open list is ((Calais 1) (Paris 1) (Rennes 1))
Closed list is ((Caen 0))

Expanding Calais
Children are ((Caen 2) (Nancy 2) (Paris 2))
New or revalued children are ((Nancy 2))
Open list is ((Nancy 2) (Paris 1) (Rennes 1))
Closed list is ((Caen 0) (Calais 1))

Expanding Nancy
Depth has been reached
Open list is ((Paris 1) (Rennes 1))
Closed list is ((Caen 0) (Calais 1) (Nancy 2))

Expanding Paris
Children are ((Caen 2) (Calais 2) (Dijon 2) (Limoges 2) (Nancy 2) (Rennes 2))
New or revalued children are ((Dijon 2) (Limoges 2))
Open list is ((Dijon 2) (Limoges 2) (Rennes 1))
Closed list is ((Caen 0) (Calais 1) (Nancy 2) (Paris 1))

Expanding Dijon
Depth has been reached
Open list is ((Limoges 2) (Rennes 1))
Closed list is ((Caen 0) (Calais 1) (Nancy 2) (Paris 1) (Dijon 2))

Expanding Limoges
Depth has been reached
Open list is ((Rennes 1))
Closed list is ((Caen 0) (Calais 1) (Nancy 2) (Paris 1) (Dijon 2) (Limoges 2))

Expanding Rennes
Children are ((Brest 2) (Caen 2) (Nantes 2) (Paris 2))
New or revalued children are ((Brest 2) (Nantes 2))
Open list is ((Brest 2) (Nantes 2))
Closed list is ((Caen 0) (Calais 1) (Nancy 2) (Paris 1) (Dijon 2) (Limoges 2) (Rennes 1))

Expanding Brest
Depth has been reached
Open list is ((Nantes 2))
Closed list is ((Caen 0) (Calais 1) (Nancy 2) (Paris 1) (Dijon 2) (Limoges 2) (Rennes 1) (Brest 2))

Expanding Nantes
Depth has been reached
Open list is Nil
Closed list is ((Caen 0) (Calais 1) (Nancy 2) (Paris 1) (Dijon 2) (Limoges 2) (Rennes 1) (Brest 2) (Nantes 2))


DFID LEVEL 3 :

Expanding Caen
Children are ((Calais 1) (Paris 1) (Rennes 1))
New or revalued children are ((Calais 1) (Paris 1) (Rennes 1))
Open list is ((Calais 1) (Paris 1) (Rennes 1))
Closed list is ((Caen 0))

Expanding Calais
Children are ((Caen 2) (Nancy 2) (Paris 2))
New or revalued children are ((Nancy 2))
Open list is ((Nancy 2) (Paris 1) (Rennes 1))
Closed list is ((Caen 0) (Calais 1))

Expanding Nancy
Children are ((Calais 3) (Dijon 3) (Paris 3) (Strasbourg 3))
New or revalued children are ((Dijon 3) (Strasbourg 3))
Open list is ((Dijon 3) (Strasbourg 3) (Paris 1) (Rennes 1))
Closed list is ((Caen 0) (Calais 1) (Nancy 2))

Expanding Dijon
Depth has been reached
Open list is ((Strasbourg 3) (Paris 1) (Rennes 1))
Closed list is ((Caen 0) (Calais 1) (Nancy 2) (Dijon 3))

Expanding Strasbourg
Depth has been reached
Open list is ((Paris 1) (Rennes 1))
Closed list is ((Caen 0) (Calais 1) (Nancy 2) (Dijon 3) (Strasbourg 3))

Expanding Paris
Children are ((Caen 2) (Calais 2) (Dijon 2) (Limoges 2) (Nancy 2) (Rennes 2))
* Dropping ( Dijon 3 ) from closed list because new value is better
New or revalued children are ((Dijon 2) (Limoges 2))
Open list is ((Dijon 2) (Limoges 2) (Rennes 1))
Closed list is ((Caen 0) (Calais 1) (Nancy 2) (Strasbourg 3) (Paris 1))

Expanding Dijon
Children are ((Lyon 3) (Nancy 3) (Paris 3) (Strasbourg 3))
New or revalued children are ((Lyon 3))
Open list is ((Lyon 3) (Limoges 2) (Rennes 1))
Closed list is ((Caen 0) (Calais 1) (Nancy 2) (Strasbourg 3) (Paris 1) (Dijon 2))

Expanding Lyon


DFID solution:
 (Caen Paris Dijon Lyon) .
21 total nodes expanded.


 
