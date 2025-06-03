from typing import List, Dict

def read_csv(filepath: str) -> List[Dict[str, str]]:
    with open(filepath, encoding='utf-8') as f:
        lines = f.read().splitlines()
    headers = [h.strip() for h in lines[0].split(',')]
    result = []
    for line in lines[1:]:
        # пропускаем пустые строки
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(',')]
        # если в строке не хватает столбцов, пропускаем
        if len(values) != len(headers):
            continue
        row = dict(zip(headers, values))
        result.append(row)
    return result

def get_hourly_rate(row: dict) -> float:
    for key in ['hourly_rate', 'rate', 'salary']:
        if key in row:
            return float(row[key])
    raise ValueError("No hourly rate column found")
