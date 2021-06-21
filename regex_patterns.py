import re
from nltk.tokenize import WhitespaceTokenizer


class RegexPatterns():
    def __init__(self):
        self.dict_month = {
            'janvier': '01',
            'février': '02',
            'fevrier': '02',
            'mars': '03',
            'avril': '04',
            'mai': '05',
            'juin': '06',
            'juillet': '07',
            'août': '08',
            'aout': '08',
            'septembre': '09',
            'octobre': '10',
            'novembre': '11',
            'décembre': '12',
            'decembre': '12'
        }
        self.months = '(?:janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre)'
        self.regex1 = r'(?:[0-2]?[0-9]|3[0-1])\s' + self.months + '\s[0-9]{4}'  # JJ mois AAAA
        self.regex2 = r'(?:[0-2][0-9]|3[0-1])(?:\/|\.|\-)(?:(?:0[0-9])|(?:1[0-2]))(?:\/|\.|\-)\d{4}'  # JJ/MM/AAAA & JJ.MM.AAAA & JJ-MM-AAAA
        self.regex3 = r'(?:[0-2][0-9]|3[0-1])(?:\/|\.|\-)(?:(?:0[0-9])|(?:1[0-2]))(?:\/|\.|\-)\d{2}\b'  # JJ/MM/AA & JJ.MM.AA & JJ-MM-AA
        self.regex4 = r'(?:1°)\s' + self.months + '\s[0-9]{4}'  # 1° mois AAAA
        self.regex5 = r'(?:1er)\s' + self.months + '\s[0-9]{4}'  # 1er mois AAAA
        self.regex6 = r'(?:[0-2][0-9]|3[0-1])\s\/\s(?:(?:0[0-9])|(?:1[0-2]))\s\/\s\d{4}'  # JJ / MM / AAAA
        self.regex7 = r'(?:[0-2][0-9]|3[0-1])\.\s(?:(?:0[0-9])|(?:1[0-2]))\.\s\d{4}'  # JJ. MM. AAAA

        self.pattern1 = re.compile(self.regex1, re.IGNORECASE)
        self.pattern2 = re.compile(self.regex2, re.IGNORECASE)
        self.pattern3 = re.compile(self.regex3, re.IGNORECASE)
        self.pattern4 = re.compile(self.regex4, re.IGNORECASE)
        self.pattern5 = re.compile(self.regex5, re.IGNORECASE)
        self.pattern6 = re.compile(self.regex6, re.IGNORECASE)
        self.pattern7 = re.compile(self.regex7, re.IGNORECASE)

        self.pattern_union = re.compile('(' + self.regex1 + '|' + self.regex2 + '|' + self.regex3 + '|' + self.regex4 + '|' + self.regex5 + '|' + self.regex6 + '|' + self.regex7 + ')', re.IGNORECASE)

    def word_tok(sentence):
        return WhitespaceTokenizer().tokenize(sentence)

    def date_processing(match):
        # Pattern 1
        if re.search(pattern1, match) is not None:
            tokens_date = word_tok(match)
            if len(tokens_date[0]) == 1:
                tokens_date[0] = '0' + tokens_date[0]
            date = tokens_date[2] + '-' + dict_month[tokens_date[1]] + '-' + tokens_date[0]
    
        # Pattern 2
        elif re.search(pattern2, match) is not None:
            date = match[6:10] + '-' + match[3:5] + '-' + match[0:2]
    
        # Pattern 3
        elif re.search(pattern3, match) is not None:
            if int(match[6:8]) <= 20:
                start_year = '20'
            else:
                start_year = '19'
    
            date = start_year + match[6:8] + '-' + match[3:5] + '-' + match[0:2]
    
        # Pattern 4
        elif re.search(pattern4, match) is not None:
            tokens_date = word_tok(match)
            date = tokens_date[2] + '-' + dict_month[tokens_date[1]] + '-' + '01'
    
        # Pattern 5
        elif re.search(pattern5, match) is not None:
            tokens_date = word_tok(match)
            date = tokens_date[2] + '-' + dict_month[tokens_date[1]] + '-' + '01'
    
        # Pattern 6
        elif re.search(pattern6, match) is not None:
            date = match[10:14] + '-' + match[5:7] + '-' + match[0:2]
    
        # Pattern 7
        elif re.search(pattern7, match) is not None:
            date = match[8:12] + '-' + match[4:6] + '-' + match[0:2]
    
        return date
