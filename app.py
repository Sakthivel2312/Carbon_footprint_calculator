from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        # Get form data (monthly values)
        energy = float(request.form['energy'])
        fuel = float(request.form['fuel'])
        methane = float(request.form['methane'])
        transportation = float(request.form['transportation'])
        commute = float(request.form['commute'])
        waste = float(request.form['waste'])
        water = float(request.form['water'])
        land = float(request.form['land'])

        # Carbon footprint calculations for each category (monthly values)
        energy_footprint = energy * 0.92  # Example factor for energy consumption
        fuel_footprint = fuel * 2.31  # Example factor for fuel combustion
        methane_footprint = methane * 25  # Methane emissions factor
        transportation_footprint = transportation * 1.45  # Transportation emissions
        commute_footprint = commute * 0.78  # Commute emissions
        waste_footprint = waste * 0.9  # Waste emissions
        water_footprint = water * 0.0000065  # Water usage emissions
        land_footprint = land * 0.000004  # Land use emissions

        # Total carbon footprint for one month
        monthly_footprint = (energy_footprint + fuel_footprint + methane_footprint +
                             transportation_footprint + commute_footprint + waste_footprint +
                             water_footprint + land_footprint)

        # Total carbon footprint for one year (multiply each monthly value by 12)
        yearly_footprint = monthly_footprint * 12

        # Render result page with calculated values (monthly and yearly totals)
        return render_template(
            'result.html',
            total_footprint=yearly_footprint,
            energy_monthly=energy_footprint,
            energy_yearly=energy_footprint * 12,
            fuel_monthly=fuel_footprint,
            fuel_yearly=fuel_footprint * 12,
            methane_monthly=methane_footprint,
            methane_yearly=methane_footprint * 12,
            transportation_monthly=transportation_footprint,
            transportation_yearly=transportation_footprint * 12,
            commute_monthly=commute_footprint,
            commute_yearly=commute_footprint * 12,
            waste_monthly=waste_footprint,
            waste_yearly=waste_footprint * 12,
            water_monthly=water_footprint,
            water_yearly=water_footprint * 12,
            land_monthly=land_footprint,
            land_yearly=land_footprint * 12
        )

    # If GET request, just show the form
    return render_template('calculate.html')

if __name__ == '__main__':
    app.run(debug=True)
