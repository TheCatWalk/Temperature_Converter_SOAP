# Import the required modules
import zeep
from zeep import Client
import ipywidgets as widgets
from IPython.display import display
import webbrowser 

# Create input widgets
temperature_input = widgets.FloatText(description="Temperature:")
from_unit_dropdown = widgets.Dropdown(options=["degreeFahrenheit", "degreeCelsius"], description="From:")
to_unit_dropdown = widgets.Dropdown(options=["degreeCelsius", "degreeFahrenheit"], description="To:")
convert_button = widgets.Button(description="Convert")

# Create output widgets
output_text = widgets.Text(description="Converted Temperature:")
output_number = widgets.Text(description="Number Converted to Words:")
error_text = widgets.Text(description="Error:")

# Event handler for the convert button
def convert_button_clicked(b):
    try:
        # Get input values
        temp = temperature_input.value
        from_unit = from_unit_dropdown.value
        to_unit = to_unit_dropdown.value
        
        # Call function to convert temperature
        converted_temp = convert_temperature(temp, from_unit, to_unit)

        # Convert the converted_temp to a float for comparison
        converted_temp_float = float(converted_temp)

        if converted_temp_float < 0:
            # Set the converted_temp to its absolute value
            converted_temp = abs(converted_temp_float)
        else:
            error_text.value = ""  # Clear any previous error message

        # Display the original converted temperature value
        output_text.value = str(converted_temp_float)
        
        # Call function to convert number to words
        number_converted = convert_number_to_words(converted_temp)
        
        # Check if the converted temperature has fractional parts other than .00
        if converted_temp_float % 1 != 0 and str(converted_temp_float % 1) != ".00":
            error_text.value = "Error: SOAP cannot convert fractional values. Temperature rounded down."
        
        if converted_temp_float < 0:
            # Display negative value with "Negative" prefix
            output_number.value = "Negative " + number_converted
        else:
            output_number.value = number_converted
                
    except Exception as e:
        error_text.value = str(e)

# Function to open a web app in a separate window
def open_web_app():
    webbrowser.open_new_tab("http://localhost:8890/notebooks/temp_converter.ipynb")
        
open_app_button = widgets.Button(description="Open Web App in Separate Window")
open_app_button.on_click(lambda b: open_web_app())

# Register the event handler for the convert button
convert_button.on_click(convert_button_clicked)

# Display the widgets
display(temperature_input, from_unit_dropdown, to_unit_dropdown, convert_button, output_text, output_number, error_text, open_app_button)

# WSDL URLs for SOAP services
tempconvert_wsdl = "https://www.w3schools.com/xml/tempconvert.asmx?WSDL"
numberconversion_wsdl = "https://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL"

# Create clients for both SOAP services
tempconvert_client = Client(tempconvert_wsdl)
numberconversion_client = Client(numberconversion_wsdl)

# Function to convert temperature using SOAP service
def convert_temperature(temp, from_unit, to_unit):
    # Call the appropriate operation based on the units
    if from_unit.lower() == 'degreecelsius' and to_unit.lower() == 'degreefahrenheit':
        result = tempconvert_client.service.CelsiusToFahrenheit(temp)
    elif from_unit.lower() == 'degreefahrenheit' and to_unit.lower() == 'degreecelsius':
        result = tempconvert_client.service.FahrenheitToCelsius(temp)
    else:
        raise ValueError(f"Invalid temperature conversion: {from_unit} to {to_unit}. Please try again.")

    return result

# Function to convert number into words using SOAP service
def convert_number_to_words(number):
    result = numberconversion_client.service.NumberToWords(number)
    return result




