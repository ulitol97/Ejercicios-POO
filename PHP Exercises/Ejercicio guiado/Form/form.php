<?php
  include ("question.php");

  // Class representing the form containg questions
  class Form {
    private $title;
    private $description;
    private $questions; // Array of questions
    private $action;

    function __construct(string $title, string $description, string $action){
      $this->title = $title;
      $this->description = $description;
      $this->questions = array();
      $this->action = $action;
    }

    public function addQuestion (Question $question){
      array_push ($this->questions, $question);
    }

    public function validate (): bool {

      $formValid = true;

      foreach ($this->questions as $question){
        if (!$question->validate()){
          $formValid = false; // Evaluate all the form, don't stop when a question is invalid
        }
      }
      return $formValid;
    }

    public function to_HTML(): string{
      $form_HTML = "<h2>$this->title</h2>";
      $form_HTML .= "<h4>$this->description</h4>";
      $form_HTML .= "<form action='/$this->action' method='post'>";
      foreach ($this->questions as $question){
        $form_HTML .= $question->to_HTML();
      }
      $form_HTML .= "<input type='submit' value='Submit'></form>";
      
      $form_HTML .= "<form action='/screen1.php' method='get'>
      <input type='checkbox' name = 'reset' checked hidden/>
      <input type='submit' value='Reset to default form'/>
      </form>";

      return $form_HTML;
    }

    public function getTitle(): string {
      return $this->title;
    }

    public function getDescription(): string {
      return $this->description;
    }

    public function getQuestions(): array {
      return $this->questions;
    }

    public function getAction(): string {
      return $this->action;
    }

    public function __toString(): string {
      return "form about: " . $this->title;
    }
  }

  $f = new Form("Formulario 1", "Descripcion", "lol");
  $f->addQuestion(new NumericQuestion("Pregunta numérica 1", "15"));
  $_SESSION['defaultForm'] = $f;
?>