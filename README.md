
# PhonePe Pulse Data Visualization

This web app allows the user to make interactive data analysis dashboard made with PhonePe pulse data.

Dataset:https://github.com/PhonePe/pulse




## Goal

The goal of this project is to make an interactive dashboard to analyse the PhonePe transactions and users to build your own understanding, insights and visualization on how digital payments have evolved over the years in India.
## Roadmap

- Data extraction - converting the unstructured data from phonepe pulse github resource to structured data and saving it as CSV file.
Data Extraction and Cleaning

- SQL migration - Importing the extracted CSV file to MySQL database.

- Visualization - With python (Pandas, Streamlit, Plotly) to make the web app.



## Installation
Packages to be installed to run this project.

```bash
  pip install mysql.connector
```
```bash
  pip install pandas
```
```bash
  pip install streamlit
```
```bash
  pip install plotly
```
## Guide

Importing the required packages to run this project.

```bash
import mysql.connector
import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
```
## Structured Data (CSV Files)

Converted data in the form of CSV files.

CSV_files
## Screenshots

This is the preview of the  web app.
![app_layout](https://github.com/HemachandarAravamuthan/PhonePe_Pulse_Data_visualization/assets/141393571/3026081d-b134-44d1-b097-b1ec3b2ce402)

Statewise transaction or user analysis by bar graph with year and quarter adjustment.
![State_transaction_count_bar_graph](https://github.com/HemachandarAravamuthan/PhonePe_Pulse_Data_visualization/assets/141393571/09c12100-aee4-4d3a-afb1-8a302762132a)

Transaction types yearly analysis.
![Payment_type_pie_chart](https://github.com/HemachandarAravamuthan/PhonePe_Pulse_Data_visualization/assets/141393571/517ece66-9176-4949-a1a9-16ab93cef60a)

Top state & district & postal code transaction analysis.
![Top_transaction_state_district_postalcode](https://github.com/HemachandarAravamuthan/PhonePe_Pulse_Data_visualization/assets/141393571/3dd0c3a2-57a4-4756-a5cd-41605c21b7b4)

Yearly analysis by selecting state.
![Statewise_analysis](https://github.com/HemachandarAravamuthan/PhonePe_Pulse_Data_visualization/assets/141393571/bb138b62-1396-47ad-b5df-b7b5828333d7)

## Appendix

This web app can enable you to understand the PhonePe data with interactive adjustment. With the same dataset by plotly dash and geoplotly we can achive the live geo visuals.


## Contact

email : hemachandar11@gmail.com

Linkedin : https://www.linkedin.com/in/hemachandar-aravamuthan-1594b1194/
