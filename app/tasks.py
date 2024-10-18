from crewai import Task

def create_data_analysis_task(agent):
    return Task(
        description=(
            "Continuously monitor and analyze market data for "
            "the selected cryptocurrency ({stock_selection}). "
            "Use statistical modeling and machine learning to "
            "identify trends and predict market movements."
        ),
        expected_output=(
            "Insights and alerts about significant market "
            "opportunities or threats for {stock_selection}. Specifically "
            "add relevant headings for key insights and use bullet points where possible."        
        ),
        agent=agent,
    )

def create_strategy_development_task(agent):
    return Task(
        description=(
            "Develop and refine trading strategies based on "
            "the insights from the Data Analyst and "
            "user-defined risk tolerance ({risk_tolerance}). "
            "Consider trading preferences ({trading_strategy_preference})."
        ),
        expected_output=(
            "A set of potential trading strategies for {stock_selection} "
            "that align with the user's risk tolerance."
        ),
        agent=agent,
    )

def create_execution_planning_task(agent):
    return Task(
        description=(
            "Analyze approved trading strategies to determine the "
            "best execution methods for {stock_selection}, "
            "considering current market conditions and optimal pricing."
        ),
        expected_output=(
            "Detailed execution plans suggesting how and when to "
            "execute trades for {stock_selection}. Use bullet points where possible."
        ),
        agent=agent,
    )

def create_risk_assessment_task(agent):
    return Task(
        description=(
            "Evaluate the risks associated with the proposed trading "
            "strategies and execution plans for {stock_selection}. "
            "Provide a detailed analysis of potential risks "
            "and suggest mitigation strategies."
        ),
        expected_output=(
            "A comprehensive risk analysis report detailing potential "
            "risks and mitigation recommendations for {stock_selection}."
        ),
        agent=agent,
    )