from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import base64
from bs4 import BeautifulSoup
import re
import time
import dateutil.parser as parser
import datetime
import csv
import datetime
from datetime import timedelta, date
import time



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
#'https://www.googleapis.com/auth/gmail.modify'
#use modify if we want to manipulate
#https://mail.google.com/
#https://www.googleapis.com/auth/gmail.modify
#https://www.googleapis.com/auth/gmail.readonly
#https://www.googleapis.com/auth/gmail.metadata

def main():
  creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
  if os.path.exists('token.pickle'):
      with open('token.pickle', 'rb') as token:
          creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
      else:
          flow = InstalledAppFlow.from_client_secrets_file(
              'credentials.json', SCOPES)
          creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open('token.pickle', 'wb') as token:
          pickle.dump(creds, token)

  service = build('gmail', 'v1', credentials=creds)

  results = service.users().labels().list(userId='me').execute()
  labels = results.get('labels', [])
  if not labels:
    print('No labels found.')
  else:
    print('Labels:')
    #for label in labels:
      #print(label['name'])
  
  user_id =  'me' 
  #me is a special value to indicate the authenticated user.
  label_id_one = 'INBOX'
  label_id_two = 'UNREAD'

  #from today until january 1, 2000, look for messages received on that day
  #make a message list array of those messages
  #take each one of those messages in that list and stick it in the master list
  
  
  def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)
        #Return sends a specified value back to its caller 
        # #whereas Yield can produce a sequence of values. 
        # #We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

  start_date = date(2019, 8, 6)
  end_date = date(2019, 8, 15)

  for single_date in daterange(start_date, end_date):
    today=str(single_date.strftime("%Y-%m-%d"))
    searchString="after"+today
    unread_msgs = service.users().messages().list(
                                                  userId='me',
                                                  maxResults=1000,
                                                  q=searchString,
                                                  labelIds=[label_id_one, label_id_two]
                                                  ).execute()

    print (single_date.strftime("%Y-%m-%d"))
    mssg_list = unread_msgs['messages'] #must be a dictionary object
    print(today)
    print ("Total  messages received on the date: ", str( len(mssg_list) ) )

main()


    