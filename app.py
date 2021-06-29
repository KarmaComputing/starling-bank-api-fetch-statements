import requests
import os
import logging
from dotenv import load_dotenv
from env_validate import validate_env

log = logging.getLogger()

load_dotenv(verbose=True)
validate_env()

log.setLevel(os.getenv("PYTHON_LOGLEVEL", logging.DEBUG))

PERSONAL_ACCESS_TOKEN = os.getenv("PERSONAL_ACCESS_TOKEN")
BANK_ACCOUNT_ID = os.getenv("BANK_ACCOUNT_ID")

headers = {
    "Authorization": PERSONAL_ACCESS_TOKEN,
    "accept": "text/csv",
}

account_id = BANK_ACCOUNT_ID
year = 2021
month = "01"
yearMonth = "2021-01"
host = f"https://api.starlingbank.com/api/v2/accounts/{account_id}/statement/download?yearMonth={yearMonth}"  # noqa

while int(month) <= 12:
    from time import sleep

    sleep(1)
    nextMonth = int(month)
    if nextMonth < 10:
        nextMonth = "0" + str(nextMonth)
    yearMonth = "2021" + "-" + str(nextMonth)
    host = f"https://api.starlingbank.com/api/v2/accounts/{account_id}/statement/download?yearMonth={yearMonth}"  # noqa
    req = requests.get(host, headers=headers)
    if req.status_code == 200:
        with open(f"{yearMonth}.csv", mode="w") as fp:
            fp.write(req.text)
    else:
        log.error(f"Failed request:{host} - {req.status_code} - {req.text}")
    month = int(month) + 1
