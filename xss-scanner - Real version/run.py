from scanner import XSSScanner
from reporter import report_html

if __name__ == "__main__":
    url = "http://localhost:5000/test"  # Change when scanning
    params = ["q", "search", "id"]

    scanner = XSSScanner()

    all_results = []
    for ctx in ["text", "attribute-value", "attribute-name"]:
        print(f"Scanning context: {ctx}")
        results = scanner.scan(url, params, method="GET", context=ctx)
        all_results.extend(results)

    report_html(all_results)
