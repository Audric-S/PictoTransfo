function validateForm() {
    var fileInput = document.getElementById('photo');
    if (fileInput.files.length === 0) {
        alert("Veuillez sélectionner une photo.");
        return false;
    }
    return true;
}