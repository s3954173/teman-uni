var openPopupButton = document.getElementById("openPopupButton");
var eventPopup = document.getElementById("eventPopup");
var popupOverlay = document.getElementById("popupOverlay");

openPopupButton.addEventListener("click", function() {
    eventPopup.style.display = "block";
    popupOverlay.style.display = "block";
    generateEventID();
    setEventAdmin();
});

function closePopupButton() {
    eventPopup.style.display = "none";
    popupOverlay.style.display = "none";
};

function generateEventID() {
    const randomNum = Math.floor(Math.random() * 100000);
    const eventID = "e" + randomNum;

    document.getElementById("eventID").value = eventID;
}

function setEventAdmin() {
    const currentUser = 'user123';

    document.getElementById("eventAdmin").value = currentUser;
}

var eventDesc = document.getElementById("eventDesc");

eventDesc.addEventListener("input", function() {
    const words = eventDesc.value.trim().split(/\s+/);
    if(words.length > 100) {
        const truncatedText = words.slice(0, 100).join(" ");
        eventDesc.value = truncatedText;
    }
});
