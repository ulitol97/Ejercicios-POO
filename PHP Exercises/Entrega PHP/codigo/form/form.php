<?php
  include ("question.php");

  // Class representing the form containg questions
  class Form {
    public $title;
    public $description;
    public $questions; // Array of questions
    public $action;
    public $disabled;

    function __construct(string $title, string $description, string $action){
      $this->title = $title;
      $this->description = $description;
      $this->questions = array();
      $this->action = $action;
      $this->disabled = "";
    }

    public function addQuestion (Question $question): void{
      array_push ($this->questions, $question);
    }

    public function validate (): bool {

      if (count($this->questions) == 0){
        return false;
      }

      $formValid = true;

      foreach ($this->questions as $question){
        if (!$question->validate()){
          $formValid = false; // Evaluate all the form, don't stop when a question is invalid
        }
      }
      return $formValid;
    }

    // Fill the form answers with the data captured from a previous post request
    public function fillForm (): void {
      if (isset($_POST)){
        // Get all keys in the array of data of the POST request
        $session_keys = array_keys($_POST);
        $n_vars = count($session_keys);

        // For each variable sent in the post
        foreach ($session_keys as $key){
          foreach ($this->questions as $question){
            if ($question->name == $key){
              $question->answer = $_POST[$key];
            }
          }
        }
      }
    }

    // Return the HTML representation of a form containing all the questions in it
    public function to_HTML(): string{
      $form_HTML = "<h2>$this->title</h2>";
      $form_HTML .= "<h4>$this->description</h4>";
      $form_HTML .= "<form action='/$this->action' method='post'>";
      $form_HTML .= "<fieldset $this->disabled>";
      foreach ($this->questions as $question){
        $form_HTML .= $question->to_HTML();
      }
      $form_HTML .= "</fieldset>";

      $form_HTML .= "<br/><input type='submit' value='Next'>";
      $form_HTML .= "</form>";

      
      $form_HTML .= "<form action='/screen1.php' method='get'>
      <input type='checkbox' name = 'reset' checked hidden/>
      <input type='submit' value='Reset to default form'/>
      </form>";

      return $form_HTML;
    }

    public function __toString(): string {
      return "Form with title: " . $this->title;
    }
  }
?>