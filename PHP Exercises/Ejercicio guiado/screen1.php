<?php session_start();?>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" title="base" href="css/base.css">
    <title>PHP - Form</title>
  </head>
  <body>
    <div class='wrapper'>
      <div class='evaluator'>
        <h2>Evaluator</h2>
        <h4>Insert your custom php form:</h4>
        <form action="/screen1.php" method='post'>
          <input type="text" name="customForm" placeholder="PHP code...">
          <input type="submit" value="Submit">
        </form>
      </div>
      <div class='form-data'>
        <?php
          include 'form/form.php';
          include 'evaluator/evaluator.php';

          // If a custom form was given by the user, show it
          if (isset($_SESSION['customForm'])){
            echo $_SESSION['customForm']->to_HTML();
          }
          else {
            echo $_SESSION['defaultForm']->to_HTML();
          }
        ?>
      </div>
      <div class='visualizer'>
        <h2>Data visualizer</h2>
      </div>
      <div class='debugger'>
        <?php include 'debugger/debugger.php';?>
      </div>
    </div>
  </body>
</html>