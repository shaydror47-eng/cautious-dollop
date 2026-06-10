# Shay Work Hub

## Purpose
Personal work organization for delivery driver work with Wolt, dual Android phone management, and app development for work tools.

## Work Ecosystem

### 1. Dual Phone System
Two Android phones running in sync for Wolt delivery work. Primary phone for active work, backup instantly available if needed.
- **Critical apps**: Wolt, Waze, Spotify, notifications, work utilities
- **Goal**: Zero downtime - switch phones in seconds if one fails

### 2. Wolt Delivery Work
Full-time delivery driver across Nes Ziona, Rehovot, Rishon LeZion, Yavne, Beer Yaakov and nearby areas.
- **Main hub**: Nes Ziona
- **Focus**: Smart area selection, order acceptance strategy, earnings optimization, stress reduction
- **Tracking**: Daily/weekly earnings, good/bad orders, high-pay areas, time/distance efficiency

### 3. Work Apps & Tools
Building and improving small utilities for delivery decisions, phone workflow, dashboards, and work optimization.
- **Approach**: Incremental improvement, not rewrites
- **Stable versions kept safe** - only make focused fixes

## Quick Navigation

| File | Purpose |
|------|----------|
| `RULES.md` | Rules for AI tools working on this repo |
| `NEXT_ACTIONS.md` | Next practical actions only |
| `DAILY_LOG.md` | Daily work log template |
| `TOOLS.md` | What each tool is used for |
| `CURRENT_PRIORITY.md` | Today's urgent focus |
| `PHONE.md` | Dual phone status, issues, and sync |
| `WORK_DAY.md` | Daily shift tracking and earnings |
| `WOLT.md` | Work areas, order strategy, weekly stats |
| `APPS.md` | Active projects and improvements |
| `BUGS.md` | Phone/app issues blocking work |
| `PROMPTS.md` | AI workflows, build commands, procedures |
| `IDEAS.md` | Future projects and improvements |
| `FINISHED.md` | Completed work and stable releases |
| `WORLD.md` | Resources, learning, observations |

## The Agents (הסוכנים) — how to use them

The agents live inside this repo (`.claude/agents/`). They are available in **every Claude Code chat opened on this repo** — no separate app, no setup. Just ask a normal question in Hebrew; Claude picks the right agent automatically.

| Agent | What it does | Ask it things like |
|-------|--------------|--------------------||
| 🛵 **wolt** | Areas, hours, money goal, accept/reject orders | "מתי הכי כדאי לעבוד?", "כמה היעד השבועי שלי?" |
| 📱 **phone** | The two phones, battery, apps, switching | "הוולט קרס, מה עושים?", "מה מצב טלפון 1?" |
| 🐞 **bugs** | Logging problems, quick fixes | "ה-GPS נתקע במשמרת, תרשום את זה" |
| 📒 **log** | Recording shifts, tracking progress | "תרשום: הרווחתי 280 שקל, 12 הזמנות", "איך השבוע שלי?" |

**Live sites** (also listed in `APPS.md`):
- My Center hub: https://jade-dragon-3d7cde.netlify.app
- Wolt app: https://guileless-macaron-451cd2.netlify.app

## How This Works

1. **Before shift**: Check `CURRENT_PRIORITY.md` and `PHONE.md` status
2. **During work**: Log in `WORK_DAY.md`, flag issues in `BUGS.md`
3. **After shift**: Update earnings in `WOLT.md`, plan next day
4. **When blocked**: Check `PROMPTS.md` for solutions
5. **Weekly review**: Check `FINISHED.md`, plan next improvements

## Contact & Context
- **Work**: Wolt delivery driver
- **Location**: Nes Ziona area (main hub)
- **Tools**: Android, GitHub, Copilot, Claude
- **Philosophy**: Simple, focused, incremental improvement
