from helpers import get_reports


def check_report_safety(report, sub_report=False):
    lastDiff = 0

    for i in range(1, len(report)):
        currentDiff = report[i] - report[i - 1]
        if abs(currentDiff) < 1 or abs(currentDiff) > 3 or currentDiff * lastDiff < 0:
            if sub_report:
                return False
            else:
                # OPTION 1
                # sub_report_1, sub_report_2, sub_report_3 = report.copy(), report.copy(), report.copy()  # Attention, sinon c'est un type reference et on va modifier report lors de modification de sub_report_1 et sub_report_2
                # del sub_report_1[i - 2]
                # del sub_report_2[i - 1]
                # del sub_report_3[i]

                # OPTION 2
                sub_report_1 = [item for idx, item in enumerate(report) if idx != i]
                sub_report_2 = [item for idx, item in enumerate(report) if idx != i - 1]
                sub_report_3 = [item for idx, item in enumerate(report) if idx != i - 2] # Ne pas oublier le cas où l'élement à supprimé est à i-2 avec il permet de changer le signe ! ex : [71, 69, 70, 71, 72, 75] (l'erreur est trouvé pour i = 2 mais la solution est de retiré i = 0 pour ne pas avoir d'inversion de signe)

                return check_report_safety(sub_report_1, True) or check_report_safety(sub_report_2, True) or check_report_safety(sub_report_3, True)

        lastDiff = currentDiff
    return True


def count_safe_reports(reports):
    return sum(1 for report in reports if check_report_safety(report))

reports = get_reports("input.txt")
print(count_safe_reports(reports))