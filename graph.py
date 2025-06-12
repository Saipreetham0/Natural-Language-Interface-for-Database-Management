import matplotlib.pyplot as plt

# Define the data
difficulty_levels = ['Extra Hard','Hard','Medium','Easy']
base_paper_accuracy = [55, 60, 65, 70]
your_agent_accuracy = [63, 68, 72, 75]

# Plot the data
plt.plot(difficulty_levels, base_paper_accuracy, marker='o', label='Base Paper')
plt.plot(difficulty_levels, your_agent_accuracy, marker='o', label='Your Agent')

# Add labels and title
plt.xlabel('Difficulty Level')
plt.ylabel('Accuracy (%)')
plt.title('Accuracy Comparison of NLP-to-SQL Agents on Spider Dataset by Difficulty Level')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
