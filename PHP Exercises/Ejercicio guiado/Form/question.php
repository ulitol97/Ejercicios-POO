<?php

  class Question {
    private $label;
    private $templateText;
    private $validated;

    function __construct(string $label, string $templateText){
      $this->label = $label;
      $this->templateText = $templateText;
      $this->validated = false;
    }

    public function getLabel(): string {
      return $this->label;
    }

    public function getTemplateText(): string {
      return $this->templateText;
    }

    public function getValidated(): bool {
      return $this->validated;
    }
  }
  
  

?>