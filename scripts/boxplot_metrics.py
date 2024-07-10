import matplotlib.pyplot as plt

# Function to read data from file
def read_values_from_file(file_path):
    values = []
    with open(file_path, 'r') as file:
        for line in file:
            _, value = line.split(': ')
            values.append(float(value.strip('%\n')))
    return values

# File path
file_path = 'results/output_metrics.txt'

# Read data from file
values = read_values_from_file(file_path)


#Create the boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(values, vert=True, patch_artist=True)

# Titles and labels
plt.title('Boxplot of Values')
plt.xlabel('Values')

# Remove x-ticks
plt.xticks([])

# Show the plot
plt.show()
