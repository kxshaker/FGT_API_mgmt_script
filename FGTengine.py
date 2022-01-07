#!/usr/bin/env python3

import requests
import json
import logging
logging.captureWarnings(True)

#    Base class to send GET/POST/PUT/DELETE request to FGT
#    All requests are from the same session initiated by each login


class FGT(object):

    def __init__(self, host):
        self.host = host
        self.url_prefix = "https://" + self.host

    def update_csrf(self):
        # retrieve server csrf and update session's headers
        for cookie in self.session.cookies:
            if cookie.name == "ccsrftoken":
                csrftoken = cookie.value[1:-1]  # token stored as a list
                self.session.headers.update({"X-CSRFTOKEN": csrftoken})

    def login(self, name="admin", key="", csrf=True):
        # close existing session if any
        self.logout()

        # start fresh new session
        self.session = requests.session()
        url = self.url_prefix + "/logincheck"
        try:
            res = self.session.post(
                url,
                data="username=" + name + "&secretkey=" + key,
                verify=False)
        except requests.exceptions.RequestException as e:
            print(e)
            print("LOGIN failed")
            exit()

        if res.text.find("error") != -1:
            # found some error in the response, consider login failed
            print("LOGIN failed")
            return False

        # update session's csrftoken
        if csrf:
            self.update_csrf()
        return True

    def logout(self):
        if hasattr(self, "session"):
            url = self.url_prefix + "/logout"
            self.session.post(url)

    def get(self, url, **options):
        url = self.url_prefix + url
        try:
            res = self.session.get(
                url,
                params=options.get("params"))
        except requests.exceptions.RequestException as e:
            print(e)
            exit()
        return res

    def post(self, url, override=None, **options):
        url = self.url_prefix + url
        data = options.get("data") if options.get("data") else None

        # override session's HTTP method if needed
        if override:
            self.session.headers.update({"X-HTTP-Method-Override": override})
        try:
            res = self.session.post(
                url,
                params=options.get("params"),
                data=json.dumps(data),
                files=options.get("files"))
        except requests.exceptions.RequestException as e:
            print(e)
            exit()

        # restore original session
        if override:
            del self.session.headers["X-HTTP-Method-Override"]
        return res

    def put(self, url, **options):
        url = self.url_prefix + url
        data = options.get("data") if options.get("data") else None
        try:
            res = self.session.put(
                url,
                params=options.get("params"),
                data=json.dumps(data),
                files=options.get("files"))
        except requests.exceptions.RequestException as e:
            print(e)
            exit()
        return res

    def delete(self, url, **options):
        url = self.url_prefix + url
        try:
            res = self.session.delete(
                url,
                params=options.get("params"))
        except requests.exceptions.RequestException as e:
            print(e)
            exit()
        return res




class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



