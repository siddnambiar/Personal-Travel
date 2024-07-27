import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Italy Trip Planner",
    page_icon="🌍",
    layout="wide"
)

# Apply custom CSS for enhanced styling
st.markdown("""
    <style>
    .main-title {
        font-size: 3.5em;
        color: #2e4053;
        text-align: center;
        margin-top: 20px;
        font-weight: bold;
    }
    .intro-text {
        font-size: 1.5em;
        color: #566573;
        text-align: center;
        margin-bottom: 30px;
    }
    .features-title {
        font-size: 2.5em;
        color: #2874a6;
        text-align: center;
        margin-top: 30px;
        font-weight: bold;
    }
    .features-list {
        font-size: 1.3em;
        color: #2e4053;
        margin-left: 20px;
        list-style-type: none;
        padding: 0;
        text-align: left;
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
    }
    .features-list li {
        margin-bottom: 15px;
        width: 45%;
    }
    .feature-icon {
        font-size: 1.5em;
        color: #2874a6;
        margin-right: 10px;
    }
    .feature-description {
        display: inline;
    }
    .personal-note {
        font-size: 1.2em;
        color: #2874a6;
        text-align: center;
        margin-top: 50px;
        font-style: italic;
    }
    .threads-link {
        font-size: 1.2em;
        color: #2874a6;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the page
st.markdown('<div class="main-title">Italy Trip Planner Home</div>', unsafe_allow_html=True)

# Introduction text
st.markdown("""
    <div class="intro-text">
        Welcome to the Italy Trip Planner! This app is a fun project I built to learn more about Streamlit's features and functionalities. 
        Use the navigation on the left to access different tools and resources.
    </div>
""", unsafe_allow_html=True)

# Available features section
st.markdown('<div class="features-title">Available Features:</div>', unsafe_allow_html=True)
st.markdown("""
    <ul class="features-list">
        <li><span class="feature-icon">💰</span><span class="feature-description"><strong>Budget Calculator:</strong> Estimate your trip expenses, including accommodation, meals, transport, and more.</span></li>
        <li><span class="feature-icon">🔗</span><span class="feature-description"><strong>Useful Travel Links:</strong> Access a curated list of travel apps and resources to help you plan every aspect of your trip.</span></li>
        <li><span class="feature-icon">💡</span><span class="feature-description"><strong>Travel Tips:</strong> Get valuable tips and recommendations for making the most out of your trip to Italy.</span></li>
    </ul>
""", unsafe_allow_html=True)

# Additional information and welcome message
st.markdown("""
    <div class="intro-text">
        Whether you're planning a romantic getaway, a family vacation, or a solo adventure, our tools and resources are here to make your trip planning seamless and enjoyable. 
        Navigate through the pages using the sidebar to get started and explore all the features we offer!
    </div>
""", unsafe_allow_html=True)

# Personal note
st.markdown("""
    <div class="personal-note">
        This project was created for fun and learning by a regular Data Scientist working for the Military Industrial complex, 
        who is a self-proclaimed man of peace and kindness. For random musings and silly posts, feel free to check out my 
        <a href="https://www.threads.net/@dar_devilry" target="_blank">Threads profile</a>.
    </div>
""", unsafe_allow_html=True)
