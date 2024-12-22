# CY-Antibio-Tech Project  
**Kamilya Abbadi**  
## General Description  
This project automates the generation of visualizations and filtered datasets from experimental data provided by laboratories. It analyzes the impact of antibiotic treatments on the gut microbiota of mice compared to a placebo. The application processes CSV files, generates charts, and outputs filtered datasets for further analysis.  
---

## Instructions to Run the Program  
### Prerequisites  
- Install required libraries:  
 ```bash
 pip install pandas matplotlib numpy
 ```
Steps
1 Create the necessary directories:
```bash
 mkdir input images output
 ```
2 Place the CSV file in the input/ folder an edit the code to put your filepath.

3 Run the Python script from the root directory:
```bash
 python main.py
 ```
4 Generated visualizations will appear in the images/ folder.

5 Filtered CSV files will be saved in the output/ folder.

---
## Functional Limitations  
### Unimplemented Features
• My code does not support processing data with experimental days that differ across entries.

## Challenges Encountered
### Data Parsing
• Malformed CSV files required adjustments to handle delimiters and errors.
### Dynamic Day Management
• Adapting the program to handle an indefinite number of experimental days required redesigning filter and loop logic.
### Visualization Consistency
• Ensuring consistent colors and legends across visualizations required extensive testing.
