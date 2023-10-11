import zeep
from zeep import Client

tempconvert_wsdl = "https://www.w3schools.com/xml/tempconvert.asmx?WSDL"
numberconversion_wsdl = "https://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL"

tempconvert_client = Client(tempconvert_wsdl)
numberconversion_client = Client(numberconversion_wsdl)

def convert_temperature(temp, from_unit, to_unit):
    if from_unit.lower() == 'degreecelsius' and to_unit.lower() == 'degreefahrenheit':
        result = tempconvert_client.service.CelsiusToFahrenheit(temp)
    elif from_unit.lower() == 'degreefahrenheit' and to_unit.lower() == 'degreecelsius':
        result = tempconvert_client.service.FahrenheitToCelsius(temp)
    else:
        raise ValueError(f"Invalid temperature conversion: {from_unit} to {to_unit}. Please try again.")
    return float(result)

def convert_number_to_words(number):
    result = numberconversion_client.service.NumberToWords(number)
    return result
