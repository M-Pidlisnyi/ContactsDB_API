import requests



if __name__ == "__main__":
    res = requests.get("https://app.nimble.com/api/v1/contacts", headers={
        "Authorization": "Bearer"+"NxkA2RlXS3NiR8SKwRdDmroA992jgu" #this is a dummy token, and its expired
    })
    print(res.content)