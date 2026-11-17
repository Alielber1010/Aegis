# Aegis

Evidence-Driven Agentic Intelligence System: cited answers and redline reviews over construction documents,
with every design choice backed by measurements on a gold eval set.

## Quick start

```bash
cp .env.example .env
make up
make test
```

## Layout

| Path | Responsibility |
|---|---|
| `src/aegis/domain.py` | Shared models: Document, Chunk, Citation, Answer, Scope |
| `src/aegis/ingestion/` | PDF -> clean, chunked, embedded rows |
| `src/aegis/retrieval/` | Lexical, dense, hybrid, rerank; always tenant- and version-scoped |
| `src/aegis/generation/` | Prompts, grounded answers, guardrails |
| `src/aegis/workflows/` | `lookup` (fast RAG) and `review` (LangGraph), plus the router |
| `src/aegis/providers/` | LLM, embedding and reranker vendors behind Protocols |
| `src/aegis/db/` | Postgres + pgvector, row-level security, migrations |
| `src/aegis/api/`, `worker.py` | HTTP in, background review jobs |
| `evals/` | Datasets, metrics, experiment configs, committed results |
| `docs/adr/` | One decision record per measured choice |

Dependency rule: `api/worker -> workflows -> generation + retrieval -> providers + db -> domain`.

The document corpus is not in this repo; see `data/manifest.json` (local only).
