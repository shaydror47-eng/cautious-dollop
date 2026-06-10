# Apps

## Purpose
Apps and tools in use and in development for work optimization, delivery decisions, and phone workflow.

## Live & Working (Stable — do not change without approval)

### 1. My Center (המרכז שלי) — main hub site
- **Live URL**: https://jade-dragon-3d7cde.netlify.app
- **Source**: `site/` folder in this repo (backed up, versioned)
- **Status**: ✅ Live on Netlify (deployed 2026-06-10)
- **What it has**: Home page with 4 worlds —
  - 🛵 Delivery: shift button (start/stop + earnings), pre-shift checklist, Wolt dashboard, link to the live Wolt app
  - 🧮 Money: bill splitter
  - 💼 Business: post builder
  - 🎡 Misc: workout timer, decision wheel, habit swap
- **v2 (2026-06-10)**: unified dark design across all pages, mobile fixes (zoom, tap targets), 3 new one-tap tools
- **Data**: saved in the browser (localStorage) on each device
- **How to update**: change files in `site/` here → drag updated zip to Netlify Deploys

### 2. Wolt App (מחשבון כדאיות + טיימר משמרת)
- **Live URL**: https://guileless-macaron-451cd2.netlify.app
- **Status**: ✅ Live on Netlify (deployed earlier, stable)

## Development Philosophy
- **Incremental improvement**: fix and enhance step by step
- **No full rewrites**: keep stable versions safe
- **Small focused changes**: one fix at a time
- **Always test on both phones** before calling something done

## Future Ideas
Kept in IDEAS.md. Promote an idea here only when work on it actually starts.

## Testing Checklist (before any release)
- [ ] Works on Phone 1 (Galaxy S23)
- [ ] Works on Phone 2
- [ ] Wolt/Waze still work normally
- [ ] No crashes, battery impact acceptable

## Next Actions
- [ ] Add the My Center link to the phone home screens (open site → "Add to Home Screen")
- [ ] Log any site issue in BUGS.md
