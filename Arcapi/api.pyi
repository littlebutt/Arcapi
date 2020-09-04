"""
All APIs are implemented according to arc-probe-server.php
links: https://gist.github.com/esterTion/c673a5e2547cd54c202f129babaf601d#file-endpoint-md
"""
from typing import List


class Api:
    def songtitle(self, start: int = 8, end: int = 12) -> List:
        """
        title objects from songlist

        :param start: the start constant, default is 8
        :param end: the end constant, default is 12
        :return: the title objects list from songlist
        """
        ...

    async def songtitle(self, start: int = 8, end: int = 12) -> List:
        """
        title objects from songlist

        :param start: the start constant, default is 8
        :param end: the end constant, default is 12
        :return: the title objects list from songlist
        """
        ...

    def userinfo(self, start: int = 8, end: int = 12) -> List:
        """
        user info from friend list response

        :param start: the start constant, default is 8
        :param end: the end constant, default is 12
        :return: the userinfo list from friend list response
        """
        ...

    async def userinfo(self, start: int = 8, end: int = 12) -> List:
        """
        user info from friend list response

        :param start: the start constant, default is 8
        :param end: the end constant, default is 12
        :return: the userinfo list from friend list response
        """
        ...

    def scores(self, start: int = 8, end: int = 12) -> List:
        """
        fetched song scores

        :param start: the start constant, default is 8
        :param end: the end constant, default is 12
        :return: the scores list from fetched song scores
        """
        ...

    async def scores(self, start: int = 8, end: int = 12) -> List:
        """
        fetched song scores

        :param start: the start constant, default is 8
        :param end: the end constant, default is 12
        :return: the scores list from fetched song scores
        """
        ...

    def lookup_result(self, start: int = 8, end: int = 12) -> List:
        """
        results for user lookup

        :param start: the start constant, default is 8
        :param end: the end constant, default is 12
        :return: the result list from results for user lookup
        """
        ...

    async def lookup_result(self, start: int = 8, end: int = 12) -> List:
        """
        results for user lookup

        :param start: the start constant, default is 8
        :param end: the end constant, default is 12
        :return: the result list from results for user lookup
        """
        ...

    def constants(self, start: int = 8, end: int = 12) -> List:
        """
        constants in database

        :param start: the start constant, default is 8
        :param end: the end constant, default is 12
        :return: the constants list from the database
        """
        ...