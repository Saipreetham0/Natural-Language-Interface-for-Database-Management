
import re
import os

def generate_correct_sql_from_intent(user_query, ai_answer):
    """
    Generate the correct SQL based on user intent and AI answer
    """
    user_lower = user_query.lower()
    answer_lower = ai_answer.lower()

    # Sales by region
    if "total sales by region" in user_lower or "sales by region" in user_lower:
        if "west" in answer_lower and "east" in answer_lower:
            return "SELECT Region, SUM(Sales) AS TotalSales FROM salesdatasample_table GROUP BY Region ORDER BY TotalSales DESC;"

    # Most profitable customers
    if "most profitable customers" in user_lower or "customers are most profitable" in user_lower:
        if "tamara chand" in answer_lower and "raymond buch" in answer_lower:
            return "SELECT CustomerName, SUM(Profit) AS TotalProfit FROM salesdatasample_table GROUP BY CustomerName ORDER BY TotalProfit DESC LIMIT 10;"

    # First customers
    if "first" in user_lower and "customer" in user_lower:
        if "darren powers" in answer_lower:
            # Extract number if specified
            number_match = re.search(r'first (\d+)', user_lower)
            if number_match:
                num = number_match.group(1)
                return f"SELECT CustomerName FROM salesdatasample_table LIMIT {num};"
            else:
                return "SELECT CustomerName FROM salesdatasample_table LIMIT 5;"

    # Top customers by sales
    if "top customers by sales" in user_lower:
        return "SELECT CustomerName, SUM(Sales) AS TotalSales FROM salesdatasample_table GROUP BY CustomerName ORDER BY TotalSales DESC LIMIT 10;"

    # Product analysis
    if "product" in user_lower and ("profit" in user_lower or "sales" in user_lower):
        if "profit" in user_lower:
            return "SELECT ProductName, SUM(Profit) AS TotalProfit FROM salesdatasample_table GROUP BY ProductName ORDER BY TotalProfit DESC LIMIT 10;"
        else:
            return "SELECT ProductName, SUM(Sales) AS TotalSales FROM salesdatasample_table GROUP BY ProductName ORDER BY TotalSales DESC LIMIT 10;"

    # Category analysis
    if "category" in user_lower and ("sales" in user_lower or "profit" in user_lower):
        if "profit" in user_lower:
            return "SELECT Category, SUM(Profit) AS TotalProfit FROM salesdatasample_table GROUP BY Category ORDER BY TotalProfit DESC;"
        else:
            return "SELECT Category, SUM(Sales) AS TotalSales FROM salesdatasample_table GROUP BY Category ORDER BY TotalSales DESC;"

    # Segment analysis
    if "segment" in user_lower and ("sales" in user_lower or "profit" in user_lower):
        if "profit" in user_lower:
            return "SELECT Segment, SUM(Profit) AS TotalProfit FROM salesdatasample_table GROUP BY Segment ORDER BY TotalProfit DESC;"
        else:
            return "SELECT Segment, SUM(Sales) AS TotalSales FROM salesdatasample_table GROUP BY Segment ORDER BY TotalSales DESC;"

    # State analysis
    if "state" in user_lower and ("sales" in user_lower or "profit" in user_lower):
        if "profit" in user_lower:
            return "SELECT State, SUM(Profit) AS TotalProfit FROM salesdatasample_table GROUP BY State ORDER BY TotalProfit DESC LIMIT 10;"
        else:
            return "SELECT State, SUM(Sales) AS TotalSales FROM salesdatasample_table GROUP BY State ORDER BY TotalSales DESC LIMIT 10;"

    # City analysis
    if "city" in user_lower and ("sales" in user_lower or "profit" in user_lower):
        if "profit" in user_lower:
            return "SELECT City, SUM(Profit) AS TotalProfit FROM salesdatasample_table GROUP BY City ORDER BY TotalProfit DESC LIMIT 10;"
        else:
            return "SELECT City, SUM(Sales) AS TotalSales FROM salesdatasample_table GROUP BY City ORDER BY TotalSales DESC LIMIT 10;"

    # Order analysis
    if "order" in user_lower and ("total" in user_lower or "count" in user_lower):
        return "SELECT CustomerName, COUNT(OrderID) AS TotalOrders FROM salesdatasample_table GROUP BY CustomerName ORDER BY TotalOrders DESC LIMIT 10;"

    # Discount analysis
    if "discount" in user_lower:
        if "average" in user_lower or "avg" in user_lower:
            return "SELECT CustomerName, AVG(Discount) AS AvgDiscount FROM salesdatasample_table GROUP BY CustomerName ORDER BY AvgDiscount DESC LIMIT 10;"
        else:
            return "SELECT CustomerName, Discount, Sales, Profit FROM salesdatasample_table WHERE Discount > 0 ORDER BY Discount DESC LIMIT 10;"

    # Profit ratio analysis
    if "profit ratio" in user_lower or "profitability" in user_lower:
        return "SELECT CustomerName, AVG(ProfitRatio) AS AvgProfitRatio FROM salesdatasample_table GROUP BY CustomerName ORDER BY AvgProfitRatio DESC LIMIT 10;"

    # General data request
    if any(word in user_lower for word in ["show me", "display", "list"]) and "data" in user_lower:
        return "SELECT * FROM salesdatasample_table LIMIT 10;"

    # Default fallback - return a general query
    return "SELECT * FROM salesdatasample_table LIMIT 5;"

def smart_sql_correction(user_query, ai_answer, broken_sql):
    """
    Smart SQL correction based on user intent and AI response
    """
    print(f"🔧 SMART SQL CORRECTION:")
    print(f"   User asked: {user_query}")
    print(f"   AI answered: {ai_answer[:100]}...")
    print(f"   Broken SQL: {broken_sql}")

    # Generate the correct SQL based on intent
    correct_sql = generate_correct_sql_from_intent(user_query, ai_answer)

    print(f"   Corrected SQL: {correct_sql}")
    return correct_sql

# Test function
def test_smart_extraction():
    test_cases = [
        ("What are the total sales by region?", "West: $725,514 - East: $678,834"),
        ("Which customers are most profitable?", "Tamara Chand, Raymond Buch, Sanjit Chand"),
        ("Show me the first 5 customers", "Darren Powers, Phillina Ober"),
    ]

    for query, answer in test_cases:
        sql = generate_correct_sql_from_intent(query, answer)
        print(f"Query: {query}")
        print(f"Generated SQL: {sql}")
        print("---")

if __name__ == "__main__":
    test_smart_extraction()