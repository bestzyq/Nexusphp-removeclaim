import requests

url = "https://ubits.club/ajax.php"
payload_template = {"action": "removeClaim", "params[id]": ""}

# 填入cookies
cookies = {
    "c_secure_uid": "",
    "c_secure_pass": "",
    "c_secure_ssl": "",
    "c_secure_tracker_ssl": "",
    "c_secure_login": "",
    "sl-session": ""
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://ubits.club",
    "Referer": "https://ubits.club/claim.php",
    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "X-Requested-With": "XMLHttpRequest"
}

# 填入ID范围替代1、2，例如取消ID为1-100的认领，则填入for claim_id in range(1, 101):
for claim_id in range(1, 2):
    payload_template["params[id]"] = str(claim_id)
    
    response = requests.post(url, data=payload_template, cookies=cookies, headers=headers)
    
    if response.status_code == 200:
        print(f"Claim ID {claim_id} removed successfully.")
    else:
        print(f"Failed to remove claim ID {claim_id}. Status code: {response.status_code}")
        print(response.text)
