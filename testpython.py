# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 08:36:02 2017

@author: Simon
"""
from lxml_scrapper import *
from flask import Flask, render_template, request, url_for
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		item = request.form['item'].replace(" ", "+")
		url = "https://sfbay.craigslist.org/search/sss?query=" + item + "&sort=rel"
		arr_title, arr_link, arr_price, arr_location = search(url)
		n = len(arr_title)
		alphabetically = None
		ascending = None	
		descending = None
		if request.form.get("sort") == 'alphabetically':
			lex_sort(arr_title, arr_price, arr_location, arr_link)
			alphabetically = "selected"


		elif request.form.get("sort") == 'ascending':
			radixSort(arr_title,arr_link,arr_price,arr_location)
			ascending = "selected"


		elif request.form.get("sort") == 'descending':
			quickSort(arr_title,arr_link,arr_price,arr_location,0,n-1)
			arr_title.reverse()
			arr_link.reverse()
			arr_price.reverse()
			arr_location.reverse()
			descending = "selected"

		return render_template('secondpage.html',
								item = item,
								n = n,
								arr_title = arr_title,
								arr_link = arr_link,
								arr_price = arr_price,
								arr_location = arr_location,
								alphabetically = alphabetically,	
								ascending = ascending,
								descending = descending)

	return render_template('index.html')

if __name__ == "__main__":
	app.debug = True
	app.run()