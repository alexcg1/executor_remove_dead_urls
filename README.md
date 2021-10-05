# RemoveDeadURLs

Checks specified tags for dead URLs and removes Documents accordingly

## Usage

#### via Docker image (recommended)

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://RemoveDeadURLs')
```

#### via source code

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://RemoveDeadURLs')
```

- To override `__init__` args & kwargs, use `.add(..., uses_with: {'key': 'value'})`
- To override class metas, use `.add(..., uses_metas: {'key': 'value})`
