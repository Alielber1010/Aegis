# Eval datasets

Versioned JSONL, one question per line. Sets are never merged.

| File | What | Author |
|---|---|---|
| `human_v1.jsonl` | 40-question gold set (from Eval Aegis.docx) | human |
| `claude_v1.jsonl` | parallel AI-written gold set | Claude |
| `access_control_v1.jsonl` | zero-leak / tenant isolation questions | Claude |
| `review_v1.jsonl` | multi-step redline review questions | Claude |

Each question carries a `path` label (`lookup` | `review`) used to score the router.
