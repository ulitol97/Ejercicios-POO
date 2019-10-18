<?php
use PHPUnit\Framework\TestCase;
include("exercise_1.php");

class FigureTest extends TestCase
{
  public function testCoordinate()
  {
    // Coordinate class is well formed
    $this->assertClassHasAttribute('x', Coordinate::class);
    $this->assertClassHasAttribute('y', Coordinate::class);

    // Coordinate constructor does it job
    $coord = new Coordinate(1,4);
    $this->assertIsNumeric($coord->x);
    $this->assertIsNumeric($coord->y);
    $this->assertEquals($coord->x, 1);
    $this->assertEquals($coord->y, 4);

    // Custom toString works
    $this->assertEquals($coord->__toString(), "x: 1 - y: 4");
  }

  public function testFigure()
  {
    // Figure class is well formed
    $this->assertClassHasAttribute('center', Figure::class);
    $this->assertClassHasAttribute('n_vertices', Figure::class);
    $this->assertClassHasAttribute('vertices', Figure::class);
  }

  public function testTriangle()
  {
    $coords = array();
    // Set up array of coordinates
    array_push ($coords, new Coordinate(1,1));
    array_push ($coords, new Coordinate(2,2));
    array_push ($coords, new Coordinate(3,3));
    array_push ($coords, new Coordinate(4,4));
    array_push ($coords, new Coordinate(5,5));
    array_push ($coords, new Coordinate(6,6));
    $this->assertEquals(count($coords), 6);


    // Triangle constructor does it job
    $tri = new Triangulo(new Coordinate(1, 4), $coords);
    
    $this->assertEquals($tri->center->x, 1);
    $this->assertEquals($tri->center->y, 4);

    $this->assertEquals($tri->n_vertices, 3);
    $this->assertEquals(count($tri->vertices), 3);

    $this->assertEquals($tri->vertices[0]->x, 1);
    $this->assertEquals($tri->vertices[0]->y, 1);
    $this->assertEquals($tri->vertices[1]->x, 2);
    $this->assertEquals($tri->vertices[1]->y, 2);
    $this->assertEquals($tri->vertices[2]->x, 3);
    $this->assertEquals($tri->vertices[2]->y, 3);
  }

  public function testSquare()
  {
    $coords = array();
    // Set up array of coordinates
    array_push ($coords, new Coordinate(-1,1));
    array_push ($coords, new Coordinate(2,-2));
    array_push ($coords, new Coordinate(-3,3));
    array_push ($coords, new Coordinate(-4,-4));
    array_push ($coords, new Coordinate(-5,-5));
    array_push ($coords, new Coordinate(6,6));
    $this->assertEquals(count($coords), 6);


    // Square constructor does it job
    $cuad = new Cuadrado(new Coordinate(5, 2), $coords);
    
    $this->assertEquals($cuad->center->x, 5);
    $this->assertEquals($cuad->center->y, 2);

    $this->assertEquals($cuad->n_vertices, 4);
    $this->assertEquals(count($cuad->vertices), 4);

    $this->assertEquals($cuad->vertices[0]->x, -1);
    $this->assertEquals($cuad->vertices[0]->y, 1);
    $this->assertEquals($cuad->vertices[1]->x, 2);
    $this->assertEquals($cuad->vertices[1]->y, -2);
    $this->assertEquals($cuad->vertices[2]->x, -3);
    $this->assertEquals($cuad->vertices[2]->y, 3);
    $this->assertEquals($cuad->vertices[3]->y, -4);
    $this->assertEquals($cuad->vertices[3]->y, -4);
  }

  public function testPolygon()
  {
    $coords = array();
    // Set up array of coordinates
    array_push ($coords, new Coordinate(-1,1));
    array_push ($coords, new Coordinate(2,-2));
    array_push ($coords, new Coordinate(-3,3));
    array_push ($coords, new Coordinate(-4,-4));
    array_push ($coords, new Coordinate(-5,-5));
    array_push ($coords, new Coordinate(6,6));
    $this->assertEquals(count($coords), 6);


    // Polygon constructor does it job
    $poly = new Poligono(new Coordinate(2, 3), $coords);
    
    $this->assertEquals($poly->center->x, 2);
    $this->assertEquals($poly->center->y, 3);

    $this->assertEquals($poly->n_vertices, 6);
    $this->assertEquals(count($poly->vertices), 6);

    $this->assertEquals($poly->vertices[0]->x, -1);
    $this->assertEquals($poly->vertices[0]->y, 1);
    $this->assertEquals($poly->vertices[1]->x, 2);
    $this->assertEquals($poly->vertices[1]->y, -2);
    $this->assertEquals($poly->vertices[2]->x, -3);
    $this->assertEquals($poly->vertices[2]->y, 3);
    $this->assertEquals($poly->vertices[3]->y, -4);
    $this->assertEquals($poly->vertices[3]->y, -4);
    $this->assertEquals($poly->vertices[4]->y, -5);
    $this->assertEquals($poly->vertices[4]->y, -5);
    $this->assertEquals($poly->vertices[5]->y, 6);
    $this->assertEquals($poly->vertices[5]->y, 6);
  }

  public function testCircle()
  {
    $radius = 5;

    // Circle constructor does it job
    $circ = new Circulo(new Coordinate(4, 4), $radius);
    
    $this->assertEquals($circ->center->x, 4);
    $this->assertEquals($circ->center->y, 4);

    $this->assertEquals($circ->radius, $radius);
  }
}
?>