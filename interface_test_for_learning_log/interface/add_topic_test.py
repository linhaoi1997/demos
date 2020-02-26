import unittest
import requests
import os, sys
from db_fixture import test_data


class AddTopicTest(unittest.TestCase):

    def setUp(self):
        test_data.init_data()
        print('start')
        self.base_url = "http://127.0.0.1:8000/api/add_topic/"

    def tearDown(self):
        print(self.result)

    def test_add_topic_all_null(self):
        '''所有参数为空'''

        payload = {'username': '', 'text': ''}
        r = requests.post(self.base_url, json=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_topic_user_not_exist(self):
        '''user不存在'''
        payload = {'username': '123', 'text': 'test'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10020)
        self.assertEqual(self.result['message'], 'no such user error')

    def test_add_topic_exist(self):
        '''topic已存在'''
        payload = {'username': 'linhao', 'text': 'Chess'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'topic already exists')

    def test_add_topic_text_too_long(self):
        '''text长度超过30'''
        text = 't'.join(['q' for x in range(16)])
        payload = {'username': 'linhao', 'text': text}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'Data too long for column "text" at row 1')

    def test_add_topic_success(self):
        payload = {'username': 'linhao', 'text': 'test_for_success'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add topic success')


if __name__ == "__main__":
    test_data.init_data()
    unittest.main()
