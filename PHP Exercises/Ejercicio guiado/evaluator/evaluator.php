<?php
  if (isset($_POST['customForm']) && ("" != trim($_POST['customForm']))){
    $output = array();
    $customForm = eval ($_POST['customForm']);
    // If the user input is a good form object, place the custom form in session.
    if (gettype($customForm) == 'object' && get_class ($customForm) == 'Form'){
      $_SESSION['customForm'] = $customForm;
    }
    // If invalid data was provided by the user, then do not set a custom form and show the default one
    else {
      unset($_SESSION['customForm']);
    }
  }
?>