import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def load_data(file_path):
    """Load data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def calculate_loop_percentage_by_length(data):
    """Calculate the percentage of sequences that make a loop in each length bin."""
    bin_edges = np.arange(74, 175, 10)
    data['length_bin'] = pd.cut(data['length'], bins=bin_edges, right=False)
    bin_groups = data.groupby('length_bin')['makes_a_loop'].apply(lambda x: (x == 'yes').mean() * 100).reset_index()
    return bin_groups

def plot_loop_percentage_by_length(bin_groups, output_file_path):
    """Plot the histogram of loop percentages."""
    plt.figure(figsize=(12, 8))
    bars = plt.bar(bin_groups['length_bin'].astype(str), bin_groups['makes_a_loop'], color='skyblue', edgecolor='black')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval:.1f}%', ha='center', va='bottom')

    plt.xlabel('Length Bin')
    plt.ylabel('Percentage of Sequences Making a Loop')
    plt.title('Percentage of Sequences Making a Loop by Length Bin')
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.2)
    plt.savefig(output_file_path, format='eps', dpi=300)
    plt.show()

def calculate_loop_percentage_by_gc_content(data):
    """Calculate the percentage of sequences that make a loop in each GC content bin."""
    data['gc_bin'] = pd.qcut(data['gc_content'], q=10, precision=10)
    bin_groups = data.groupby('gc_bin')['makes_a_loop'].apply(lambda x: (x == 'yes').mean() * 100).reset_index()
    return bin_groups

def plot_loop_gc_content_vs_length(data, output_file_path):
    """Plot GC content vs. length with points colored by loop presence."""
    plt.figure(figsize=(10, 6))
    loop_colors = {'yes': 'blue', 'no': 'red'}
    plt.scatter(data['gc_content'], data['length'], c=data['makes_a_loop'].map(loop_colors), alpha=0.6)
    plt.xlabel('GC Content')
    plt.ylabel('Length')
    plt.title('GC Content vs. Length (Colored by Loop Presence)')
    plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Loop'),
                        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='No Loop')],
               title='Loop Presence')
    plt.grid(True)
    plt.savefig(output_file_path, format='eps', dpi=300)
    plt.show()

def calculate_nick_percentage_by_length(data):
    """Calculate the percentage of sequences that make a nick in each length bin."""
    bin_edges = np.arange(74, 175, 10)
    data['length_bin'] = pd.cut(data['length'], bins=bin_edges, right=False)
    bin_groups = data.groupby('length_bin')['DNA_broken'].apply(lambda x: (x == 'yes').mean() * 100).reset_index()
    return bin_groups

def plot_nick_percentage_by_length(bin_groups, output_file_path):
    """Plot the histogram of nick percentages."""
    plt.figure(figsize=(12, 8))
    bars = plt.bar(bin_groups['length_bin'].astype(str), bin_groups['DNA_broken'], color='skyblue', edgecolor='black')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval:.1f}%', ha='center', va='bottom')

    plt.xlabel('Length Bin')
    plt.ylabel('Percentage of Sequences with Nicked DNA')
    plt.title('Percentage of Sequences with Nicked DNA by Length Bin')
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.2)

    # Set y-axis limits to extend beyond the maximum point
    max_percentage = bin_groups['DNA_broken'].max()
    plt.ylim(0, max_percentage + 5)  # Adjust the additional unit as needed

    plt.savefig(output_file_path, format='eps', dpi=300)
    plt.show()

def plot_nick_gc_content_vs_length(data, output_file_path):
    """Plot GC content vs. length with points colored by nick presence."""
    plt.figure(figsize=(10, 6))
    loop_colors = {'yes': 'blue', 'no': 'red'}
    plt.scatter(data['gc_content'], data['length'], c=data['DNA_broken'].map(loop_colors), alpha=0.6)
    plt.xlabel('GC Content')
    plt.ylabel('Length')
    plt.title('GC Content vs. Length (Colored by DNA nick Presence)')
    plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Nick'),
                        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='No Nick')],
               title='Nick Presence')
    plt.grid(True)
    plt.savefig(output_file_path, format='eps', dpi=300)
    plt.show()

def main():
    file_path = input("Please enter the file path: ")
    output_folder = input("Please enter the output folder path: ")
    output_file_path_length_loop = os.path.join(output_folder, "loop_percentage_by_length_plot.eps")
    output_file_path_gc_loop = os.path.join(output_folder, "loop_percentage_by_gc_content_plot.eps")
    output_file_path_scatter_loop = os.path.join(output_folder, "loop_gc_content_vs_length_plot.eps")
    output_file_path_length_nick = os.path.join(output_folder, "nick_percentage_by_length_plot.eps")
    output_file_path_gc_nick = os.path.join(output_folder, "nick_percentage_by_gc_content_plot.eps")
    output_file_path_scatter_nick = os.path.join(output_folder, "nick_gc_content_vs_length_plot.eps")


    data = load_data(file_path)
    
    bin_groups_length = calculate_loop_percentage_by_length(data)
    plot_loop_percentage_by_length(bin_groups_length, output_file_path_length_loop)
    
    plot_loop_gc_content_vs_length(data, output_file_path_scatter_loop)

    bin_groups_length = calculate_nick_percentage_by_length(data)
    plot_nick_percentage_by_length(bin_groups_length, output_file_path_length_nick)
    
    plot_nick_gc_content_vs_length(data, output_file_path_scatter_nick)


if __name__ == "__main__":
    main()

