import xmlrpclib

if __name__ == '__main__':

    # Create an object to represent our server.
    server_url = 'http://www.pythonchallenge.com/pc/phonebook.php';
    server = xmlrpclib.Server(server_url);

    # Call the server and get our result.
    result = server.phone('555-ITALY')
    print result