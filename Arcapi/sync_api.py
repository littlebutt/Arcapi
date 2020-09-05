import re
import json
from typing import List, Dict, Any
from websocket import create_connection

import brotli

from Arcapi.api import Api
from Arcapi.exceptions import *


class SyncApi(Api):
    user_code: str  # User's 9-digit code for login
    start: int  # The beginning constant for consulting
    end: int  # The ending constant for consulting
    timeout: int  # The time for connecting wss

    def __init__(self, user_code: str, start: int = 8, end: int = 12, timeout: int = 5) -> None:
        self.ws_endpoint = 'wss://arc.estertion.win:616'
        if not re.fullmatch(r'\d{9}', user_code):
            raise ArcInvaidUserCodeException
        self.user_code = user_code
        self.start = start
        self.end = end
        self.timeout = timeout

    def call_action(self, action: str, **params) -> Any:
        if 'start' in params:
            _start = params['start']
        else:
            _start = self.start
        if 'end' in params:
            _end = params['end']
        else:
            _end = self.end
        container: List[Dict] = []  # The result list for request objects
        conn = create_connection(self.ws_endpoint, timeout=self.timeout)
        conn.send(f'{self.user_code} {_start} {_end}')
        _recv = conn.recv()
        if _recv == 'invalid id':
            raise ArcInvaidUserCodeException
        elif _recv == 'queried':
            while True:
                _r = conn.recv()
                if isinstance(_r, str) and _r == 'bye':
                    break
                elif isinstance(_r, (bytes, bytearray)):
                    _data = json.loads(brotli.decompress(_r))
                    if _data['cmd'] == action:
                        if type(_data['data']) is list:
                            for _item in _data['data']:
                                container.append(_item)
                    else:
                        container.append(_data['data'])
        else:
            raise ArcUnknownException(_recv)
        return container
