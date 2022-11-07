import re


def URL(input):
    url = "мне очень понравился этот сайт https://regex101.com/ советую зайти"
    pattern = r'https:\S*'
    replacement = ""
    d = {}
    matches = re.sub(pattern, replacement, url)
    for i in range(len(matches)):
        d[i] = matches
    return matches
