#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized

import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''Testing the GithubOrgClient class methods'''
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_org):
        '''Testing TestGithubOrgClient's org method'''
        org_test = GithubOrgClient(org)

        test_response = org_test.org
        self.assertEqual(test_response, mock_org.return_value)
        mock_org.assert_called_once()
    
    def test_public_repos_url(self):
        '''Testing TestGithubOrgClient's _public_repos_url method'''
        with patch.object(GithubOrgClient,
                          'org',
                          new_callable=PropertyMock) as m:
            m.return_value = {"repos_url": "89"}
            test_org = GithubOrgClient('holberton')
            test_repo_url = test_org._public_repos_url
            self.assertEqual(test_repo_url, m.return_value.get('repos_url'))
            m.assert_called_once()