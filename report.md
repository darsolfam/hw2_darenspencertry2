# Report — Meeting Notes to Action Items
**Week 2 GenAI Workflow Assignment**

---

## Business Use Case

I work in semiconductor manufacturing where every shift begins with a Daily Action Meeting (DAM). After each DAM, Zoom AI generates an automatic summary that gets emailed to the team. These summaries are useful but incomplete — they capture what happened but do not reliably extract who needs to do what, by when, or flag issues that went unresolved.

The goal of this prototype is to take those Zoom-generated DAM summaries and produce three structured outputs: a tool status section (down tools are a primary focus of every DAM), a clear action item list with owners and deadlines, and a follow-up section for anything discussed but not resolved.

The user is anyone on the manufacturing team who attends or receives notes from a DAM — engineers, supervisors, and shift leads. The value of automating this is real: meetings move fast, notes are incomplete, and people half-listening miss action items. A consistent structured summary reduces missed follow-ups and creates accountability that informal notes do not.

---

## Model Choice

I used **Claude Haiku** (claude-haiku-4-5-20251001) via the Anthropic API.

My original plan was to use Google Gemini through Google AI Studio, which the assignment recommends as the free default. However, my Google account was flagged for suspicious activity during setup, which locked the free tier quota to 0 for all models. I switched to the Anthropic API, which provided $20 in existing credits — more than sufficient for this assignment.

I initially chose Haiku for its speed and low cost, reasoning that structured extraction does not require deep reasoning. I later tested Sonnet (claude-sonnet-4-6) on the same input and observed two meaningful differences: Sonnet correctly captured an internal escalation ("A Shift escalated to WS") that Haiku dropped entirely, and Sonnet flagged a contradiction in the notes where the same tool appeared as both "down to vendor" and "back in queue" — placing it in NEEDS FOLLOW-UP rather than silently picking one. For clean, well-structured notes Haiku performs comparably. For real-world DAM notes that contain contradictions, jargon, and incomplete information, Sonnet handles edge cases more reliably. The cost difference is negligible for this use case, so the final version uses Sonnet.

---

## Baseline vs. Final Design

**Version 1 (Baseline)** used a simple prompt: extract action items as a bulleted list, keep jargon verbatim, say "no action items found" if nothing was clear. Testing revealed three problems:

1. Items already in progress (e.g. a tool already at the vendor for repair) were listed as new action items
2. Vague statements with no owner ("will revisit tomorrow") were turned into action items
3. Internal escalations using unknown abbreviations (e.g. "escalated to WS") were silently dropped

**Version 2** restructured the output into three sections — TOOL STATUS, ACTION ITEMS, and NEEDS FOLLOW-UP. This was directly informed by domain knowledge: in a real DAM, tool status is a primary topic and deserves its own section. The improvement was significant. Tool issues were correctly separated from tasks, and unresolved discussions were flagged for human review.

**Version 3 (Final)** made two additional improvements based on Version 2 output: tool codes now appear first in each status line for faster scanning, and explicit status labels (DOWN, IN PROGRESS, RETURNED TO QUEUE, NEEDS ATTENTION) were added. Escalations were also explicitly called out in the NEEDS FOLLOW-UP instructions.

The final output for a representative test case correctly identified 3 tool statuses, 6 action items with owners and deadlines, and 3 unresolved discussion topics — all without inventing information or misinterpreting internal tool codes.

---

## Where the Prototype Still Fails

During prompt iteration with Haiku, a recurring failure appeared: when an internal abbreviation had no surrounding context, the model dropped it rather than flagging it. In testing, "A Shift escalated to WS" disappeared from all three Haiku outputs. Sonnet handled this better — it included the WS escalation in the tool status entry. However, both models remain unreliable when encountering completely unknown internal terms with no context clues.

This is a meaningful gap. In semiconductor manufacturing, internal team names and process abbreviations are common, and a missed escalation could have real operational consequences. The prototype cannot be trusted to catch everything — it requires a human to review the output against the original notes, especially for any line containing an unfamiliar abbreviation.

---

## Deployment Recommendation

I would recommend deploying this workflow as a **draft aid, not a replacement for human review.**

The current Zoom AI summaries are likely not being read consistently — they are too generic to be immediately useful. The structured three-section output this prototype produces (tool status, action items, needs follow-up) is a meaningfully better format. If the output is more useful, people will actually read it, and that alone increases the value of the meeting.

However, deployment should include the following conditions:
- A human reviewer compares the output to the original notes before distributing
- The team is informed that items with unknown abbreviations may be dropped
- The prompt is updated over time as new internal terms and team names are identified

The opportunity here is not just automation — it is making the post-meeting summary worth reading in the first place.
