<?php
use PHPUnit\Framework\TestCase;
include("../form/form.php");

// Unit tests regarding the functionality of the form as a whole
class FormTest extends TestCase
{
  // Test parent question class functionality
  public function testForm()
  {
    // Form class is well formed
    $this->assertClassHasAttribute('title', Form::class);
    $this->assertClassHasAttribute('description', Form::class);
    $this->assertClassHasAttribute('questions', Form::class);
    $this->assertClassHasAttribute('action', Form::class);
    $this->assertClassHasAttribute('disabled', Form::class);

    // Form constructor does it job
    $form = new Form("Test Form","form for testing","post.php");
    $this->assertEquals($form->title, "Test Form");
    $this->assertEquals($form->description, "form for testing");
    $this->assertEquals($form->action, "post.php");
    $this->assertEquals(gettype($form->questions), "array");
    $this->assertEquals(count($form->questions), 0);
    $this->assertEquals($form->disabled, "");

    // Create example questions
    $stringQuestion = new StringQuestion("string","question for testing","answer...");
    $numericNuestion = new NumericQuestion("number","question for testing","placeholder...", 0, 10);
    $radioQuestion = new RadioButtonQuestion("radio","question for testing","option1", "option2","option3", "option4");

    // Adding questions
    $form->addQuestion ($stringQuestion);
    $this->assertEquals(count($form->questions), 1);
    $form->addQuestion ($numericNuestion);
    $this->assertEquals(count($form->questions), 2);
    $form->addQuestion ($radioQuestion);
    $this->assertEquals(count($form->questions), 3);

    // Testing validation and filling form
    $this->assertFalse($form->validate());

    // Create fake post variables that have the same name as te questions in the form:
    $_POST['string'] = "String answer";
    $_POST['number'] = "5";
    $_POST['radio'] = "option1";
    $this->assertFalse($form->validate()); // The variables are there but he form has not filled the answer yet

    $form->fillForm(); // Change the answers of each question with the data in the POST request

    $this->assertTrue($form->validate()); // The form is valid

    // Place some invalid answers
    $_POST['string'] = "";
    $form->fillForm();
    $this->assertFalse($form->validate()); // The form is invalid
  }
}
?>