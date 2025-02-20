<?php 
  spl_autoload_register(function () {
    include 'form/form.php';
  });
  session_start();
?>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" title="base" href="css/base.css">
    <title>PHP - Form</title>
  </head>
  <body>
    <!-- Wrapper to arrange the screen items -->
    <div class='wrapper'>
      <?php
        // When the reset form signal is fired, remove old custom data before anything else
        if (isset($_GET['reset'])){
          unset($_SESSION['customForm']);
          unset($_SESSION['customFormError']);
        };
        include 'evaluator/evaluator.php';
      ?>
      <!-- Evaluator module with the form to introduce PHP code -->
      <div class='evaluator'>
        <h2>Evaluator</h2>
        <h4>Insert your custom php form:</h4>
        <form action="/screen1.php" method='post'>
          <input type="text" name="customForm" placeholder="PHP code...">
          <input type="submit" value="Submit">
        </form>
        <?php 
          if (isset($_SESSION['customFormError'])){
            echo "<p class='error'>Invalid form introduced. Showing default form.</p>";
          }
          else if ("" == trim($_POST['customForm'])) unset($_SESSION['customForm']);
          else if (isset($_SESSION['customForm']) && ("" != trim($_POST['customForm'])))
            echo "<p class='valid'>Form parsed</p>";
        ?>
      </div>
      <!-- Main body of the form -->
      <div class='form-data'>
        <?php
          // If a custom form was given by the user, show it
          if (isset($_SESSION['customForm']) && ("" != trim($_POST['customForm'])
          && (!isset($_GET['reset'])))){
            // Ensure POST data is sent to the second page
            $_SESSION['customForm']->action = "screen2.php";
            $_SESSION['customForm']->disabled = "";
            echo $_SESSION['customForm']->to_HTML();
          }
          else {
            $f = new Form("Rate your trip experience", "Please rate a few aspects about your last trip:", "screen2.php");
            $f->addQuestion(new StringQuestion("place","What was the last foreign country you visited", "France..."));
            $f->addQuestion(new RadioButtonQuestion("journey","How did you feel during the jouney?", 
              "Angry", "Bored", "Curious", "Interested", "In love"));
            $f->addQuestion(new RadioButtonQuestion("monuments","How did you feel when visiting the different monuments?", 
              "Angry", "Bored", "Curious", "Interested", "In love"));
            $f->addQuestion(new NumericQuestion("score","From 0 to 10, how much did you enjoy the visit?", "0..10", 0, 10));
            $_SESSION['defaultForm'] = $f;
            
            echo $_SESSION['defaultForm']->to_HTML();
          }
        ?>
      </div>
      <div class='visualizer'>
        <h2>Data visualizer</h2>
          <?php
            if (isset($_SESSION['validForm'])){
              if ($_SESSION['validForm']->title == "Rate your trip experience"){
                echo "<h4>Graph of the last valid input data:</h4><div id='graph-wrapper''></div>";
                $json_form = json_encode($_SESSION['validForm']);
                echo "<script>var incomingData = $json_form</script>";
              }
              else {
                echo "<h4 class='error'>Sorry but graphs are only generated for the default form and not user custom forms.</h4>";
              }
            } 
            else echo "<h4 class='error'>Please complete the rest of the steps before accessing the visualization page.</h4>";
          ?>
      </div>
      <div class='debugger'>
        <?php include 'debugger/debugger.php';?>
      </div>
    </div>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script src='js/visualizer.js'></script>
  </body>
</html>