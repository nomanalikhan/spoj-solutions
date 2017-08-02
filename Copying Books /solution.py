import os
import glob

def balanceWorkLoad(no_of_books, book_pages_arr, no_of_scribers):
	ideal_books_per_scriber = int(no_of_books / no_of_scribers)
	is_odd = (no_of_books % no_of_scribers)
	books_per_scriber = []

	for index, scriber in enumerate(range(no_of_scribers)):
		if(index != no_of_scribers - 1):
			books = book_pages_arr[0:ideal_books_per_scriber]
			del book_pages_arr[0:ideal_books_per_scriber]
			books_per_scriber.append(books)
		else:
			if(is_odd):
				books = book_pages_arr[0:ideal_books_per_scriber + 1]
				del book_pages_arr[0:ideal_books_per_scriber + 1]
				books_per_scriber.append(books)
			else:
				books = book_pages_arr[0:ideal_books_per_scriber]
				del book_pages_arr[0:ideal_books_per_scriber]
				books_per_scriber.append(books)


	flag = True
	ind = 1
	while(flag):
		last_scriber = books_per_scriber[no_of_scribers - ind]
		prev_scriber = books_per_scriber[no_of_scribers - (ind + 1)]

		if(sum(last_scriber) > sum(prev_scriber)):
			fetched_book = last_scriber[0:1]
			del books_per_scriber[no_of_scribers - ind][0:1]
			books_per_scriber[no_of_scribers - (ind + 1)].append(fetched_book[0])
		else:
			if(ind > no_of_scribers - 1):
				flag = False
			ind = ind + 1

	# transform nested array to string
	output = ''
	for ind, book in enumerate(books_per_scriber):
		for name in book:
			output += '%s ' % (name)

		if(ind != len(books_per_scriber) - 1):
			output += '/ '
	
	return output.strip()


# execute all test cases
outputs = [];
inp_path = './testcases/input/*'
out_path = './testcases/output/*'

for file in glob.glob(inp_path):
	inpfile = open(file, 'r')
	
	# take the inputs from first file
	first_line = inpfile.readline().split(' ')
	no_of_books = int(first_line[0])
	no_of_scribers = int(first_line[1])
	book_pages_arr = inpfile.readline().split(' ')
	book_pages_arr = [int(numeric_str) for numeric_str in book_pages_arr]

	res = balanceWorkLoad(no_of_books, book_pages_arr, no_of_scribers)
	# push the output to array to check with output file later on
	outputs.append(res)

for index, file in enumerate(glob.glob(out_path)):
	inpfile = open(file, 'r')
	
	# take the inputs from first file
	expected_out = inpfile.readline()

	status = 'failed'
	if(expected_out == outputs[index]):
		status = 'passed'

	tc = 'testcase# %s: %s' % ((index + 1), status)
	print(tc)