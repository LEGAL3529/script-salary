import argparse
import os
import sys
from parser import parse_employees
from reports import payout_report, payout_report_json

REPORTS = {
    'payout': payout_report,
    'payout_json': payout_report_json,
}

def main() -> None:
    parser = argparse.ArgumentParser(
        description='Payroll Report Script'
    )
    parser.add_argument('files', nargs='+', help='Пути к CSV-файлам')
    parser.add_argument('--report', required=True, help='Тип отчёта')
    args = parser.parse_args()

    # Проверка: есть ли все файлы
    for file in args.files:
        if not os.path.isfile(file):
            print(f"Ошибка: файл не найден — {file}")
            sys.exit(1)

    # Проверка: есть ли отчёт такого типа
    if args.report not in REPORTS:
        print(f"Ошибка: неизвестный тип отчёта — '{args.report}'. Допустимые: {', '.join(REPORTS.keys())}")
        sys.exit(1)

    # Парсинг сотрудников с обработкой ошибок
    try:
        employees = parse_employees(args.files)
    except KeyError as e:
        print(f"Ошибка: не хватает обязательной колонки в файле: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при обработке файлов: {e}")
        sys.exit(1)

    print(REPORTS[args.report](employees))

if __name__ == '__main__':
    main()
