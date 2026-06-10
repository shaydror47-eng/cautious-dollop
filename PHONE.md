# Phone

## Purpose
Dual Android phone management for Wolt delivery work. Both phones must be ready at all times - if one fails, switch instantly to the backup.

## System Requirements
Both phones must have:
- [ ] Wolt app (installed, logged in, notifications on)
- [ ] Waze (installed, GPS enabled, voice on)
- [ ] Spotify (optional, for delivery breaks)
- [ ] Location services enabled
- [ ] Mobile data/WiFi active
- [ ] Battery 80%+ before shift
- [ ] Storage: at least 2GB free
- [ ] All work notifications enabled

## Phone 1 (Primary)
**Status**: In use  
**Model**: Samsung Galaxy S23 (SM-S911B)  
**Android version**: 16  
**Last updated**: 2026-06-10

### Apps Status
- Wolt: ✓ Logged in
- Waze: ✓ Updated
- Spotify: ✓ Working
- Notifications: ✓ All enabled

### Known Issues
- Battery health at 88% of original capacity (in use since 2023-04) — likely cause of fast battery drain. Not urgent.

### Performance (checked 2026-06-10 via ADB)
- Battery: 100% charged, health OK, capacity 88% (BSOH 98)
- Storage: 135GB free of 223GB
- Heat: Normal (~34°C)
- GPS: Working

## Phone 2 (Backup)
**Status**: Backup ready  
**Model**: Samsung Galaxy S24 Ultra (SM-S908E)  
**Android version**: 15  
**Last updated**: 2026-06-10

### Apps Status
- Wolt: ✓ Logged in
- Waze: ✓ Updated
- Spotify: ✓ Working
- Notifications: ✓ All enabled

### Known Issues
- None currently reported

### Performance (checked 2026-06-10 via ADB)
- Battery: 100% charged, AC powered, health good
- Battery capacity: 4540000 mAh (Full capacity)
- Battery health (ASOC): 88%
- Temperature: 336°C (normal operating range)
- Voltage: 4290mV
- Storage: 205GB used of 462GB (257GB free, 45% usage)
- Heat: Normal (~33-36°C)
- GPS: Working
- Super Fast Charging: Enabled
- Battery Lifespan: First used 2024-07-07

## Sync & Handoff Procedure

### Before Shift (Do Both)
1. Charge both phones to 80%+
2. Verify Wolt logged in on both
3. Test Waze navigation on both
4. Check mobile data working
5. Verify notifications enabled

### Emergency Switch
If Phone 1 fails during shift:
1. Stop accepting new orders on Phone 1
2. Switch immediately to Phone 2
3. Open Wolt on Phone 2 - ready to accept
4. Log issue in BUGS.md with time and error
5. Continue working, troubleshoot later

## Common Issues & Quick Fixes

| Issue | Fix |
|-------|-----|
| Phone overheats | Stop using, let cool 5 min, switch to backup |
| GPS stops working | Restart location services, restart Waze |
| Wolt app crashes | Force stop > Restart app |
| No mobile signal | Check airplane mode OFF, restart phone |
| Battery draining fast | Disable background apps, lower screen brightness |
| Storage full | Clear cache: Settings > Apps > Wolt > Storage > Clear Cache |

## Maintenance Schedule
- **Daily before shift**: Quick status check
- **Weekly**: Full restart of both phones, cache clear
- **Monthly**: Check for OS updates, app updates

## Next Actions
- [x] Fill in exact Phone 1 model and Android version (Galaxy S23, Android 16)
- [x] Fill in exact Phone 2 model and Android version (Galaxy S24 Ultra, Android 15)
- [ ] Confirm Phone 2 is the one that is slow to boot
- [ ] Test both phones today
- [ ] Run through sync procedure
- [ ] Log any issues found
