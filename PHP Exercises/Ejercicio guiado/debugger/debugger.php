<?php
  if (!isset($_SESSION)){
    echo '<p>Session not started or cannot be found!</p>';
  }
  else {
    $session_keys = array_keys($_SESSION);
    $n_vars = count($session_keys);
    echo "<h2>Session debugger</h2>";
    echo "<h4>$n_vars variable(s) in session.</h4>";
    
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
  }
?>