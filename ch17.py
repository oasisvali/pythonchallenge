from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib
import urllib
import urllib2
import bz2
import re
import requests
import xmlrpclib

if __name__ == '__main__':

  info = '' 

  i=0
  # while (i<400):

  #   if i == 0:
  #     url = url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345"
  #   else:
  #     matchO = re.search(r'busynothing is (\d+)$',html)
  #     try:
  #       url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='+matchO.group(1)
  #     except AttributeError:
  #       break
    
  #   #Create a CookieJar object to hold the cookies
  #   cj = cookielib.CookieJar()
  #   #Create an opener to open pages using the http protocol and to process cookies.
  #   opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())

  #   #create a request object to be used to get the page.
  #   req = Request(url)
  #   f = opener.open(req)

  #   #see the first few lines of the page
  #   html = f.read()
  #   print html
  #   i+=1

  #   #Check out the cookies
  #   for cookie in cj:
  #       if cookie.name == 'info':
  #         print 'value: ' + cookie.value
  #         info += cookie.value

  info = "BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"

  print info
  print bz2.decompress(urllib.unquote_plus(info))

  server_url = 'http://www.pythonchallenge.com/pc/phonebook.php';
  server = xmlrpclib.Server(server_url);

  # Call the server and get our result.
  result = server.phone('Leopold')
  print result

  uri = "http://www.pythonchallenge.com/pc/stuff/violin.php"
  msg = "the flowers are on their way"
  req = urllib2.Request(
      uri, headers = { "Cookie": "info=the+flowers+are+on+their+way"}
  )

  print urllib2.urlopen(req).read()
