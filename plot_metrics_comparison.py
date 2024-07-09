import matplotlib.pyplot as plt
import numpy as np

def read_metrics(file_path):
    metrics = {}
    with open(file_path, 'r') as file:
        for line in file:
            metric, value = line.split(':')
            metrics[metric.strip()] = float(value.strip().replace('%', ''))
    return metrics

def plot_metrics(metrics1, metrics2, labels1, labels2):
    metrics_names = metrics1.keys()
    
    values1 = [metrics1[metric] for metric in metrics_names]
    values2 = [metrics2[metric] for metric in metrics_names]

    x = np.arange(len(metrics_names))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    bars1 = ax.bar(x - width/2, values1, width, label=labels1)
    bars2 = ax.bar(x + width/2, values2, width, label=labels2)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Metrics')
    ax.set_ylabel('Scores (%)')
    ax.set_title('Metric Comparison')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics_names, rotation=45, ha="right")
    ax.legend()

    # Attach a text label above each bar in *bars*, displaying its height.
    def autolabel(bars):
        """Attach a text label above each bar in *bars*, displaying its height."""
        for bar in bars:
            height = bar.get_height()
            ax.annotate('{}'.format(height),
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(bars1)
    autolabel(bars2)

    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    file1 = 'results/subset_output.txt'
    #file2 = 'results/subset_output_persona.txt'
    file2 = 'results/subset_output_few_shot.txt'
    
    metrics1 = read_metrics(file1)
    metrics2 = read_metrics(file2)
    
    plot_metrics(metrics1, metrics2, 'Subset Output', 'Subset Output Prompt Pattern')
