# ConnectIT: Hello World

The grammar located in `ConnectIT.g4` allows for declaring `UNIT`s and `LAYER`s, as well as `SHOW`ing them in the console. <br />

Having activated your virtual environment, use the command:

```
antlr4 -Dlanguage=Python3 -visitor ConnectIT.g4
```

to generate the necessary components (`Lexer`, `Parser`, `Visitor`). You should now be able to interpret your expressions by appropriately editing the `hello_word.txt` file and running:

```
py interpreter.py
```
