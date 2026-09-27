import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

ADGUARD_URL = os.getenv("ADGUARD_URL")
USERNAME = os.getenv("ADGUARD_USERNAME")
PASSWORD = os.getenv("ADGUARD_PASSWORD")

def extract_raw_logs():
    endpoint = f"{ADGUARD_URL}/control/querylog"
    
    try:
        print("Fetching raw logs from AdGuard...")
        response = requests.get(endpoint, auth=(USERNAME, PASSWORD))
        response.raise_for_status() 
        
        # Extract the raw logs directly
        raw_data = response.json().get("data", [])
        
        # Save a 100-record sample of the true, unfiltered data
        sample_size = min(100, len(raw_data))
        with open("raw_telemetry.json", "w") as outfile:
            json.dump(raw_data[:sample_size], outfile, indent=4)
            
        print(f"Success! ✅ {sample_size} raw records saved to raw_telemetry.json.")
        
    except requests.exceptions.RequestException as e:
        print(f"Extraction Failed: {e}")

if __name__ == "__main__":
    extract_raw_logs()