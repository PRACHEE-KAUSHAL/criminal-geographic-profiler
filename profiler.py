"""
Criminal Geographic & Behavioral Profiler
Author: Prachi Kaushal
Description: Spatial clustering and behavioral density analysis of crime records
             using DBSCAN and interactive Folium geospatial mapping.
"""

import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
import folium
from folium.plugins import HeatMap, MarkerCluster

def load_or_generate_data(num_samples=500):
    np.random.seed(42)
    center_lat, center_lon = 41.8781, -87.6298  # Chicago reference center
    
    zone1_lat = np.random.normal(center_lat + 0.02, 0.005, int(num_samples * 0.4))
    zone1_lon = np.random.normal(center_lon - 0.01, 0.005, int(num_samples * 0.4))
    
    zone2_lat = np.random.normal(center_lat - 0.015, 0.004, int(num_samples * 0.35))
    zone2_lon = np.random.normal(center_lon + 0.02, 0.004, int(num_samples * 0.35))
    
    noise_lat = np.random.uniform(center_lat - 0.04, center_lat + 0.04, int(num_samples * 0.25))
    noise_lon = np.random.uniform(center_lon - 0.04, center_lon + 0.04, int(num_samples * 0.25))
    
    lats = np.concatenate([zone1_lat, zone2_lat, noise_lat])
    lons = np.concatenate([zone1_lon, zone2_lon, noise_lon])
    
    crime_types = np.random.choice(
        ["Burglary", "Aggravated Robbery", "Larceny", "Motor Vehicle Theft"],
        size=len(lats),
        p=[0.25, 0.35, 0.25, 0.15]
    )
    
    hours = np.random.choice(range(24), size=len(lats))
    
    df = pd.DataFrame({
        "Incident_ID": [f"INC-{i:05d}" for i in range(1, len(lats) + 1)],
        "Crime_Type": crime_types,
        "Latitude": lats,
        "Longitude": lons,
        "Hour": hours
    })
    
    return df

def run_dbscan_clustering(df, eps_km=0.5, min_samples=10):
    kms_per_radian = 6371.0088
    epsilon = eps_km / kms_per_radian
    coords = np.radians(df[['Latitude', 'Longitude']])
    
    db = DBSCAN(eps=epsilon, min_samples=min_samples, metric='haversine')
    df['Cluster'] = db.fit_predict(coords)
    return df

def generate_interactive_map(df, output_html="crime_hotspots.html"):
    center_lat = df['Latitude'].mean()
    center_lon = df['Longitude'].mean()
    
    crime_map = folium.Map(location=[center_lat, center_lon], zoom_start=12, tiles="CartoDB dark_matter")
    heat_data = [[row['Latitude'], row['Longitude']] for _, row in df.iterrows()]
    HeatMap(heat_data, radius=12, blur=15, min_opacity=0.4).add_to(crime_map)
    
    marker_cluster = MarkerCluster(name="Identified Incidents").add_to(crime_map)
    for _, row in df.iterrows():
        color = "red" if row['Cluster'] != -1 else "gray"
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=4,
            color=color,
            fill=True,
            fill_opacity=0.7,
            popup=f"<b>ID:</b> {row['Incident_ID']}<br><b>Type:</b> {row['Crime_Type']}<br><b>Cluster:</b> {row['Cluster']}<br><b>Hour:</b> {row['Hour']}:00"
        ).add_to(marker_cluster)
    
    crime_map.save(output_html)
    print(f"[✓] Map saved to {output_html}")

if __name__ == "__main__":
    data = load_or_generate_data()
    clustered_data = run_dbscan_clustering(data, eps_km=0.6, min_samples=8)
    generate_interactive_map(clustered_data)
