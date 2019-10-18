<?php
  include ("question.php");

  // Class representing the form containg questions
  class Form {
    private $title;
    private $description;
    private $questions; // Array of questions

    function __construct(string $title, string $description){
      $this->title = $title;
      $this->description = $description;
      $this->questions = array();
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

    public function to_HTML(string $destination): string{
      $form_HTML = "<h2>$this->title</h2>";
      $form_HTML .= "<p>$this->description</p>";
      $form_HTML .= "<form action='/$destination'>";
      foreach ($this->questions as $question){
        $form_HTML .= $question->to_HTML();
      }
      $form_HTML .= "<input type='submit' value='Submit'></form>";

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
  }

  $f = new Form("Hola", "desc");
  echo $f->to_HTML("ja");

?>