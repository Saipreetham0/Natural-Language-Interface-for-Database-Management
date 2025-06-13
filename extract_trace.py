# import re

# def extract_action_input_and_observation(trace_file):
#     with open(trace_file, 'r') as file:
#         content = file.read()
#         sql_text="Action Input:"
#     sql_index=content.rfind(sql_text)
#     observation_text='Observation:'
#     obs_index=content.rfind(observation_text)
#     thought_text='Thought:'
#     thought_index=content.rfind(thought_text)
#     ans_text="Final Answer:"
#     ans_index=content.rfind(ans_text)
#     sqlquery,observation,Thought,Final_answer="","","",""

#     for i in range(sql_index+len(sql_text),obs_index):
#         sqlquery=sqlquery+content[i]

#     for i in range(obs_index+len(observation_text),thought_index):
#         observation=observation+content[i]

#     for i in range(thought_index+len(thought_text),ans_index):
#         Thought=Thought+content[i]
#     l=[]
#     l=[i.replace('\n',' ') for i in [sqlquery,observation,Thought]]

#     return l



# def get_final_trace(full_trace=False):

#     trace_file_path = "fulltrace.txt"
#     if full_trace:
#         fulltrace=extract_action_input_and_observation(trace_file_path,full_trace=True)
#         return fulltrace
#     action_input, observation, thought = extract_action_input_and_observation(trace_file_path)

#     return action_input,observation,thought

# # print(get_final_trace())


import re

def extract_action_input_and_observation(trace_file):
    with open(trace_file, 'r') as file:
        content = file.read()

    # Extract all SQL queries from the trace
    sql_queries = []

    # Find all Action Input sections that contain SQL
    action_input_pattern = r'Action Input:\s*(SELECT.*?)\s*(?=\[|\n|Observation:)'
    matches = re.finditer(action_input_pattern, content, re.DOTALL | re.IGNORECASE)

    for match in matches:
        sql_query = match.group(1).strip()
        # Clean up the SQL query
        sql_query = sql_query.replace('\n', ' ').strip()
        if sql_query and sql_query.upper().startswith('SELECT'):
            sql_queries.append(sql_query)

    # Get the LAST SQL query (most relevant one)
    final_sql = sql_queries[-1] if sql_queries else ""

    # Extract observation and thought as before
    sql_text = "Action Input:"
    sql_index = content.rfind(sql_text)
    observation_text = 'Observation:'
    obs_index = content.rfind(observation_text)
    thought_text = 'Thought:'
    thought_index = content.rfind(thought_text)
    ans_text = "Final Answer:"
    ans_index = content.rfind(ans_text)

    observation, thought = "", ""

    if obs_index != -1 and thought_index != -1:
        for i in range(obs_index + len(observation_text), thought_index):
            observation += content[i]

    if thought_index != -1 and ans_index != -1:
        for i in range(thought_index + len(thought_text), ans_index):
            thought += content[i]

    # Clean up
    observation = observation.replace('\n', ' ').strip()
    thought = thought.replace('\n', ' ').strip()

    return final_sql, observation, thought

def get_final_trace(full_trace=False):
    trace_file_path = "fulltrace.txt"

    if full_trace:
        with open(trace_file_path, 'r') as file:
            return file.read()

    try:
        action_input, observation, thought = extract_action_input_and_observation(trace_file_path)
        return action_input, observation, thought
    except Exception as e:
        print(f"Error extracting trace: {e}")
        return "", "", ""

def extract_correct_sql_from_trace():
    """
    Extract the correct SQL query that matches the user's intent
    """
    try:
        with open("fulltrace.txt", 'r') as file:
            content = file.read()

        # Look for the SQL query that was actually executed and returned results
        # Pattern: Action Input: SELECT ... followed by observation with results
        pattern = r'Action Input:\s*(SELECT[^[\n]*)\s*\[.*?\]'
        matches = re.finditer(pattern, content, re.DOTALL | re.IGNORECASE)

        executed_queries = []
        for match in matches:
            sql = match.group(1).strip().replace('\n', ' ')
            executed_queries.append(sql)

        # Return the query that was actually executed (usually the last one with results)
        if executed_queries:
            return executed_queries[-1]

        # Fallback to the original method
        sql, _, _ = get_final_trace()
        return sql

    except Exception as e:
        print(f"Error extracting correct SQL: {e}")
        return ""
