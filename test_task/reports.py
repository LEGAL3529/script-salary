from typing import List, Dict
from models import Employee
import json

def payout_report(employees: List[Employee]) -> str:
    by_department: Dict[str, List[Employee]] = {}
    for emp in employees:
        by_department.setdefault(emp.department, []).append(emp)
    lines = []
    for dept, emps in by_department.items():
        lines.append(f"{dept}")
        total_hours = 0
        total_payout = 0
        for emp in emps:
            payout = emp.hours * emp.rate
            total_hours += emp.hours
            total_payout += payout
            lines.append(f"--------------- {emp.name:15} {int(emp.hours):>5} {int(emp.rate):>4} ${int(payout):>7}")
        # Итоги — часы и payout
        lines.append(f"{' ' * 32}{int(total_hours):>5}{' ' * 6}${int(total_payout):>7}")
        lines.append("")  # Пустая строка между отделами
    return '\n'.join(lines)

def payout_report_json(employees: List[Employee]) -> str:
    """Формирует payout-отчёт в формате JSON."""
    by_department: Dict[str, List[Dict]] = {}
    for emp in employees:
        payout = emp.hours * emp.rate
        by_department.setdefault(emp.department, []).append({
            'name': emp.name,
            'hours': int(emp.hours),
            'rate': int(emp.rate),
            'payout': int(payout)
        })
    result = []
    for dept, emps in by_department.items():
        total_hours = sum(emp['hours'] for emp in emps)
        total_payout = sum(emp['payout'] for emp in emps)
        result.append({
            'department': dept,
            'employees': emps,
            'total_hours': total_hours,
            'total_payout': total_payout
        })
    return json.dumps(result, indent=2, ensure_ascii=False)
