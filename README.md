# RemoveDeadURLs

Checks specified tags for dead URLs and removes Documents accordingly.

| Scenario             | Outcome                  |
| ---                  | ---                      |
| `tag` is valid URL   | Don't touch the Document |
| `tag` is invalid URL | Remove Document          |
| `tag` doesn't exist  | Don't touch the Document |
| `tag` is empty       | Don't touch the Document |

## Usage

Pass the name of the tag that stores the URL to check.

#### via Docker image (recommended)

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://RemoveDeadURLs', uses_with={'tag': 'url'})
```

#### via source code

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://RemoveDeadURLs', uses_with={'tag': 'url'})
```

- To override `__init__` args & kwargs, use `.add(..., uses_with: {'key': 'value'})`
- To override class metas, use `.add(..., uses_metas: {'key': 'value})`
