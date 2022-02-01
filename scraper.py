import requests
import time
import re
import json

import os
from dotenv import load_dotenv
load_dotenv()
# your acadinfo username and password
CREDENTIALS = { 'username': os.getenv("SIMASTER_USERNAME"),
                'password': os.getenv("SIMASTER_PASSWORD")}

def scrap_acadinfo():
    def dictify(string):
        # replace non-breaking spaces and remove multiple whitespaces
        string = re.sub(r'[\t\n\r\f\v]+', '', string.replace('&nbsp;',' ').strip())
        # remove empty html tags
        string = re.sub(r'</?[abi(hr)].*?>', ' ', string)
        string = re.sub(r'[ \t]+', ' ', string)
        # replace html element with list bracket
        string = re.sub(r'<.*?>', '[', re.sub(r'</.*?>', ']', string))
        # add commas between values
        string = re.sub(r'\]\s*?\[', '],\n[', string)
        # replace non-nested list element as string
        string = re.sub(r'\[(?!.*?\[).*?\]', lambda x: x.group(0).replace('[', '"').replace(']', '"'), string)
        # remove remaining trailing whitespaces
        string = re.sub(r'\[\s+', '[', re.sub(r'\s+\]', ']', string))
        string = re.sub(r'" +', '"', re.sub(r' +"', '"', string))
        return string

    session = requests.Session()

    if session.get("https://acadinfo.jteti.ugm.ac.id/").status_code != 200:
        raise Exception("Error retrieving acadinfo site")

    session.post("https://acadinfo.jteti.ugm.ac.id/index.php/auth/login", data = CREDENTIALS)
    html = session.get("https://acadinfo.jteti.ugm.ac.id/index.php/mhs/jadwalkuliah").text
    thead = dictify(html.split('</thead>')[0].split('<thead')[1].split('>',1)[1])
    tbody = dictify(html.split('</tbody>')[0].split('<tbody')[1].split('>',1)[1])
    #thead = json.loads(thead) # long dict keys
    thead = [d.split(" ",1)[0] for d in json.loads(thead)] # shorter dict keys
    tbody = json.loads(f'[{tbody}]')

    json_table = [{d: body[thead.index(d)] for d in thead} for body in tbody]

    stringified = json.dumps(json_table, indent=4)
    with open("output.json", 'w') as f:
        f.write(stringified)

    return json_table
