<?php

  class Question {
    public $name; // Inner name of the question in the form
    public $label;  // Informative text next to the question
    public $templateText; // Template text shown in the form field
    public $answer; // Answer of the question
    public $validated; // Bool, question validated or not

    function __construct(string $name, string $label, string $templateText){
      $this->name = $name;
      $this->label = $label;
      $this->templateText = $templateText;
      $this->validated = true;
    }

    public function validate (): bool {
      $this->validated = true;
      return true;
    }

    public function to_HTML(): string {
      $question_HTML = "$this->label:<br>";
      $question_HTML .= "<input type='text' required='required' name='$this->name' placeholder='$this->templateText' value='$this->answer'>";
      if (!$this->validated){
        $question_HTML .= "<span class='error'> * </span>";
      }
      $question_HTML .= "<br/>";
      return $question_HTML;
    }
  }

  class StringQuestion extends Question {
    function __construct(string $name, string $label, string $templateText){
      parent::__construct($name, $label, $templateText);
    }

    public function validate (): bool {
      $this->answer = trim($this->answer);
      $this->validated = true;
      return true;
    }
  }

  class NumericQuestion extends Question {
    public $min;
    public $max;
    function __construct(string $name, string $label, string $templateText, float $min, float $max){
      parent::__construct($name, $label, $templateText);
      $this->min = $min;
      $this->max = $max;
    }

    public function to_HTML(): string {
      $question_HTML = "$this->label:<br>";
      $question_HTML .= "<input type='number' required='required' name='$this->name' placeholder='$this->templateText'
       value='$this->answer' min='$this->min' max='$this->max'>";
      if (!$this->validated){
        $question_HTML .= "<span class='error'> * </span>";
      }
      $question_HTML .= "<br/>";
      return $question_HTML;
    }

    public function validate (): bool {
      $this->answer = trim($this->answer);
      if (!is_numeric($this->answer)){
        $this->validated = false;
        return false;
      } 
      $numeric_answer = (int)$this->answer;
      if ($numeric_answer < $this->min || $numeric_answer > $this->max){
        $this->validated = false;
        return false;
      }
      $this->validated = true;
      return true;
    }
  }
?>