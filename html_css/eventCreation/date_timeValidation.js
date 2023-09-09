var eventDateInput = document.getElementById("eventDate");
var eventTimeInput = document.getElementById("eventTime");

document.querySelector("form").addEventListener("submit", function(event) {
    var currentDate = new Date(); 
    var selectedDate = new Date(eventDateInput.value + " " + eventTimeInput.value);

    if (selectedDate <= currentDate) {
        event.preventDefault();
        alert("Please select a future date and time.");
    }
 });