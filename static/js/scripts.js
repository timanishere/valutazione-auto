function popluateCarMake() {

    // Get value for make drop down
    var car_make_select_value = document.getElementById('make').value;

    // Populate car make dropdown
    $.ajax({
        url: '/process-car-make',
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

function populateCarKW() {

    // Get values from fields
    var car_make = document.getElementById('make').value
    var car_model = document.getElementById('model').value
    var car_year = document.getElementById('year').value
    var car_colour = document.getElementById('colour').value
    var car_gear = document.getElementById('gear').value
    var car_fuelType = document.getElementById('fuelType').value
    var car_km = document.getElementById('km').value

     // Populate car make dropdown
     $.ajax({
        url: '/process-car-kw',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 
            'car_make': car_make,
            'car_model': car_model,
            'car_year': car_year,
            'car_colour': car_colour,
            'car_gear': car_gear,
            'car_fuelType': car_fuelType,
            'car_km': car_km

        }),
        success: function(response) { 
            console.log(response);

            // Get select element for car KW
            var car_kw_select_el = document.getElementById('kw');

            // Clear options
            car_kw_select_el.innerHTML = '';

            // Create option element
            var first_option_el = document.createElement('option')

            // Set the text of the option
            first_option_el.text = 'Select kW'

            // Add option to the select element
            car_kw_select_el.appendChild(first_option_el)

            // Loop through car models
            for (var i = 0; i < response.length; i++) {

                // Create option element
                var option_el = document.createElement('option')

                // Set the text of the option
                option_el.text = response[i][0]

                // Set the valud
                option_el.value = response[i][0]

                // Add option to the select element
                car_kw_select_el.appendChild(option_el)
            }

            console.log(car_kw_select_el)
        }, 
        error: function(error) { 
            console.log(error);
        } 
    });
}