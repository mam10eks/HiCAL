from config.settings.base import STATICFILES_DIRS
from urllib.parse import quote
from bs4 import BeautifulSoup
from html2text import html2text
from functools import lru_cache
from distutils.dir_util import copy_tree

def __query_dir(query):
    return '/mnt/ceph/storage/data-in-progress/kibi9872/crypsor/persisted-queries/' + quote(query.strip()) +'/'

def __static_query_dir(query):
    return STATICFILES_DIRS[0] + '/persisted-queries/' + query.strip().replace(' ', '-') +'/'

def __normalize_url(url):
    return url.replace(':', '.').replace('/', '.')

def __url_dir(query, url):
    return __query_dir(query) + normalize_url(url) + '/'

def __static_url_image(query, url):
    return __static_query_dir(query) + normalize_url(url) + '/script/page.png'

def __documents_for_query(query):
    with open(__query_dir(query) + 'queries.txt', 'r') as f:
        return [i.strip() for i in f.readlines() if i.strip()]


def __parse_document_for_query(query, url):
    with open(__url_dir(query, url) + 'script/page.html', 'r') as f:
        return BeautifulSoup(f.read(), 'html.parser')

def __url_to_document(query, url):
    doc = __parse_document_for_query(query, url)

    return {
        'doc_id': url,
        'title': doc.title.text if doc and doc.title else url,
        'content': html2text(str(doc)),
        'doc_image': __static_url_image(query, url),
        'date': '',
        'snippet': '',
    }


@lru_cache(maxsize=None)
def cached_get_documents(query):
    copy_tree(__query_dir(query), __static_query_dir(query))
    return [__url_to_document(query, i) for i in __documents_for_query(query)]


def get_documents(query):
    return cached_get_documents(query)

