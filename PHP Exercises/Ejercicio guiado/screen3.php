<?php 
  spl_autoload_register(function () {
    include 'form/form.php';
  });
  session_start();
?><html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" title="base" href="css/base.css">
    <script src='js/visualizer.js'></script>
    <title>PHP - Visualization</title>
  </head>
  <body>
    <div class='wrapper'>
      <?php
        include 'evaluator/evaluator.php';
      ?>
      <div class='evaluator'>
        <h2>Evaluator</h2>
        <h4>Insert your custom php form:</h4>
        <form action="/screen1.php" method='post'>
          <input type="text" name="customForm" placeholder="PHP code...">
          <input type="submit" value="Submit">
        </form>
      </div>
      <div class='visualizer' style="grid-column: 1 / 3; text-align: center">
          <h2>Data visualizer</h2>
          <?php
            if (isset($_SESSION['validForm'])){
              echo "<h4>Graph of the las valid input data:</h4><div id='graph-wrapper'></div>";
            } 
            else echo "<h4 class='error'>Please complete the rest of the steps before accessing the visualization page.</h4>";
          ?>
          <button type="button" onClick='location.href="screen1.php"'>Restart process</button>
      </div>
      <div class='debugger'>
        <?php include 'debugger/debugger.php';?>
      </div>
    </div>
  </body>
</html>