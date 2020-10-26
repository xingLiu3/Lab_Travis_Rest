import pytest
import requests


url_ddg = "https://api.duckduckgo.com"

presidents = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Jackson', 'Buren', 'Harrison', 'Tyler',
              'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield',
              'Arthur', 'Cleveland', 'Harrison', 'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding',
              'Coolidge', 'Hoover', 'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford',
              'Carter', 'Reagan', 'Bush', 'Clinton', 'Obama', 'Trump']

def test_ddg0():

    resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")

    rsp_data = resp.json()

    topics = []

    for topic in rsp_data["RelatedTopics"]:
        topics.append(topic.get('Text'))


    for pre in presidents:
        for i in topics:
            if pre in i:
                result = 'success'
        assert 'success' in result

