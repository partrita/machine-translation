## Completion Status Markers [STRICT - EVERY TEXT RESPONSE]

At the end of **every** text-only response, include exactly one marker on its own line:

```
TASK_STATUS: COMPLETE
TASK_STATUS: BLOCKED
TASK_STATUS: INCOMPLETE
```

**Mapping to Turn Continuity rules:**
- `COMPLETE` → used when task is fully done and verified (aligns with Turn Continuity reason #1)
- `BLOCKED` → used when hard blocker or unrecoverable error (aligns with Turn Continuity reasons #2 and #3)
- `INCOMPLETE` → **platform-forced only** when OpenCode terminates mid-task due to limits; never choose deliberately

**Placement rules:**
- The marker must be the last line of the response
- No additional text after the marker
- Only ONE marker per response

---
