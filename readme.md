# 🤖 SQL Chat Agent

An intelligent natural language to SQL query system that allows you to interact with your databases using plain English. Ask questions about your data and get instant insights with automatically generated SQL queries and beautiful visualizations.

![SQL Chat Agent](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-green)
![SQLite](https://img.shields.io/badge/Database-SQLite%20%7C%20PostgreSQL-orange)

## 🚀 Features

- **Natural Language Queries**: Ask questions in plain English
- **Multi-Database Support**: SQLite and PostgreSQL
- **Smart SQL Generation**: Automatic query generation and correction
- **Interactive Chat Interface**: Conversation-style interaction
- **Data Visualization**: Automatic charts and insights
- **Export Functionality**: Download results as CSV
- **File Upload Support**: Upload your own CSV/DB files
- **Real-time Results**: Instant query execution and display

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**
- **pip (Python package installer)**
- **OpenAI API Key** (for natural language processing)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sql-chat-agent.git
cd sql-chat-agent
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install manually:

```bash
pip install streamlit pandas sqlite3 sqlalchemy python-dotenv openai langchain langchain-community langchain-openai plotly
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
touch .env
```

Add your OpenAI API key to the `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

**To get an OpenAI API key:**
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste it into your `.env` file

## 📁 Project Structure

```
sql-chat-agent/
├── README.md
├── requirements.txt
├── .env
├── chatui.py              # Main Streamlit interface
├── main.py                # Core logic and SQL correction
├── gptsql.py              # OpenAI integration for NL to SQL
├── sqlgen.py              # SQL query generation
├── extract_trace.py       # Query trace extraction
├── db_info.py             # Database information utilities
├── csvtodb.py             # CSV to SQLite conversion
├── styles.md              # Custom CSS styles (optional)
├── sales.db               # Default sample database
├── sales-data-sample.csv  # Default sample data
└── fulltrace.txt          # Query execution traces
```

## 🏃‍♂️ How to Run

### 1. Basic Startup

```bash
streamlit run chatui.py
```

The application will open in your default web browser at `http://localhost:8501`

### 2. Alternative Port

If port 8501 is busy, specify a different port:

```bash
streamlit run chatui.py --server.port 8502
```

### 3. Network Access

To allow access from other devices on your network:

```bash
streamlit run chatui.py --server.address 0.0.0.0
```

## 📖 Usage Guide

### Step 1: Configure Database

1. **Select Database Type**:
   - Choose **SQLite** for local files and sample data
   - Choose **PostgreSQL** for existing database connections

2. **Choose Data Source** (SQLite only):
   - **Use default sales data**: Pre-loaded sample dataset
   - **Upload custom file**: Upload your own .csv or .db file

### Step 2: Select Chat Mode

- **Response Agent**: Get natural language answers with automatic SQL generation
- **Query Agent**: Focus on SQL query generation and optimization

### Step 3: Start Asking Questions

Try these example questions:

#### Customer Analysis
```
Show me the first 5 customers
Who are the top 10 customers by sales?
Which customers are most profitable?
Find customers with negative profits
```

#### Sales Analysis
```
What are the total sales by region?
Show me sales trends by category
Analyze profit margins by segment
What's the average order value?
```

#### Product Analysis
```
What are the most profitable products?
Show me product performance by category
Which products have the highest sales?
```

#### Business Intelligence
```
Compare sales performance by region
Show me monthly sales trends
What's our profit ratio analysis?
Find the best performing states
```

### Step 4: Interact with Results

- **View Data Tables**: Interactive, sortable data tables
- **Download Results**: Export query results as CSV
- **Generate Charts**: Automatic visualizations for suitable data
- **Quick Insights**: Automatic statistical summaries

## 🔧 Configuration Options

### Database Configuration

#### SQLite (Default)
- Automatically uses `sales.db` sample database
- Upload custom `.csv` files (automatically converted to SQLite)
- Upload existing `.db` files

#### PostgreSQL
Update the connection string in `main.py`:

```python
db_uri = "postgresql://username:password@localhost:5432/database_name"
```

### OpenAI Model Configuration

In `gptsql.py`, you can change the model:

```python
llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=api_key)
```

Available models:
- `gpt-3.5-turbo` (default, faster, cheaper)
- `gpt-4` (more accurate, slower, more expensive)

## 🛠️ Troubleshooting

### Common Issues

#### 1. OpenAI API Key Error
```
Error: OPENAI_API_KEY not found in environment variables
```
**Solution**: Ensure your `.env` file contains the correct API key

#### 2. Database Connection Error
```
Database file not found
```
**Solution**: Ensure `sales.db` exists in the project directory

#### 3. Module Import Errors
```
ModuleNotFoundError: No module named 'streamlit'
```
**Solution**: Install missing dependencies:
```bash
pip install streamlit pandas sqlalchemy python-dotenv openai langchain
```

#### 4. Port Already in Use
```
Port 8501 is already in use
```
**Solution**: Use a different port:
```bash
streamlit run chatui.py --server.port 8502
```

#### 5. Query Results Always Show Same Data
This is a known issue with SQL extraction. The system includes smart correction logic that should automatically fix this.

### Performance Tips

1. **Use specific questions** for better results
2. **Start with simple queries** before complex analysis
3. **Check the generated SQL** to understand what's happening
4. **Use the Query Agent mode** for more control over SQL generation

## 📊 Sample Data

The default `sales-data-sample.csv` includes:

- **Customer Information**: Names, segments, regions
- **Product Details**: Categories, sub-categories, product names
- **Sales Metrics**: Sales amounts, quantities, discounts
- **Profit Analysis**: Profit values, profit ratios
- **Geographic Data**: States, cities, postal codes
- **Order Information**: Order dates, ship dates, modes

## 🔒 Security Considerations

1. **API Key Security**: Never commit your `.env` file to version control
2. **Database Access**: Ensure proper database permissions
3. **Input Validation**: The system includes SQL injection protection
4. **Network Security**: Use HTTPS in production environments

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter issues:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review the console output for error messages
3. Ensure all dependencies are correctly installed
4. Verify your OpenAI API key is valid and has sufficient credits

## 🔄 Updates and Maintenance

### Updating Dependencies

```bash
pip install --upgrade streamlit pandas sqlalchemy openai langchain
```

### Clearing Cache

If you encounter issues, clear Streamlit's cache:

```bash
streamlit cache clear
```


**Made with ❤️ using Streamlit, OpenAI, and Python**

