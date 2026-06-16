# Podcast System - Working Notes

**Status**: System ready for first run — 2026-06-16

---

## Quick Start

To run the podcast system, ask for one of these modes in Claude Code chat:

1. **"Discover podcast topics for 20-29 year-olds"**
   - Generates 3-5 topic ideas with scores

2. **"Research this topic: [your specific topic/question]"**
   - Deep research with sources and verification

3. **"Build an episode from this research: [research text]"**
   - Complete episode blueprint

4. **"Create interactive games for: [topic]"**
   - 5+ sophisticated games with mechanics

5. **"Run a full podcast research workflow on: [topic]"**
   - Complete discovery → research → episode → games → final report

6. **"Update the episode about: [old topic]"**
   - Refresh with new research and updated content

7. **"Fact-check these claims: [text/claims]"**
   - Verify statistics, quotes, assertions

---

## Completed Runs

(Track all podcast generation runs here)

### Run 1: [Topic Name]
- **Date**: [When run]
- **Mode**: [Which mode used]
- **Output file**: [Path to report]
- **Status**: ✓ Complete / In Progress / Needs Revision
- **Notes**: [Key observations, what worked well, issues]

---

## Topics Under Consideration

List potential episode topics to research:

- [ ] Why do financial decisions in your twenties affect wealth by 30?
- [ ] How does your friend group at 20-25 determine your future?
- [ ] Career changes during your twenties: switch early or stay?
- [ ] Relationship timing: how to know if it's the right person/time
- [ ] Social media comparison trap: measuring yourself against peers
- [ ] Side projects and entrepreneurship: risk vs. stability
- [ ] Moving out and independence: financial and emotional readiness
- [ ] Mental health and pressure in your twenties
- [ ] Education debt and career decisions
- [ ] Family expectations vs. personal choices

---

## Episode Ideas to Develop

Ideas with potential for strong research and guest interviews:

1. **"Working Throughout Your Twenties and Still Reaching 30 Broke"**
   - Central question: Where does the money go?
   - Guest: Financial advisor + person who lived this
   - Why relevant: 60% of 20-somethings have financial anxiety

2. **"The Friendships That Changed Everything"**
   - Central question: Which friendships shaped your future?
   - Guest: Sociologist + people who credit friendships
   - Why relevant: Friendships now affect career, health, happiness

3. **"The Career Change You Almost Made"**
   - Central question: How do you know when to switch paths?
   - Guest: Career coach + people who switched
   - Why relevant: Most 20-somethings consider changing careers

4. **"Dating in Your Twenties: Red Flags and Growth Stages"**
   - Central question: How do you know if it's wrong vs. just hard?
   - Guest: Therapist + people with relationship experience
   - Why relevant: Many lasting relationships start/fail in twenties

5. **"The Skill Nobody Teaches You: How to Make Hard Decisions"**
   - Central question: What framework actually works?
   - Guest: Decision-making researcher + mentors
   - Why relevant: Major decisions get harder, guidance is rare

---

## Verified Sources to Reference

(Add sources as we research)

### Financial Planning
- [ ] Federal Reserve: Young adult financial behavior (2023)
- [ ] Pew Research: Student debt and millennials
- [ ] BLS: Income data by age cohort

### Relationships & Social
- [ ] Harvard Study of Adult Development (findings on relationships)
- [ ] Pew: Friendship trends among young adults
- [ ] Psychology Today: Decision making in relationships

### Career
- [ ] Bureau of Labor Statistics: Career change frequency
- [ ] LinkedIn Workplace Report (annual)
- [ ] Gallup: Career satisfaction by age

### Mental Health
- [ ] CDC: Mental health among 18-29 year-olds
- [ ] NAMI: Young adult mental health statistics
- [ ] APA: Stress and anxiety in young adults

---

## Games Created So Far

(Track which games have been created and which topics they work for)

- [ ] "I Wish I Knew This at 20" — [Topics used on]
- [ ] "Age 20 or Age 30" — [Topics used on]
- [ ] [Custom game name] — [Topic and mechanics]

---

## Quality Checklist (Before Publishing)

Every report should pass:

- [ ] No invented facts or statistics
- [ ] All claims have real source citations
- [ ] Publication dates included for sources
- [ ] Links to sources are functional
- [ ] No correlation treated as causation
- [ ] Conclusions are not overstated
- [ ] Facts separated from opinions
- [ ] Games are sophisticated, not childish
- [ ] Episode structure is tight and clear
- [ ] Questions prompt real conversation
- [ ] Practical advice is actionable
- [ ] Content is relevant to 20-29 audience
- [ ] Section completeness verified

---

## Known Limitations / To Improve

(Track issues or areas that need improvement)

- [ ] [Issue 1]: [How to address]
- [ ] [Issue 2]: [How to address]

---

## Feedback Loop

After each run, note:
- What worked well
- What could be improved
- Suggestions for next run
- User feedback

---

## Archive Management

Reports that are completed and don't need updates should be moved to `/podcast_reports/archive/` with the naming convention:
```
ARCHIVE_[original-date]_[mode]_[topic].md
```

---

## System Configuration

**Directory structure**:
```
/podcast_reports/          # All new reports
/podcast_reports/archive/  # Completed episodes
podcast_system.md          # User guide
podcast_prompts.md         # Agent instructions
podcast_notes.md           # This file (working notes)
```

**Report file naming**:
```
[DATE]_[MODE]_[TOPIC-SLUG].md
2026-06-16_discover-topics_general.md
2026-06-16_research_financial-twenties.md
2026-06-16_full-run_career-changes.md
```

---

**Last Updated**: 2026-06-16  
**Next Action**: Run first test mode (DISCOVER TOPICS) to verify system works
