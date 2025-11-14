thonimport json
import logging
from pathlib import Path
from extractors.arbeitsagentur_parser import ArbeitsagenturParser
from outputs.exporters import Exporter

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

def main():
    base = Path(__file__).resolve().parent.parent
    input_file = base / "data" / "inputs.sample.json"

    if not input_file.exists():
        raise FileNotFoundError("inputs.sample.json not found.")

    with open(input_file, "r", encoding="utf-8") as f:
        params = json.load(f)

    parser = ArbeitsagenturParser()
    job_list = parser.search_jobs(
        keyword=params.get("keyword"),
        location=params.get("location"),
        radius=params.get("radius_km", 25)
    )

    logging.info(f"Extracted {len(job_list)} jobs")

    out_dir = base / "data"
    Exporter.export(job_list, out_dir, "json")
    Exporter.export(job_list, out_dir, "csv")
    Exporter.export(job_list, out_dir, "xml")
    Exporter.export(job_list, out_dir, "html")

    logging.info("Export complete.")

if __name__ == "__main__":
    main()