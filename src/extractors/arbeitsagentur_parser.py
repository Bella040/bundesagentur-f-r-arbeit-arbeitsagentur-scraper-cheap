thonimport logging
from datetime import datetime
from .utils_geo import compute_distance_km

class ArbeitsagenturParser:
    """
    Simulated parser for Arbeitsagentur job portal.
    This offline implementation generates structured job data from inputs.
    """

    def search_jobs(self, keyword: str, location: str, radius: int = 25):
        logging.info(f"Searching jobs for '{keyword}' near '{location}' (radius={radius}km)")

        # Simulated base coordinates for location
        coords = {
            "Berlin": (52.52, 13.4050),
            "Munich": (48.1351, 11.5820),
            "Hamburg": (53.5511, 9.9937)
        }
        lat, lon = coords.get(location, (52.52, 13.40))

        sample_jobs = [
            {
                "title": f"{keyword} Engineer",
                "reference": "REF-123456",
                "occupation": keyword,
                "employer": "TechCorp GmbH",
                "location": location,
                "region": "Berlin",
                "country": "Deutschland",
                "latitude": lat,
                "longitude": lon,
                "distance": compute_distance_km(lat, lon, lat + 0.01, lon + 0.01),
                "publication_date": str(datetime.now().date()),
                "modification_date": datetime.now().isoformat(),
                "start_date": str(datetime.now().date()),
                "link": "https://example.com/job",
                "link_to_profile": "https://www.arbeitsagentur.de/jobdetail/example"
            }
        ]

        return sample_jobs