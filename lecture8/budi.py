API_KEY = '9b97a3f4557422d1a8eb4afc826dc653-35c033e048e478935d278bdc8d15773e17c4ef3b57c38c640746c9e0a0054578f0718d1006281b55'
URL = 'http://192.168.56.102:10000/api/public/v1'
APP_MAP = {
    'HRMS' : 'app_8f1f4f7f4a484965b315ecbd509e0469'
}
TABLE_IDS = {
    'personnel' : 'ta_fea99be2f08b45d691cb87de2953d0f9'
}

import requests
import json
class budiapi:

    def __init__(self, api_key = API_KEY, master_url = URL, app_map = APP_MAP, table_ids = TABLE_IDS):
        self.api_key = api_key
        self.master_url = master_url
        self.app_map = app_map
        self.table_ids = table_ids

    def post_headers(self, app_id = None):
        headers = {"Accept": "application/json",
                   "Content-Type": "application/json",
                   "x-budibase-api-key" : self.api_key }
        if app_id is not None:
            headers['x-budibase-app-id'] = app_id

        return headers

    def get_table_info(self, table_name, app_name):
        table_id = self.table_ids[ table_name ]
        app_id = self.app_map[ app_name ]
        url = self.master_url + '/tables/' + table_id
        headers = self.post_headers( app_id = app_id )
        response = requests.get(url, headers = headers)
        return json.loads(response.text)[ 'data' ]

    def get_table_data(self, table_name, app_name):
        table_id = self.table_ids[ table_name ]
        app_id = self.app_map[ app_name ]
        url = self.master_url + '/tables/' + table_id + '/rows/search'
        headers = self.post_headers( app_id = app_id )
        response = requests.post(url, headers = headers)
        return json.loads(response.text)[ 'data' ]

    def create_row(self, table_name, app_name, value_dict):
        table_id = self.table_ids[ table_name ]
        app_id = self.app_map[ app_name ]
        url = self.master_url + '/tables/' + table_id + '/rows'
        headers = self.post_headers( app_id = app_id )
        response = requests.post(url, headers = headers, json = value_dict)
        return json.loads(response.text)[ 'data' ]

    def search_rows(self, table_name, app_name, query_dict):
        table_id = self.table_ids[ table_name ]
        app_id = self.app_map[ app_name ]
        url = self.master_url + '/tables/' + table_id + '/rows/search'
        headers = self.post_headers( app_id = app_id )
        payload = {'query' : {'string' : query_dict} }
        response = requests.post(url, headers = headers, json = payload )
        return json.loads(response.text)[ 'data' ]

    def update_row(self, table_name, app_name, query_dict, value_dict):

        rows = self.search_rows(table_name, app_name, query_dict)
        if len(rows) == 1:
            table_id = self.table_ids[ table_name ]
            app_id = self.app_map[ app_name ]
            row_id = rows[0]['_id']
            url = self.master_url + '/tables/' + table_id + '/rows/' + row_id
            headers = self.post_headers( app_id = app_id )
            response = requests.put(url, headers = headers, json = value_dict)
            return json.loads(response.text)[ 'data' ]
        else:
            raise ValueError('Number of matching rows must be exactly 1 not ' + str(len(rows)) + '.')
