def count_words(text):
    return len(text.split())

def count_chars(text):
    text = text.lower()
    res = dict()
    for c in text:
        if c not in res:
            res[c] = 1
        else:
            res[c] +=1
    return res

def report(char_dict):
    res = []
    for c in char_dict:
        res.append({
            "char" : c,
            "num" : char_dict[c]
        })
    res.sort(reverse=True,key= lambda x: x['num'])
    return res