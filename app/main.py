from flask import Flask, render_template, request
import os
from .crew import create_financial_trading_crew
from .utils import set_environment_variables

# Set environment variables at the start of the application
set_environment_variables()

# Create the Flask app with the correct template folder
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        inputs = {
            'stock_selection': request.form['stock_selection'],
            'initial_capital': request.form['initial_capital'],
            'risk_tolerance': request.form['risk_tolerance'],
            'trading_strategy_preference': request.form['trading_strategy_preference'],
            'news_impact_consideration': request.form.get('news_impact_consideration') == 'on'
        }
        crew = create_financial_trading_crew()
        result = crew.kickoff(inputs=inputs)
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)