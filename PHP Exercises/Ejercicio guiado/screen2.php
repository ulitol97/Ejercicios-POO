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
    <title>PHP - Form</title>
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
      <div class='form-data'>
        <h1>Confirmation screen:</h1>
        <?php
          $valid = false;
          // If a custom form was given by the user, show it
          if (isset($_SESSION['customForm'])){
            $_SESSION['customForm']->fillForm();
            $valid = $_SESSION['customForm']->validate();
            if (!$valid){
              echo "<p class='error'>The form has invalid data marked with '*'</p>";
              // Do not redirect incorrect data to the final screen
              $_SESSION['customForm']->disabled = "";
              $_SESSION['customForm']->action = "screen2.php";
            }
            else {
              echo "<p class='valid'>The form submitted had valid data that has been locked and stored</p>";
              // Redirect data to the final screen
              $_SESSION['customForm']->action = "screen3.php";
              // Store last valid data for representation
              $_SESSION['customForm']->disabled = "disabled";
              $_SESSION['validForm'] = clone $_SESSION['customForm'];
            }
            echo $_SESSION['customForm']->to_HTML();
          }
          else {
            $_SESSION['defaultForm']->fillForm();
            $valid = $_SESSION['defaultForm']->validate();
            if (!$valid){
              echo "<p class='error'>The form has invalid data marked with '*'</p>";
              // Do not redirect incorrect data to the final screen
              $_SESSION['defaultForm']->disabled = "";
              $_SESSION['defaultForm']->action = "screen2.php";
            }
            else {
              echo "<p class='valid'>The form submitted had valid data that has been locked and stored</p>";
              // Redirect data to the final screen
              $_SESSION['defaultForm']->action = "screen3.php";
              // Store last valid data for representation
              $_SESSION['defaultForm']->disabled = "disabled";
              $_SESSION['validForm'] = clone $_SESSION['defaultForm'];
            }
            echo $_SESSION['defaultForm']->to_HTML();
          }
        ?>
      </div>
      <div class='visualizer'>
        <h2>Data visualizer</h2>
        <h4>No validated data to visualize yet</h4>
      </div>
      <div class='debugger'>
        <?php include 'debugger/debugger.php';?>
      </div>
    </div>
  </body>
</html>