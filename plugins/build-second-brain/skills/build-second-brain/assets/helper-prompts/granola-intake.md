Instructions
Append today's Granola meeting notes to the daily-intake file in your second-brain wiki.

Steps:
1. Use the Granola connector (tools: list_meetings, get_meetings) to fetch all meetings from today (local date). If the Granola connector is unavailable or not authenticated, stop and notify the user that Granola needs to be reconnected.
2. For each meeting today, get the full enhanced Granola notes (not transcripts).
3. Target file: daily-intake/<YYYY-MM-DD>.md (relative to your brain repo root) using today's local date.
   - If the file exists, APPEND to it — never overwrite or delete existing content.
   - If it doesn't exist, create it.
4. Append a section like:

## Granola notes — <YYYY-MM-DD>

### <Meeting title> (<start time>)
<full Granola notes for the meeting>

(one subsection per meeting, in chronological order)

5. If a meeting's notes are already present in the file (check for its title under a "Granola notes" heading), skip it to avoid duplicates.
6. If there were no meetings today, do nothing — don't create an empty section.

Success: today's daily-intake file contains the full notes of every Granola meeting from today, with no duplicates and no lost prior content.