<?php

  class Question {
    private $label;  // Informative text next to the question
    private $name; // Inner name of the question in the form
    private $templateText; // Template text shown in the form field
    private $answer; // Answer of the question
    private $validated; // Bool, question validated or not

    function __construct(string $label, string $templateText){
      $this->label = $label;
      $this->templateText = $templateText;
      $this->validated = false;
    }

    public function validate (): bool {
      return false;
    }

    public function to_HTML(): string {
      $question_HTML = "$this->label:<br>";
      $question_HTML .= "<input type='text' name='$this->name' placeholder='$this->templateText' value='$this->answer'><br>";
      return $question_HTML;
    }

    public function getLabel(): string {
      return $this->label;
    }

    public function getTemplateText(): string {
      return $this->templateText;
    }

    public function getAnswer(): string {
      return $this->answer;
    }

    public function getValidated(): bool {
      return $this->validated;
    }
  }

  class StringQuestion extends Question {
    function __construct(string $label, string $templateText){
      parent::__construct($label, $templateText);
    }

    public function validate (): bool {
      $this->answer = trim($this->answer);
      return true;
    }
  }

  class NumericQuestion extends Question {
    function __construct(string $label, string $templateText){
      parent::__construct($label, $templateText);
    }

    public function validate (): bool {
      $this->answer = trim($this->answer);
      return is_numeric($this->answer);
    }
  }
?>