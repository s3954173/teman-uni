$(function(){
    
    const yearSelect = document.getElementById("year");
    const monthSelect = document.getElementById("month");
    const daySelect = document.getElementById("day");
    
    const months = ['January', 'February', 'March', 'April', 
    'May', 'June', 'July', 'August', 'September', 'October',
    'November', 'December'];
    
    
    (function populateMonths(){
        for(let i = 0; i < months.length; i++){
            const option = document.createElement('option');
            option.textContent = months[i];
            monthSelect.appendChild(option);
        }
        monthSelect.value = "January";
    })();
    
    let previousDay;
    
    function populateDays(month){
     
        while(daySelect.firstChild){
            daySelect.removeChild(daySelect.firstChild);
        }
    
        let dayNum;
    
        let year = yearSelect.value;
    
        if(month === 'January' || month === 'March' || 
        month === 'May' || month === 'July' || month === 'August' 
        || month === 'October' || month === 'December') {
            dayNum = 31;
        } else if(month === 'April' || month === 'June' 
        || month === 'September' || month === 'November') {
            dayNum = 30;
        }else{
    
            if(new Date(year, 1, 29).getMonth() === 1){
                dayNum = 29;
            }else{
                dayNum = 28;
            }
        }
    
        for(let i = 1; i <= dayNum; i++){
            const option = document.createElement("option");
            option.textContent = i;
            daySelect.appendChild(option);
        }
        if(previousDay){
            daySelect.value = previousDay;
            if(daySelect.value === ""){
                daySelect.value = previousDay - 1;
            }
            if(daySelect.value === ""){
                daySelect.value = previousDay - 2;
            }
            if(daySelect.value === ""){
                daySelect.value = previousDay - 3;
            }
        }
    }
    
    function populateYears(){
    
        let year = new Date().getFullYear() - 16;
    
        for(let i = 0; i < 65; i++){
            const option = document.createElement("option");
            option.textContent = year - i;
            yearSelect.appendChild(option);
        }
    }

    // Function to combine day, month, and year into a single date string
    function combineDate() {
        const day = daySelect.value;
        const monthName = monthSelect.value;
        const year = yearSelect.value;

        // Map month name to month number
        const monthMap = {
            'January': '01',
            'February': '02',
            'March': '03',
            'April': '04',
            'May': '05',
            'June': '06',
            'July': '07',
            'August': '08',
            'September': '09',
            'October': '10',
            'November': '11',
            'December': '12'
        };

        // Get the month number from the map
        const monthNumber = monthMap[monthName];

        // Combine into a date string in the format "YYYY-MM-DD"
        const dateString = `${year}-${monthNumber}-${day}`;

        // Set the value of a hidden input field with the combined date
        document.getElementById("combinedDate").value = dateString;
    }

    populateDays(monthSelect.value);
    populateYears();
    
    yearSelect.onchange = function() {
        populateDays(monthSelect.value);
    }
    monthSelect.onchange = function() {
        populateDays(monthSelect.value);
    }
    daySelect.onchange = function() {
        previousDay = daySelect.value;
    }

    // Collect selected interests into a comma-separated string
    const selectedInterests = [];
    const interestCheckboxes = document.querySelectorAll('input[name="selected_choices"]:checked');
    interestCheckboxes.forEach((checkbox) => {
        selectedInterests.push(checkbox.nextElementSibling.textContent.trim());
    });
    document.getElementById('interests').value = selectedInterests.join(',');

    // Collect selected languages into a comma-separated string
    const selectedLanguages = [];
    const languageSelect = document.getElementById('language');
    const selectedLanguageOptions = languageSelect.selectedOptions;
    for (let i = 0; i < selectedLanguageOptions.length; i++) {
        selectedLanguages.push(selectedLanguageOptions[i].textContent.trim());
    }
    document.getElementById('languages').value = selectedLanguages.join(',');
    
    // Add an event listener to the form submission to call combineLocation
    function combineLocation() {
        const city = document.getElementById("city").value;
        const state = document.getElementById("state").value;
    
        // Combine into a location string in the format "City, State"
        const locationString = `${city}, ${state}`;
    
        // Set the value of the hidden input field with the combined location
        document.getElementById("location").value = locationString;
    }

    $('form').on('submit', function (event) {
        console.log('Form working?')
        event.preventDefault(); // Prevent the form from submitting immediately
        combineLocation(); // Call the combineLocation function to update the hidden input
        combineDate(); // Call the combineDate function to update the hidden input
        this.submit(); // Now submit the form
    });
})

    
    