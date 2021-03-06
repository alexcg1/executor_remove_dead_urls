from jina import Flow, Document, DocumentArray
from executor import RemoveDeadURLs

rm_dead_url_executor = RemoveDeadURLs
rm_dead_url_executor = "jinahub+docker://RemoveDeadURLs"

docs = DocumentArray(
    [
        Document(tags={"url": "https://example.com"}, text="foo"),
        Document(tags={"url": "https://google.com"}, text="foo"),
        Document(tags={"url": "https://jina.ai"}, text="foo"),
        Document(tags={"url": "http://dsfrwgerijgwioi.com"}, text="foo"),
        Document(tags={"url": "http://example.com/foo"}, text="foo"),
        Document(tags={"url": ""}, text="foo"),
        Document(text="foo"),
    ]
)

flow = (
    Flow()
    .add(
        uses=rm_dead_url_executor,
        uses_with={"tag": "url"},
        name="remove_dead_urls",
        force=True
    )
    .add(uses="jinahub+docker://SpacyTextEncoder", name="encoder")
    .add(uses="jinahub+docker://SimpleIndexer", name="indexer")
)

query_doc = Document(text="foo")

with flow:
    flow.index(inputs=docs, show_progress=True)
    response = flow.search(inputs=[query_doc], return_results=True)

print(response)

matches = response[0].docs[0].matches

for doc in matches:
    if 'url' not in doc.tags.keys():
        doc.tags['url'] = None

    print(f"- {doc.text} - {doc.tags['url']}")
