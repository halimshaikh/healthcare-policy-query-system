import sqlite3
import pandas as pd

conn = sqlite3.connect("healthcare_large.db")

# Load CSVs directly from root
hospitals = pd.read_csv("hospitals_large.csv")
resources = pd.read_csv("hospital_resources_large.csv")
districts = pd.read_csv("district_health_large.csv")
emergencies = pd.read_csv("emergency_requests_large.csv")

# Save into SQLite
hospitals.to_sql("hospitals", conn, if_exists="replace", index=False)
resources.to_sql("hospital_resources_daily", conn, if_exists="replace", index=False)
districts.to_sql("district_health", conn, if_exists="replace", index=False)
emergencies.to_sql("emergency_requests", conn, if_exists="replace", index=False)

conn.close()
print("✅ CSV data imported into healthcare_large.db successfully!")
