import requests
# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")

# Print the status code of the response.
print(response.status_code)

'''
    200 -- everything went okay, and the result has been returned (if any)
    301 -- the server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
    401 -- the server thinks you're not authenticated. This happens when you don't send the right credentials to access an API (we'll talk about authentication in a later post).
    400 -- the server thinks you made a bad request. This can happen when you don't send along the right data, among other things.
    403 -- the resource you're trying to access is forbidden -- you don't have the right permissions to see it.
    404 -- the resource you tried to access wasn't found on the server.
'''
response = requests.get("http://api.open-notify.org/iss-pass")
#print(response.status_code)
response = requests.get("http://api.open-notify.org/iss-pass.json")
#print(response.status_code)

# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Print the content of the response (the data the server returned)
#print(response.content)

# This gets the same data as the command above
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
#print(response.content)

#prueba webscr1

response = requests.get("http://v-www.ihep.ac.cn/cgi-bin/traceroute.pl?target=youtube.com&function=traceroute")
print(response.content.decode("utf-8"))
