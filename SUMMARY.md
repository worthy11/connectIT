## Zrobione

- Newline jako EOL
- UNIT: Deklaracja i inicjalizacja kolorem i/lub patternem
- LAYER: Deklaracja i inicjalizacja przez UNIT \* NUMBER lub sumę takich wyrażeń
- SHAPE: Deklaracja i przypisanie łańcuchu LAYER
- Operator strzałki -- różne warianty:
  - <- -- standardowe łączenie 'pomiędzy'
  - <<- -- standardowe łączenie 'stack'
  - <-- -- standardowe łączenie 'stack'
- Assignmenty: UNIT, LAYER ---> **(unit = \*blue\*, layer = unit \* 10)**
- Dowolna kolejność w deklaracji UNIT ---> **(\*red\* \*striped\* == \*striped\* \*red\*)**
- Dowolna kolejność w deklaracji LAYER ---> **(r \* 10 == 10 \* r)**
- Rzutowanie typów

## Do zrobienia

### Gramatyka

- Weryfikacja IF / ELSE, FOR / WHILE, funkcji
- Extension (-->)
- MODEL: deklaracja, assignment
- BEND
- Przesuwanie i rotowanie brył
- Potencjalnie rozłączanie brył

### Interpreter

- Obsługa błędów
- Implementacja IF / ELSE, FOR / WHILE, funkcji
- Extension (-->)
- MODEL: deklaracja, assignment
- BEND
- Przesuwanie i rotowanie brył
- Rozszerzenie deklaracji i assignmentów o podtypy

### Wizualizacja

- Przesuwanie i rotowanie brył
- BEND
