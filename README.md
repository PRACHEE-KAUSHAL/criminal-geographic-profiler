# 📍 Criminal Geographic & Behavioral Profiler
### Spatial Clustering and Behavioral Hotspot Analysis Using Unsupervised ML

---

## 🔍 Investigation Overview
In criminal psychology, environmental criminology states that offenders operate within predictable spatial routines (their "awareness space"). Criminal behavior is rarely spatially random; it is shaped by opportunity, cognitive friction, and geographic comfort zones.

This project translates **qualitative behavioral profiling principles** into an **unsupervised spatial analytics pipeline**. By analyzing crime incidence records across geographic coordinates and temporal dimensions, this system detects crime density hotspots, clusters Modus Operandi (M.O.), and surfaces high-risk temporal windows.

---

## 🎯 Key Questions & Hypotheses
1. **Spatial Anchor Hypothesis:** Do high-severity offenses cluster around specific environmental transit/commercial anchors?
2. **Temporal Rhythms:** At what specific diurnal cycles (time of day / day of week) do distinct offense types peak?
3. **Behavioral Hotspots:** Can density-based clustering (**DBSCAN**) isolate tight geographic clusters while ignoring background urban noise?

---

## 🛠️ Technical Stack
- **Data Engineering:** Python, Pandas, NumPy
- **Spatial Analytics & Geospatial Mapping:** Folium, Geopandas
- **Unsupervised Machine Learning:** DBSCAN (Density-Based Spatial Clustering of Applications with Noise), K-Means
- **Visualization:** Matplotlib, Seaborn

---

## 💡 Key Behavioral Insights
- **Density Over Dispersal:** While general property crime disperses across commercial corridors, severe offenses exhibit tight clustering within a 0.8 km operational radius.
- **The "Awareness Space" Signature:** Repeat behavioral patterns peak during transition hours (18:00–22:00), reflecting offender familiarity with localized foot-traffic patterns.

---

## 🏢 Enterprise Application
The algorithms used to model criminal geographic behavior translate directly to enterprise risk and commercial analytics:
- **Financial Fraud Analytics:** Detecting clustered coordinated fraud attacks across merchant locations or IP subnets.
- **Cybersecurity & Threat Intel:** Geospatial and network anomaly detection for unauthorized intrusion attempts.
- **Supply Chain Logistics:** Route risk scoring and predictive asset protection.

---
**Author:** [Prachi Kaushal](https://www.linkedin.com/in/prachi-kaushal-63a395231/) | Data Analyst & Behavioral Risk Modeler
