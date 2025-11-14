thonimport json
import csv
from xml.etree.ElementTree import Element, tostring
from pathlib import Path

class Exporter:
    @staticmethod
    def export(data, output_dir: Path, fmt: str):
        output_dir.mkdir(parents=True, exist_ok=True)

        if fmt == "json":
            Exporter._to_json(data, output_dir / "export.json")
        elif fmt == "csv":
            Exporter._to_csv(data, output_dir / "export.csv")
        elif fmt == "xml":
            Exporter._to_xml(data, output_dir / "export.xml")
        elif fmt == "html":
            Exporter._to_html(data, output_dir / "export.html")

    @staticmethod
    def _to_json(data, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def _to_csv(data, path):
        if not data:
            return
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def _to_xml(data, path):
        root = Element("jobs")
        for item in data:
            job_el = Element("job")
            for k, v in item.items():
                child = Element(k)
                child.text = str(v)
                job_el.append(child)
            root.append(job_el)
        with open(path, "wb") as f:
            f.write(tostring(root))

    @staticmethod
    def _to_html(data, path):
        if not data:
            html = "<html><body><p>No data</p></body></html>"
        else:
            headers = data[0].keys()
            rows = "".join(
                "<tr>" + "".join(f"<td>{row[h]}</td>" for h in headers) + "</tr>"
                for row in data
            )
            html = f"""
            <html>
            <body>
                <table border="1">
                    <tr>{''.join(f'<th>{h}</th>' for h in headers)}</tr>
                    {rows}
                </table>
            </body>
            </html>
            """
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)