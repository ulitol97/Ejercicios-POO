function loadGoogleCharts(): void{
  // Load the Visualization API and the corechart package.
  google.charts.load('current', {'packages':['corechart']});
  // Set a callback to run when the Google Visualization API is loaded.
  google.charts.setOnLoadCallback(drawCharts);
}

// Draws the graphs
function drawCharts() {

  // Create data tables
  let journeyAndVisitData = new google.visualization.DataTable();
  let scoreData = new google.visualization.DataTable();

  let satisfactionResults = {};

  // Create the data table.
  journeyAndVisitData.addColumn('string', 'Feeling');
  journeyAndVisitData.addColumn('number', 'Times');

  scoreData.addColumn('number', 'Score');
  scoreData.addColumn('number', 'Times');

  
  // Parse form encoded as JSON data
  for (i = 0; i < incomingData.questions.length; i++){
    if (incomingData.questions[i].name == "journey" || incomingData.questions[i].name == "monuments"){

      // Deal with different opinions about the journey and the monuments
      if (satisfactionResults[incomingData.questions[i].answer] != "undefined"){
        satisfactionResults[incomingData.questions[i].answer] = 1;
      }
      else {
        satisfactionResults[incomingData.questions[i].answer] += 1;
      }
    }
    else if (incomingData.questions[i].name == "score"){
      scoreData.addRows([
        [-1, 0],
        [parseInt(incomingData.questions[i].answer, 10), 1]
      ]);
    }
  }
  

  for (opinion in satisfactionResults){
    journeyAndVisitData.addRows([
      [opinion, satisfactionResults[opinion]]
    ]);
  }

  console.log(incomingData)


  // Set chart options
  let journeyAndVisitOptions = {'title':'Feeling towards the journey and the monuments seen in ' + visitedPlace,
  'width':400,
  'height':300};

  let scoreOptions = {'title':'Score (0 - 10) given to the overall trip',
  'width':500,
  'height':300};

  // Instantiate and draw our charts, passing in some options.
  let journeyAndVisitChart = new google.visualization.PieChart(pieChartDiv);
  let scoreChart = new google.visualization.ColumnChart(barChartDiv);

  journeyAndVisitChart.draw(journeyAndVisitData, journeyAndVisitOptions);
  scoreChart.draw(scoreData, scoreOptions);
}

let graphsDiv: Element = document.getElementById("graph-wrapper");
if (graphsDiv != null){

  var pieChartDiv = graphsDiv.appendChild(document.createElement('div'));
  var barChartDiv = graphsDiv.appendChild(document.createElement('div'));



  console.log("Plotting chart");
  var visitedPlace: string = incomingData.questions[0].answer;
  loadGoogleCharts();
}