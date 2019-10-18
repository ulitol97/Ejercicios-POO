<?php

// Coordinate to represent 2D points
class Coordinate {
  private $x;
  private $y;

  function __construct(float $x, float $y){
    $this->x = $x;
    $this->y = $y;
    }

  public function getX(): string {
      return $this->x;
  }

  public function getY(): string {
    return $this->y;
  }

  // Re-define toString
  public function __toString() : string {
      return "x: " . $this->x . " - y: " . $this->y;
  }


}

// Template Figure class
class Figure {
  public $center; // Center location 
  public $n_vertices; // Number of vertices of the figure
  public $vertices = array(); // Array of vertices

  function __construct(Coordinate $center, array $vertices, int $n_vertices){
    $this->center = $center;
    $this->n_vertices = $n_vertices;

    for ($i = 0; $i < $n_vertices; $i++){
      array_push ($this->vertices, $vertices[$i]);
    }
  }

  public function getCenter(): Coordinate {
    return $this->center;
  }

  public function getNVertices(): int {
    return $this->n_vertices;
  }

  public function getVertices(): array {
    return $this->n_vertices;
  }

  // String representation of the Figure
  public function __toString() {
    $ret =  "Center:\n\t" . $this->center->__toString();
    if (count($this->vertices) > 0){
      $ret = $ret . "\nVertices:\n";

      for ($i = 0; $i < $this->n_vertices; $i++){
        $ret = $ret . "\t" . $this->vertices[$i]->__toString() . "\n";
      }
    }
    return $ret;
  }
}

// Triangle figure
class Triangulo extends Figure {
  function __construct(Coordinate $center, array $vertices){
      parent::__construct($center, $vertices, 3); // Maximum of 3 vertices
    }
  
  public function __toString() {
    return "\nTRIANGULO\n" . parent::__toString();
  }
}

// Square figure
class Cuadrado extends Figure {
  function __construct(Coordinate $center, array $vertices){
    parent::__construct($center, $vertices, 4); // Maximum of 4 vertices
  }
  public function __toString() {
    return "\nCUADRADO\n" . parent::__toString();
  }
}

// Polygon figure
class Poligono extends Figure {
  function __construct(Coordinate $center, array $vertices){
    parent::__construct($center, $vertices, count($vertices)); // As many vertices as the length of the array passed
  }

  public function __toString() {
    return "\nPOLIGONO (lados: " . $this->n_vertices . ")\n" . parent::__toString();
  }
}

// Circle figure: the circle has a radius and no vertices specified to the parent constructor
class Circulo extends Figure {
  private $radius;
  function __construct(Coordinate $center, float $radius){
    $this->radius = $radius;
    parent::__construct($center, array(), 0);
  }

  public function getRadius(): float {
    return $this->radius;
  }

  public function __toString() {
    return "\nCirculo (radio: " . $this->radius . ")\n" . parent::__toString();
  }
}

// Program. Trying to build a figure with less sides that it needs throws an exception.
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

$circle = new Circulo(new Coordinate(4,4), 5);
echo ($circle);
?>