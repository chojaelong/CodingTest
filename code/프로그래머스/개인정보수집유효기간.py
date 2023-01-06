from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    today = datetime.strptime(today, "%Y.%m.%d")
    answer = []
    
    dict1 = dict()
    for term in terms:
        word, digit = term.split(' ')
        dict1[word] = int(digit)
        
    for idx, privacy in enumerate(privacies):
        date, word = privacy.split(' ')
        date = datetime.strptime(date, "%Y.%m.%d")
        after_date = date + relativedelta(months=dict1[word])
        if today >= after_date:
            answer.append(idx + 1)
        
    return answer