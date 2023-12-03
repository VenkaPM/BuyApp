import openpyxl as openpyxl
from django.shortcuts import render
from openpyxl.cell import cell


def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {}

    # return render(request, 'index.html', context)

    if "GET" == request.method:
        return render(request, 'index.html', {})
    else:
        excel_file = request.FILES['excel_file']

        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb['Sheet1']
        print(worksheet)

        excel_data = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)

        return render(request, 'index.html', {'excel_data': excel_data}, context)


def info(request):
    return render(request, 'info.html')

