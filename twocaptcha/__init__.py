import ssl
ssl.match_hostname = lambda cert, hostname: True

from .api import ApiClient
from .solver import (TwoCaptcha, SolverExceptions, ValidationException,
                     NetworkException, ApiException, TimeoutException)

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

__version__ = '1.1.2'
