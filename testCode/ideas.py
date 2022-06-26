import json
from source.ToOrganize.Maid  import *
clave = 'sites'

with open('info.json') as f:
    data = json.load(f)

for site in data[clave][0]:
    if site in rec:
        talk(f"abriendo {site}")
        subp.call(f'start msedge.exe {data[clave][0][site]}', shell=True)

