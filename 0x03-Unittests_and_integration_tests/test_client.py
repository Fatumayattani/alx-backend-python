#!/usr/bin/env python3
""" Unittest module for testing the GithubOrgClient class """

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org_method_returns_correct_output(self, org_name, mock_json):
        """ Test if the org method returns the correct output """
        endpoint = 'https://api.github.com/orgs/{}'.format(org_name)
        spec = GithubOrgClient(data)
        spec.org()
        mock_json.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url_returns_correct_output(self, name, result):
        """ Test if the public_repos_url property returns the correct output """
        with patch('client.GithubOrgClient.org', PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))
