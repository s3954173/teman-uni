function toggleDropdown(dropdownId) {
    var content = document.querySelector('#' + dropdownId + ' .content');
    content.style.display = content.style.display === 'flex' ? 'none' : 'flex';
    console.log("test")
}

function openModal(modalId) {
    document.getElementById(modalId).style.display = 'flex';
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

function updateProfile() {
    closeModal('modal2');
    closeModal('modal1');


    var contentElement = document.querySelector('#dropdown1 .content');


    contentElement.innerHTML = '';

    var checkboxes = document.querySelectorAll('#modal2 input[type=checkbox]');


    checkboxes.forEach(function(checkbox) {
        if (checkbox.checked) {

            var newPill = document.createElement('span');
            newPill.className = 'pill';
            newPill.textContent = checkbox.value;


            contentElement.appendChild(newPill);
        }
    });

}