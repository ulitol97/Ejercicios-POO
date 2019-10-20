<?php // DEBUGGER: If the session exists, print all session variables nicely.
  if (!isset($_SESSION)){
    echo '<p>Session not started or cannot be found!</p>';
  }
  else {
    // Get all session variables
    $session_keys = array_keys($_SESSION);
    $get_keys = array_keys($_GET);
    $post_keys = array_keys($_POST);

    $n_vars = count($session_keys);
    $n_get_vars = count($get_keys);
    $n_post_vars = count($post_keys);

    echo "<h2>Session debugger</h2>";
    echo "<h4>$n_vars variable(s) in session.</h4>";
    
    // $_SESSION vars
    if ($n_vars > 0){
      // Print table headers
      echo "<table>
      <tr>
        <th>name</th>
        <th>value</th>
        <th>type</th>
      </tr>";
      // Print each variable into the table
      foreach ($session_keys as $value){
        echo "<tr>";
        $current_var = $_SESSION[$value];
        if (gettype($current_var) == "object"){
          $type = "object: " . get_class($current_var);
        }
        else {
          $type = gettype($current_var);
        }
        echo "<td>$value</td>";

        if ($type == "boolean" && $current_var == true){
          echo "<td>True</td>";
        }
        else if ($current_var == false) {
          echo "<td>False</td>";
        }
        else echo "<td>$current_var</td>";
        echo "<td>$type</td>";
        echo "</tr>";
      }
      echo "</table>";
    }

    // $_GET vars
    echo "<h4>$n_get_vars GET request variable(s) in session.</h4>";

    if ($n_get_vars > 0){
      // Print table headers
      echo "<table>
      <tr>
        <th>name</th>
        <th>value</th>
        <th>type</th>
      </tr>";
      // Print each variable into the table
      foreach ($get_keys as $value){
        echo "<tr>";
        $current_var = $_GET[$value];
        if (gettype($current_var) == "object"){
          $type = "object: " . get_class($current_var);
        }
        else {
          $type = gettype($current_var);
        }
        echo "<td>$value</td>";

        if ($type == "boolean" && $current_var == true){
          echo "<td>True</td>";
        }
        else if ($current_var == false) {
          echo "<td>False</td>";
        }
        else echo "<td>$current_var</td>";
        echo "<td>$type</td>";
        echo "</tr>";
      }
      echo "</table>";
    }

    // $_POST vars
    echo "<h4>$n_post_vars POST request variable(s) in session.</h4>";

    if ($n_post_vars > 0){
      // Print table headers
      echo "<table>
      <tr>
        <th>name</th>
        <th>value</th>
        <th>type</th>
      </tr>";
      // Print each variable into the table
      foreach ($post_keys as $value){
        echo "<tr>";
        $current_var = $_POST[$value];
        if (gettype($current_var) == "object"){
          $type = "object: " . get_class($current_var);
        }
        else {
          $type = gettype($current_var);
        }
        echo "<td>$value</td>";

        if ($type == "boolean" && $current_var == true){
          echo "<td>True</td>";
        }
        else if ($current_var == false) {
          echo "<td>False</td>";
        }
        else echo "<td>$current_var</td>";
        echo "<td>$type</td>";
        echo "</tr>";
      }
      echo "</table>";
    }
  }
?>