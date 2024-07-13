import matplotlib.pyplot as plt

def read_metrics(file_path):
    metrics = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                metric, value = line.split(':')
                metrics.append((metric.strip(), float(value.strip().strip('%'))))
    return metrics

# Read metrics from both files
metrics1 = read_metrics('results/output_metrics.txt')
metrics2 = read_metrics('results/output2_metrics.txt')

# Extract metric names and values, preserving the order from the first file
all_metrics = [metric for metric, value in metrics1]
metrics1_values = [value for metric, value in metrics1]
metrics2_dict = {metric: value for metric, value in metrics2}
metrics2_values_ordered = [metrics2_dict.get(metric, 0) for metric in all_metrics]

# Plot the metrics for comparison
fig, ax = plt.subplots(figsize=(10, 6))
index = range(len(all_metrics))
bar_width = 0.35

bar1 = ax.bar(index, metrics1_values, bar_width, label='Model 1')
bar2 = ax.bar([i + bar_width for i in index], metrics2_values_ordered, bar_width, label='Model 2')

# Add values on top of bars
for i, value in enumerate(metrics1_values):
    ax.text(i, value + 1, f'{value:.2f}%', ha='center', va='bottom')
for i, value in enumerate(metrics2_values_ordered):
    ax.text(i + bar_width, value + 1, f'{value:.2f}%', ha='center', va='bottom')

ax.set_xlabel('Metrics')
ax.set_ylabel('Values (%)')
ax.set_title('Comparison of Metrics Between Two Models')
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(all_metrics, rotation=45)
ax.legend()

plt.tight_layout()
plt.show()