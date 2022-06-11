from string import hexdigits
import requests, sys, hashlib

password = sys.argv[1]
#take the password from the command line and convert it to "SHA1" hashed password
def cnvrt(password):
    password = hashlib.sha1(password.encode('utf-8')).hexdigits().upper()
    return password

#take the converted (the hashed) version of the password and check if it was leacked
def leacked_or_not(password):
    url = "https://api.pwnedpasswords.com/range/" + password
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the API and try again")
    else:
        print("Password NOT leacked :) ")

password = cnvrt(password)
leacked_or_not(password)