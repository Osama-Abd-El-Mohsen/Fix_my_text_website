fixTextDict={
    'a':'ش',
    'b':'لا',
    'c':'ؤ',
    'd':'ي',
    'e':'ث',
    'f':'ب',
    'g':'ل',
    'h':'ا',
    'i':'ه',
    'j':'ت',
    'k':'ن',
    'l':'م',
    'm':'ة',
    'n':'ى',
    'o':'خ',
    'p':'ح',
    'q':'ض',
    'r':'ق',
    's':'س',
    't':'ف',
    'u':'ع',
    'v':'ر',
    'w':'ص',
    'x':'ء',
    'y':'غ',
    'z':'ئ',
    '`':'ذ',
    "'":'ط',
    ";":'ك',
    "/":'ظ',
    "[":'ج',
    "]":'د',
    ".":'ز',
    ",":'و',
}


text = "hshli lpl] uf] hglpsk lpl]"

def FixMyText(BadText : str):
    fixedText = ''
    for x in BadText.lower() :
        if x in fixTextDict.keys():
            fixedText+=fixTextDict[f'{x}']
        else  :
            fixedText+=x
    return fixedText

print(FixMyText(text))