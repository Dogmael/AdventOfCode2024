from helpers import get_reports


def check_report_safety(report):
    lastDiff = 0
    for i in range(1, len(report)):
        currentDiff = report[i] - report[i - 1]
        if abs(currentDiff) < 1 or abs(currentDiff) > 3 or currentDiff * lastDiff < 0:
            return False

        lastDiff = currentDiff
    return True


def count_safe_reports(reports):
    # safeReportsCount = 0

    # for report in reports:
    #     if check_report_safety(report):
    #         safeReportsCount += 1

    # return safeReportsCount

    return sum(1 for report in reports if check_report_safety(report))


reports = get_reports("input.txt")

print(count_safe_reports(reports))
