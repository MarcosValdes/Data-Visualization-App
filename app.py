import streamlit as st 
import pandas as pd
import plotly.express as px

vehicles_df = pd.read_csv('vehicles_us.csv')

st.header('My Data Visualization Dashboard')

st.write('This is my vehicles DataFrame')
st.write(vehicles_df)

# preparing the data for the chart
model_price_df = vehicles_df[['model', 'price']]
grouped_models_data = model_price_df.groupby('model')
new_df = grouped_models_data.mean()
new_df = new_df.reset_index()
new_df

# histogram comparison: Price vs Model
# create the figure
fig = px.bar(new_df, x='model', y='price', title='Bar Chart Comparison: Total Price by Model', width=1800, height=500)
fig.update_xaxes(tickangle=40)

st.write('This is a price comparison between car models')
st.plotly_chart(fig)

# preparing the data for the scatter plot
odometer_vs_price_df = vehicles_df[['price', 'odometer']]
odometer_vs_price_df

#scatter plot comparison: Odometer vs Price
#create the figure
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


