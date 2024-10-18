from crewai import Crew, Process
from langchain_openai import ChatOpenAI
import sys
import os
sys.path.append('../')
# from llm_adapters.gemini_adapter import GeminiChatAdapter

from llm_adapters.gemini_adapter import GeminiChatAdapter

from .agents import (
    create_data_analyst_agent,
    create_trading_strategy_agent,
    create_execution_agent,
    create_risk_management_agent
)
from .tasks import (
    create_data_analysis_task,
    create_strategy_development_task,
    create_execution_planning_task,
    create_risk_assessment_task
)

def create_financial_trading_crew(llm_type='openai'):
    data_analyst_agent = create_data_analyst_agent()
    trading_strategy_agent = create_trading_strategy_agent()
    execution_agent = create_execution_agent()
    risk_management_agent = create_risk_management_agent()

    data_analysis_task = create_data_analysis_task(data_analyst_agent)
    strategy_development_task = create_strategy_development_task(trading_strategy_agent)
    execution_planning_task = create_execution_planning_task(execution_agent)
    risk_assessment_task = create_risk_assessment_task(risk_management_agent)

    if llm_type == 'openai':
        # llm_adapter = OpenAIAdapter()
        llm_adapter = ChatOpenAI(model="gpt-4o", temperature=0.7)
    elif llm_type == 'gemini':
        llm_adapter = GeminiChatAdapter()  # Instantiate the Gemini adapter

    return Crew(
        agents=[data_analyst_agent, trading_strategy_agent, execution_agent, risk_management_agent],
        tasks=[data_analysis_task, strategy_development_task, execution_planning_task, risk_assessment_task],
        manager_llm=llm_adapter,
        process=Process.hierarchical,
        verbose=True
    )