import os
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
cls=lambda:os.system("cls")

def main():
    cls()
    token=input("Token: ")
    cls()
    check(token)
    data=info(token)
    datalist(data,token)
    ask_log(token)

def check(token):
    rep=requests.get("https://discord.com/api/users/@me", headers={"authorization": token})
    code=rep.status_code
    if code==200:
        return True
    else:
        cls()
        print("Invalid token...")
        sleep(2)
        main()

def info(token):
    data=requests.get("https://discord.com/api/users/@me", headers={"authorization": token}).json()
    return data

def datalist(token_info,token):
    dat=f"""Username: {token_info["username"]}#{token_info["discriminator"]}\nId: {token_info["id"]}\nEmail: {token_info["email"]}\nPhone: {token_info["phone"]}\nNitro: {"Yes" if token_info["premium_type"] > 0 else "No"}\nLanguage: {token_info["locale"]}\nToken: {token}"""
    print(dat)
    rep=input("\nDo you want to save this data? [Y/N]: ")
    if rep == "y" or rep == "yes":
        f=open(f"{token_info['username']}#{token_info['discriminator']}.txt", "w").write(dat)

def ask_log(token):
    login=input("\nDo you want to login to the account? [Y/N]: ")
    login=login.lower()
    if login == "y" or login == "yes":
        cls()
        log(token)
    elif login == "n" or login == "no":
        quit()
    else:
        ask_log(token)

def log(token):
    print("[*]Starting browser")
    chrome_options = Options().add_argument('--log-level=3')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://discord.com/login")
    js="""
let token = '"""+token+"""';
  
function login(token) {
  setInterval(() => {
    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
  }, 50);
  setTimeout(() => {
    location.reload();
  }, 2500);
}

login(token);
"""
    print("\n[*]Injecting javascript\n")
    driver.execute_script(js)
    print("Do not close that window it will close the browser")
    input("\nPress enter to quit...")
if __name__ == '__main__':
    main()