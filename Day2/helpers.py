def get_reports(filneame):
    reports = []
    with open(filneame, "r") as file:
        for line in file.readlines():
            report = line.split()
            reports.append([int(x) for x in report])

    return reports
