#!/usr/bin/python
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sys import argv

counter = 0

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name(argv[2], scope)
client = gspread.authorize(creds)

sheet = client.open(argv[3]).sheet1

with open(argv[1]) as fp:
    for line in fp:
        counter += 1
        sheet.update_cell(counter, 1, counter) #A dimmer value
        sheet.update_cell(counter, 2, line) #An illuminance value
