<html>
    <head>
    <title>Paso 1</title>
    </head>
    <body>
    <h1>Paso 1</h1>
    <p>Hola</p>
    <button type="button" onClick='location.href="paso2.php"'>On Click</button>
    <button type="button" action="paso3.php">Atras</button>
    <form method="POST" action='paso2.php'>
        <input type="submit" name="boton 1"  value="Submit">
    </form>
    <p>Otro Ejemplo de boto JS</p>
    <button type="submit" formtarget="_blank" formmethod="post" formaction="paso2.php">Nuevo</button>
    <p><?php get_headers("paso1.php") ?></p>
 </body>
</html>
