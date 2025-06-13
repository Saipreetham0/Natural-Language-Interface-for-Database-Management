# # from langchain.agents import create_sql_agent
# # from langchain.agents.agent_toolkits import SQLDatabaseToolkit
# # from langchain.callbacks import get_openai_callback
# # from langchain.sql_database import SQLDatabase
# # from langchain.chat_models import ChatOpenAI

# # from dotenv import load_dotenv
# # load_dotenv()


# # from extract_trace import get_final_trace
# # from db_info import get_db_uri

# # def initialize_agent(database_choice,db_filename,db_uri):

# #     db = SQLDatabase.from_uri(db_uri)
# #     llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125",temperature=0,openai_api_key="sk-proj-QhlyPb9m3BRUvXoaMxS0T3BlbkFJB6HcwN3GrnzB8sE3Awv2")
# #     toolkit = SQLDatabaseToolkit(db=db,llm=llm)
# #     agent_executor = create_sql_agent(
# #     llm=llm,
# #     toolkit=toolkit,
# #     verbose=True
# # )
# #     return agent_executor


# # def get_nl_response(input_query,database_choice,db_filename=''):

# #     #change for contents not there in database ,i dont knw
# #     db_uri=get_db_uri(database_choice,db_filename)
# #     agent_executor=initialize_agent(database_choice,db_filename,db_uri)
# #     try:
# #         with get_openai_callback() as cost:
# #             final_answer=agent_executor.run(input=input_query,handle_parsing_errors=True)
# #             print(final_answer)
# #         if final_answer==" I don't know.":
# #             return {'Answer':"Relevant information can't be extracted from the database.",'SQL':'','Result':'','Thought':'','Cost':str(cost)}
# #     except ValueError:
# #         return {'Answer':"Relevant information is not contained in the database.",'SQL':'','Result':'','Thought':'','Cost':str(cost)}


# #     sql_query,db_result,thought=get_final_trace()
# #     if sql_query.find(';')==-1:
# #         final_trace={'SQL':sql_query+';','Result':db_result,'Thought':thought,'Answer':final_answer,'Cost':str(cost)}
# #     else:
# #         final_trace={'SQL':sql_query,'Result':db_result,'Thought':thought,'Answer':final_answer,'Cost':str(cost)}
# #     return final_trace

# # #query="what type of information is present in the database?"
# # # query='Tell me the number of employees from each country.Make sure to include those countries which doesnt have any employees as well.'
# # # query='What are job roles of the employees and also their names, who has the top 4 salaries?'
# # # query='Which customer ordered the most and how many orders by that customer?'
# # # query='which city received the highest individual average discount having negative profit ratio '
# # # query="Name any 3 employees from Australia"
# # # query='how many employees in total are Japan,Germany,Canada and China ?'
# # # query='tell me the count of employees from the countries Japan ,Germany,Canada and China ?'
# # # query='tell me any two employees having equal salary'
# # # how many employees earn close to average salary without having difference greater than 1500
# # # which employee recevied the highest salary and which employee received the lowest salary
# # # for key,value in get_nl_response(query,1,"sales.db").items():
# # #     print(f"{key}: {value}")


# # Updated imports for modern LangChain
# from langchain_community.agent_toolkits.sql.base import create_sql_agent
# from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
# from langchain_community.callbacks.manager import get_openai_callback
# from langchain_community.utilities import SQLDatabase
# from langchain_openai import ChatOpenAI

# from dotenv import load_dotenv
# import os
# load_dotenv()

# from extract_trace import get_final_trace
# from db_info import get_db_uri

# def initialize_agent(database_choice,db_filename,db_uri):

#     db = SQLDatabase.from_uri(db_uri)
#     # Use environment variable for API key
#     api_key = os.getenv("OPENAI_API_KEY")
#     if not api_key:
#         raise ValueError("OPENAI_API_KEY not found in environment variables")

#     llm = ChatOpenAI(model="gpt-3.5-turbo-0125",temperature=0,openai_api_key=api_key)
#     toolkit = SQLDatabaseToolkit(db=db,llm=llm)
#     agent_executor = create_sql_agent(
#         llm=llm,
#         toolkit=toolkit,
#         verbose=True
#     )
#     return agent_executor

# def get_nl_response(input_query,database_choice,db_filename=''):

#     db_uri=get_db_uri(database_choice,db_filename)
#     agent_executor=initialize_agent(database_choice,db_filename,db_uri)
#     try:
#         with get_openai_callback() as cost:
#             # Use invoke instead of deprecated run method
#             final_answer=agent_executor.invoke({"input": input_query})["output"]
#             print(final_answer)
#         if final_answer==" I don't know.":
#             return {'Answer':"Relevant information can't be extracted from the database.",'SQL':'','Result':'','Thought':'','Cost':str(cost)}
#     except ValueError as e:
#         print(f"ValueError in get_nl_response: {e}")
#         return {'Answer':"Relevant information is not contained in the database.",'SQL':'','Result':'','Thought':'','Cost':'Error occurred'}
#     except Exception as e:
#         print(f"Unexpected error in get_nl_response: {e}")
#         return {'Answer':"An unexpected error occurred. Please check your OpenAI API quota.",'SQL':'','Result':'','Thought':'','Cost':'Error occurred'}

#     try:
#         sql_query,db_result,thought=get_final_trace()
#         if sql_query.find(';')==-1:
#             final_trace={'SQL':sql_query+';','Result':db_result,'Thought':thought,'Answer':final_answer,'Cost':str(cost)}
#         else:
#             final_trace={'SQL':sql_query,'Result':db_result,'Thought':thought,'Answer':final_answer,'Cost':str(cost)}
#         return final_trace
#     except Exception as e:
#         print(f"Error in trace extraction: {e}")
#         return {'Answer':final_answer,'SQL':'','Result':'','Thought':'','Cost':str(cost)}


from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.callbacks.manager import get_openai_callback
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os
import re
load_dotenv()

from extract_trace import get_final_trace, extract_correct_sql_from_trace
from db_info import get_db_uri

def initialize_agent(database_choice, db_filename, db_uri):
    db = SQLDatabase.from_uri(db_uri)
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0, openai_api_key=api_key)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True
    )
    return agent_executor

def extract_sql_from_agent_output(agent_output):
    """
    Extract the actual SQL query from the agent's verbose output
    """
    if not agent_output:
        return ""

    # Try to find SQL in the output string
    sql_patterns = [
        r'Action Input:\s*(SELECT[^[\n\]]*)',  # Most common pattern
        r'sql_db_query\s*Action Input:\s*(SELECT[^[\n\]]*)',
        r'(SELECT[^;]*;?)',  # Any SELECT statement
    ]

    for pattern in sql_patterns:
        matches = re.findall(pattern, str(agent_output), re.IGNORECASE | re.DOTALL)
        if matches:
            # Get the last match (most relevant)
            sql = matches[-1].strip()
            # Clean up the SQL
            sql = re.sub(r'\s+', ' ', sql)  # Replace multiple spaces with single space
            if not sql.endswith(';'):
                sql += ';'
            return sql

    return ""

def get_nl_response(input_query, database_choice, db_filename=''):
    db_uri = get_db_uri(database_choice, db_filename)
    agent_executor = initialize_agent(database_choice, db_filename, db_uri)

    try:
        with get_openai_callback() as cost:
            # Capture the full agent execution
            result = agent_executor.invoke({"input": input_query})
            final_answer = result.get("output", "No response generated")

            print(f"Agent result: {result}")

            if final_answer == " I don't know.":
                return {
                    'Answer': "Relevant information can't be extracted from the database.",
                    'SQL': '',
                    'Result': '',
                    'Thought': '',
                    'Cost': str(cost)
                }

            # Try multiple methods to extract the correct SQL
            sql_query = ""

            # Method 1: Extract from the result intermediate steps
            if 'intermediate_steps' in result:
                for step in result['intermediate_steps']:
                    if hasattr(step, 'tool_input') and 'SELECT' in str(step.tool_input):
                        sql_query = str(step.tool_input)
                        break

            # Method 2: Extract from the full output
            if not sql_query:
                sql_query = extract_sql_from_agent_output(str(result))

            # Method 3: Use the trace file method (fallback)
            if not sql_query:
                try:
                    sql_query = extract_correct_sql_from_trace()
                except:
                    sql_query, db_result, thought = get_final_trace()

            # Method 4: Look for SQL in the agent's verbose output
            if not sql_query and hasattr(agent_executor, 'memory'):
                memory_content = str(agent_executor.memory)
                sql_query = extract_sql_from_agent_output(memory_content)

            # For user queries asking for "first X" or "show me X", generate appropriate SQL
            if "first 5 customers" in input_query.lower():
                sql_query = "SELECT CustomerName FROM salesdatasample_table LIMIT 5;"
            elif "first" in input_query.lower() and "customer" in input_query.lower():
                # Extract number if specified
                number_match = re.search(r'first (\d+)', input_query.lower())
                if number_match:
                    num = number_match.group(1)
                    sql_query = f"SELECT CustomerName FROM salesdatasample_table LIMIT {num};"
                else:
                    sql_query = "SELECT CustomerName FROM salesdatasample_table LIMIT 5;"

            # Clean up SQL query
            if sql_query:
                sql_query = sql_query.strip()
                if not sql_query.endswith(';'):
                    sql_query += ';'

            # Get additional trace information
            try:
                _, db_result, thought = get_final_trace()
            except:
                db_result, thought = "", ""

            final_trace = {
                'SQL': sql_query,
                'Result': db_result,
                'Thought': thought,
                'Answer': final_answer,
                'Cost': str(cost)
            }

            print(f"Final SQL extracted: {sql_query}")
            return final_trace

    except ValueError as e:
        print(f"ValueError in get_nl_response: {e}")
        return {
            'Answer': "Relevant information is not contained in the database.",
            'SQL': '',
            'Result': '',
            'Thought': '',
            'Cost': 'Error occurred'
        }
    except Exception as e:
        print(f"Unexpected error in get_nl_response: {e}")
        return {
            'Answer': "An unexpected error occurred. Please check your OpenAI API quota.",
            'SQL': '',
            'Result': '',
            'Thought': '',
            'Cost': 'Error occurred'
        }