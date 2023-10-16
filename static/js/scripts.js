function sendData() {

    // Get value for make drop down
    var car_make_select_value = document.getElementById('make').value;

    $.ajax({
        url: '/process',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 'car_make': car_make_select_value }),
        success: function(response) { 
            console.log(response)
            
            // Get select element for car model
            var car_model_select_el = document.getElementById('model');

            // Clear options
            car_model_select_el.innerHTML = '';

            // Create option element
            var first_option_el = document.createElement('option')

            // Set the text of the option
            first_option_el.text = 'Select a model'

            // Add option to the select element
            car_model_select_el.appendChild(first_option_el)

            // Loop through car models
            for (var i = 0; i < response.length; i++) {

                // Create option element
                var option_el = document.createElement('option')

                // Set the text of the option
                option_el.text = response[i][0]

                // Set the valud
                option_el.value = response[i][0]

                // Add option to the select element
                car_model_select_el.appendChild(option_el)
            }
        }, 
        error: function(error) { 
            console.log(error); 
        } 
    });

}