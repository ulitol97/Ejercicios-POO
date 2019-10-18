<?php

class Coordinate {
  private $x;
  private $y;
  function __construct($x, $y){
    $this->x = $x;
    $this->y = $y;
    }
  
  public function __toString() {
      return "x: " . $this->x . " - y: " . $this->y;
  }
}
class Figure {
  private $center; // Center location 
  public $n_vertices; // Number of vertices of the figure
  private $vertices = array(); // Array of vertices

  function __construct($center, $vertices, $n_vertices){
    $this->center = $center;
    $this->n_vertices = $n_vertices;

    for ($i = 0; $i < $n_vertices; $i++){
      array_push ($this->vertices, $vertices[$i]);
    }
  }

  public function __toString() {
    $ret =  "Center:\n\t" . $this->center->__toString() . "\nVertices:\n";
    for ($i = 0; $i < $this->n_vertices; $i++){
      $ret = $ret . "\t" . $this->vertices[$i]->__toString() . "\n";
    }
    return $ret;
  }
}

class Triangulo extends Figure {
  function __construct($center, $vertices){
      parent::__construct($center, $vertices, 3);
    }
  
  public function __toString() {
    return "\nTRIANGULO\n" . parent::__toString();
  }
}

class Cuadrado extends Figure {
  function __construct($center, $vertices){
    parent::__construct($center, $vertices, 4);
  }
  public function __toString() {
    return "\nCUADRADO\n" . parent::__toString();
  }
}

class Poligono extends Figure {
  function __construct($center, $vertices){
    parent::__construct($center, $vertices, count($vertices));
  }

  public function __toString() {
    return "\nPOLIGONO (lados: " . $this->n_vertices . ")\n" . parent::__toString();
  }
}

// EJERCICIO 1 AL FINAL:
// Triangulo, Cuadrado, Polígono, Círculo y expresando el centro como una coordenada x e y.

// EJERCICIO 2 AL FINAL:
// Tests unitarios al ejercicio 1.

// EJERCICIO 3 AL FINAL:
// Tipos al ejercicio 1.


// Program
$coords = array();
array_push ($coords, new Coordinate(1,1));
array_push ($coords, new Coordinate(2,2));
array_push ($coords, new Coordinate(3,3));
array_push ($coords, new Coordinate(4,4));
array_push ($coords, new Coordinate(5,5));
array_push ($coords, new Coordinate(6,6));


$tri = new Triangulo(new Coordinate(4,4), $coords);
echo ($tri);

$cuad = new Cuadrado(new Coordinate(4,4), $coords);
echo ($cuad);

$poli = new Poligono(new Coordinate(4,4), $coords);
echo ($poli);
?>