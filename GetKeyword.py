import konlpy
import json
import csv

def load_keywords():
    with open("keywords.json") as f:
        data = json.load(f)
    return data

def get_noun(sentence):
    kkma = konlpy.tag.Twitter()
    origin = kkma.pos(sentence)
    alpha = []
    hangul = []
    for i in origin:
        if i[1] == 'Alpha':
            alpha.append(i[0].lower())
        if i[1] == 'Noun':
            hangul.append(i[0])
    nouns = alpha + hangul
    return nouns

def classification_by_keyword(sentence):
    keywords = load_keywords()
    nouns = get_noun(sentence)
    count = {}
    for k in keywords:
        count[k] = 0
    for n in nouns:
        for k in keywords:
            if n in keywords[k]:
                count[k] += 1
    mode = 0
    keyword = ''
    for c in count:
        if count[c] >= mode:
            mode = count[c]
            keyword = c
    if mode == 0:
        return 'No keyword'
    else:
        return keyword

if __name__ == "__main__":
    filename = input("csv파일경로를 입력해주세요")
    with open(filename, 'r', encoding='utf-8') as f:
        rdr = csv.reader(f)
    for line in rdr:
        print(line[0])
        print(classification_by_keyword(line[1]))