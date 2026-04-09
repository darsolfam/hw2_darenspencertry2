# Evaluation Set — Meeting Notes to Action Items

Each case includes raw meeting notes (as input) and a description of what a good output should do.

---

## Case 1 — Normal Case (Clear Notes, Obvious Owners)

**Input:**
BC5 is down for unplanned maintenance, tech assigned. Yield on lot 4471 came in low, PE to investigate recipe on K1D. Team agreed to move Thursday scrap review to Friday. Sarah to send updated WIP report by EOD.

**What a good output should do:**
- Extract at least 3 action items
- Identify Sarah as the owner of the WIP report
- Flag the PE as owner of the K1D recipe investigation
- Include the Friday deadline for the scrap review
- NOT invent details that aren't in the notes

---

## Case 2 — Normal Case (Multiple Workstreams, Multiple Owners)

**Input:**
297 PM completed, back in queue. Discussed throughput drop on F shift — supervisor to pull run data and present tomorrow. New lot release schedule reviewed, no changes. Training for two new techs scheduled for next week, Mark owns.

**What a good output should do:**
- Extract at least 2 clear action items (run data, training)
- Correctly assign Mark to the training item
- Note that 297 PM is complete (informational, not an action)
- Recognize "present tomorrow" as a deadline for the run data item

---

## Case 3 — Edge Case (Extremely Sparse Notes)

**Input:**
Quick DAM. No major issues. Team aligned. BC5 still down.

**What a good output should do:**
- Recognize there are no clear action items to extract
- NOT hallucinate or invent action items from vague statements
- Ideally flag that human review is needed or that notes are too sparse
- May note BC5 downtime as a watch item

---

## Case 4 — Jargon / Hallucination Risk Case (Internal Language + Tool Codes)

**Input:**
K1D showing drift on the 200 recipe, talked to the guy from the vendor, he says it's probably the widget. 297 and BC5 both in queue. Lot 4490 needs a PE sign-off before it can move. Someone needs to talk to J-team about the A shift handoff.

**What a good output should do:**
- Keep tool codes (K1D, 297, BC5) verbatim — do NOT expand or explain them
- Keep "J-team" and "the widget" verbatim — do NOT guess what they mean
- Extract the PE sign-off on Lot 4490 as a clear action item
- Flag the J-team handoff as an action item with an unassigned owner
- NOT invent what "the widget" is or what "J-team" stands for

---

## Case 5 — No-Decision Case (Discussion Only, Nothing Resolved)

**Input:**
Long discussion about the rework process for defective lots. Several opinions shared. No consensus reached. Will revisit tomorrow. Also mentioned the C shift and 1st shift overlap issue again — no resolution.

**What a good output should do:**
- Recognize that no decisions or owners were assigned
- NOT fabricate action items from unresolved discussion
- Ideally flag both topics (rework process, shift overlap) as needing follow-up
- May suggest these items be added to the next DAM agenda
