# CY-Antibio-Tech Project  
**Kamilya Abbadi**  
## General Description  
This project automates the generation of visualizations and filtered datasets from experimental data provided by laboratories. It analyzes the impact of antibiotic treatments on the gut microbiota of mice compared to a placebo. The application processes CSV files, generates charts, and outputs filtered datasets for further analysis.  
---
## Features  
### 1. **Data Loading**  
- Reads CSV files with predefined columns.  
- Supports specific delimiters (;) and handles parsing errors.  
- Cleans columns (`sample_type`, `experimental_day`, etc.) to ensure compatibility with the program.  
### 2. **Generated Visualizations**  
- **Multi-segment Chart:**  
 - Shows the evolution of live bacteria quantity in fecal matter for each mouse.  
 - Visual separation of antibiotic-treated and placebo groups.  
- **Violin Charts:**  
 - Displays the distribution of bacterial quantity in cecal and ileal samples.  
 - Compares treated and untreated groups.  
 - Charts generated for multiple experimental days.  
### 3. **Output Data Files**  
- Creates filtered CSV files for each visualization, allowing detailed analysis:  
 - Fecal data.  
 - Cecal data for specified days.  
 - Ileal data for specified days.  
### 4. **Compatibility**  
- Supports CSV files of varying sizes (small, medium, large, huge).  
- Adapts to different numbers of mice and experimental days.  
---
## File Organization  
- **input/**: Contains raw CSV files provided by the laboratory.  
- **images/**: Stores generated visualizations.  
- **output/**: Contains filtered CSV files corresponding to the visualizations.  
- **Main Script**: The Python file located at the project's root.  
---
## Instructions to Run the Program  
### Prerequisites  
- Python 3.7+  
- Install required libraries:  
 ```bash
 pip install pandas matplotlib numpy
 ```
Steps
1 Create the necessary directories:
```bash
 mkdir input images output
 ```
2 Place the CSV file in the input/ folder.

3 Run the Python script from the root directory:
```bash
 python main.py
 ```
4 Generated visualizations will appear in the images/ folder.

5 Filtered CSV files will be saved in the output/ folder.

---
## Functional Limitations  
### Unimplemented Features
• Automatic validation of column content (e.g., type checks).
• Advanced handling of missing or abnormal values in numeric columns.
### Partially Implemented Features
• Charts for unspecified days in the data display warning messages instead of full error handling.
• Handling outliers (e.g., negative values) relies on basic transformations (e.g., logarithmic scaling).

## Challenges Encountered
### Data Parsing
• Malformed CSV files required adjustments to handle delimiters and errors.
### Dynamic Day Management
• Adapting the program to handle an indefinite number of experimental days required redesigning filter and loop logic.
### Visualization Consistency
• Ensuring consistent colors and legends across visualizations required extensive testing.

---
## Useful Resources
• Pandas Documentation
• Matplotlib Documentation
• Numpy Documentation
