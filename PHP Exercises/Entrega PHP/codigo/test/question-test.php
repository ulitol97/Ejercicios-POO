<?php
use PHPUnit\Framework\TestCase;
include("../form/question.php");

// Unit tests regarding the functionality of the questions in the form
class QuestionTest extends TestCase
{
  // Test parent question class functionality
  public function testQuestion()
  {
    // Question class is well formed
    $this->assertClassHasAttribute('name', Question::class);
    $this->assertClassHasAttribute('label', Question::class);
    $this->assertClassHasAttribute('templateText', Question::class);
    $this->assertClassHasAttribute('answer', Question::class);
    $this->assertClassHasAttribute('validated', Question::class);

    
  }

  // Test string question class functionality, questions that expect a textual answer
  public function testStringQuestion()
  {
    // StringQuestion constructor does it job
    $question = new StringQuestion("Test question","question for testing","answer...");
    $this->assertEquals($question->name, "Test question");
    $this->assertEquals($question->label, "question for testing");
    $this->assertEquals($question->templateText, "answer...");
    $this->assertTrue($question->validated);

    // Standard validation works
    $this->assertFalse($question->validate()); // The question has empty answer so it is not valid
    $question->answer = "Answer   ";
    $this->assertTrue($question->validate()); // The question has an answer so it trims it and is valid
    $this->assertEquals($question->answer, "Answer");

    // Custom toString works
    $this->assertEquals($question->to_HTML(), "question for testing:<br>" .
    "<input type='text' name='Test question' placeholder='answer...' value='Answer'>" . "<br/>");
  }

  // Test numeric question class functionality, questions that expect a numeric answer
  public function testNumericQuestion()
  {
    // Clild class is well formed
    $this->assertClassHasAttribute('min', NumericQuestion::class);
    $this->assertClassHasAttribute('max', NumericQuestion::class);

    // NumericQuestion constructor does it job
    $question = new NumericQuestion("number","question for testing","placeholder...", 0, 10);
    $this->assertEquals($question->min, 0);
    $this->assertEquals($question->max, 10);

    // Standard validation works
    $this->assertFalse($question->validate()); // The question has empty answer so it is not valid
    $question->answer = "Answer";
    $this->assertFalse($question->validate()); // The question has a non numeric answer so it is not valid
    $question->answer = -5;
    $this->assertFalse($question->validate()); // The question has an invalid number as answer so it is not valid
    $question->answer = 11;
    $this->assertFalse($question->validate()); // The question has an invalid number as answer so it is not valid
    $question->answer = 5;
    $this->assertTrue($question->validate());
  }

  // Test radio button question class functionality, questions that offer a single choice answer
  public function testRadioButtonQuestion()
  {
    // Clild class is well formed
    $this->assertClassHasAttribute('options', RadioButtonQuestion::class);

    // NumericQuestion constructor does it job
    $question = new RadioButtonQuestion("radio","question for testing","option1", "option2","option3", "option4");
    $this->assertEquals(count($question->options), 4);
    $this->assertEquals($question->options[0], "option1");
    $this->assertEquals($question->options[1], "option2");
    $this->assertEquals($question->options[2], "option3");
    $this->assertEquals($question->options[3], "option4");
  }
}
?>