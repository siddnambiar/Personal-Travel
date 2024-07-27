import streamlit as st

# Function to add a link with an icon and tooltip
def add_link(category, name, url, description, icon):
    st.markdown(f"""
    <div style="margin-bottom: 15px; border: 2px solid #4CAF50; border-radius: 10px; padding: 10px; background-color: #f9f9f9;">
        <span style="font-size: 1.5em; margin-right: 10px;">{icon}</span>
        <a href="{url}" target="_blank" title="{description}" style="font-size: 1.3em; text-decoration: none; color: #4CAF50;">
            <strong>{name}</strong>
        </a>
        <p style="margin-top: 5px; font-size: 1em; color: #555;">{description}</p>
    </div>
    """, unsafe_allow_html=True)

# Title of the page
st.markdown("""
    <div style="text-align: center; background-color: #4CAF50; padding: 20px; border-radius: 10px;">
        <h1 style="color: white; font-family: 'Comic Sans MS', cursive, sans-serif;">🌍✈️ Useful Travel Links ✈️🌍</h1>
    </div>
""", unsafe_allow_html=True)

# Description
st.markdown("""
    <div style="text-align: center; margin-top: 20px; font-family: 'Comic Sans MS', cursive, sans-serif;">
        <p style="font-size: 1.2em; color: #4CAF50;">
            Here is a collection of useful links to help you plan your travel. These resources cover a wide range of topics including flight booking, accommodation, travel tips, local attractions, and more. 
            You can add more links to this list as you discover new and helpful resources. Enjoy your journey! 🌟🚀
        </p>
    </div>
""", unsafe_allow_html=True)

# Travel Apps for Italy
st.markdown("""
    <h2 style="color: #4CAF50; font-family: 'Comic Sans MS', cursive, sans-serif;">🇮🇹 Travel Apps for Italy 🇮🇹</h2>
""", unsafe_allow_html=True)

# General Travel Apps
st.markdown("""
    <h3 style="color: #FF5722; font-family: 'Comic Sans MS', cursive, sans-serif;">📱 General Travel Apps</h3>
""", unsafe_allow_html=True)
add_link('General Travel Apps', 'Omio', 'https://www.omio.com', 'Compare and book trains, buses, and flights across Europe, including Italy.', '🌍')
add_link('General Travel Apps', 'Get Your Guide', 'https://www.getyourguide.com/-l169011/?ad_id=628087481036&ad_position=&adgroup_id=143214982478&campaign_id=16347902802&cmp=dce9147a91e34944a55799b7b-403208&cq_cmp=16347902802&cq_con=143214982478&cq_med=&cq_net=g&cq_plac=&cq_plt=gp&cq_pos=&cq_src=google_ads&cq_term=getyourguide+italy&device=c&feed_item_id=&gad_source=1&gclid=CjwKCAiA29auBhBxEiwAnKcSqk7k68dSIO2ApgOtSIZ5Tt2sz5598E-LZhbkAAql9RIADJT4WRmAlBoCuPUQAvD_BwE&keyword=getyourguide+italy&loc_physical_ms=9032812&match_type=e&partner_id=0JJQDRO&partner_visitor_id=&placement=&target_id=aud-607387271913%3Akwd-445217630328', 'Discover and book unique travel experiences and guided tours.', '🗺️')

# Transportation Apps
st.markdown("""
    <h3 style="color: #FF5722; font-family: 'Comic Sans MS', cursive, sans-serif;">🚗 Transportation Apps</h3>
""", unsafe_allow_html=True)
add_link('Transportation Apps', 'Trenitalia', 'https://www.trenitalia.com', 'Official app for navigating Italy’s train network, allowing ticket bookings and real-time updates.', '🚆')
add_link('Transportation Apps', 'Italo', 'https://www.italotreno.it', 'App for booking high-speed train travel across Italy.', '🚄')
add_link('Transportation Apps', 'Trainline', 'https://www.thetrainline.com', 'Simplifies train travel by comparing prices and booking tickets.', '🚊')
add_link('Transportation Apps', 'Free Now', 'https://apps.apple.com/us/app/freenow-taxi-and-more/id357852748', 'Taxi app for booking rides in cities where Uber is not available.', '🚖')

# Accommodation Apps
st.markdown("""
    <h3 style="color: #FF5722; font-family: 'Comic Sans MS', cursive, sans-serif;">🏨 Accommodation Apps</h3>
""", unsafe_allow_html=True)
add_link('Accommodation Apps', 'Hotel Tonight', 'https://www.hoteltonight.com', 'Book last-minute hotel stays, especially useful in lower season travel.', '🏨')

# Food and Dining Apps
st.markdown("""
    <h3 style="color: #FF5722; font-family: 'Comic Sans MS', cursive, sans-serif;">🍽️ Food and Dining Apps</h3>
""", unsafe_allow_html=True)
add_link('Food and Dining Apps', 'The Fork', 'https://www.thefork.com', 'Best restaurant reservation app in Europe, offering reviews and booking options.', '🍴')
add_link('Food and Dining Apps', 'Michelin Guide', 'https://guide.michelin.com', 'Discover top-rated restaurants and make reservations.', '⭐')
add_link('Food and Dining Apps', 'Deliveroo', 'https://www.deliveroo.it', 'Food delivery app connecting users with local restaurants.', '🍔')

# Currency and Budgeting Apps
st.markdown("""
    <h3 style="color: #FF5722; font-family: 'Comic Sans MS', cursive, sans-serif;">💸 Currency and Budgeting Apps</h3>
""", unsafe_allow_html=True)
add_link('Currency and Budgeting Apps', 'XE Currency', 'https://www.xe.com', 'Provides real-time exchange rates for managing travel budgets.', '💱')

# Language and Communication Apps
st.markdown("""
    <h3 style="color: #FF5722; font-family: 'Comic Sans MS', cursive, sans-serif;">🗣️ Language and Communication Apps</h3>
""", unsafe_allow_html=True)
add_link('Language and Communication Apps', 'Google Translate', 'https://translate.google.com', 'Essential for communication and understanding menus in Italian.', '🔤')

# Weather Apps
st.markdown("""
    <h3 style="color: #FF5722; font-family: 'Comic Sans MS', cursive, sans-serif;">🌦️ Weather Apps</h3>
""", unsafe_allow_html=True)
add_link('Weather Apps', 'Accuweather', 'https://www.accuweather.com', 'Offers short and long-range weather forecasts for various Italian cities.', '🌦')

# Other Useful Apps
st.markdown("""
    <h3 style="color: #FF5722; font-family: 'Comic Sans MS', cursive, sans-serif;">🔧 Other Useful Apps</h3>
""", unsafe_allow_html=True)
add_link('Other Useful Apps', 'WeTap', 'https://www.wetap.org', 'Locate water fountains to refill your bottles and save money.', '🚰')
add_link('Other Useful Apps', 'Rick Steves Audio Tours', 'https://www.ricksteves.com/watch-read-listen/audio/audio-tours/italy', 'Free audio tours for major attractions in Italy.', '🎧')
