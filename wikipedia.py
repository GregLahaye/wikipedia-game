import requests


def random(num=1):
    params = {
              "format": "json",
              "action": "query",
              "generator": "random",
              "grnnamespace": "0",
              "grnlimit": num
             }
    
    r = s.get(API_URL, params=params)
    response = r.json()
    titles = [item["title"] for item in response["query"]["pages"].values()]
    return titles 


def check(title):
    params = {
              "action": "query",
              "titles": title,
              "prop": "categories",
              "clcategories": "Category:All disambiguation pages",
              "format": "json",
              "redirects": "true"
             }
    
    r = s.get(API_URL, params=params)
    response = r.json()
    pageid = list(response["query"]["pages"].keys())[0]
    valid = False
    if "redirects" in response["query"]:
        valid = response["query"]["redirects"][0]["to"]
    elif "categories" in response["query"]["pages"][pageid]:
        print("'{}' is a disambiguation page".format(title))
    elif pageid == "-1": 
        print("'{}' is not a valid article".format(title))
    else:
        valid = title

    return valid


def get_links(title):
    params = {
              "action": "query",
              "titles": title,
              "prop": "links",
              "pllimit": "max",
              "format": "json",
              "plnamespace": 0
             }

    done = False
    while not done:
        links = []
        try:
            r = s.get(API_URL, params=params)
            response = r.json()
            pageid = list(response["query"]["pages"].keys())[0]
            if "links" in response["query"]["pages"][pageid]:
                links += [link["title"] for link in response["query"]["pages"][pageid]["links"]]
                while "continue" in response:
                    params["plcontinue"] = response["continue"]["plcontinue"]    
                    r = s.get(API_URL, params=params)
                    response = r.json()
                    pageid = list(response["query"]["pages"].keys())[0]
                    links += [link["title"] for link in response["query"]["pages"][pageid]["links"]]
            done = True
        except requests.exceptions.ConnectionError:
            input("Connect Error, <Enter> to try again")
    
    return links    


API_URL = "https://en.wikipedia.org/w/api.php"
s = requests.session()

