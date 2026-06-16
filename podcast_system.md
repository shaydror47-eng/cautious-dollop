# Podcast Research & Content System

## Overview

A manually-triggered multi-agent podcast research and content system designed to develop episodes for people aged 20–29.

**Core Concept**: "What should people understand, build, change, experience, or prepare during their twenties so that they reach age thirty stronger, more prepared, and less surprised by life?"

The system runs **only when you manually activate it**—no scheduled runs, no fixed times.

---

## How It Works

This system consists of **4 specialized agents** that work together:

1. **Podcast Orchestrator** — Coordinates the workflow and quality-checks all output
2. **Topic Discovery Agent** — Finds strong, relevant podcast topics for 20-29 year-olds
3. **Research & Verification Agent** — Researches topics and verifies all facts
4. **Episode & Games Producer** — Creates episode blueprints and interactive games

Each run produces a **timestamped markdown report** in `/podcast_reports/`.

---

## Run Modes

Choose one of these modes when you invoke the Podcast Orchestrator:

### 1. DISCOVER TOPICS
**What it does**: Generates 3–5 new podcast topic ideas, ranked and scored.

**Output**: Topic proposals with scores for relevance, emotional strength, research potential, viral potential, and audience interaction.

**Use when**: You want fresh episode ideas or need topic inspiration.

**Example**: "Run DISCOVER TOPICS mode to find new episode ideas."

---

### 2. RESEARCH A TOPIC
**What it does**: Performs deep research on a topic you provide.

**Input needed**: A specific topic or question (e.g., "Why do people work throughout their twenties and still reach thirty without savings?")

**Output**: 
- Research summary
- 5 important findings with sources
- 3 surprising facts
- 3 common myths
- 3 mistakes people in their twenties make
- 3 points experts disagree about
- 5 practical actions for the audience
- Risks and sensitive areas
- Unanswered questions
- Complete source list with citations

**Use when**: You have a topic and want verified research.

**Example**: "Research the topic: How do financial decisions in your twenties affect wealth by thirty?"

---

### 3. BUILD AN EPISODE
**What it does**: Creates a complete episode blueprint from already-researched material.

**Input needed**: The verified research from Mode 2 (or research you've already compiled).

**Output**:
- 5 episode title options
- Opening hook
- 30-second introduction
- Episode structure and outline
- Host questions
- Guest questions
- Audience participation sections
- 3 polls for viewers
- 5 short-form video moments
- 5 social media captions
- Closing question
- Weekly challenge for listeners

**Use when**: You have good research and want to develop the episode content.

**Example**: "Build an episode from the research on financial decisions in your twenties."

---

### 4. CREATE GAMES
**What it does**: Generates 5+ interactive games or segments for a podcast episode.

**Input needed**: The topic and any relevant research.

**Output**: Interactive games with:
- Game name and purpose
- How it works (mechanics)
- Questions or scenarios
- Guest participation method
- Audience participation method
- Estimated duration
- What emotion/insight/humor it creates

**Example games**:
- "I Wish I Knew This at 20"
- "Age 20 or Age 30"
- "The Cost of the Mistake"
- "Red Flag or Normal Stage"
- "Truth or Bad Advice"
- "Impossible Choice"

**Use when**: You have an episode concept and want engaging interactive segments.

**Example**: "Create games for an episode about relationship red flags in your twenties."

---

### 5. FULL PODCAST RUN
**What it does**: Complete workflow from topic discovery → research → episode development → games → final review.

**Output**: One comprehensive dated report with everything:
- Recommended topic with justification
- Target audience relevance
- Verified research summary
- Key facts and sources
- Myths and common mistakes
- Episode angle and titles
- Complete episode structure
- Host and guest questions
- Audience interaction ideas
- Interactive games
- Short-form video ideas
- Practical listener takeaways
- Quality report (what's verified vs. interpretation vs. creative)

**Use when**: You want a complete episode ready for production.

**Example**: "Run a FULL PODCAST RUN on the topic: Career choices in your twenties."

---

### 6. UPDATE AN EXISTING EPISODE
**What it does**: Refreshes an old episode idea with new research and updated content.

**Input needed**: Name or summary of the old episode from `/podcast_reports/archive/`.

**Output**: Updated episode package with new research, refreshed content, and revised games.

**Use when**: An existing episode needs current information or improvements.

**Example**: "Update the episode on social media comparison—use 2026 research."

---

### 7. FACT-CHECK ONLY
**What it does**: Verifies claims, statistics, scripts, or guest statements you provide.

**Input needed**: The text to fact-check (claims, statistics, quotes, script excerpts).

**Output**: Fact-check report showing:
- Which claims are verified
- Which claims need citations
- Which claims contradict available evidence
- Which claims cannot be verified
- Suggested corrections
- Source list

**Use when**: You want to verify a script, guest statement, or claims before recording.

**Example**: "Fact-check this claim: 'People who have side projects in their twenties earn 30% more by age thirty.'"

---

## How to Invoke the System

### Step 1: Open Claude Code Chat (in this repo)

Ask for a specific run mode. The Podcast Orchestrator will handle it.

### Step 2: Provide Your Input

Depending on the mode, give:
- **DISCOVER TOPICS**: No input needed (or optional topic category)
- **RESEARCH A TOPIC**: Your specific topic or question
- **BUILD AN EPISODE**: The research you want to use
- **CREATE GAMES**: The topic and episode concept
- **FULL PODCAST RUN**: Optional starting topic (or orchestrator discovers one)
- **UPDATE AN EXISTING EPISODE**: The episode name/date to update
- **FACT-CHECK ONLY**: The claims or script to verify

### Step 3: Wait for the Agents

The Orchestrator will:
- Spawn specialized agents as needed
- Coordinate their work
- Quality-check all output
- Produce a final report

### Step 4: Review Your Report

Reports are saved as timestamped markdown files in `/podcast_reports/`:
- `2026-06-16_topic-discovery.md`
- `2026-06-16_research-salary.md`
- `2026-06-16_full-episode-dating.md`

All reports are preserved—nothing gets overwritten.

---

## Quality Guarantees

Every report includes:

✓ **No invented facts** — All claims are based on real research  
✓ **Complete citations** — Every finding has a source with publication date and link  
✓ **Clear distinctions** — Report marks what is verified fact vs. interpretation vs. creative suggestion  
✓ **No unsubstantiated claims** — Correlation is never treated as causation  
✓ **Credible sources** — Primary sources preferred, all sources are real and accessible  
✓ **Honesty about limitations** — Uncertain claims are clearly labeled  
✓ **Sophisticated content** — Games are engaging, not childish  

---

## Report Structure

Each timestamped report contains:

```
# Podcast Report: [Topic]
Date: 2026-06-16  
Mode: [DISCOVER TOPICS / RESEARCH / BUILD EPISODE / etc.]

## A. Topic & Relevance
[Why this topic matters for 20-29 year-olds]

## B. Research Summary
[Key findings]

## C. Episode Structure
[Titles, hook, outline]

## D. Interactive Games
[5+ games with mechanics]

## E. Quality Report
✓ Verified facts: [Count]
→ Interpretations: [Count]
◆ Creative suggestions: [Count]
? Requires additional research: [Count]

## F. Complete Source List
[All citations with dates and links]
```

---

## Example Workflow

**You ask**: "I want a FULL PODCAST RUN on a topic about relationships in your twenties."

**Orchestrator**:
1. Calls Topic Discovery Agent → "relationships in twenties" topic is refined
2. Calls Research Agent → Finds 40+ sources on dating, breakups, commitment
3. Calls Episode Producer → Creates episode, games, video ideas
4. Quality-checks everything
5. Produces final report: `2026-06-16_full-episode-relationships.md`

**You get**: A complete podcast blueprint with research, episode structure, games, and everything ready for production.

---

## Notes

- **Manual only**: System does NOT run on a schedule. You control when runs happen.
- **Fresh starts**: Each run is independent. No state carries over.
- **Reports preserved**: Old reports go to `/podcast_reports/archive/` when needed, nothing is deleted.
- **Audience**: All content is designed for people aged 20–29.
- **Central theme**: Every episode explores: "What should they understand/build/change/prepare to reach 30 stronger and less surprised?"

---

## Next Steps

1. **Decide what you want**: Choose a run mode from the list above
2. **Ask in Claude Code chat**: Invoke the Podcast Orchestrator with your chosen mode
3. **Wait for the report**: Agents work together and produce output
4. **Review and iterate**: Check your report, then run another mode if needed

---

## Questions or Adjustments?

If an agent produces weak output or you need changes:
- Ask the Orchestrator to refine or regenerate
- Specify which section needs improvement
- The next run will be fresh and use your feedback

---

**Created**: 2026-06-16  
**Last updated**: 2026-06-16  
**Status**: Ready for manual invocation
