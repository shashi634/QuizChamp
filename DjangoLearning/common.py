import hashlib, binascii, os
import re
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
def hashPassword(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def checkEmail(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex,email)):
        return True
    else:
        return False

def currentLoggedInUserData():
    data = dict()
    if "quizChampAdmin" in request.session:
        sessionData = request.session["quizChampAdmin"].split('~')
        data['UserName'] = sessionData[0]
        data['EmailId'] = sessionData[1]
        data['OrganizationId'] = sessionData[2]
    return data

class AuthRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not "quizChampAdmin" in request.session:
            return render(request,'login.html')
        return None