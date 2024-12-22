#--------------------- Importing the necessary libraries ---------------------------
import pandas as pd  # for data manipulation and analysis
import matplotlib.pyplot as plt  # for data visualization
import numpy as np  # for numerical operations
#----------------------- Loading and cleaning data ----------------------------
# Define the path to the input CSV file
file_path = "input/"
# Load the CSV file into a pandas DataFrame
data = pd.read_csv(file_path, sep=";")
# Rename columns for easier reference and usage
data.rename(columns={
   'frequency_live_bacteria_%': 'frequency_live_bacteria',  
   'counts_live_bacteria_per_wet_g': 'counts_live_bacteria'
}, inplace=True)
# Apply a logarithmic transformation to bacterial counts
# Replace negative or zero values with NaN to avoid calculation errors
data['counts_live_bacteria'] = data['counts_live_bacteria'].apply(
   lambda x: np.log10(x) if x > 0 else np.nan  # Apply log10 only if value is positive
)
#----- Function to plot multi-segment curves for fecal live bacteria and save the data used for it -------
def plot_fecal_live_bacteria(data):
   # Filter the data for fecal samples only
   fecal_data = data[data['sample_type'] == 'fecal']
   # Standardize treatment names for consistency
   fecal_data.loc[:, 'treatment'] = fecal_data['treatment'].replace({'ABX': 'ABX', 'placebo': 'Placebo'})
   # Create a figure for the plot
   plt.figure(figsize=(10, 6))  # Set the figure size
   # Group data by treatment and mouse ID to create individual curves
   for treatment, group in fecal_data.groupby('treatment'):
       for mouse_id, mouse_group in group.groupby('mouse_ID'):
           plt.plot(
               mouse_group['experimental_day'],  # X-axis: experimental days
               mouse_group['counts_live_bacteria'],  # Y-axis: log-transformed counts
               label=treatment if mouse_id == group['mouse_ID'].iloc[0] else "",  # Add legend only once per treatment
               color='#FF9999' if treatment == 'ABX' else '#99CCFF',  # Use different colors for treatments
               alpha=0.7  # Set transparency for overlapping curves
           )
   # Add title and axis labels
   plt.title("Fecal live bacteria")  # Title of the plot
   plt.xlabel("Washout day")  # X-axis label
   plt.ylabel("log10(live bacteria/wet g)")  # Y-axis label
   # Add a legend and grid
   plt.legend(title="")  # Show legend with no title
   plt.grid(axis='both', linestyle='--', alpha=0.5)  # Add grid lines
   # Adjust layout
   plt.tight_layout()
   # Save the plot as an image file
   plt.savefig("images/fecal_graph.jpeg")
   # Save the filtered data to a CSV file
   fecal_data.to_csv("output/fecal_data.csv", index=False)

#----- Function to create violin plots for cecal and ileal samples and save the data used for it -------
def generate_violin_plot(data, sample_type, day, title, output_file):
   # Filter data for the specified sample type and experimental day
   filtered_data = data[(data['sample_type'] == sample_type) & (data['experimental_day'] == day)]
   # Extract bacterial counts for ABX and placebo treatments
   abx_data = filtered_data[filtered_data['treatment'] == 'ABX']['counts_live_bacteria']
   placebo_data = filtered_data[filtered_data['treatment'] == 'placebo']['counts_live_bacteria']
   # Prepare the data for the violin plot
   data_to_plot = [abx_data.dropna(), placebo_data.dropna()]
   # Create a figure for the plot
   fig, ax = plt.subplots(figsize=(8, 6))
   # Generate the violin plot
   violins = ax.violinplot(
       data_to_plot,  # Data for the plot
       showmeans=False,  # Do not display mean lines
       showmedians=False,  # Do not display median lines
       widths=0.6  # Adjust the width of the violins
   )
   # Customize the appearance of violins
   colors = ['#FF9999', '#99CCFF']  # Colors for ABX and Placebo groups
   for i, pc in enumerate(violins['bodies']):
       pc.set_facecolor(colors[i])  # Set fill color
       pc.set_edgecolor('black')  # Set border color
       pc.set_alpha(0.7)  # Set transparency
   # Add individual data points with slight horizontal jitter
   positions = [1, 2]  # Positions for ABX and Placebo groups
   for i, single_data in enumerate(data_to_plot):
       jitter = np.random.uniform(-0.1, 0.1, size=len(single_data))
       ax.scatter(
           [positions[i] + jitter_value for jitter_value in jitter],
           single_data,  
           color='black',  # Black points
           alpha=0.6,  # Transparency for points
           s=30,  # Point size
           label='_nolegend_'  # Exclude these points from the legend
       )
   # Add a custom legend for the treatments
   custom_lines = [
       plt.Line2D([0], [0], color='#FF9999', lw=4, label='ABX'),  # Line for ABX
       plt.Line2D([0], [0], color='#99CCFF', lw=4, label='Placebo')  # Line for Placebo
   ]
   ax.legend(handles=custom_lines, title="", loc="upper right", fontsize=12, title_fontsize=14)
   # Customize axis labels and title
   ax.set_xticks([1, 2])  # Set x-tick positions
   ax.set_xticklabels(['ABX', 'Placebo'], fontsize=12)  # Set x-tick labels
   ax.set_xlabel("Treatment", fontsize=14)  # X-axis label
   ax.set_ylabel("log10(live bacteria/wet g)", fontsize=14)  # Y-axis label
   ax.set_title(title, fontsize=16)  # Title of the plot
   # Add a grid
   ax.grid(True, linestyle="--", alpha=0.6)  # Dashed grid lines
   # Save the plot as an image file
   plt.tight_layout()  # Adjust layout
   plt.savefig(output_file)  # Save as specified output file
   # Save the filtered data to a CSV file
   filtered_data.to_csv(f"output/{sample_type}_data.csv", index=False)  # Save without index
# Call the function to generate the fecal live bacteria plot
plot_fecal_live_bacteria(data)
# Call the function to generate violin plots for cecal and ileal samples
generate_violin_plot(
   data=data,
   sample_type='cecal',  # Specify sample type
   day=1,  # Specify experimental day
   title="Cecal live bacteria",  # Title of the plot
   output_file="images/cecal_graph.jpeg"  # Output file path
)
generate_violin_plot(
   data=data,
   sample_type='ileal',  # Specify sample type
   day=1,  # Specify experimental day
   title="Ileal live bacteria",  # Title of the plot
   output_file="images/ileal_graph.jpeg"  # Output file path
)

# Display a completion message

print("\nProcessing complete!")
print("The generated files are available in the following directories:")
print("- Graphs: 'images/'")
print("- Filtered CSV files: 'output/'")
 
