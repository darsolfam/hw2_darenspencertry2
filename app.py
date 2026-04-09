"""
app.py - Meeting Notes to Action Items
Week 2 HW - GenAI Workflow

How to run:
    python3 app.py

Requirements:
    pip3 install anthropic
    export ANTHROPIC_API_KEY=your_key_here
"""

import os
import anthropic

# ─── CONFIGURATION ────────────────────────────────────────────────────────────

# The model we are using.
MODEL = "claude-haiku-4-5-20251001"

# The system instruction tells the AI what its job is.
# This is what we will revise in Step 5.
SYSTEM_INSTRUCTION = """
You are an assistant that processes Daily Action Meeting (DAM) notes for a manufacturing team.

Produce output in exactly three sections:

TOOL STATUS:
- List every tool mentioned as down, in progress, or being serviced
- Format: <tool code> — <status label>, <current situation and what is being done>
- Status labels: DOWN, IN PROGRESS, RETURNED TO QUEUE, NEEDS ATTENTION
- Keep all tool codes exactly as written — do not explain or expand them

ACTION ITEMS:
- List each task that needs to be completed
- Format: - <action> | Owner: <name or "unassigned"> | Due: <deadline or "not specified">
- Keep all tool codes, team names, and jargon exactly as written
- Do not list things already captured in TOOL STATUS as action items

NEEDS FOLLOW-UP:
- List any topic discussed with no decision, no owner, or no resolution
- Include any escalations where the outcome or next step is unclear
- Format: - <topic> — <reason it needs follow-up>, human review recommended
"""

# ─── MEETING NOTES INPUT ──────────────────────────────────────────────────────

# To test a different case, replace the text between the triple quotes below.
MEETING_NOTES = """
297 is down to ASML for lens setup, A Shift saw an issue Sunday and escalated to WS. ChemicalX is going to need a bottle change sometime today on BC5.
297 PM completed, back in queue. Discussed throughput drop on F shift — supervisor to pull run data and present tomorrow. New lot release schedule reviewed, no changes. Training for two new techs scheduled for next week, Mark owns.
Quick DAM. No major issues. Team aligned. BC5 still down.
K1D showing drift on the 200 recipe, talked to the guy from the vendor, he says it's probably the widget. 297 and BC5 both in queue. Lot 4490 needs a PE sign-off before it can move. Someone needs to talk to J-team about the A shift handoff.
Long discussion about the rework process for defective lots. Several opinions shared. No consensus reached. Will revisit tomorrow. Also mentioned the C shift and 1st shift overlap issue again — no resolution.
"""

# ─── CALL THE API ─────────────────────────────────────────────────────────────

def get_action_items(notes):
    """Send meeting notes to Claude and return the action items."""

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set.")
        print("Run: export ANTHROPIC_API_KEY=your_key_here")
        return None

    client = anthropic.Anthropic(api_key=api_key)

    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=SYSTEM_INSTRUCTION,
        messages=[
            {"role": "user", "content": "Meeting notes:\n" + notes}
        ]
    )

    return response.content[0].text

# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 50)
    print("MEETING NOTES TO ACTION ITEMS")
    print("=" * 50)
    print("\nInput notes:\n")
    print(MEETING_NOTES.strip())
    print("\n" + "-" * 50)
    print("\nAction items:\n")

    result = get_action_items(MEETING_NOTES)

    if result:
        print(result)

        # Save output to a file
        with open("output.txt", "w") as f:
            f.write("INPUT NOTES:\n")
            f.write(MEETING_NOTES.strip())
            f.write("\n\nACTION ITEMS:\n")
            f.write(result)

        print("\n" + "-" * 50)
        print("Output saved to output.txt")

if __name__ == "__main__":
    main()
