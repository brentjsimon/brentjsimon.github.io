#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import re
import math
from lxml import html, etree
import csv, os, json
from requests import get
from time import sleep

# Method to do Radix Sort
def radixSort(arr_title,arr_link,arr_price,arr_location):
 
    # Find the maximum number to know number of digits
    max1 = max(arr_price)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr_title,arr_link,arr_price,arr_location,exp)
        exp *= 10

# Function to do insertion sort
def insertionSort(arr_title, arr_price, arr_location, arr_link):
    
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr_price)):        
        key = arr_price[i]

        key_title = arr_title[i]
        key_location = arr_location[i]
        key_link = arr_link[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr_price[j]:
            arr_price[j+1] = arr_price[j]

            arr_title[j+1] = arr_title[j]            
            arr_location[j+1] = arr_location[j]
            arr_link[j+1] = arr_link[j]

            j -= 1
        arr_price[j+1] = key

        arr_title[j+1] = key_title
        arr_location[j+1] = key_location
        arr_link[j+1] = key_link

# A function to do counting sort of arr[] according to
# the digit represented by exp.
def countingSort(arr_title, arr_link, arr_price, arr_location, exp1):
    
    n = len(arr_price)
    
    remove_punc(arr_title)
 
    # The output array elements that will have sorted arr
    output_title = [0] * (n)
    output_link = [0] * (n)
    output_price = [0] * (n)
    output_location = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index_1 = (arr_price[i]/exp1)
        index_2 = (index_1)%10
        index = math.floor(index_2)
        count[ index ] += 1
 
    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1,10):
        count[i] += count[i-1]
 
    # Build the output array
    i = n-1
    while i>=0:
        index_1 = (arr_price[i]/exp1)
        index_2 = (index_1)%10
        index = math.floor(index_2)
        output_title[ count[ index ] - 1] = arr_title[i]
        output_link[ count[ index ] - 1] = arr_link[i]
        output_price[ count[ index ] - 1] = arr_price[i]
        output_location[ count[ index ] - 1] = arr_location[i]
        count[ (index)%10 ] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0,len(arr_price)):
        arr_title[i] = output_title[i]
        arr_link[i] = output_link[i]
        arr_price[i] = output_price[i]
        arr_location[i] = output_location[i]
                

# Python program for implementation of Quicksort Sort

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr_title,arr_link,arr_price,arr_location,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr_title,arr_link,arr_price,arr_location,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr_title,arr_link,arr_price,arr_location, low, pi-1)
        quickSort(arr_title,arr_link,arr_price,arr_location, pi+1, high)


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr_title,arr_link,arr_price,arr_location,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr_price[high]     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        if   arr_price[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr_title[i],arr_title[j] = arr_title[j],arr_title[i]
            arr_link[i],arr_link[j] = arr_link[j],arr_link[i]
            arr_price[i],arr_price[j] = arr_price[j],arr_price[i]
            arr_location[i],arr_location[j] = arr_location[j],arr_location[i]
 
    arr_title[i+1],arr_title[high] = arr_title[high],arr_title[i+1]
    arr_link[i+1],arr_link[high] = arr_link[high],arr_link[i+1]
    arr_price[i+1],arr_price[high] = arr_price[high],arr_price[i+1]
    arr_location[i+1],arr_location[high] = arr_location[high],arr_location[i+1]
    return ( i+1 )
    

def lex_sort(arr_title, arr_price, arr_location, arr_link):
    arr_copy = []
    index = 0
    while index < len(arr_title):
        arr_copy.append(arr_title[index])
        index = index+1
    remove_punc(arr_copy)
    arr_copy = [element.lower() for element in arr_copy]

    temp_title = []
    temp_price = []
    temp_location = []
    temp_link = []
    temp_copy = []
    
    n = len(arr_copy)
    i = 0
    while i < n-1:
        j = i+1
        while j < n:
                #Nonpucutuated Array
            if arr_copy[i] > arr_copy[j]:
                temp_copy = arr_copy[i]
                arr_copy[i] = arr_copy[j]
                arr_copy[j] = temp_copy
                #Has Punctuation
                temp_title = arr_title[i]
                arr_title[i] = arr_title[j]
                arr_title[j] = temp_title
                
                temp_price = arr_price[i]
                arr_price[i] = arr_price[j]
                arr_price[j] = temp_price
                
                temp_location = arr_location[i]
                arr_location[i] = arr_location[j]
                arr_location[j] = temp_location
                
                temp_link = arr_link[i]
                arr_link[i] = arr_link[j]
                arr_link[j] = temp_link
            j = j+1
        i = i+1


def remove_punc(arr):
    punctuations = '()[]{}\<>/.,!?;:@#$%^&*_~'
    n = len(arr)
    i = 0
    while i < n:
        my_str = arr[i]
        no_punct = ""
        for char in my_str:
            if char not in punctuations:
                no_punct = no_punct + char
        arr[i] = no_punct
        i = i+1



def print_data(arr_title, arr_link, arr_price, arr_location):
    for i in range(0,len(arr_title)):
        print("Title: ",arr_title[i])
        print("Price: ",arr_price[i])
        print("Location: ",arr_location[i])
        print("URL: ",arr_link[i])
        print("")
        
        
####################MAIN CODE####################
#MAIN Function to be used by USER



#query = input("Please enter your search parameter: ")
# query = pie
# print ("You entered: ",query)




# def search(url):
#     arr_title = []
#     arr_link = []
#     arr_price = []
#     arr_location = []
#     print ("Your search url: ", url)
#     print("")
#     body = get(url)
#     doc = html.fromstring(body.content)

#     #print(doc.xpath('//img/@src'))
#     for product in doc.xpath('//*[@id="sortable-results"]/ul/li'):
#         raw_title = product.xpath('p/a/text()')
#         raw_link = product.xpath('a/@href')
#         raw_price = product.xpath('p/span/span[@class="result-price"]/text()')
#         raw_location = product.xpath('p/span/span[@class="result-hood"]/text()')

#         title = raw_title[0] if raw_title else None
#         link = raw_link[0] if raw_link else None
#         price = eval(raw_price[0][1:]) if raw_price else 0
#         location = raw_location[0] if raw_location else None
        
#         arr_title.append(title)
#         arr_link.append(link)
#         arr_price.append(price)
#         arr_location.append(location)
#     return arr_title, arr_link, arr_price, arr_location

# url = "https://sfbay.craigslist.org/search/sss?query=pie&sort=rel"
# print ("Your search url: ",url)
# print("")
# body = get(url)
# doc = html.fromstring(body.content)

# #print(doc.xpath('//img/@src'))
# for product in doc.xpath('//*[@id="sortable-results"]/ul/li'):
#     raw_title = product.xpath('p/a/text()')
#     raw_link = product.xpath('a/@href')
#     raw_price = product.xpath('p/span/span[@class="result-price"]/text()')
#     raw_location = product.xpath('p/span/span[@class="result-hood"]/text()')

#     title = raw_title[0] if raw_title else None
#     link = raw_link[0] if raw_link else None
#     price = eval(raw_price[0][1:]) if raw_price else 0
#     location = raw_location[0] if raw_location else None
    
#     arr_title.append(title)
#     arr_link.append(link)
#     arr_price.append(price)
#     arr_location.append(location)
#     #prints out AFTER webscrape is called [RAW]
# print_data(arr_title, arr_link, arr_price, arr_location)

# option = 0
# while option != 4:
#     print ("Please select from the following options: ")
#     print ("1) Sort search results by price: low to high")
#     print ("2) Sort search results by price: high to low")
#     print ("3) Sort search results by location")
#     print ("4) Exit program")
#     print ("")
#     option = input("")
#     print ("You entered option: ",option)
#     print ("")

#     if option == "1":
#         radixSort(arr_title,arr_link,arr_price,arr_location)
#         print_data(arr_title, arr_link, arr_price, arr_location)
        
#     elif option == "2":
#         n = len(arr_price)
#         quickSort(arr_title,arr_link,arr_price,arr_location,0,n-1)
#         arr_title.reverse()
#         arr_link.reverse()
#         arr_price.reverse()
#         arr_location.reverse()
#         print_data(arr_title, arr_link, arr_price, arr_location)

#     elif option == "3":
#         lex_sort(arr_title, arr_price, arr_location, arr_link)
#         print_data(arr_title, arr_link, arr_price, arr_location)

#     elif option == "4":
#         print ("Exiting program...")
#         break

#     else:
#         print("Please select a valid option")
#         print("")  


def peer_search(url):
    arr_title = []
    arr_link = []
    arr_price = []
    arr_location = []
    # url = "https://www.peerhub.com/?filter=marketplace&top=good&q=" + str(query)
    print ("Your search url: ", url)
    print("")
    body = get(url)
    doc = html.fromstring(body.content)

    for product in doc.xpath('/html/body/div/div/div/div/div/div/div/div/ul/li'):#for craigslist: //*[@id="sortable-results"]/ul/li
        raw_title = product.xpath('a/div/div[@class="title"]/text()')#p/a/text()
        raw_link = product.xpath('a/@href')#a/@href
        raw_price = product.xpath('a/div/div[@class="price"]/text()')#p/span/span[@class="result-price"]/text()
        raw_location = product.xpath('a/div/div[@class="location"]/text()')#p/span/span[@class="result-hood"]/text()

        title = raw_title[0] if raw_title else None
        link = "https://www.peerhub.com" + raw_link[0] if raw_link else None
        price = eval(raw_price[0][1:]) if raw_price else 0
        location = raw_location[0] if raw_location else None
        
        arr_title.append(title)
        arr_link.append(link)
        arr_price.append(price)
        arr_location.append(location)
    return arr_title, arr_link, arr_price, arr_location
    
    #print_data(arr_title, arr_link, arr_price, arr_location)


def craigs_search(url):
    arr_title = []
    arr_link = []
    arr_price = []
    arr_location = []
    #url = "https://sfbay.craigslist.org/search/sss?query=" + str(query) + "&sort=rel"
    print ("Your search url: ", url)
    print("")
    body = get(url)
    doc = html.fromstring(body.content)

    #print(doc.xpath('//img/@src'))
    for product in doc.xpath('//*[@id="sortable-results"]/ul/li'):
        raw_title = product.xpath('p/a/text()')
        raw_link = product.xpath('a/@href')
        raw_price = product.xpath('p/span/span[@class="result-price"]/text()')
        raw_location = product.xpath('p/span/span[@class="result-hood"]/text()')

        title = raw_title[0] if raw_title else None
        link = raw_link[0] if raw_link else None
        price = float(eval(raw_price[0][1:])) if raw_price else 0.0
        location = raw_location[0] if raw_location else None
        
        arr_title.append(title)
        arr_link.append(link)
        arr_price.append(price)
        arr_location.append(location) 
    return arr_title, arr_link, arr_price, arr_location