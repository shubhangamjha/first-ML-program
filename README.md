# first-ML-program
import pandas as pd
India_Menu_path = 'C:/Users/Shubhangam/Desktop/ML/CSV files/India_Menu.csv'
India_menu_data=pd.read_csv(India_Menu_path)
India_menu_data.describe()
India_menu_data.columns
India_menu_data = India_menu_data.dropna(axis=0)
y = India_menu_data.Price
India_menu_features = ['Menu_Category', 'Menu_Items', 'Per_Serve_Size', 'Energy _(kCal)', 'Protein_(g)']
x=India_menu_data[India_menu_features]
x.describe()
x.head()
