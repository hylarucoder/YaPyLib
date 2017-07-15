from parsel import Selector


class ParseWorker(object):
    pass


class ExtendedSelector(Selector):
    """
    对文本记性
    """

    def __init__(self, text=None, type=None, namespaces=None, root=None, base_url=None, _expr=None):
        super().__init__(text, type, namespaces, root, base_url, _expr)

    def final_xpath_extract_first(self, query, delimiter="|", namespaces=None, **kwargs):
        if delimiter in query:
            query, suffix_query = query.split(delimiter)
            result = self.xpath(query, namespaces=namespaces, **kwargs).extract_first()
            if suffix_query == 'int':
                pass
            elif suffix_query == 'str':
                pass
            else:
                pass
        else:
            result = self.xpath(query, namespaces=namespaces, **kwargs).extract_first()
        return query
