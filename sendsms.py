#!/usr/bin/python
#-----------------------------------
# Send SMS Text Message using Python
#
# Site   : http://www.raspberrypi-spy.co.uk/
#
# Requires account with TxtLocal
# http://www.txtlocal.co.uk/?tlrx=114032
#
#-----------------------------------

# Import required libraries
import urllib      # URL functions
import urllib2     # URL functions

def sendText():
    # Set YOUR TextLocal username
    username = 'goluck25@gmail.com'

    # Set YOUR unique API hash
    # It is available from the docs page
    # https://control.txtlocal.co.uk/docs/
    hash = '95c0661fe01fb596eed7b575fff10f7e593668dbcf344af69d192fc6b34df21c'

    # Set a sender name.
    # Sender name must alphanumeric and
    # between 3 and 11 characters in length.
    sender = 'RatDetector'

    # Set flag to 1 to simulate sending
    # This saves your credits while you are
    # testing yourcode.
    # To send real message set this flag to 0
    test_flag = 0

    # Set the phone number you wish to send
    # message to.
    # The first 2 digits are the country code.
    # 44 is the country code for the UK
    # Multiple numbers can be specified if required
    # e.g. numbers = ('447xxx123456','447xxx654321')
    numbers = ('254718414613')

    # Define your message
    message = 'There is a Rat in your location'

    #-----------------------------------------
    # No need to edit anything below this line
    #-----------------------------------------

    values = {'test'    : test_flag,
            'uname'   : username,
            'hash'    : hash,
            'message' : message,
            'from'    : sender,
            'selectednums' : numbers }

    url = 'http://www.txtlocal.co.uk/sendsmspost.php'

    postdata = urllib.urlencode(values)
    req = urllib2.Request(url, postdata)

    print ('Attempt to send SMS ...')

    try:
        response = urllib2.urlopen(req)
        response_url = response.geturl()
        if response_url==url:
            print ('SMS sent!')
    except (urllib2.URLError, e):
        print ('Send failed!')
        print (e.reason)
