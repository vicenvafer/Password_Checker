import requests

#print(requests.__file__)

url = "https://api.pwnedpasswords.com/range/" + "password123"

res = requests.get(url)

print(res)

def request_api_data(query_char):
    pass


def pwned_api_check(password):
    #check is passwrd exists in api response
    pass



