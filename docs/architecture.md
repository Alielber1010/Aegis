# Architecture

Dependency direction (nothing points back up):

```
api / worker -> workflows -> generation + retrieval -> providers + db -> domain
```

- **lookup**: fast single-shot RAG (persona: clerk).
- **review**: multi-step redline review, background job (persona: senior engineer).
