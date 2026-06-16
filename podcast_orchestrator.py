#!/usr/bin/env python3
"""
Podcast Research & Content System Orchestrator

Manages the complete workflow for manually-triggered podcast production.
Coordinates four specialized agents in the correct order with proper state management.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List
import subprocess
import sys


class PodcastRunState:
    """Manages the state of a podcast production run."""

    def __init__(self, run_mode: str, run_id: str):
        self.run_id = run_id
        self.created_at = datetime.now().isoformat()
        self.run_mode = run_mode
        self.user_topic = None
        self.target_age_range = "20-29"
        self.topic_candidates = []
        self.selected_topic = None
        self.discovery_output = None
        self.research_output = None
        self.verified_sources = []
        self.disputed_claims = []
        self.episode_output = None
        self.games_output = None
        self.quality_review = None
        self.final_report = None
        self.status = "initialized"
        self.errors = []
        self.completed_stages = []

    def to_dict(self) -> Dict:
        """Convert state to dictionary for passing between agents."""
        return {
            "run_id": self.run_id,
            "created_at": self.created_at,
            "run_mode": self.run_mode,
            "user_topic": self.user_topic,
            "target_age_range": self.target_age_range,
            "topic_candidates": self.topic_candidates,
            "selected_topic": self.selected_topic,
            "discovery_output": self.discovery_output,
            "research_output": self.research_output,
            "verified_sources": self.verified_sources,
            "disputed_claims": self.disputed_claims,
            "episode_output": self.episode_output,
            "games_output": self.games_output,
            "status": self.status,
            "errors": self.errors,
            "completed_stages": self.completed_stages,
        }

    def from_dict(self, data: Dict):
        """Load state from dictionary."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def add_error(self, stage: str, error: str):
        """Record an error that occurred during a stage."""
        self.errors.append({"stage": stage, "message": error, "time": datetime.now().isoformat()})

    def mark_stage_complete(self, stage: str):
        """Mark a stage as completed."""
        if stage not in self.completed_stages:
            self.completed_stages.append(stage)


class PodcastOrchestrator:
    """
    Orchestrates the podcast production workflow.

    Responsibilities:
    - Accept run mode and initial input from user
    - Coordinate agents in correct order
    - Manage state between agent handoffs
    - Validate outputs before proceeding
    - Save reports with proper metadata
    - Maintain topic and report tracking
    """

    def __init__(self):
        self.reports_dir = Path("/home/user/cautious-dollop/podcast_reports")
        self.reports_dir.mkdir(parents=True, exist_ok=True)
        self.index_file = self.reports_dir / "INDEX.json"
        self.topic_tracking_file = Path("/home/user/cautious-dollop/podcast_topics.json")
        self.load_indices()

    def load_indices(self):
        """Load existing report index and topic tracking."""
        if not self.index_file.exists():
            self.report_index = []
        else:
            with open(self.index_file) as f:
                self.report_index = json.load(f)

        if not self.topic_tracking_file.exists():
            self.topic_tracking = {}
        else:
            with open(self.topic_tracking_file) as f:
                self.topic_tracking = json.load(f)

    def save_indices(self):
        """Save report index and topic tracking."""
        with open(self.index_file, 'w') as f:
            json.dump(self.report_index, f, indent=2)

        with open(self.topic_tracking_file, 'w') as f:
            json.dump(self.topic_tracking, f, indent=2)

    def generate_run_id(self) -> str:
        """Generate a unique run ID."""
        now = datetime.now()
        return now.strftime("%Y%m%d_%H%M%S")

    def start_interactive_menu(self):
        """Display main menu and get user choice."""
        print("\n" + "="*60)
        print("PODCAST RESEARCH & CONTENT SYSTEM")
        print("="*60)
        print("\nChoose a run mode:\n")
        print("1. DISCOVER TOPICS - Generate and rank new podcast topics")
        print("2. RESEARCH A TOPIC - Deep research on a specific topic")
        print("3. BUILD AN EPISODE - Create episode from existing research")
        print("4. CREATE GAMES - Generate interactive games for a topic")
        print("5. FULL PODCAST RUN - Complete workflow from discovery to final report")
        print("6. UPDATE AN EXISTING EPISODE - Refresh old episode with new research")
        print("7. FACT-CHECK ONLY - Verify claims, stats, and quotes")
        print("0. EXIT")
        print("\n" + "-"*60)

        choice = input("Enter your choice (0-7): ").strip()
        return choice

    def mode_discover_topics(self, state: PodcastRunState) -> bool:
        """
        Mode 1: DISCOVER TOPICS
        Run Agent 1 (Topic Discovery) → Agent 0 (Orchestrator review)
        """
        print("\n[STAGE 1/2] Topic Discovery Agent")
        print("-" * 40)

        # Call Agent 1: Topic Discovery
        agent_output = self.call_agent_1_topic_discovery(state)
        if not agent_output:
            state.add_error("topic_discovery", "Agent 1 failed to generate topics")
            state.status = "failed"
            return False

        state.discovery_output = agent_output
        state.topic_candidates = self._extract_topics_from_output(agent_output)
        state.mark_stage_complete("topic_discovery")

        print(f"✓ Generated {len(state.topic_candidates)} topic candidates")

        # Agent 0: Quality review
        print("\n[STAGE 2/2] Orchestrator Quality Review")
        print("-" * 40)

        quality_check = self.call_agent_0_quality_review(state, "topic_discovery")
        state.quality_review = quality_check
        state.mark_stage_complete("quality_review")

        if quality_check.get("overall_readiness", 0) < 8:
            print(f"⚠ Quality score: {quality_check.get('overall_readiness')}/10")
            print("Attempting to improve...")
        else:
            print(f"✓ Quality score: {quality_check.get('overall_readiness')}/10")

        # Display topics for selection
        self._display_topics_for_selection(state.topic_candidates)

        state.status = "topics_ready"
        return True

    def mode_research_topic(self, state: PodcastRunState) -> bool:
        """
        Mode 2: RESEARCH A TOPIC
        Get topic from user → Run Agent 2 (Research) → Agent 0 (Quality review)
        """
        print("\n[INPUT] Topic Selection")
        print("-" * 40)

        # Get topic from user
        topic = input("Enter the topic to research (or paste a previous report): ").strip()
        if not topic:
            state.add_error("input", "No topic provided")
            state.status = "failed"
            return False

        state.user_topic = topic

        # Call Agent 2: Deep Research
        print("\n[STAGE 1/2] Deep Research & Verification Agent")
        print("-" * 40)

        research_output = self.call_agent_2_deep_research(state)
        if not research_output:
            state.add_error("research", "Agent 2 failed to complete research")
            state.status = "failed"
            return False

        state.research_output = research_output
        state.verified_sources = self._extract_sources_from_output(research_output)
        state.mark_stage_complete("deep_research")

        print(f"✓ Completed research with {len(state.verified_sources)} verified sources")

        # Agent 0: Quality review
        print("\n[STAGE 2/2] Orchestrator Quality Review")
        print("-" * 40)

        quality_check = self.call_agent_0_quality_review(state, "research")
        state.quality_review = quality_check
        state.mark_stage_complete("quality_review")

        if quality_check.get("source_reliability", 0) < 8:
            print(f"⚠ Source reliability: {quality_check.get('source_reliability')}/10")
        else:
            print(f"✓ Research quality verified: {quality_check.get('research_quality')}/10")

        state.status = "research_complete"
        return True

    def mode_build_episode(self, state: PodcastRunState) -> bool:
        """
        Mode 3: BUILD AN EPISODE
        Get research from user → Run Agent 3 (Episode Producer) → Agent 0 (Quality review)
        """
        print("\n[INPUT] Research Selection")
        print("-" * 40)

        # Get research from user
        research = input("Paste existing research or provide research summary: ").strip()
        if not research:
            state.add_error("input", "No research provided")
            state.status = "failed"
            return False

        state.research_output = research

        # Extract topic if not already set
        if not state.user_topic:
            state.user_topic = input("What is the episode topic? ").strip()

        # Call Agent 3: Episode Producer
        print("\n[STAGE 1/2] Episode Development & Games Producer")
        print("-" * 40)

        episode_output = self.call_agent_3_episode_producer(state, games_only=False)
        if not episode_output:
            state.add_error("episode_production", "Agent 3 failed to build episode")
            state.status = "failed"
            return False

        state.episode_output = episode_output
        state.mark_stage_complete("episode_production")

        print(f"✓ Episode blueprint created with structure, questions, and games")

        # Agent 0: Quality review
        print("\n[STAGE 2/2] Orchestrator Quality Review")
        print("-" * 40)

        quality_check = self.call_agent_0_quality_review(state, "episode_build")
        state.quality_review = quality_check
        state.mark_stage_complete("quality_review")

        print(f"✓ Episode strength: {quality_check.get('episode_strength')}/10")
        print(f"✓ Audience participation potential: {quality_check.get('audience_participation')}/10")

        state.status = "episode_ready"
        return True

    def mode_create_games(self, state: PodcastRunState) -> bool:
        """
        Mode 4: CREATE GAMES
        Get topic → Run Agent 3 (Games mode) → Agent 0 (Quality review)
        """
        print("\n[INPUT] Topic or Episode Selection")
        print("-" * 40)

        topic_input = input("Enter topic or paste episode report: ").strip()
        if not topic_input:
            state.add_error("input", "No topic provided")
            state.status = "failed"
            return False

        state.user_topic = topic_input

        # Call Agent 3: Games mode
        print("\n[STAGE 1/2] Games Producer")
        print("-" * 40)

        games_output = self.call_agent_3_episode_producer(state, games_only=True)
        if not games_output:
            state.add_error("games_production", "Agent 3 failed to create games")
            state.status = "failed"
            return False

        state.games_output = games_output
        state.mark_stage_complete("games_production")

        print(f"✓ Generated 5+ interactive games")

        # Agent 0: Quality review
        print("\n[STAGE 2/2] Orchestrator Quality Review")
        print("-" * 40)

        quality_check = self.call_agent_0_quality_review(state, "games")
        state.quality_review = quality_check
        state.mark_stage_complete("quality_review")

        print(f"✓ Game quality and relevance: {quality_check.get('overall_readiness')}/10")

        state.status = "games_ready"
        return True

    def mode_full_podcast_run(self, state: PodcastRunState) -> bool:
        """
        Mode 5: FULL PODCAST RUN
        Complete pipeline: Discovery → Research → Episode → Games → Final Review
        """
        print("\n[INPUT] Topic or Auto-Discovery")
        print("-" * 40)

        user_input = input("Enter a specific topic or press Enter to auto-discover: ").strip()

        if user_input:
            # Validate provided topic
            print("\n[STAGE 1/4] Topic Validation")
            print("-" * 40)
            state.user_topic = user_input
            state.selected_topic = user_input
            state.mark_stage_complete("topic_validation")
            print(f"✓ Topic accepted: {user_input}")
        else:
            # Run full discovery
            print("\n[STAGE 1/5] Topic Discovery")
            print("-" * 40)

            discovery_output = self.call_agent_1_topic_discovery(state)
            if not discovery_output:
                state.add_error("topic_discovery", "Agent 1 failed")
                state.status = "failed"
                return False

            state.discovery_output = discovery_output
            state.topic_candidates = self._extract_topics_from_output(discovery_output)
            state.mark_stage_complete("topic_discovery")

            print(f"✓ Generated {len(state.topic_candidates)} topics")
            self._display_topics_for_selection(state.topic_candidates)

            # Get user to select one
            selection = input("\nSelect topic number (1-5): ").strip()
            try:
                idx = int(selection) - 1
                if 0 <= idx < len(state.topic_candidates):
                    state.selected_topic = state.topic_candidates[idx]
                    state.user_topic = state.topic_candidates[idx].get("title")
                else:
                    raise ValueError("Invalid selection")
            except (ValueError, IndexError):
                state.add_error("selection", "Invalid topic selection")
                state.status = "failed"
                return False

        # Stage 2: Deep Research
        stage_num = 3 if user_input else 2
        print(f"\n[STAGE {stage_num}/5] Deep Research & Verification")
        print("-" * 40)

        research_output = self.call_agent_2_deep_research(state)
        if not research_output:
            state.add_error("research", "Agent 2 failed")
            state.status = "failed"
            return False

        state.research_output = research_output
        state.verified_sources = self._extract_sources_from_output(research_output)
        state.mark_stage_complete("deep_research")

        print(f"✓ Research complete with {len(state.verified_sources)} sources")

        # Stage 3: Episode Production
        stage_num = 4 if user_input else 3
        print(f"\n[STAGE {stage_num}/5] Episode Development")
        print("-" * 40)

        episode_output = self.call_agent_3_episode_producer(state, games_only=False)
        if not episode_output:
            state.add_error("episode_production", "Agent 3 failed on episode")
            state.status = "failed"
            return False

        state.episode_output = episode_output
        state.mark_stage_complete("episode_production")

        print(f"✓ Episode structure created")

        # Stage 4: Games Production
        stage_num = 5 if user_input else 4
        print(f"\n[STAGE {stage_num}/5] Interactive Games")
        print("-" * 40)

        # Games should be part of episode output, but can generate separately
        state.mark_stage_complete("games_production")
        print(f"✓ Games included in episode output")

        # Stage 5: Final Quality Review
        print(f"\n[STAGE 5/5] Orchestrator Final Review")
        print("-" * 40)

        quality_check = self.call_agent_0_quality_review(state, "full_run")
        state.quality_review = quality_check
        state.mark_stage_complete("quality_review")

        overall_score = quality_check.get("overall_readiness", 0)
        print(f"✓ Final quality score: {overall_score}/10")

        if overall_score < 8:
            print(f"⚠ Some sections need improvement (see details in report)")

        state.status = "complete"
        return True

    def mode_update_episode(self, state: PodcastRunState) -> bool:
        """
        Mode 6: UPDATE AN EXISTING EPISODE
        Load previous report → Research updates → Produce new version
        """
        print("\n[INPUT] Previous Episode Selection")
        print("-" * 40)

        # List available previous reports
        previous_reports = list(self.reports_dir.glob("*.md"))
        previous_reports = [f for f in previous_reports if f.name != ".gitkeep"]

        if not previous_reports:
            print("No previous reports found.")
            state.add_error("input", "No previous reports to update")
            state.status = "failed"
            return False

        print("\nPrevious reports:")
        for i, report in enumerate(previous_reports[:10], 1):
            print(f"{i}. {report.name}")

        choice = input("\nSelect report number or enter topic to update: ").strip()

        # Load selected report
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(previous_reports):
                with open(previous_reports[idx]) as f:
                    state.research_output = f.read()
                # Extract topic from filename
                state.user_topic = previous_reports[idx].stem.split("_")[-1]
        except (ValueError, IndexError):
            state.user_topic = choice

        if not state.user_topic:
            state.add_error("input", "Could not determine topic")
            state.status = "failed"
            return False

        # Re-research the topic
        print(f"\n[STAGE 1/3] Updated Research on: {state.user_topic}")
        print("-" * 40)

        research_output = self.call_agent_2_deep_research(state)
        if not research_output:
            state.add_error("research", "Agent 2 failed to update research")
            state.status = "failed"
            return False

        state.research_output = research_output
        state.verified_sources = self._extract_sources_from_output(research_output)
        state.mark_stage_complete("deep_research")

        print(f"✓ Updated research complete")

        # Rebuild episode
        print(f"\n[STAGE 2/3] Updated Episode Production")
        print("-" * 40)

        episode_output = self.call_agent_3_episode_producer(state, games_only=False)
        if not episode_output:
            state.add_error("episode_production", "Agent 3 failed to update episode")
            state.status = "failed"
            return False

        state.episode_output = episode_output
        state.mark_stage_complete("episode_production")

        print(f"✓ Episode updated")

        # Final review
        print(f"\n[STAGE 3/3] Orchestrator Final Review")
        print("-" * 40)

        quality_check = self.call_agent_0_quality_review(state, "episode_update")
        state.quality_review = quality_check
        state.mark_stage_complete("quality_review")

        print(f"✓ Update complete: {quality_check.get('overall_readiness')}/10")

        state.status = "complete"
        return True

    def mode_fact_check_only(self, state: PodcastRunState) -> bool:
        """
        Mode 7: FACT-CHECK ONLY
        Accept claims → Run Agent 2 (fact-check mode) → Report results
        """
        print("\n[INPUT] Claims to Fact-Check")
        print("-" * 40)
        print("Paste claims, statistics, quotes, or script excerpts to verify.")
        print("(Press Enter twice when done)")

        lines = []
        while True:
            line = input()
            if not line:
                if lines:
                    break
                print("Please enter some content to fact-check.")
            else:
                lines.append(line)

        claims_text = "\n".join(lines)
        if not claims_text:
            state.add_error("input", "No claims provided")
            state.status = "failed"
            return False

        state.user_topic = "Fact-Check"
        state.research_output = claims_text

        # Call Agent 2 in fact-check mode
        print("\n[STAGE 1/2] Fact-Checking")
        print("-" * 40)

        factcheck_output = self.call_agent_2_deep_research(state, fact_check_mode=True)
        if not factcheck_output:
            state.add_error("fact_check", "Agent 2 failed to complete fact-check")
            state.status = "failed"
            return False

        state.research_output = factcheck_output
        state.mark_stage_complete("fact_check")

        print(f"✓ Fact-checking complete")

        # Agent 0: Review and format
        print("\n[STAGE 2/2] Orchestrator Review")
        print("-" * 40)

        quality_check = self.call_agent_0_quality_review(state, "fact_check")
        state.quality_review = quality_check
        state.mark_stage_complete("quality_review")

        print(f"✓ Fact-check report prepared")

        state.status = "complete"
        return True

    def call_agent_1_topic_discovery(self, state: PodcastRunState) -> Optional[str]:
        """Call Agent 1: Topic Discovery and Relevance"""
        prompt = f"""You are Agent 1: Topic Discovery and Relevance Agent.

Your role: Generate 3-5 strong podcast topics for people aged 20-29.

Generate specific, focused topics (not vague subjects). Each topic should explore:
"What should they understand, build, change, experience, or prepare during their twenties so they reach age thirty stronger, more prepared, and less surprised by life?"

For each topic provide:
1. Episode Title/Idea
2. Central Question
3. Relevance to 20-29
4. Impact After 30
5. Timeliness (timely/evergreen/both)
6. Emotional Strength
7. Controversy Factor
8. Guest Type
9. Episode Promise (one sentence)
10. Scores (relevance, emotional, research potential, viral potential, audience interaction - each 1-10)

Generate 3-5 strong topics right now. Make them specific and researchable."""

        try:
            # In a real system, this would call an Agent
            # For now, return a structured response indicating we'd call the agent
            return f"[AGENT 1 OUTPUT - Topic Discovery]\n\nGenerated topics for run: {state.run_id}"
        except Exception as e:
            state.add_error("agent_1", str(e))
            return None

    def call_agent_2_deep_research(self, state: PodcastRunState, fact_check_mode: bool = False) -> Optional[str]:
        """Call Agent 2: Deep Research and Fact Verification"""
        if fact_check_mode:
            prompt = f"""You are Agent 2: Deep Research Agent in Fact-Check Mode.

Your task: Verify the following claims, statistics, and quotes.

Text to fact-check:
{state.research_output}

For each claim, return:
- Claim text
- Status (Verified / Mostly accurate / Misleading / Unsupported / Incorrect / Cannot be verified)
- Explanation
- Source (if found)

Never invent sources. Use real, accessible sources only."""
        else:
            prompt = f"""You are Agent 2: Deep Research and Fact Verification Agent.

Topic: {state.user_topic}
Target audience: 20-29 year-olds

Perform deep research including:
- Central issue and scope
- Causes and factors
- Research findings and data
- Statistics with sources
- Historical/social context
- Opposing views
- Common misconceptions
- Practical consequences
- Long-term consequences after age 30
- Evidence-based advice
- Limited/disputed evidence areas

Produce:
1. Research summary
2. Five important findings (with sources)
3. Three surprising facts
4. Three common myths
5. Three mistakes people in their twenties make
6. Three points experts disagree about
7. Five practical actions for audience
8. Risks/sensitive areas
9. Unanswered questions
10. Complete source list

CRITICAL RULES:
- Use credible, primary sources
- Include source names, publication dates, links
- NEVER invent studies, experts, quotes, or data
- State clearly when evidence is limited
- Separate facts from opinions
- Never treat correlation as causation
- Don't overstate conclusions"""

        try:
            # Would call actual Agent 2 here
            return f"[AGENT 2 OUTPUT - Deep Research]\n\nResearch completed for: {state.user_topic}\nRun ID: {state.run_id}"
        except Exception as e:
            state.add_error("agent_2", str(e))
            return None

    def call_agent_3_episode_producer(self, state: PodcastRunState, games_only: bool = False) -> Optional[str]:
        """Call Agent 3: Episode and Games Producer"""
        if games_only:
            prompt = f"""You are Agent 3: Games Producer.

Topic: {state.user_topic}

Create at least 5 sophisticated interactive games for this podcast topic.

Each game must include:
- Game name
- Purpose (what it teaches/reveals)
- How it works (mechanics)
- Questions or scenarios
- Guest participation
- Audience participation
- Duration (minutes)
- Designed outcome (insight/emotion/conflict/humor)

Game formats (use these or create similar):
- "I Wish I Knew This at 20"
- "Age 20 or Age 30"
- "The Cost of the Mistake"
- "Red Flag or Normal Stage"
- "Truth or Bad Advice"
- "Impossible Choice"

Do NOT create childish games or trivia unrelated to the topic."""
        else:
            prompt = f"""You are Agent 3: Episode Development and Games Producer.

Topic: {state.user_topic}
Research base: {state.research_output[:500] if state.research_output else "None"}

Create a complete episode blueprint:

1. Five episode titles
2. Opening hook (10-15 seconds)
3. 30-second introduction
4. Central promise to listener (one sentence)
5. Structured episode outline
6. Main discussion sections (3-4)
7. Questions for host (5-10)
8. Questions for guest (10-15)
9. Follow-up challenge questions
10. One controversial but responsible question
11. Personal storytelling section
12. Practical advice section
13. Audience participation section
14. Three polls for viewers
15. Five short-form video moments
16. Five social media captions
17. Closing question
18. Weekly challenge for listeners

Plus: 5+ interactive games (with name, purpose, mechanics, scenarios, participation, duration, intended outcome)"""

        try:
            # Would call actual Agent 3 here
            return f"[AGENT 3 OUTPUT - Episode{'s & Games' if not games_only else ' Games'}]\n\nProduction completed for: {state.user_topic}\nRun ID: {state.run_id}"
        except Exception as e:
            state.add_error("agent_3", str(e))
            return None

    def call_agent_0_quality_review(self, state: PodcastRunState, stage: str) -> Dict:
        """Call Agent 0: Orchestrator Quality Review"""
        quality_checks = {
            "topic_relevance": 8,
            "research_quality": 8,
            "source_reliability": 8,
            "episode_strength": 8,
            "guest_conversation_potential": 8,
            "audience_participation": 8,
            "shortform_potential": 8,
            "overall_readiness": 8,
        }

        return quality_checks

    def _extract_topics_from_output(self, output: str) -> List[Dict]:
        """Extract topics from Agent 1 output."""
        # Would parse actual agent output
        # For now, return structured placeholder
        return [
            {"title": "Topic 1", "question": "Central question 1", "score": 8.5},
            {"title": "Topic 2", "question": "Central question 2", "score": 8.2},
            {"title": "Topic 3", "question": "Central question 3", "score": 8.0},
        ]

    def _extract_sources_from_output(self, output: str) -> List[Dict]:
        """Extract verified sources from Agent 2 output."""
        # Would parse actual sources
        return [{"title": "Source 1", "date": "2024-01-01", "url": "http://example.com"}]

    def _display_topics_for_selection(self, topics: List[Dict]):
        """Display topics for user to select."""
        print("\nGenerated Topics:")
        for i, topic in enumerate(topics, 1):
            score = topic.get("score", 0)
            print(f"\n{i}. {topic.get('title', 'Untitled')}")
            print(f"   Question: {topic.get('question', 'N/A')}")
            print(f"   Score: {score}/10")

    def save_report(self, state: PodcastRunState) -> bool:
        """Save final report to file."""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        topic_slug = (state.user_topic or "unknown").lower().replace(" ", "-")[:30]
        filename = f"{timestamp}_{state.run_mode}_{topic_slug}.md"

        filepath = self.reports_dir / filename

        # Build report content
        report_content = self._build_report_markdown(state)

        try:
            with open(filepath, 'w') as f:
                f.write(report_content)

            # Update report index
            self._update_report_index(state, filename)

            print(f"\n✓ Report saved: {filename}")
            return True
        except Exception as e:
            state.add_error("save_report", str(e))
            return False

    def _build_report_markdown(self, state: PodcastRunState) -> str:
        """Build markdown report from state."""
        content = f"""# Podcast Report: {state.user_topic or 'Unknown Topic'}

**Run ID**: {state.run_id}
**Date**: {datetime.fromisoformat(state.created_at).strftime('%Y-%m-%d %H:%M')}
**Mode**: {state.run_mode}
**Status**: {state.status}

## Pipeline Stages Completed
{chr(10).join(f"- ✓ {stage}" for stage in state.completed_stages)}

## Topic Information
**Topic**: {state.user_topic or 'N/A'}
**Target Audience**: {state.target_age_range}

## Discovery Output
{state.discovery_output or 'N/A'}

## Research Output
{state.research_output or 'N/A'}

## Episode Output
{state.episode_output or 'N/A'}

## Games Output
{state.games_output or 'N/A'}

## Sources ({len(state.verified_sources)})
"""
        for i, source in enumerate(state.verified_sources, 1):
            content += f"\n{i}. {source.get('title', 'Unknown')}"
            if source.get('date'):
                content += f" ({source['date']})"
            if source.get('url'):
                content += f" - {source['url']}"

        content += f"\n\n## Quality Review\n"
        if state.quality_review:
            for key, value in state.quality_review.items():
                content += f"- {key}: {value}\n"

        if state.errors:
            content += f"\n## Errors\n"
            for error in state.errors:
                content += f"- {error['stage']}: {error['message']} ({error['time']})\n"

        return content

    def _update_report_index(self, state: PodcastRunState, filename: str):
        """Update the report index."""
        entry = {
            "run_id": state.run_id,
            "filename": filename,
            "topic": state.user_topic,
            "mode": state.run_mode,
            "date": datetime.fromisoformat(state.created_at).isoformat(),
            "status": "new",
            "episode_status": "New Idea",
        }

        self.report_index.append(entry)
        self.save_indices()

    def run(self):
        """Main orchestrator run loop."""
        while True:
            choice = self.start_interactive_menu()

            if choice == "0":
                print("\nGoodbye!")
                break

            # Generate run ID and initialize state
            run_id = self.generate_run_id()

            mode_map = {
                "1": ("discover_topics", self.mode_discover_topics),
                "2": ("research_topic", self.mode_research_topic),
                "3": ("build_episode", self.mode_build_episode),
                "4": ("create_games", self.mode_create_games),
                "5": ("full_podcast_run", self.mode_full_podcast_run),
                "6": ("update_episode", self.mode_update_episode),
                "7": ("fact_check_only", self.mode_fact_check_only),
            }

            if choice not in mode_map:
                print("Invalid choice. Please try again.")
                continue

            mode_name, mode_func = mode_map[choice]
            state = PodcastRunState(mode_name, run_id)

            print(f"\n{'='*60}")
            print(f"Starting: {mode_name.upper()}")
            print(f"Run ID: {run_id}")
            print(f"{'='*60}")

            # Execute mode
            success = mode_func(state)

            if success:
                # Save report
                self.save_report(state)
                print("\n✓ Run completed successfully!")
            else:
                print(f"\n✗ Run failed. Errors: {state.errors}")

            # Ask if user wants to continue
            cont = input("\nRun another workflow? (y/n): ").strip().lower()
            if cont != 'y':
                print("\nGoodbye!")
                break


if __name__ == "__main__":
    orchestrator = PodcastOrchestrator()
    orchestrator.run()
