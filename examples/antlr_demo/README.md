# ANTLR4 Demo

The grammar located in `Expr.g4` describes the language of simple math expressions. <br />

Having activated your virtual environment, use the command:

```
antlr4 -Dlanguage=Python3 -visitor Expr.g4
```

to generate the necessary components (`Lexer`, `Parser`, `Visitor`). You should now be able to interpret your expressions by running:

```
py ExprInterpreter.py
```

Separate all tokens in your expression (except for parentheses) with spaces. Example expressions:

```
2 + 5
3 - 4 * 2
10 * (7 - 3) + 9
```
