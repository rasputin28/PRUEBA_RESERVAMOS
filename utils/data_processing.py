def preprocess_rooms_data(rooms_data, city_name):
    # Filtrar datos de habitaciones por ciudad y seleccionar columnas relevantes
    filtered_df = rooms_data.loc[rooms_data['city'].str.lower() == city_name.lower()]
    filtered_df = filtered_df[['title', 'price_per_night', 'amenities', 'rating_overall']]
    # Convertir 'price_per_night' a tipo float
    filtered_df['price_per_night'] = filtered_df['price_per_night'].replace('[\$,]', '', regex=True).astype(float)
    return filtered_df

def format_room_data(room_data):
    # Formatear datos de habitaciones para visualización
    formatted_data = room_data.copy()
    formatted_data['Precio por Noche'] = formatted_data['price_per_night'].apply(lambda x: f"${x:.2f}")
    formatted_data['Amenidades'] = formatted_data['amenities'].apply(lambda x: x.replace("[", "").replace("]", "").replace("'", ""))
    formatted_data['Hospedaje'] = formatted_data['title']
    formatted_data['Calificación'] = formatted_data['rating_overall']
    # Eliminar columnas originales no formateadas
    formatted_data = formatted_data.drop(columns=['price_per_night', 'amenities', 'title', 'rating_overall'])
    return formatted_data