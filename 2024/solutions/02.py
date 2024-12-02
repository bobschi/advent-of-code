import aocd
import typer

app = typer.Typer()


def get_data() -> list[int]:
    data = aocd.get_data(day=2, year=2024).split("\n")
    return list(list(map(int, line.split())) for line in data)


def is_monotone(report: list[int]) -> bool:
    return report == sorted(report) or report == sorted(report, reverse=True)


def diffs_in_bounds(report: list[int]) -> bool:
    differences = (abs(a - b) for a, b in zip(report, report[1:]))
    return all(1 <= difference <= 3 for difference in differences)


def is_safe(report: list[int]) -> bool:
    return is_monotone(report) and diffs_in_bounds(report)


@app.command()
def part1() -> None:
    reports = get_data()
    safe_reports = [is_safe(report) for report in reports]
    aocd.submit(sum(safe_reports), "a", day=2, year=2024)


@app.command()
def part2() -> None:
    reports = get_data()
    safe_reports = []
    for report in reports:
        if is_safe(report):
            safe_reports.append(True)
        else:
            for index in range(len(report)):
                problem_dampened_report = report[:index] + report[index + 1 :]
                if is_safe(problem_dampened_report):
                    safe_reports.append(True)
                    break
            safe_reports.append(False)
    aocd.submit(sum(safe_reports), "b", day=2, year=2024)
