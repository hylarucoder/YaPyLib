from urllib.parse import urlparse, urlunparse, urljoin, urlsplit, urlencode, quote, unquote, quote_plus, unquote_plus, \
    urldefrag


def encode_url(url):
    return urlencode(url)
