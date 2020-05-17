import uuid
import socket
import platform
import os
from flask import request
import subprocess

class Whoami:

    # Super general error wrapper, because I don't really want to handle errors now, just return values
    def error_wrapper(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                return "Could not retrieve value"
        return wrapper

    @error_wrapper
    def raise_error(self):
        raise SyntaxError
        return 0

    @error_wrapper
    def get_own_hostname(self):
        return socket.gethostname()

    @error_wrapper
    def get_own_ip(self):
        return socket.gethostbyname(socket.gethostname())

    def format_mac(self, mac):
        mac = hex(mac)
        mac = mac.upper()[2:]
        formatted_mac = ""
        for i in range(0, int(len(mac)), 2):
            formatted_mac = formatted_mac + mac[i:i + 2] + ":"  # Insert colons after every two characters
        return formatted_mac[:-1]

    @error_wrapper
    def get_own_mac(self):
        return self.format_mac(uuid.getnode())


    @error_wrapper
    def get_own_platform(self):
        return platform.platform()

    @error_wrapper
    def get_own_env_variables(self):
        keylist = []
        for k, v in os.environ.items(): #Print only keys, omit values
            keylist.append(k)
        return keylist

    @error_wrapper
    def get_python_version(self):
        return platform.python_version()

    @error_wrapper
    def get_visitor_ip(self):
        return request.remote_addr

    @error_wrapper
    def get_fortune(self):
        return subprocess.check_output(['sh', '-c', 'fortune']).decode("UTF-8").strip() #Convert bytestring to UTF-8.

    def to_json(self):
        # TODO: Return some useful information about the environment we're running in
        return {"whoami": {"name": "Lauri's Whoami App",
                           "service_ip": self.get_own_ip(),
                           "service_hostname": self.get_own_hostname(),
                           "service_mac": self.get_own_mac(),
                           "service_platform": self.get_own_platform(),
                           "env_variables": self.get_own_env_variables(),
                           "python_version:": self.get_python_version(),
                           "YOUR_IP": self.get_visitor_ip(),
                           "YOUR_FORTUNE_FOR_TODAY": self.get_fortune()}}

