$(document).ready(function() {
    $('#number-of-barcodes').on('change', function() {
        var numberOfBarcodes = parseInt($(this).val());
        $('#barcode-inputs-container').empty(); // Clear previous inputs
        
        for (var i = 0; i < numberOfBarcodes; i++) {
            var input = $('<input>').attr({
                type: 'text',
                name: 'barcode' + (i + 1), // Add 1 to make it start from 1 instead of 0
                placeholder: 'Enter Barcode ' + (i + 1),
                class: 'form-control'
            });
            var label = $('<label>').attr('for', 'barcode' + (i + 1)).text('Barcode ' + (i + 1));
            var div = $('<div>').addClass('form-floating').append(input, label);
            $('#barcode-inputs-container').append(div);
        }
    });

    $('#barcode-form').on('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        var formData = $(this).serialize(); // Serialize form data
        console.log(formData); // Just for testing, you can send it via Ajax or perform other actions
    });
});