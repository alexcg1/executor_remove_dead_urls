from jina import Executor, DocumentArray, requests
import requests as rq


class RemoveDeadURLs(Executor):
    def __init__(self, tag: str = "url", **kwargs):
        super().__init__(**kwargs)
        self.tag = tag

    """Checks specified tags for dead URLs and removes Documents accordingly"""

    @requests(on="/index")
    def remove_dead_urls(self, docs: DocumentArray, **kwargs):
        dead_links = []
        for idx, doc in enumerate(docs):
            try:
                response = rq.get(doc.tags[self.tag])
                assert response.status_code == 200
            except:
                dead_links.append(idx)

        dead_links.reverse()

        for idx in dead_links:
            del docs[idx]
