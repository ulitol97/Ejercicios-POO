<?php

class Coordinate {
  private $x;
  private $y;

  function __construct($x, $y){
    $this->x = $x;
    $this->y = $y;
    }
}

class Triangulo {
  public $center_abs_coordinate;
  public $v1_rel_coordinate;
  public $v2_rel_coordinate;
  public $v3_rel_coordinate;

  function __construct($center_abs_coordinate, $v1_rel_coordinate, $v2_rel_coordinate, $v3_rel_coordinate){
    $this->center = $center_abs_coordinate;
    $this->v1_rel_coordinate = $v1_rel_coordinate;
    $this->v2_rel_coordinate = $v2_rel_coordinate;
    $this->v3_rel_coordinate = $v3_rel_coordinate;
    }
}

// Posición absoluta = centro + posición relativa


// NO USAR MAGIC METHODS

// EJERCICIO 1 AL FINAL:
// Triangulo, Cuadrado, Polígono, Círculo y expresando el centro como una coordenada x e y.

// EJERCICIO 2 AL FINAL:
// Tests unitarios al ejercicio 1.

// EJERCICIO 3 AL FINAL:
// Tipos al ejercicio 1.

?>