# E-Commerce Public Data Analysis with Python - Dicoding

## Overview
This project dedicated to analysis and visualizing a Bike Sharing Dataset, to see users behaviour and bussiness performance.

## Project Structure
- `dashboard/`: This directory contains `dashboard.py` and `main_data.csv` which are used to create an interactive dashboard.
- `datasets/`: This directory contains raw dataset.
- `notebook.ipynb`: This Jupyter Notebook file is used to perform data analysis.
- `requirements.txt`: This file lists all required Python libraries to this projct.
- `README.md`: This documentation file.

## Installation
1. Clone this repository to your local machine:
   ```
   git clone https://github.com/agoritma/bike-analysis.git
   ```
2. Go to the project directory
   ```
   cd bike-analysis
   ```
3. Install the required Python libraries by running this command:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. **Data Wrangling**: Explore and run the data management scripts available in the `notebook.ipynb` file to prepare and clean the data for analysis, you can run each cell one by one or you can run them all at once.

2. **Visualization**: Experience interactive data exploration by running the Streamlit dashboard:
   ```
   cd dashboard
   streamlit run dashboard.py
   ```
   or you can do it directly without changing the directory
   ```
   streamlit run ./dashboard/dashboard.py
   ```
   and then Access the dashboard in your favorite web browser at `http://localhost:8501`.

## Data Sources
For this project i used a Bike Sharing Dataset [Bike Sharing Dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view) offered by [Dicoding](https://www.dicoding.com/).

Feel free to explore the my simple dashboard [Bike Sharing Dashboard](https://ahmadghozali-bike-sharing.streamlit.app/) and explore useful information interactively there.

Copyright 2024 - Ahmad Ghozali