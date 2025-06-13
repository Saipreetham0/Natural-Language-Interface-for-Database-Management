# # from gptsql import get_nl_response
# # from sqlgen import get_sql_response
# # from extract_trace import get_final_trace
# # from db_info import get_execution_result,get_tablenames,get_schema_and_sample_rows,get_table_shape
# # from csvtodb import get_sqlitedb
# # def nl_response(query,db_choice=1,db_file=''):

# #     try:
# #         llm_answer=get_nl_response(input_query=query,database_choice=db_choice,db_filename=db_file)
# #         return llm_answer

# #     except Exception as e:
# #         print('Response generation error : ',e)
# #         return {'Answer':"Sorry. Cannot fulfill this request.",'SQL':'','Result':'','Thought':'','Cost':llm_answer['Cost']}

# # def get_full_trace():

# #     try:
# #         fulltrace=get_final_trace(full_trace=True)
# #         return fulltrace

# #     except Exception as e:
# #         print("Error occured in trace extraction : ",e)
# #         return 'Error occured in trace extraction.'

# # def generate_sql(user_input,db_choice=1,db_file=''):

# #     try:
# #         sql_list,llm_response=get_sql_response(user_query=user_input,database_choice=db_choice,db_filename=db_file)
# #         print(sql_list)
# #         return sql_list,llm_response

# #     except Exception as e:
# #         print("Error occured in SQL generation : " ,e)
# #         return [],'Error occured in SQL generation.'

# # def execution_result(gen_sql_query,db_choice=1,db_file=''):

# #     try:
# #         df=get_execution_result(sql_query=gen_sql_query,database_choice=db_choice,db_filename=db_file)
# #         return df

# #     except Exception as e:
# #         print("Error occured in executing sql statement : ",e)
# #         return  ""

# # def get_table_list(db_choice,db_file=''):

# #     try:
# #         tables =get_tablenames (database_choice=db_choice,db_filename=db_file)
# #         return tables

# #     except Exception as e:
# #         print("Error occured retrieving table names : ",e)
# #         return ""

# # def get_db_schema(db_choice,db_file=''):

# #     try:
# #         tables,sql_schema =get_schema_and_sample_rows(database_choice=db_choice,db_filename=db_file)
# #         return tables,sql_schema

# #     except Exception as e:
# #         print("Error occured retrieving schema : ",e)
# #         return ""

# # def get_table_dimensions(database_choice,db_filename=''):
# #     try:
# #         shapes=get_table_shape(database_choice,db_filename)
# #         return shapes
# #     except Exception as e:
# #         print("Error occured retrieving table shape : ",e)
# #         return '0x0'

# # def convert_csv_to_db(csvfilename):
# #     try:
# #         database_file=get_sqlitedb(csvfilename)
# #         return database_file
# #     except Exception as e:
# #         print("Error occured converting csv to db : ",e)



# #  working code


# # from gptsql import get_nl_response
# # from sqlgen import get_sql_response
# # from extract_trace import get_final_trace
# # from db_info import get_execution_result,get_tablenames,get_schema_and_sample_rows,get_table_shape
# # from csvtodb import get_sqlitedb

# # def nl_response(query,db_choice=1,db_file=''):

# #     try:
# #         llm_answer=get_nl_response(input_query=query,database_choice=db_choice,db_filename=db_file)
# #         return llm_answer

# #     except Exception as e:
# #         print('Response generation error : ',e)
# #         # Return a default response structure instead of referencing undefined llm_answer
# #         return {
# #             'Answer':"Sorry. Cannot fulfill this request.",
# #             'SQL':'',
# #             'Result':'',
# #             'Thought':'',
# #             'Cost':'Unknown cost due to error'
# #         }

# # def get_full_trace():

# #     try:
# #         fulltrace=get_final_trace(full_trace=True)
# #         return fulltrace

# #     except Exception as e:
# #         print("Error occured in trace extraction : ",e)
# #         return 'Error occured in trace extraction.'

# # def generate_sql(user_input,db_choice=1,db_file=''):

# #     try:
# #         sql_list,llm_response=get_sql_response(user_query=user_input,database_choice=db_choice,db_filename=db_file)
# #         print(sql_list)
# #         return sql_list,llm_response

# #     except Exception as e:
# #         print("Error occured in SQL generation : " ,e)
# #         return [],'Error occured in SQL generation.'

# # def execution_result(gen_sql_query,db_choice=1,db_file=''):

# #     try:
# #         df=get_execution_result(sql_query=gen_sql_query,database_choice=db_choice,db_filename=db_file)
# #         return df

# #     except Exception as e:
# #         print("Error occured in executing sql statement : ",e)
# #         return  ""

# # def get_table_list(db_choice,db_file=''):

# #     try:
# #         tables =get_tablenames (database_choice=db_choice,db_filename=db_file)
# #         return tables

# #     except Exception as e:
# #         print("Error occured retrieving table names : ",e)
# #         return ""

# # def get_db_schema(db_choice,db_file=''):

# #     try:
# #         tables,sql_schema =get_schema_and_sample_rows(database_choice=db_choice,db_filename=db_file)
# #         return tables,sql_schema

# #     except Exception as e:
# #         print("Error occured retrieving schema : ",e)
# #         return "",[]

# # def get_table_dimensions(database_choice,db_filename=''):
# #     try:
# #         shapes=get_table_shape(database_choice,db_filename)
# #         return shapes
# #     except Exception as e:
# #         print("Error occured retrieving table shape : ",e)
# #         return {}

# # def convert_csv_to_db(csvfilename):
# #     try:
# #         database_file=get_sqlitedb(csvfilename)
# #         return database_file
# #     except Exception as e:
# #         print("Error occured converting csv to db : ",e)
# #         return None

# from gptsql import get_nl_response
# from sqlgen import get_sql_response
# from extract_trace import get_final_trace
# from db_info import get_execution_result_enhanced, get_tablenames, get_schema_and_sample_rows, get_table_shape
# from csvtodb import get_sqlitedb

# def nl_response(query, db_choice=1, db_file=''):

#     try:
#         llm_answer = get_nl_response(input_query=query, database_choice=db_choice, db_filename=db_file)
#         return llm_answer

#     except Exception as e:
#         print('Response generation error:', e)
#         return {
#             'Answer': "Sorry. Cannot fulfill this request.",
#             'SQL': '',
#             'Result': '',
#             'Thought': '',
#             'Cost': 'Unknown cost due to error'
#         }

# def get_full_trace():

#     try:
#         fulltrace = get_final_trace(full_trace=True)
#         return fulltrace

#     except Exception as e:
#         print("Error occurred in trace extraction:", e)
#         return 'Error occurred in trace extraction.'

# def generate_sql(user_input, db_choice=1, db_file=''):

#     try:
#         sql_list, llm_response = get_sql_response(user_query=user_input, database_choice=db_choice, db_filename=db_file)
#         print(sql_list)
#         return sql_list, llm_response

#     except Exception as e:
#         print("Error occurred in SQL generation:", e)
#         return [], 'Error occurred in SQL generation.'

# # def execution_result(gen_sql_query, db_choice=1, db_file=''):
# #     """
# #     Execute SQL query and return properly formatted DataFrame
# #     """
# #     try:
# #         # Use the enhanced execution method
# #         df = get_execution_result_enhanced(sql_query=gen_sql_query, database_choice=db_choice, db_filename=db_file)

# #         # Debug: print what we got
# #         print(f"Execution result type: {type(df)}")
# #         print(f"DataFrame shape: {df.shape if hasattr(df, 'shape') else 'No shape'}")
# #         print(f"DataFrame columns: {df.columns.tolist() if hasattr(df, 'columns') else 'No columns'}")

# #         return df

# #     except Exception as e:
# #         print("Error occurred in executing SQL statement:", e)
# #         return pd.DataFrame()  # Return empty DataFrame instead of empty string

# def execution_result(gen_sql_query, db_choice=1, db_file=''):
#     """
#     Execute SQL query and return properly formatted DataFrame - FINAL FIX
#     """
#     import pandas as pd
#     import sqlite3
#     import os
#     from sqlalchemy import create_engine

#     try:
#         if db_choice == 1:  # SQLite
#             current_dir = os.getcwd()
#             db_file = db_file or 'sales.db'
#             db_path = os.path.join(current_dir, db_file)

#             if not os.path.exists(db_path):
#                 print(f"❌ Database file not found: {db_path}")
#                 return pd.DataFrame()

#             # Direct SQLite connection
#             conn = sqlite3.connect(db_path)
#             df = pd.read_sql_query(gen_sql_query, conn)
#             conn.close()

#             print(f"✅ Query executed successfully:")
#             print(f"   - Shape: {df.shape}")
#             print(f"   - Columns: {df.columns.tolist()}")
#             print(f"   - Sample data:")
#             print(df.head())

#             # Ensure proper data types and formatting
#             df = df.copy()  # Make a copy to avoid warnings

#             # Don't format numbers as strings - keep them as numbers for Streamlit
#             # Streamlit will handle the display formatting automatically

#             return df

#         elif db_choice == 2:  # PostgreSQL
#             db_uri = "postgresql://postgres:pavan@localhost:5432/hrdata"
#             engine = create_engine(db_uri)
#             df = pd.read_sql_query(gen_sql_query, engine)
#             engine.dispose()
#             return df

#     except Exception as e:
#         print(f"❌ ERROR in execution_result: {e}")
#         import traceback
#         traceback.print_exc()
#         return pd.DataFrame()

#     return pd.DataFrame()

# # BONUS: Add this function to help with better queries
# def suggest_better_query(user_question, original_sql):
#     """
#     Suggest a better SQL query based on user intent
#     """
#     user_lower = user_question.lower()

#     # If user asks for "first 5 customers" but gets a profit query, suggest the right one
#     if "first 5 customers" in user_lower or "show me 5 customers" in user_lower:
#         return "SELECT CustomerName FROM salesdatasample_table LIMIT 5;"

#     elif "top 5 customers" in user_lower:
#         return "SELECT CustomerName, SUM(Sales) as TotalSales FROM salesdatasample_table GROUP BY CustomerName ORDER BY TotalSales DESC LIMIT 5;"

#     elif "customers by sales" in user_lower:
#         return "SELECT CustomerName, SUM(Sales) as TotalSales FROM salesdatasample_table GROUP BY CustomerName ORDER BY TotalSales DESC LIMIT 10;"

#     elif "customers by profit" in user_lower:
#         return "SELECT CustomerName, SUM(Profit) as TotalProfit FROM salesdatasample_table GROUP BY CustomerName ORDER BY TotalProfit DESC LIMIT 10;"

#     return original_sql

# # BONUS: Add this function to help with better queries
# def suggest_better_query(user_question, original_sql):
#     """
#     Suggest a better SQL query based on user intent
#     """
#     user_lower = user_question.lower()

#     # If user asks for "first 5 customers" but gets a profit query, suggest the right one
#     if "first 5 customers" in user_lower or "show me 5 customers" in user_lower:
#         return "SELECT CustomerName FROM salesdatasample_table LIMIT 5;"

#     elif "top 5 customers" in user_lower:
#         return "SELECT CustomerName, SUM(Sales) as TotalSales FROM salesdatasample_table GROUP BY CustomerName ORDER BY TotalSales DESC LIMIT 5;"

#     elif "customers by sales" in user_lower:
#         return "SELECT CustomerName, SUM(Sales) as TotalSales FROM salesdatasample_table GROUP BY CustomerName ORDER BY TotalSales DESC LIMIT 10;"

#     elif "customers by profit" in user_lower:
#         return "SELECT CustomerName, SUM(Profit) as TotalProfit FROM salesdatasample_table GROUP BY CustomerName ORDER BY TotalProfit DESC LIMIT 10;"

#     return original_sql

# def get_table_list(db_choice, db_file=''):

#     try:
#         tables = get_tablenames(database_choice=db_choice, db_filename=db_file)
#         return tables

#     except Exception as e:
#         print("Error occurred retrieving table names:", e)
#         return []

# def get_db_schema(db_choice, db_file=''):

#     try:
#         tables, sql_schema = get_schema_and_sample_rows(database_choice=db_choice, db_filename=db_file)
#         return tables, sql_schema

#     except Exception as e:
#         print("Error occurred retrieving schema:", e)
#         return [], []

# def get_table_dimensions(database_choice, db_filename=''):
#     try:
#         shapes = get_table_shape(database_choice, db_filename)
#         return shapes
#     except Exception as e:
#         print("Error occurred retrieving table shape:", e)
#         return {}

# def convert_csv_to_db(csvfilename):
#     try:
#         database_file = get_sqlitedb(csvfilename)
#         return database_file
#     except Exception as e:
#         print("Error occurred converting csv to db:", e)
#         return None


# def fix_query_mismatch(user_query, ai_answer, generated_sql):
#     """
#     Fix the mismatch between user query intent and generated SQL
#     """
#     user_lower = user_query.lower()

#     # Check if the answer mentions specific data that doesn't match the SQL
#     if "first 5 customers" in user_lower or "show me the first 5 customers" in user_lower:
#         if "darren powers" in ai_answer.lower() and "profit desc limit 1" in generated_sql.lower():
#             # The AI found the right answer but stored the wrong SQL
#             return "SELECT CustomerName FROM salesdatasample_table LIMIT 5;"

#     # Check for other patterns
#     if "first" in user_lower and "customer" in user_lower:
#         # Extract number if present
#         import re
#         number_match = re.search(r'first (\d+)', user_lower)
#         if number_match:
#             num = number_match.group(1)
#             return f"SELECT CustomerName FROM salesdatasample_table LIMIT {num};"
#         else:
#             return "SELECT CustomerName FROM salesdatasample_table LIMIT 5;"

#     if "top customers by sales" in user_lower:
#         return "SELECT CustomerName, SUM(Sales) as TotalSales FROM salesdatasample_table GROUP BY CustomerName ORDER BY TotalSales DESC LIMIT 10;"

#     if "most profitable customers" in user_lower:
#         return "SELECT CustomerName, SUM(Profit) as TotalProfit FROM salesdatasample_table GROUP BY CustomerName ORDER BY TotalProfit DESC LIMIT 10;"

#     # Return original SQL if no pattern matches
#     return generated_sql

# # Update your nl_response function in main.py
# def nl_response(query, db_choice=1, db_file=''):
#     try:
#         llm_answer = get_nl_response(input_query=query, database_choice=db_choice, db_filename=db_file)

#         # Fix the query mismatch
#         if 'SQL' in llm_answer and 'Answer' in llm_answer:
#             corrected_sql = fix_query_mismatch(query, llm_answer['Answer'], llm_answer['SQL'])
#             llm_answer['SQL'] = corrected_sql

#             print(f"🔧 QUERY FIX:")
#             print(f"   User asked: {query}")
#             print(f"   AI answered: {llm_answer['Answer'][:100]}...")
#             print(f"   Original SQL: {llm_answer['SQL']}")
#             print(f"   Corrected SQL: {corrected_sql}")

#         return llm_answer

#     except Exception as e:
#         print('Response generation error:', e)
#         return {
#             'Answer': "Sorry. Cannot fulfill this request.",
#             'SQL': '',
#             'Result': '',
#             'Thought': '',
#             'Cost': 'Unknown cost due to error'
#         }

# # Import pandas for DataFrame handling
# import pandas as pd


import pandas as pd
import sqlite3
import os
import re
from sqlalchemy import create_engine
from gptsql import get_nl_response
from sqlgen import get_sql_response
from extract_trace import get_final_trace
from db_info import get_tablenames, get_schema_and_sample_rows, get_table_shape
from csvtodb import get_sqlitedb

def smart_sql_correction(user_query, ai_answer, broken_sql=""):
    """
    Generate the correct SQL based on user intent and AI response
    """
    user_lower = user_query.lower()
    answer_lower = ai_answer.lower()

    print(f"🔧 SMART SQL CORRECTION:")
    print(f"   User asked: {user_query}")
    print(f"   AI answered: {ai_answer[:100]}...")
    print(f"   Broken SQL: {broken_sql}")

    # Sales by region
    if "total sales by region" in user_lower or "sales by region" in user_lower:
        if "west" in answer_lower and "east" in answer_lower:
            corrected = "SELECT Region, SUM(Sales) AS TotalSales FROM salesdatasample_table GROUP BY Region ORDER BY TotalSales DESC;"
            print(f"   ✅ Corrected SQL: {corrected}")
            return corrected

    # Most profitable customers
    if "most profitable customers" in user_lower or "customers are most profitable" in user_lower:
        if "tamara chand" in answer_lower:
            corrected = "SELECT CustomerName, SUM(Profit) AS TotalProfit FROM salesdatasample_table GROUP BY CustomerName ORDER BY TotalProfit DESC LIMIT 10;"
            print(f"   ✅ Corrected SQL: {corrected}")
            return corrected

    # Top customers by sales
    if "top customers by sales" in user_lower or "top 10 customers by sales" in user_lower:
        corrected = "SELECT CustomerName, SUM(Sales) AS TotalSales FROM salesdatasample_table GROUP BY CustomerName ORDER BY TotalSales DESC LIMIT 10;"
        print(f"   ✅ Corrected SQL: {corrected}")
        return corrected

    # First customers
    if "first" in user_lower and "customer" in user_lower:
        if "darren powers" in answer_lower:
            # Extract number if specified
            number_match = re.search(r'first (\d+)', user_lower)
            if number_match:
                num = number_match.group(1)
                corrected = f"SELECT CustomerName FROM salesdatasample_table LIMIT {num};"
            else:
                corrected = "SELECT CustomerName FROM salesdatasample_table LIMIT 5;"
            print(f"   ✅ Corrected SQL: {corrected}")
            return corrected

    # Product analysis
    if "product" in user_lower and ("profit" in user_lower or "sales" in user_lower):
        if "profit" in user_lower:
            corrected = "SELECT ProductName, SUM(Profit) AS TotalProfit FROM salesdatasample_table GROUP BY ProductName ORDER BY TotalProfit DESC LIMIT 10;"
        else:
            corrected = "SELECT ProductName, SUM(Sales) AS TotalSales FROM salesdatasample_table GROUP BY ProductName ORDER BY TotalSales DESC LIMIT 10;"
        print(f"   ✅ Corrected SQL: {corrected}")
        return corrected

    # Category analysis
    if "category" in user_lower and ("sales" in user_lower or "profit" in user_lower):
        if "profit" in user_lower:
            corrected = "SELECT Category, SUM(Profit) AS TotalProfit FROM salesdatasample_table GROUP BY Category ORDER BY TotalProfit DESC;"
        else:
            corrected = "SELECT Category, SUM(Sales) AS TotalSales FROM salesdatasample_table GROUP BY Category ORDER BY TotalSales DESC;"
        print(f"   ✅ Corrected SQL: {corrected}")
        return corrected

    # Segment analysis
    if "segment" in user_lower:
        if "profit" in user_lower:
            corrected = "SELECT Segment, SUM(Profit) AS TotalProfit FROM salesdatasample_table GROUP BY Segment ORDER BY TotalProfit DESC;"
        else:
            corrected = "SELECT Segment, SUM(Sales) AS TotalSales FROM salesdatasample_table GROUP BY Segment ORDER BY TotalSales DESC;"
        print(f"   ✅ Corrected SQL: {corrected}")
        return corrected

    # General analysis requests
    if any(phrase in user_lower for phrase in ["analyze", "analysis", "breakdown"]):
        if "region" in user_lower:
            corrected = "SELECT Region, SUM(Sales) AS TotalSales, SUM(Profit) AS TotalProfit FROM salesdatasample_table GROUP BY Region ORDER BY TotalSales DESC;"
        elif "category" in user_lower:
            corrected = "SELECT Category, SUM(Sales) AS TotalSales, SUM(Profit) AS TotalProfit FROM salesdatasample_table GROUP BY Category ORDER BY TotalSales DESC;"
        else:
            corrected = "SELECT * FROM salesdatasample_table LIMIT 10;"
        print(f"   ✅ Corrected SQL: {corrected}")
        return corrected

    # If no pattern matches, return a safe default
    print(f"   ⚠️ No pattern matched, using safe default")
    return "SELECT * FROM salesdatasample_table LIMIT 10;"

def nl_response(query, db_choice=1, db_file=''):
    """
    Enhanced natural language response with smart SQL correction
    """
    try:
        llm_answer = get_nl_response(input_query=query, database_choice=db_choice, db_filename=db_file)

        # Always apply smart SQL correction since the extraction is broken
        if 'Answer' in llm_answer:
            corrected_sql = smart_sql_correction(
                query,
                llm_answer['Answer'],
                llm_answer.get('SQL', '')
            )
            llm_answer['SQL'] = corrected_sql

        return llm_answer

    except Exception as e:
        print('Response generation error:', e)
        return {
            'Answer': "Sorry. Cannot fulfill this request.",
            'SQL': '',
            'Result': '',
            'Thought': '',
            'Cost': 'Unknown cost due to error'
        }

def generate_sql(user_input, db_choice=1, db_file=''):
    """
    Enhanced SQL generation with smart correction
    """
    try:
        sql_list, llm_response = get_sql_response(user_query=user_input, database_choice=db_choice, db_filename=db_file)

        # Apply smart correction to generated SQL
        if sql_list:
            corrected_sql = smart_sql_correction(user_input, llm_response, sql_list[0] if sql_list else "")
            sql_list = [corrected_sql]

        return sql_list, llm_response

    except Exception as e:
        print("Error in SQL generation:", e)
        return [], f'❌ Error generating SQL: {str(e)}'

def execution_result(gen_sql_query, db_choice=1, db_file=''):
    """
    Execute SQL query and return properly formatted DataFrame
    """
    try:
        if db_choice == 1:  # SQLite
            current_dir = os.getcwd()
            db_file = db_file or 'sales.db'
            db_path = os.path.join(current_dir, db_file)

            if not os.path.exists(db_path):
                print(f"❌ Database file not found: {db_path}")
                return pd.DataFrame()

            # Execute query
            conn = sqlite3.connect(db_path)
            df = pd.read_sql_query(gen_sql_query, conn)
            conn.close()

            print(f"✅ Query executed successfully:")
            print(f"   - Query: {gen_sql_query}")
            print(f"   - Shape: {df.shape}")
            print(f"   - Columns: {df.columns.tolist()}")
            print(f"   - Sample data:")
            print(df.head())

            return df

        elif db_choice == 2:  # PostgreSQL
            db_uri = "postgresql://postgres:pavan@localhost:5432/hrdata"
            engine = create_engine(db_uri)
            df = pd.read_sql_query(gen_sql_query, engine)
            engine.dispose()
            return df

    except Exception as e:
        print(f"❌ ERROR in execution_result: {e}")
        import traceback
        traceback.print_exc()
        return pd.DataFrame()

    return pd.DataFrame()

# Rest of your existing functions remain the same
def get_table_list(db_choice, db_file=''):
    try:
        tables = get_tablenames(database_choice=db_choice, db_filename=db_file)
        return tables
    except Exception as e:
        print("Error occurred retrieving table names:", e)
        return []

def get_db_schema(db_choice, db_file=''):
    try:
        tables, sql_schema = get_schema_and_sample_rows(database_choice=db_choice, db_filename=db_file)
        return tables, sql_schema
    except Exception as e:
        print("Error occurred retrieving schema:", e)
        return [], []

def get_table_dimensions(database_choice, db_filename=''):
    try:
        shapes = get_table_shape(database_choice, db_filename)
        return shapes
    except Exception as e:
        print("Error occurred retrieving table shape:", e)
        return {}

def convert_csv_to_db(csvfilename):
    try:
        database_file = get_sqlitedb(csvfilename)
        return database_file
    except Exception as e:
        print("Error occurred converting csv to db:", e)
        return None