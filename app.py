import streamlit as st
from app.crew import create_financial_trading_crew
from app.utils import set_environment_variables

# Set environment variables at the start of the application
set_environment_variables()

def main():
    st.set_page_config(layout="wide")  # Use wide layout for better column separation
    st.title("Financial Trading Analysis")

    # Create two columns with 30% for left and 70% for right
    left_column, right_column = st.columns([3, 7])

    # Left column for inputs
    with left_column:
        st.header("Input Parameters")
        stock_selection = st.text_input("Cryptocurrency Pair:")
        initial_capital = st.number_input("Initial Capital:", min_value=0)
        risk_tolerance = st.selectbox("Risk Tolerance:", ["Low", "Medium", "High"])
        trading_strategy_preference = st.selectbox("Trading Strategy Preference:", ["Short Term", "Medium Term", "Long Term"])
        llm_type = st.selectbox("Select LLM:", ["openai", "gemini"])
        news_impact_consideration = st.checkbox("Consider News Impact")

        analyze_button = st.button("Analyze")

    # Right column for output
    with right_column:
        st.header("Analysis Result")
        output_container = st.empty()

    if analyze_button:
        inputs = {
            'stock_selection': stock_selection,
            'initial_capital': initial_capital,
            'risk_tolerance': risk_tolerance,
            'trading_strategy_preference': trading_strategy_preference,
            'news_impact_consideration': news_impact_consideration,
            'llm_type': llm_type
        }
        crew = create_financial_trading_crew(llm_type=inputs['llm_type'])
        result = crew.kickoff(inputs=inputs)
        
        # Display the result in the right column
        with output_container.container():
            st.markdown(result)

    # Add custom CSS to make the right column scrollable
    st.markdown("""
        <style>
        .stApp [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
            height: calc(100vh - 100px);
            overflow-y: auto;
        }
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()