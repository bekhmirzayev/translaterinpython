import requests


app_id='62b446b5'
app_key='c2fe6960887f53bb88999a767283d7e3d'
language='en'

def getDefinitions(word_id):
    url = "https://api.dictionaryapi.dev/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url)
    res = r.json()

    
    output = {}
    
    senses = res[0]['meanings'][0]['definitions']  # Yangi qator
    definitions = []
    # if  res.status_code == 404:
    #     return False
    
    for i in senses:
        for j in i:
            if j == 'definition':
                definitions.append(i[j])
    # return definitions
    output['definitions '] = ''.join(definitions)

    if res[0]['phonetics'][0]['audio']:
        output['audio'] = res[0]['phonetics'][0]['audio']

    return output


if __name__ == '__main__':
    from pprint import pprint  as print
    print(getDefinitions('face'))
