from scanner import Scanner
from reporter import report_html

def main():
    sc = Scanner()

    target = "http://localhost:5000/echo"
    params = {'q': 'test', 'id': '1'}
    contexts = ['attribute-name', 'attribute-value', 'text']
    sc.scan_get(target, params, contexts)

    report_html(sc.results)

if __name__ == '__main__':
    main()
