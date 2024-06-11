// Define global variables
var selectedCell = null;
var selectedSubject = null;

// Function to select a cell in the table
function selectCell(cell) {
  // Check if there is a currently selected cell
  if (selectedCell) {
    // Deselect the currently selected cell
    selectedCell.classList.remove('selected');
  }
  // Select the new cell
  cell.classList.add('selected');
  selectedCell = cell;
}

// Function to select a subject from the dropdown
function selectSubject() {
  // Get the selected subject from the dropdown
  var select = document.getElementById('subject-dropdown');
  selectedSubject = select.value;
}

// Function to add the selected subject to the selected cell
function addSubject() {
  // Check that a cell and subject are selected
  if (selectedCell && selectedSubject) {
    // Add the subject to the cell
    selectedCell.textContent = selectedSubject;
  }
}

// Attach event listeners to the table cells
var cells = document.getElementsByTagName('td');
for (var i = 0; i < cells.length; i++) {
  cells[i].addEventListener('click', function() {
    selectCell(this);
  });
}

// Attach event listener to the subject dropdown
var subjectDropdown = document.getElementById('subject-dropdown');
subjectDropdown.addEventListener('change', function() {
  selectSubject();
});

// Attach event listener to the add subject button
var addButton = document.getElementById('add-subject-button');
addButton.addEventListener('click', function() {
  addSubject();
});
