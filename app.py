import streamlit as st
from app.crew import create_financial_trading_crew
from app.utils import set_environment_variables

# Set environment variables at the start of the application
set_environment_variables()

def main():
    st.title("Financial Trading Analysis")

    # Create form inputs
    stock_selection = st.text_input("Cryptocurrency Pair:")
    initial_capital = st.number_input("Initial Capital:", min_value=0)
    risk_tolerance = st.selectbox("Risk Tolerance:", ["Low", "Medium", "High"])
    trading_strategy_preference = st.selectbox("Trading Strategy Preference:", ["Short Term", "Medium Term", "Long Term"])
    llm_type = st.selectbox("Select LLM:", ["openai", "gemini"])
    news_impact_consideration = st.checkbox("Consider News Impact")

    if st.button("Analyze"):
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
        st.markdown(result)

if __name__ == "__main__":
    main()