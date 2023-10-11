from flask import render_template, request, redirect, url_for
from app import create_app
from .soap_services import convert_temperature, convert_number_to_words

app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    converted_temp = None
    number_converted = None
    
    if request.method == 'POST':
        try:
            temp = float(request.form['temperature'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            converted_temp = convert_temperature(temp, from_unit, to_unit)
            number_converted = convert_number_to_words(abs(int(converted_temp)))
            if converted_temp < 0:
                number_converted = "Negative " + number_converted
        except Exception as e:
            error = str(e)
    
    return render_template('index.html', converted_temp=converted_temp, number_converted=number_converted, error=error)
