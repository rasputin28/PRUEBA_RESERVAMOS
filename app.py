import streamlit as st
import os
import pandas as pd
from utils.api import search_city
from utils.data_processing import preprocess_rooms_data, format_room_data

# Title of the app
st.title("Full Stack Data Engineer Challenge")

logo_path = os.path.join(os.path.dirname(__file__), "data", "logo.svg")
st.image(logo_path, width=600)

# Text input
user_input = st.text_input("¿A dónde quieres ir?")

if user_input:
    city_data = search_city(user_input)
    if city_data:
        st.write("Hospedajes en", city_data['city_name'])

        # Load and process the data
        rooms_data_path = os.path.join(os.path.dirname(__file__), "data", "rooms_data.csv")
        rooms_data = pd.read_csv(rooms_data_path)
        filtered_df = preprocess_rooms_data(rooms_data, city_data['city_name'])

        if filtered_df.empty:
            st.write("No se encontraron resultados para la ciudad especificada.")
        else:
            formatted_df = format_room_data(filtered_df)

            # Extract numeric values for the slider
            min_price_value = int(filtered_df['price_per_night'].min())
            max_price_value = int(filtered_df['price_per_night'].max())

            # Add sliders for filtering
            min_price, max_price = st.slider(
                "Precio por Noche",
                min_value=min_price_value,
                max_value=max_price_value,
                value=(min_price_value, max_price_value)
            )

            min_rating, max_rating = st.slider(
                "Calificación",
                min_value=float(filtered_df['rating_overall'].min()),
                max_value=float(filtered_df['rating_overall'].max()),
                value=(float(filtered_df['rating_overall'].min()), float(filtered_df['rating_overall'].max()))
            )

            # Convert 'Precio por Noche' back to numeric for filtering
            formatted_df['Precio por Noche'] = formatted_df['Precio por Noche'].replace('[\$,]', '', regex=True).astype(float)

            # Filter the data based on slider values
            filtered_df = formatted_df[
                (formatted_df['Precio por Noche'] >= min_price) & 
                (formatted_df['Precio por Noche'] <= max_price) & 
                (formatted_df['Calificación'] >= min_rating) & 
                (formatted_df['Calificación'] <= max_rating)
            ]

            # Extract unique amenities
            all_amenities = []
            for index in formatted_df.index:
                amenities_list = formatted_df.loc[index, 'Amenidades'].replace('[', '').replace(']', '').replace('"', '').split(', ')
                for amenity in amenities_list:
                    all_amenities.append(amenity)

            unique_amenities = list(set(all_amenities))
            unique_amenities = [amenity for amenity in unique_amenities if amenity]

            # Add checkboxes for amenities
            selected_amenities = []
            for amenity in unique_amenities:
                if st.checkbox(amenity):
                    selected_amenities.append(amenity)

            # Filter the data based on selected amenities
            if selected_amenities:
                filtered_df = filtered_df[filtered_df['Amenidades'].apply(lambda x: all(amenity in x for amenity in selected_amenities))]

            # Initialize session state for sorting order
            if 'sort_order' not in st.session_state:
                st.session_state.sort_order = 'asc'

            # Toggle sorting order
            if st.button('Ordenar por Precio'):
                st.session_state.sort_order = 'desc' if st.session_state.sort_order == 'asc' else 'asc'

            # Sort the filtered data by 'Precio por Noche'
            filtered_df = filtered_df.sort_values(by='Precio por Noche', ascending=(st.session_state.sort_order == 'asc'))

            # Display the filtered and sorted data
            if filtered_df.empty:
                st.write("No se encontraron resultados")
            else:
                for index, row in filtered_df.iterrows():
                    st.write(f"Hospedaje: {row['Hospedaje']}")
                    st.write(f"Precio por Noche: ${row['Precio por Noche']:.2f}")
                    if row['Amenidades']:
                        st.write(f"Amenidades: {row['Amenidades']}")
                    st.write(f"Calificación: {row['Calificación']}")
                    st.write("---")