import requests
import random

class GrabUrl:
  
  def getUrl():
    URL_START = 'https://leetcode.com/problems/'
    response = requests.get('https://leetcode.com/api/problems/all/')
    url_list = []

    for data in response.json()['stat_status_pairs']:
      url_list.append(data['stat']['question__title_slug'])

    random_num = random.randint(0, len(url_list)-1)
    return(URL_START + url_list[random_num])