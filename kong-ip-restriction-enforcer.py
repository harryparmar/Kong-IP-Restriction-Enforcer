import requests
import argparse

parser = argparse.ArgumentParser(description='Kong IP-Restriction Enforcer')

parser.add_argument('-u','--url', help='Kong Server Location starting with http...',required=True)
args = parser.parse_args()

try:
    
    response = requests.get(args.url,timeout=5)
    response.raise_for_status()

except requests.exceptions.HTTPError as e:
        print ('Http Error:', e)
except requests.exceptions.Timeout as e:
        print ('Timeout Error:', e)
except requests.exceptions.ConnectionError as e:
        print ('Error Connecting:', e)
except requests.exceptions.RequestException  as e:
        print('Something went wrong trying to fulfill the request -->', e)
   
else:

       apis_json_object = response.json()
       apis_count = len(apis_json_object['data'])
       count_apis = 0
       while (count_apis < apis_count):
               print(apis_json_object['data'][count_apis]['id'])
               api_plugins_url = args.url + apis_json_object['data'][count_apis]['id'] + '/plugins/'
               response = requests.get(api_plugins_url)
               api_plugins_json_object = response.json()
               api_plugins_count = len(api_plugins_json_object['data'])
               count_plugins = 0
               ip_restriction_plugin_present = False
               while (count_plugins < api_plugins_count):
                   if api_plugins_json_object['data'][count_plugins]['name'] == 'ip-restriction':
                                 ip_restriction_plugin_present = True
                                 break
                   count_plugins = count_plugins + 1
               if ip_restriction_plugin_present == False:
                             try:
                                 payload = (('name','ip-restriction'),('config.whitelist','10.0.0.0/8,172.16.0.0/12,192.168.0.0/16'))
                                 response = requests.post(api_plugins_url, data = payload)
                                 print(response.text)
                                 response.raise_for_status()
                             except requests.exceptions.HTTPError as e:
                                 print ('Http Error:', e)
                             except requests.exceptions.Timeout as e:
                                 print ('Timeout Error:', e)
                             except requests.exceptions.ConnectionError as e:
                                 print ('Error Connecting:', e)
                             except requests.exceptions.RequestException  as e:
                                 print('Something went wrong trying to fulfill the request -->', e)
                             
               count_apis = count_apis + 1



	
