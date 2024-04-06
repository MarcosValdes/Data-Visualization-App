import streamlit as st 
import pandas as pd
import plotly.express as px

vehicles_df = pd.read_csv('vehicles_us.csv')

# we do some vehicles_df cleaning first:

# we change the 'date_posted' column into a datetime64 data type 
vehicles_df['date_posted'] = pd.to_datetime(vehicles_df['date_posted'])


# we substitute all the NaN values with integer 0
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].fillna(0)

# we change the datatype of the column to integers 
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].astype(int)


# we fill in model_year missing values with the columns average
vehicles_df['model_year'] = vehicles_df['model_year'].fillna(vehicles_df['model_year'].median())

# we fill in cylinders missing values
vehicles_df['cylinders'] = vehicles_df.groupby('model')['cylinders'].fillna(vehicles_df['cylinders'].median())

# we fill in odometer missing values
vehicles_df['odometer'] = vehicles_df.groupby('model')['odometer'].fillna(vehicles_df['odometer'].median())

# we fill in paint_color missing values
vehicles_df['paint_color'] = vehicles_df['paint_color'].fillna('unknown')


st.header('My Data Visualization Dashboard')

st.write('This is my vehicles DataFrame')
st.write(vehicles_df)

# preparing the data for the chart
model_price_df = vehicles_df[['model', 'price']]
grouped_models_data = model_price_df.groupby('model')
new_df = grouped_models_data.mean()
new_df = new_df.reset_index()

# histogram comparison: Price vs Model
# create the figure
fig = px.bar(new_df, x='model', y='price', title='Bar Chart Comparison: Total Price by Model', width=1800, height=500)
fig.update_xaxes(tickangle=40)

st.write('This is a price comparison between car models')
st.plotly_chart(fig)

# preparing the data for the scatter plot
odometer_vs_price_df = vehicles_df[['price', 'odometer']]

# scatter plot comparison: Odometer vs Price
# create the figure
fig = px.scatter(odometer_vs_price_df, x='price', y='odometer', title='Odometer vs Price Comparison')

st.write('This is a scatter plot comparison between the odometer and the car price')
st.plotly_chart(fig)

# We prepare a chart to display when interacting with the checkbox
# prepare the data
fig = px.violin(vehicles_df, x='condition', y='price', title='Violin Plot by Condition (Price)')
fig.update_layout(yaxis_range=[0, 100000])

st.write('Click the checkbox to show the extra chart below')

show_data = st.checkbox('Show Data')

if show_data:
    # display the extra chart
    st.plotly_chart(fig)
    st.write("We show the chart since the checkbox is been displayed")
else:
    st.write("Data is hidden since the checkbox is unchecked")
