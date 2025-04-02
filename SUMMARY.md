## Zrobione

- Newline jako EOL
- UNIT: Deklaracja i inicjalizacja kolorem i/lub patternem
- LAYER: Deklaracja i inicjalizacja przez UNIT \* NUMBER lub sumę takich wyrażeń
- SHAPE: Deklaracja i przypisanie łańcuchu LAYER
- Operator strzałki -- różne warianty:
  - <- -- standardowe łączenie 'pomiędzy'
  - <<- -- standardowe łączenie 'stack'
  - <-- -- standardowe łączenie 'stack'

## Do zrobienia

### Gramatyka

- Assignmenty: UNIT, LAYER ---> **(unit = \*blue\*, layer = unit \* 10)**
- Łączenie UNIT do istniejącego LAYER ---> **(layer += unit)**
- Łączenie LAYER do istniejącego SHAPE ---> **(shape <- layer --> shape)**
- Łączenie SHAPE do istniejącego MODEL ---> **(model <- shape --> model)**
- MODEL: deklaracja, assignment
- BEND
- Przesuwanie i rotowanie brył
- Dowolna kolejność w deklaracji UNIT ---> **(\*red\* \*striped\* == \*striped\* \*red\*)**
- Dowolna kolejność w deklaracji LAYER ---> **(r \* 10 == 10 \* r)**
- Rozszerzenie deklaracji i assignmentów o podtypy ---> **(UNIT u = \*red\*, LAYER l = u, SHAPE s = l)**
- Potencjalnie rozłączanie brył
- ...?

### Interpreter

- Assignmenty: UNIT, LAYER
- MODEL: deklaracja, assignment
- Łączenie UNIT do istniejącego LAYER
- Łączenie LAYER do istniejącego SHAPE
- Łączenie SHAPE do istniejącego MODEL
- BEND
- Przesuwanie i rotowanie brył
- Rozszerzenie deklaracji i assignmentów o podtypy
- If / Else
- For / While
- Funkcje
- Scopy
- ...?

### Wizualizacja

- Przesuwanie i rotowanie brył
- BEND
