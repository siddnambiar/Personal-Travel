import streamlit as st
from datetime import datetime
import pandas as pd
import altair as alt

# Title of the page
st.title('Budget Calculator')

# User inputs
st.sidebar.header('Travel Details')
start_date = st.sidebar.date_input("Start Date", datetime(2024, 11, 22))
end_date = st.sidebar.date_input("End Date", datetime(2024, 12, 1))

if start_date >= end_date:
    st.error("End date must be after start date.")
else:
    # Calculate number of days
    num_days = (end_date - start_date).days

    # User inputs for costs
    st.sidebar.header('Budget Preferences')
    airfare_range = st.sidebar.slider('Airfare Range', 0, 2000, (500, 800))
    accommodation_range = st.sidebar.slider('Accommodation per Night', 0, 500, (60, 150))
    meal_range = st.sidebar.slider('Meal per Day', 0, 200, (30, 50))
    transport_per_day = st.sidebar.slider('Transport per Day', 0, 100, 20)
    entertainment_per_day = st.sidebar.slider('Entertainment per Day', 0, 100, 20)
    shopping_per_day = st.sidebar.slider('Shopping per Day', 0, 100, 20)
    misc_per_day = st.sidebar.slider('Miscellaneous per Day', 0, 100, 10)

    # Extract min and max values from sliders
    airfare_min, airfare_max = airfare_range
    accommodation_min_per_night, accommodation_max_per_night = accommodation_range
    meal_min_per_day, meal_max_per_day = meal_range

    # Calculations
    total_accommodation_min = num_days * accommodation_min_per_night
    total_accommodation_max = num_days * accommodation_max_per_night
    total_meal_min = num_days * meal_min_per_day
    total_meal_max = num_days * meal_max_per_day
    total_transport = num_days * transport_per_day
    total_entertainment = num_days * entertainment_per_day
    total_shopping = num_days * shopping_per_day
    total_misc = num_days * misc_per_day

    total_min_budget = (airfare_min + total_accommodation_min + total_meal_min + 
                        total_transport + total_entertainment + total_shopping + total_misc)
    total_max_budget = (airfare_max + total_accommodation_max + total_meal_max + 
                        total_transport + total_entertainment + total_shopping + total_misc)

    # Prepare data for charts
    budget_data = {
        'Category': ['Accommodation', 'Meals', 'Transport', 'Entertainment', 'Shopping', 'Miscellaneous', 'Airfare'],
        'Min Cost': [total_accommodation_min, total_meal_min, total_transport, total_entertainment, total_shopping, total_misc, airfare_min],
        'Max Cost': [total_accommodation_max, total_meal_max, total_transport, total_entertainment, total_shopping, total_misc, airfare_max]
    }

    df = pd.DataFrame(budget_data)

    # Display results
    st.subheader("Estimated Budget")
    st.markdown(f"""
    <style>
    .budget-item {{
        font-size: 1.2em;
        margin-bottom: 10px;
    }}
    .budget-value {{
        font-weight: bold;
        color: #2ecc71;
    }}
    .icon {{
        display: inline-block;
        width: 24px;
        height: 24px;
        margin-right: 10px;
    }}
    </style>
    <div class="budget-item"><span class="icon">🛏️</span><strong>Total Accommodation Cost:</strong> <span class="budget-value">${total_accommodation_min} — ${total_accommodation_max}</span></div>
    <div class="budget-item"><span class="icon">🍽️</span><strong>Total Meal Cost:</strong> <span class="budget-value">${total_meal_min} — ${total_meal_max}</span></div>
    <div class="budget-item"><span class="icon">🚗</span><strong>Total Transport Cost:</strong> <span class="budget-value">${total_transport}</span></div>
    <div class="budget-item"><span class="icon">🎭</span><strong>Total Entertainment Cost:</strong> <span class="budget-value">${total_entertainment}</span></div>
    <div class="budget-item"><span class="icon">🛍️</span><strong>Total Shopping Cost:</strong> <span class="budget-value">${total_shopping}</span></div>
    <div class="budget-item"><span class="icon">💡</span><strong>Total Miscellaneous Cost:</strong> <span class="budget-value">${total_misc}</span></div>
    <div class="budget-item"><span class="icon">✈️</span><strong>Airfare:</strong> <span class="budget-value">${airfare_min} — ${airfare_max}</span></div>
    <div class="budget-item"><span class="icon">💰</span><strong>Overall Estimated Budget:</strong> <span class="budget-value">${total_min_budget} — ${total_max_budget}</span></div>
    """, unsafe_allow_html=True)

    # Visualize the data
    st.subheader("Cost Breakdown")
    
    st.bar_chart(df.set_index('Category'))

    st.subheader("Cost Distribution")

    def create_pie_chart(data, title):
        chart = alt.Chart(data).mark_arc().encode(
            theta=alt.Theta(field="Cost", type="quantitative"),
            color=alt.Color(field="Category", type="nominal"),
            tooltip=["Category", "Cost"]
        ).properties(title=title)
        return chart

    min_cost_pie_data = pd.DataFrame({
        'Category': ['Accommodation', 'Meals', 'Transport', 'Entertainment', 'Shopping', 'Miscellaneous', 'Airfare'],
        'Cost': [total_accommodation_min, total_meal_min, total_transport, total_entertainment, total_shopping, total_misc, airfare_min]
    })

    max_cost_pie_data = pd.DataFrame({
        'Category': ['Accommodation', 'Meals', 'Transport', 'Entertainment', 'Shopping', 'Miscellaneous', 'Airfare'],
        'Cost': [total_accommodation_max, total_meal_max, total_transport, total_entertainment, total_shopping, total_misc, airfare_max]
    })
    
    st.altair_chart(create_pie_chart(min_cost_pie_data, "Minimum Cost Distribution"), use_container_width=True)
    st.altair_chart(create_pie_chart(max_cost_pie_data, "Maximum Cost Distribution"), use_container_width=True)
