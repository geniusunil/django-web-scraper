from django.shortcuts import render
from django.http import HttpResponse
import csv

def comp(request):

	if request.method == 'POST':

		file1  = request.FILES['file1'].read().decode("utf-8")
		file2  = request.FILES['file2'].read().decode("utf-8")

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="update.csv"'
		
		lines = file1.split("\n")
		
		for line in lines:
			fields = line.split(",")

		writer = csv.writer(response)
		updated_csv_list = []

		for line in file1:
			updated_csv_list.append(line.split(','))

		for line in file2:
			llist = line.split(',')
			if llist not in updated_csv_list:
				updated_csv_list.append(llist)

		for line in updated_csv_list:
			writer.writerow(line)

			return response

	return render(request,'compare.html')

