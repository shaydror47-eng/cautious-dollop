# Ideas

## Purpose
Brainstorm and track new projects, features, and improvements. Filter by effort and value.

## עדיפות: ג'ארוויס — דשבורד AI ("חוות נמלים")

**Concept**: מערכת דשבורד שמחברת סוכני AI וכלים שונים, כל אחד לאזור משלו — כמו חוות נמלים: כל אזור בחווה קשור לסוכן/כלי ספציפי, והכל פועל ומוצג יחד באותו מקום.
**Value**: גבוה מאוד — שי חוזר על הפרויקט הזה כמה שיחות ברציפות; זה מה שהכי חשוב לו לסיים עכשיו, כמה שיותר מהר.
**Status**: תכנון — הפרויקט לא מתועד עדיין באף קובץ במאגר הזה, וזו הפעם הראשונה שהוא נרשם (יש שאלות פתוחות למטה לפני שממשיכים).

**דרישת ליבה — לא לשכוח בשום שלב תכנון או בנייה עתידי**:
פשטות מקסימלית. לא API מסובך, לא הטמעות עמוקות בתוך האתר. חיבור מהיר וברור בין כל כלי/סוכן לבין הדף/האפליקציה הנכונה. מה שצריך זה בקרה פשוטה — משהו שמראה "זה פועל עכשיו" כשזה נפתח, והתראה כשזה מסתיים. זהו, לא יותר מזה. כל דבר שמורכב מדי — לפשט.

### בקשה 1: כניסה בפועל לדשבורד
שי רוצה דרך פשוטה להיכנס בפועל לאפליקציה/לדשבורד ולראות שהכלים שמחוברים אכן פועלים ומוצגים שם.

### בקשה 2: סוכן פייסבוק — מעקב פוסטים למכרזי קלפי פוקימון
**Concept**: התחברות עם חשבון הפייסבוק האישי של שי; סוכן שמסנן פוסטים לפי קטגוריות/מילות מפתח שנבחרות מראש (כמו סימניות).
**מיקוד**: בעיקר קלפי פוקימון וקלפים למכרז — פחות פופים (פופים משני).

**לכל פוסט מציגים**:
- [ ] התמונה מהפוסט
- [ ] הכיתוב (הטקסט) של הפוסט
- [ ] זמן פרסום מדויק — **לא** "לפני X זמן" יחסי, אלא הרגע המדויק שבו הפוסט פורסם
- [ ] התגובה האחרונה על הפוסט + לפני כמה זמן היא פורסמה (קריטי — לא פחות חשוב מזמן הפרסום עצמו)

**סינון ומיון**: לפי מילים/קטגוריות ספציפיות שנבחרות מראש, לפי קבוצות ספציפיות, מתוך חשבון הפייסבוק של שי, ממוין מהעדכני ביותר.

**חשוב מאוד**: שי רוצה **לגלוש בעצמו** בפוסטים ובתמונות — לא שהמערכת תחליט בשבילו ותשלח לו רק מה שהיא חושבת שהוא צריך לדעת. אפשר בעתיד גם אימייל/התראה כאופציה נוספת, אבל זו לא המטרה העיקרית.
**מחובר ל**: אותו דשבורד של ג'ארוויס (בקשה 1) — לא כלי נפרד ומבודד.

**אילוץ טכני לבדוק לפני בנייה (לא לפני שמדברים על זה)**: פייסבוק לא מאפשר כברירת מחדל גישה חופשית לקריאת פוסטים מתוך קבוצות דרך API רגיל — נדרש אישור אפליקציה, וגרידה (scraping) מפרה את תנאי השימוש. זה דורש בדיקת היתכנות נפרדת לפני תחילת בנייה בפועל. **(הנחה שלי — צריך לאמת בהמשך, לא עכשיו)**

### הערה על אופן העבודה
שי לא רוצה לחזור ולהסביר/"לתקן" את הבנת הפרויקט בכל שיחה מחדש. המטרה: להבין את הקונספט פעם אחת כמו שצריך, כך שכל עבודה עתידית על ג'ארוויס תזוז מהר בלי לאבד זמן על יישור קו מחדש.

### שאלות פתוחות (לפני תכנון מפורט/בנייה)
1. איפה נמצא הדף/ההדגמה של ג'ארוויס שכבר דיברתם עליו קודם — repo אחר, כלי אחר, או שזה עדיין לא קיים בשום מקום?
2. ג'ארוויס הוא פרויקט נפרד לגמרי, או "עולם" חדש בתוך אתר My Center הקיים (`site/`)?

**Next step**: לענות על 2 השאלות הפתוחות → לפי התשובה, לבנות MVP פשוט לפי דרישת הליבה (פשטות) → לבדוק היתכנות טכנית של חיבור פייסבוק. תזכורת: לפי `RULES.md`/`CURRENT_PRIORITY.md` הנוכחיים עדיין לא בונים קוד — זה שלב תכנון בלבד.

---

## Priority: Dual Phone Work Mode
**Concept**: Synchronize and automate workflow across two phones  
**Value**: High - enables instant switching, zero work loss  
**Effort**: Medium - sync system + UI  
**Status**: In progress  
**Next step**: Define sync requirements  

**Features to build**:
- [ ] App state synchronization
- [ ] One-tap phone switch indicator
- [ ] Backup phone auto-activation
- [ ] Work flow optimization (which apps open first)
- [ ] Notification routing to active phone

---

## High Value Ideas

### Wolt Delivery Helper
**Concept**: Smart tool to help accept better orders and choose better areas  
**Value**: High - directly impacts earnings  
**Effort**: Medium-High - needs data analysis  
**Status**: Planning  
**Why**: Track which orders/areas pay best, make smarter decisions  

**Potential features**:
- [ ] Order quality predictor (size, distance, pay ratio)
- [ ] Area profitability tracker
- [ ] Peak hours analyzer (when is area busiest)
- [ ] Restaurant pickup time database
- [ ] Bad order blocker (auto-reject low-pay orders)
- [ ] Weekly earnings trend

### Daily Earnings Dashboard
**Concept**: Real-time earnings tracking with alerts  
**Value**: High - track progress toward goals  
**Effort**: Medium - data collection + UI  
**Status**: Planning  
**Why**: Know if you're on pace to hit daily/weekly goals  

**Features**:
- [ ] Live ₪ counter during shift
- [ ] Area performance comparison
- [ ] Order count tracker
- [ ] Goal progress bar
- [ ] Weekly trend graph
- [ ] Estimated total at current rate

### Weekly Goal Tracker
**Concept**: Plan and track weekly earnings targets  
**Value**: Medium - helps planning  
**Effort**: Low - simple tracker  
**Status**: Not started  
**Why**: Know exactly what you need each day to hit weekly goal  

**Features**:
- [ ] Set weekly goal (₪X)
- [ ] Auto-calculate daily target
- [ ] Track progress each day
- [ ] Alert if falling behind
- [ ] Weekly summary

### Area Analysis Tool
**Concept**: Compare area profitability by time/day  
**Value**: Medium-High - optimize area choice  
**Effort**: Medium - data collection + analysis  
**Status**: Not started  
**Why**: Identify which areas pay best at different times  

**Analysis needed**:
- [ ] ₪ per hour by area
- [ ] Order density by time
- [ ] Peak earning hours
- [ ] Worst times to work
- [ ] Distance efficiency (₪ per km)

---

## Medium Value Ideas (Build Later)

### Phone Troubleshooting Workflow
**Concept**: Quick diagnostic and fix procedures  
**Value**: Medium - reduces downtime  
**Effort**: Low-Medium - documentation + simple app  

**Features**:
- [ ] Quick diagnosis (is it app? phone? network?)
- [ ] Auto-restart procedures
- [ ] Common fixes guide
- [ ] Emergency backup procedures

### Waze Integration
**Concept**: Better Waze routing for delivery areas  
**Value**: Medium - faster navigation  
**Effort**: Medium - API integration  

**Features**:
- [ ] Save frequent delivery zones as favorites
- [ ] Smart routing suggestions
- [ ] Traffic alert integration

### Restaurant Database
**Concept**: Track pickup times and reliability by restaurant  
**Value**: Low-Medium - helps decision making  
**Effort**: Medium - data collection  

**Data to track**:
- [ ] Average pickup time
- [ ] Reliability (are they ready when promised?)
- [ ] Order type (burgers, sushi, groceries, etc.)
- [ ] Peak hours

---

## Low Effort, High Fun Ideas (Viral Potential)

### Simple Android Tools
- [ ] Quick battery manager app (disable heavy apps instantly)
- [ ] Notification filter (only show important alerts)
- [ ] Phone temp monitor (warn if overheating)
- [ ] Simple shift timer (tap start/stop)
- [ ] Quick notes widget (fast shift notes)

### Useful Utilities
- [ ] GPS accuracy checker
- [ ] Mobile data speed test
- [ ] App battery drain analyzer
- [ ] Storage cleaner
- [ ] Notification blocker

---

## Future: Home Computer/Server Project
**Concept**: Centralized work hub on home computer  
**Value**: High - consolidate all work data  
**Effort**: High - full system design  
**Timeline**: Later (after core apps done)  

**Ideas**:
- [ ] Earnings dashboard accessible from desktop
- [ ] Area analysis with maps
- [ ] Historical data storage
- [ ] Phone sync server
- [ ] Automated backup
- [ ] Report generation

---

## Feature Request Ideas (From Daily Work)

### For Wolt App
- [ ] Better order filtering (by distance, minimum pay)
- [ ] Batch request acceptance (when multiple orders show)
- [ ] Order history analysis
- [ ] Rate prediction (before accepting)
- [ ] Offline map download

### For Waze
- [ ] Delivery zone presets
- [ ] Avoid road markers (bad areas)
- [ ] Quick favorite routes

---

## Evaluation Framework

When deciding which idea to build next:

| Factor | Weight | Score |
|--------|--------|-------|
| Earnings impact | 40% | [1-10] |
| Implementation difficulty | 30% | [1-10] |
| Time to build | 20% | [1-10] |
| User value | 10% | [1-10] |
| **TOTAL** | 100% | [Score] |

---

## How Ideas Move

1. **New idea** → Listed in Ideas.md
2. **Planning** → Define features and effort
3. **Started** → Moved to APPS.md "Active Projects"
4. **Completed** → Moved to FINISHED.md "Completed work"
5. **Archived** → Old ideas not pursued

---

## Next Actions
- [ ] Pick top 3 ideas to prioritize
- [ ] Define "MVP" (minimum viable product) for each
- [ ] Estimate effort in hours
- [ ] Plan which to start first
- [ ] Start with Dual Phone Work Mode (high impact)

---

## 2026-06-10 — אחרי עליית v5 לאוויר (לזכור!)

### שדרוג "שעות עם אורי" / כלים אישיים — קטגוריות ואישי
**מה שדיברנו**: האפליקציה עם הקטגוריות והחלוקה האישית —
- [ ] קטגוריות לשעות/הוצאות (עבודה / אישי / עסק)
- [ ] הפרדה בין אישי לעסקי
- [ ] לעשות את זה פשוט וקל ("easy") — מינימום לחיצות
**סטטוס**: לתכנן בשיחה הבאה — להגדיר בדיוק מה רוצים לפני שבונים
