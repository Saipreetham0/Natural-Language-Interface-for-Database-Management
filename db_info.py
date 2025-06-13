

# import os
# import pandas as pd
# from decimal import Decimal
# from sqlalchemy import create_engine, inspect,text,MetaData
# from langchain_community.utilities import SQLDatabase
# from csvtodb import get_sqlitedb


# def create_dbengine(database_choice,db_filename=''):

#     try:

#         db_uri=""
#         current_dir = os.getcwd()

#         if database_choice==1:
#             # if db_filename==None:
#             #     db_filename='salesdatasample.db'
#             db_filename=db_filename or 'salesdatasample.db'
#             db_path = os.path.join(current_dir, db_filename)
#             db_uri="sqlite:///"+db_path

#             # db_uri="sqlite:////home/Sravan/Desktop/d/prjcode/chinook.db"

#         elif database_choice==2:
#             db_uri= "postgresql://postgres:pavan@localhost:5432/hrdata"
#             # db_uri= "postgresql://postgres:3033@localhost:5432/hrdata"

#         engine= create_engine(db_uri)

#         return engine

#     except Exception as e:
#         print("sqlalchemy engine error: ",e)


# def get_relations(engine):

#     metadata = MetaData()
#     metadata.reflect(bind=engine)
#     relations= ""

#     for table_name, table in metadata.tables.items():
#         for fk in table.foreign_key_constraints:
#             local_columns = ", ".join(str(column) for column in fk.columns)
#             referenced_table = fk.elements[0].column.table
#             referenced_columns = ", ".join(str(column) for column in referenced_table.primary_key)
#             relations=relations+"# "+f"{local_columns} --> {referenced_columns}"+'\n'
#             # print(f"{table_name}.{local_columns} = {referenced_table.name}.{referenced_columns}")
#             # print(f"{local_columns} = {referenced_columns}")

#     return relations

# def get_table_info(database_choice,db_filename=''):

#     try:
#         if db_filename:
#             if db_filename.endswith('csv'):
#                 db_filename=get_sqlitedb(db_filename)
#         # if database_choice==1:
#         #     engine=create_dbengine(database_choice,db_filename)
#         # elif database_choice==2:
#         #     engine=create_dbengine(database_choice)
#         engine=create_dbengine(database_choice,db_filename)
#         inspector = inspect(engine)
#         relations=get_relations(engine)
#         connection=engine.connect()
#         table_names = [i for i in inspector.get_table_names() if not i.startswith('sql')]
#         table_info,table_shape = {},{}

#         for table_name in table_names:
#             column_details = inspector.get_columns(table_name)
#             columns = [column['name'] for column in column_details]
#             if table_name not in table_info:
#                 table_info[table_name]=columns

#             count_query = f'SELECT COUNT(*) FROM {table_name}'
#             num_rows = connection.execute(text(count_query)).scalar()

#             if table_name not in table_shape:
#                 table_shape[table_name]=f"{num_rows} rows x {len(columns)} columns"
#         # print(table_shape)
#         connection.close()
#         engine.dispose()
#         return table_names,table_info,relations


#     except Exception as e:
#         print(f"table info Error: {e}")
#         return None


# # print(table_names,table_info)
# def get_formatted_schema(database_choice=1,db_filename=''):

#     table_names,table_info,relations=get_table_info(database_choice,db_filename)
#     formatted_schema=""
#     start_string=""

#     for table_name in table_names:
#         start_string="# "+table_name+" ( "
#         for column in table_info[table_name]:
#             start_string=start_string+column+", "
#         start_string=start_string[:-2]+" )"
#         # sample rows add here
#         formatted_schema=formatted_schema+ start_string+"\n"

#     formatted_schema=formatted_schema+relations
#     return formatted_schema

# def get_db_uri(database_choice,db_filename=''):

#     if db_filename.endswith('csv'):
#         db_filename=get_sqlitedb(db_filename)

#     db_uri=''
#     if database_choice==1:

#         start_str='sqlite:///'
#         current_dir = os.getcwd()
#         db_filename=db_filename or 'sales.db'
#         db_path = os.path.join(current_dir, db_filename)
#         # default_db_uri = "sqlite:////home/Sravan/Desktop/d/prjcode/demo.db"
#         db_uri=start_str+db_path

#     elif database_choice==2:

#         db_username='postgres'
#         password='pavan'
#         host='localhost'
#         port=5432
#         db='hrdata'

#         # db_username='postgres'
#         # password='3033'
#         # db='Employees'
#         start_str='postgresql+psycopg2://'
#         db_uri=f'{start_str}{db_username}:{password}@{host}:{port}/{db}'
#         # default_db_uri="postgresql+psycopg2://tempuser:password@localhost:5432/hrdata"

#     return db_uri

# def get_SQLdb(database_choice,db_filename):
#     db_uri=get_db_uri(database_choice,db_filename)
#     db = SQLDatabase.from_uri(db_uri)
#     return db

# def get_execution_result(sql_query='',database_choice=1,db_filename='',shape=False):

#     db=get_SQLdb(database_choice,db_filename)
#     if sql_query.lower().find('select')!=-1:
#         col_list,rows=db.run_no_throw(sql_query,columns=True)
#         if shape==True:
#             return f'{len(rows)} rows X {len(col_list)} columns'
#         df = pd.DataFrame(rows, columns=col_list)

#     return df

# def get_schema_and_sample_rows(database_choice,db_filename=''):

#     db=get_SQLdb(database_choice,db_filename)
#     tables=db.get_usable_table_names()
#     df_list=[]

#     for table_name in tables:
#         df=get_execution_result(sql_query=f'SELECT * FROM {table_name} LIMIT 5',database_choice=database_choice,db_filename=db_filename)
#         df_list.append(df)
#     # schema_sample_rows=db.get_table_info_no_throw()

#     return tables,df_list

# def get_tablenames(database_choice,db_filename=''):

#     db=get_SQLdb(database_choice,db_filename)
#     tables=db.get_usable_table_names()
#     return tables

# def get_table_shape(database_choice,db_filename=''):

#     tables=get_tablenames(database_choice,db_filename)
#     shapes={}
#     for table_name in tables:
#         shapes[f'{table_name}']=get_execution_result(f'SELECT * FROM {table_name}',database_choice,db_filename,shape=True)

#     return shapes

# def get_3_rows(database_choice,db_filename=''):
#     db=get_SQLdb(database_choice,db_filename)
#     tables=get_tablenames(database_choice,db_filename)
#     table_rows=""
#     for table_name in tables:
#         full_desc=db.get_table_info_no_throw(table_names=[table_name])
#         # print(full_desc)
#         row_start=full_desc.rfind('/*')
#         rows_end=len(full_desc)
#         table_rows+=full_desc[row_start:rows_end]+'\n'
#     return table_rows.replace('/*','#').replace('*/','#')

# print(get_3_rows(1,'sales.db'))
# # print(get_execution_result("SELECT COUNT(*)  FROM employees  JOIN countries ON employees.country_id = countries.country_id  WHERE countries.country_name IN ('Canada', 'Australia');",2))
# # print(get_table_shape(1,'chinook.db'))



import os
import pandas as pd
from decimal import Decimal
from sqlalchemy import create_engine, inspect, text, MetaData
from langchain_community.utilities import SQLDatabase
from csvtodb import get_sqlitedb


def create_dbengine(database_choice, db_filename=''):
    """
    Create SQLAlchemy engine for database connection
    """
    try:
        db_uri = ""
        current_dir = os.getcwd()

        if database_choice == 1:
            # SQLite database
            db_filename = db_filename or 'sales.db'
            db_path = os.path.join(current_dir, db_filename)
            db_uri = "sqlite:///" + db_path

        elif database_choice == 2:
            # PostgreSQL database
            db_uri = "postgresql://postgres:pavan@localhost:5432/hrdata"

        engine = create_engine(db_uri)
        return engine

    except Exception as e:
        print("SQLAlchemy engine error:", e)
        return None


def get_relations(engine):
    """
    Extract foreign key relationships from database
    """
    metadata = MetaData()
    metadata.reflect(bind=engine)
    relations = ""

    for table_name, table in metadata.tables.items():
        for fk in table.foreign_key_constraints:
            local_columns = ", ".join(str(column) for column in fk.columns)
            referenced_table = fk.elements[0].column.table
            referenced_columns = ", ".join(str(column) for column in referenced_table.primary_key)
            relations = relations + "# " + f"{local_columns} --> {referenced_columns}" + '\n'

    return relations


def get_table_info(database_choice, db_filename=''):
    """
    Get comprehensive table information including names, columns, and relationships
    """
    try:
        if db_filename:
            if db_filename.endswith('csv'):
                db_filename = get_sqlitedb(db_filename)

        engine = create_dbengine(database_choice, db_filename)
        if engine is None:
            return None, None, None

        inspector = inspect(engine)
        relations = get_relations(engine)
        connection = engine.connect()
        table_names = [i for i in inspector.get_table_names() if not i.startswith('sql')]
        table_info, table_shape = {}, {}

        for table_name in table_names:
            column_details = inspector.get_columns(table_name)
            columns = [column['name'] for column in column_details]
            if table_name not in table_info:
                table_info[table_name] = columns

            count_query = f'SELECT COUNT(*) FROM {table_name}'
            num_rows = connection.execute(text(count_query)).scalar()

            if table_name not in table_shape:
                table_shape[table_name] = f"{num_rows} rows x {len(columns)} columns"

        connection.close()
        engine.dispose()
        return table_names, table_info, relations

    except Exception as e:
        print(f"Table info Error: {e}")
        return None, None, None


def get_formatted_schema(database_choice=1, db_filename=''):
    """
    Format database schema for LLM consumption
    """
    try:
        table_names, table_info, relations = get_table_info(database_choice, db_filename)
        if table_names is None:
            return "Error: Could not retrieve database schema"

        formatted_schema = ""

        for table_name in table_names:
            start_string = "# " + table_name + " ( "
            for column in table_info[table_name]:
                start_string = start_string + column + ", "
            start_string = start_string[:-2] + " )"
            formatted_schema = formatted_schema + start_string + "\n"

        formatted_schema = formatted_schema + relations
        return formatted_schema
    except Exception as e:
        print(f"Error formatting schema: {e}")
        return "Error: Could not format database schema"


def get_db_uri(database_choice, db_filename=''):
    """
    Generate database URI for connection
    """
    if db_filename and db_filename.endswith('csv'):
        db_filename = get_sqlitedb(db_filename)

    db_uri = ''
    if database_choice == 1:
        # SQLite
        start_str = 'sqlite:///'
        current_dir = os.getcwd()
        db_filename = db_filename or 'sales.db'
        db_path = os.path.join(current_dir, db_filename)
        db_uri = start_str + db_path

    elif database_choice == 2:
        # PostgreSQL
        db_username = 'postgres'
        password = 'pavan'
        host = 'localhost'
        port = 5432
        db = 'hrdata'

        start_str = 'postgresql+psycopg2://'
        db_uri = f'{start_str}{db_username}:{password}@{host}:{port}/{db}'

    return db_uri


def get_SQLdb(database_choice, db_filename):
    """
    Create LangChain SQLDatabase object
    """
    db_uri = get_db_uri(database_choice, db_filename)
    db = SQLDatabase.from_uri(db_uri)
    return db


# def get_execution_result(sql_query='', database_choice=1, db_filename='', shape=False):
#     """
#     Execute SQL query and return results as DataFrame
#     """
#     try:
#         db = get_SQLdb(database_choice, db_filename)
#         if sql_query.lower().find('select') != -1:
#             try:
#                 # Try with columns parameter first (newer versions)
#                 result = db.run_no_throw(sql_query)

#                 # Handle different result formats
#                 if isinstance(result, str):
#                     # Parse string result
#                     lines = result.strip().split('\n')
#                     if len(lines) > 1:
#                         # Try to parse tabular data
#                         rows = []
#                         for line in lines[1:]:
#                             if line.strip():
#                                 # Split by multiple spaces or tabs
#                                 row = [item.strip() for item in line.split() if item.strip()]
#                                 rows.append(row)
#                         col_list = ['Column_' + str(i) for i in range(len(rows[0]))] if rows else []
#                     else:
#                         rows = []
#                         col_list = []

#                 elif isinstance(result, list):
#                     # Result is already a list of tuples/lists
#                     rows = result
#                     col_list = ['Column_' + str(i) for i in range(len(rows[0]))] if rows else []

#                 else:
#                     # Single value result
#                     rows = [[result]] if result is not None else []
#                     col_list = ['Result'] if rows else []

#                 if shape == True:
#                     return f'{len(rows)} rows X {len(col_list)} columns'

#                 # Create DataFrame
#                 df = pd.DataFrame(rows, columns=col_list) if rows else pd.DataFrame()
#                 return df

#             except Exception as e:
#                 print(f"Error executing query: {e}")
#                 return pd.DataFrame()

#         return pd.DataFrame()

#     except Exception as e:
#         print(f"Database connection error: {e}")
#         return pd.DataFrame()


def get_execution_result(sql_query='', database_choice=1, db_filename='', shape=False):
    """
    Execute SQL query and return results as properly formatted DataFrame
    """
    try:
        db = get_SQLdb(database_choice, db_filename)

        if sql_query.lower().find('select') != -1:
            # Execute the query using LangChain's database
            result = db.run(sql_query)

            if shape == True:
                # For shape requests, count the lines in result
                lines = result.strip().split('\n') if isinstance(result, str) else []
                return f'{len(lines)} rows returned'

            # Parse the result string into structured data
            if isinstance(result, str) and result.strip():
                lines = result.strip().split('\n')

                if len(lines) == 0:
                    return pd.DataFrame()

                # Try to detect if first line contains column headers
                if '|' in lines[0] or '\t' in lines[0]:
                    # Tabular format with separators
                    data_rows = []
                    for line in lines:
                        if line.strip():
                            # Split by pipe or tab, clean whitespace
                            if '|' in line:
                                row = [cell.strip() for cell in line.split('|') if cell.strip()]
                            else:
                                row = [cell.strip() for cell in line.split('\t') if cell.strip()]
                            if row:
                                data_rows.append(row)

                    if data_rows:
                        # Use first row as headers if it looks like headers
                        if len(data_rows) > 1:
                            headers = data_rows[0]
                            data = data_rows[1:]
                        else:
                            headers = [f'Column_{i}' for i in range(len(data_rows[0]))]
                            data = data_rows

                        df = pd.DataFrame(data, columns=headers)
                        return df

                else:
                    # Simple comma/space separated format
                    data_rows = []
                    for line in lines:
                        if line.strip():
                            # Try comma first, then spaces
                            if ',' in line:
                                row = [cell.strip() for cell in line.split(',')]
                            else:
                                # Split by multiple spaces
                                row = [cell for cell in line.split() if cell]
                            if row:
                                data_rows.append(row)

                    if data_rows:
                        # Auto-generate column names
                        max_cols = max(len(row) for row in data_rows) if data_rows else 0
                        headers = [f'Column_{i}' for i in range(max_cols)]

                        # Pad rows to same length
                        padded_rows = []
                        for row in data_rows:
                            padded_row = row + [''] * (max_cols - len(row))
                            padded_rows.append(padded_row)

                        df = pd.DataFrame(padded_rows, columns=headers)
                        return df

            # Fallback: return empty DataFrame
            return pd.DataFrame()

        else:
            # Non-SELECT query
            return pd.DataFrame()

    except Exception as e:
        print(f"Error in get_execution_result: {e}")

        # Fallback: try direct SQLAlchemy execution
        try:
            engine = create_dbengine(database_choice, db_filename)
            if engine:
                df = pd.read_sql_query(sql_query, engine)
                engine.dispose()
                return df
        except Exception as e2:
            print(f"Fallback execution also failed: {e2}")

        return pd.DataFrame()


def get_execution_result_direct(sql_query='', database_choice=1, db_filename=''):
    """
    Alternative execution method using direct SQLAlchemy connection
    """
    try:
        engine = create_dbengine(database_choice, db_filename)
        if engine is None:
            return pd.DataFrame()

        # Use pandas to execute query and return DataFrame directly
        df = pd.read_sql_query(sql_query, engine)
        engine.dispose()
        return df

    except Exception as e:
        print(f"Direct execution error: {e}")
        return pd.DataFrame()


def get_execution_result_enhanced(sql_query='', database_choice=1, db_filename='', shape=False):
    """
    Enhanced execution with multiple fallback methods
    """
    # Method 1: Try direct pandas execution (most reliable)
    try:
        df = get_execution_result_direct(sql_query, database_choice, db_filename)
        if not df.empty:
            if shape:
                return f'{len(df)} rows X {len(df.columns)} columns'
            return df
    except Exception as e:
        print(f"Method 1 failed: {e}")

    # Method 2: Try LangChain execution with enhanced parsing
    try:
        return get_execution_result(sql_query, database_choice, db_filename, shape)
    except Exception as e:
        print(f"Method 2 failed: {e}")

    # Method 3: Raw SQLAlchemy execution
    try:
        engine = create_dbengine(database_choice, db_filename)
        if engine:
            connection = engine.connect()
            result = connection.execute(text(sql_query))

            # Convert to DataFrame
            rows = result.fetchall()
            columns = result.keys()
            df = pd.DataFrame(rows, columns=columns)

            connection.close()
            engine.dispose()

            if shape:
                return f'{len(df)} rows X {len(df.columns)} columns'
            return df

    except Exception as e:
        print(f"Method 3 failed: {e}")

    return pd.DataFrame()

def get_schema_and_sample_rows(database_choice, db_filename=''):
    """
    Get database schema with sample rows for each table
    """
    try:
        db = get_SQLdb(database_choice, db_filename)
        tables = db.get_usable_table_names()
        df_list = []

        for table_name in tables:
            df = get_execution_result(
                sql_query=f'SELECT * FROM {table_name} LIMIT 5',
                database_choice=database_choice,
                db_filename=db_filename
            )
            df_list.append(df)

        return tables, df_list

    except Exception as e:
        print(f"Error getting schema and sample rows: {e}")
        return [], []


def get_tablenames(database_choice, db_filename=''):
    """
    Get list of table names in database
    """
    try:
        db = get_SQLdb(database_choice, db_filename)
        tables = db.get_usable_table_names()
        return tables
    except Exception as e:
        print(f"Error getting table names: {e}")
        return []


def get_table_shape(database_choice, db_filename=''):
    """
    Get shape (rows x columns) for each table
    """
    try:
        tables = get_tablenames(database_choice, db_filename)
        shapes = {}
        for table_name in tables:
            shape = get_execution_result(
                f'SELECT COUNT(*) FROM {table_name}',
                database_choice,
                db_filename,
                shape=True
            )
            shapes[table_name] = shape

        return shapes

    except Exception as e:
        print(f"Error getting table shapes: {e}")
        return {}


def get_3_rows(database_choice, db_filename=''):
    """
    Get sample rows from all tables for schema understanding
    """
    try:
        db = get_SQLdb(database_choice, db_filename)
        tables = get_tablenames(database_choice, db_filename)
        table_rows = ""

        for table_name in tables:
            try:
                full_desc = db.get_table_info_no_throw(table_names=[table_name])
                row_start = full_desc.rfind('/*')
                rows_end = len(full_desc)
                if row_start != -1:
                    table_rows += full_desc[row_start:rows_end] + '\n'
            except Exception as e:
                print(f"Error getting sample rows for {table_name}: {e}")
                continue

        return table_rows.replace('/*', '#').replace('*/', '#')

    except Exception as e:
        print(f"Error getting sample rows: {e}")
        return ""


# Test function - can be removed in production
if __name__ == "__main__":
    try:
        print("Testing database connection...")
        print(get_3_rows(1, 'sales.db'))
    except Exception as e:
        print(f"Test error: {e}")