# Module with various utilities to help with web manipulations
import ssl
import os


class IsoCodes:
    # languages ISO 639-2 codes
    iso639_2 = ['aa', 'ab', 'af', 'am', 'ar', 'as', 'ay', 'az', 'ba', 'be', 'bg', 'bh', 'bi', 'bn', 'bo', 'br', 'ca',
                'co', 'cs', 'cy', 'da', 'de', 'dz', 'el', 'en', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fj', 'fo', 'fr',
                'fy', 'ga', 'gd', 'gl', 'gn', 'gu', 'ha', 'hi', 'he', 'hr', 'hu', 'hy', 'ia', 'id', 'ie', 'ik', 'in',
                'is', 'it', 'iu', 'iw', 'ja', 'ji', 'jw', 'ka', 'kk', 'kl', 'km', 'kn', 'ko', 'ks', 'ku', 'ky', 'la',
                'ln', 'lo', 'lt', 'lv', 'mg', 'mi', 'mk', 'ml', 'mn', 'mo', 'mr', 'ms', 'mt', 'my', 'na', 'ne', 'nl',
                'no', 'oc', 'om', 'or', 'pa', 'pl', 'ps', 'pt', 'qu', 'rm', 'rn', 'ro', 'ru', 'rw', 'sa', 'sd', 'sg',
                'sh', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sq', 'sr', 'ss', 'st', 'su', 'sv', 'sw', 'ta', 'te', 'tg',
                'th', 'ti', 'tk', 'tl', 'tn', 'to', 'tr', 'ts', 'tt', 'tw', 'ug', 'uk', 'ur', 'uz', 'vi', 'vo', 'wo',
                'xh', 'yi', 'yo', 'za', 'zh', 'zu']


class Domains:
    # All Google domains, used in google searching modules
    google = ['ae', 'am', 'as', 'at', 'az', 'ba', 'be', 'bg', 'bi', 'bs', 'ca', 'cd', 'cg', 'ch', 'ci', 'cl',
              'co.ck', 'co.cr', 'co.hu', 'co.id', 'co.il', 'co.im', 'co.in', 'co.je', 'co.jp', 'co.ke', 'co.kr',
              'co.ls', 'co.ma', 'co.nz', 'co.th', 'co.ug', 'co.uk', 'co.uz', 'co.ve', 'co.vi', 'co.za', 'co.zm',
              'com', 'com.af', 'com.ag', 'com.ar', 'com.au', 'com.bd', 'com.bo', 'com.br', 'com.bz', 'com.co',
              'com.cu', 'com.do', 'com.ec', 'com.eg', 'com.et', 'com.fj', 'com.gi', 'com.gt', 'com.hk', 'com.jm',
              'com.kw', 'com.ly', 'com.mt', 'com.mx', 'com.my', 'com.na', 'com.nf', 'com.ni', 'com.np', 'com.om',
              'com.pa', 'com.pe', 'com.ph', 'com.pk', 'com.pr', 'com.py', 'com.qa', 'com.sa', 'com.sb', 'com.sg',
              'com.sv', 'com.tj', 'com.tr', 'com.tw', 'com.ua', 'com.uy', 'com.uz', 'com.vc', 'com.vn', 'cz', 'de',
              'dj', 'dk', 'dm', 'ee', 'es', 'fi', 'fm', 'fr', 'gg', 'gl', 'gm', 'gr', 'hn', 'hr', 'ht', 'hu', 'ie',
              'is', 'it', 'jo', 'kg', 'kz', 'li', 'lk', 'lt', 'lu', 'lv', 'md', 'mn', 'ms', 'mu', 'mw', 'net', 'nl',
              'no', 'nr', 'nu', 'off.ai', 'org', 'pl', 'pn', 'pt', 'ro', 'ru', 'rw', 'sc', 'se', 'sh', 'si', 'sk',
              'sm', 'sn', 'tm', 'to', 'tp', 'tt', 'tv', 'uz', 'vg', 'vu', 'ws', 'com']


def determine_ssl():
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
            getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context


def extract_keyword(url):
    url = str(url)
    if url.find('https') != -1:
        if url.find('www') != -1:
            url = url[12:].split('/')
            url = url[0]
            url = url.split('.')
            keyword = url[0]
        else:
            url = url[8:].split('/')
            url = url[0]
            url = url.split('.')
            if len(url[0]) != 2:
                keyword = url[0]
            else:
                keyword = url[1]
    elif url.find('http') != -1:
        if url.find('www') != -1:
            url = url[11:].split('/')
            url = url[0]
            url = url.split('.')
            keyword = url[0]
        else:
            url = url[7:].split('/')
            url = url[0]
            url = url.split('.')
            keyword = url[0]
    elif url.find('www') != -1:
        url = url[4:].split('.')
        keyword = url[0]
    else:
        url = url[0:].split('.')
        keyword = url[0]
    return keyword
