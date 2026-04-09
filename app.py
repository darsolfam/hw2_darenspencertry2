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
You are an assistant that extracts action items from meeting notes.

Rules:
- List each action item on its own line starting with a dash (-)
- Include the owner's name if mentioned
- Include the deadline if mentioned
- Keep all tool codes, team names, and jargon exactly as written — do not explain or expand them
- If no clear action items exist, say: "No clear action items found. Human review recommended."
- Do not invent information that is not in the notes
"""

# ─── MEETING NOTES INPUT ──────────────────────────────────────────────────────

# To test a different case, replace the text between the triple quotes below.
MEETING_NOTES = """
BC5 is down for unplanned maintenance, tech assigned. Yield on lot 4471 came in low,
PE to investigate recipe on K1D. Team agreed to move Thursday scrap review to Friday.
Sarah to send updated WIP report by EOD.
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
