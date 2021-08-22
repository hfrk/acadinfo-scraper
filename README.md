# Acadinfo scraper
Scrap schedules from acadinfo.jteti.ugm.ac.id into JSON-like format, in case you are too lazy to open browser and prefer using the Python interpreter instead.

# How-to
## Installation
1. Clone and install the required dependency
```bash
$ git clone https://github.com/hfrk/acadinfo-scraper
$ pip install requirements.txt
```
2. Revvv up your VPN
3. Import to your Python interpreter and do stuff
```python
import scraper

data = scraper.scrap_acadinfo()

# Getting your class' URLs
for d in data:
    if some_random_matkul_names in d['Matakuliah']:
        print(d['URL'])
```

## JSON structure
```json
{
    "#": "",
    "Hari/Jam": "",
    "Matakuliah": "",
    "Kelas": "",
    "Dosen": "",
    "URL": [
        "KELAS:",
        "PRESENSI:",
        "WAG/Telegram:"
    ],
    "Keterangan": [
        "",
        "Pertemuan ke:"
    ]
}
```
