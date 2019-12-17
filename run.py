from Func.Porcess import process
import configparser
import os
import json

def readUser():
    dictAccounts = []
    cfg = configparser.ConfigParser()
    cfg.read("cfg.ini")
    for key in cfg["User information"]:
        jsonData = json.loads(cfg["User information"][key])
        account = (jsonData["Email"], jsonData["Passwd"])
        dictAccounts.append(account)
    return dictAccounts

if __name__ == "__main__":

    dic = readUser()
    p=process(dic[0][0],dic[0][1])

    p.run()