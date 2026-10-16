# Lawnchair setup guide

This guide documents a manual starting point for the **Kali Red Dark** look on a Cubot KINGKONG ACE 2 running Android 14. Menu names and available options vary by Lawnchair version.

## Target appearance

- Main background: near-black `#0B0B0D`
- Secondary surface: `#09090B`
- Original theme red: `#EC0101`
- Brighter optional red: `#FF0000`
- Main text: `#E8E8E8`
- Muted text: `#777777`

The `#FF0000` value is an optional brighter mobile accent; it does not replace the original palette token. Use it only if a custom hex field is available.

## 1. Open Lawnchair settings

1. Go to the home screen.
2. Press and hold an empty area.
3. Open **Home settings** or the equivalent option.

## 2. Set a clean layout

Treat these as starting values, not requirements. Adjust them to suit the screen.

| Setting | Suggested starting point |
|---|---|
| Home-screen grid | 5 columns × 7 rows, if supported |
| Icon size | Around 90–100%, if supported |
| Home-screen labels | Keep enabled for readability |
| Dock | 4–5 frequently used apps |
| Folders | Group apps by purpose |
| Widgets | One clock/date widget near the top with open space around it |

The grid and dock can have separate settings. Look for **Home screen**, **Layout**, **Icons**, and **Dock** if the menu wording differs.

## 3. Choose a red accent

1. Open Lawnchair's settings and look for **General**, **Appearance**, or **Accent color**.
2. Choose **Custom** only if your installed version offers it.
3. Enter `#FF0000` for a brighter red, or `#EC0101` to match the original theme palette.
4. Apply or save the selection if the interface provides that action.

**Important:** accepting a hex value does not mean every part of the launcher will change. The accent may affect only selected controls. It may not recolor app icons, third-party widgets, Android Settings, Quick Settings, notifications, or the status bar.

If the screen looks unchanged, check whether the setting affects only selected UI elements. Do not reset Lawnchair or clear its data just to test a color.

## 4. Configure icons

1. Look for **Icon style**, **Icon pack**, or **Themed icons** in Lawnchair settings.
2. Select an installed compatible icon pack, if you have one.
3. If themed icons are offered, enable them and inspect the result.
4. If icons become unexpectedly tinted, disable **Tint with accent color** if that option exists.
5. To customize one app, long-press its home-screen icon and look for **Customize** or a pencil icon, if available.

The repository does not currently include its own icon pack. Themed icons are not guaranteed to turn pure red; Android or the launcher may use a system-derived palette.

Do not install an unknown APK just because it claims to be a theme. Prefer trusted app stores and official project releases.

## 5. Add widgets

1. Long-press an empty area and choose **Widgets**.
2. Add a clock/date widget if desired.
3. Keep the first screen simple: clock/date near the top, essential apps in the middle, dock at the bottom.
4. Prefer soft-white or gray widget text with red used sparingly.

Each widget controls its own appearance. Lawnchair cannot force every third-party widget to use the same colors.

## 6. Android system appearance

Open the phone's Display or Wallpaper settings and enable dark mode if available. Some manufacturers do not expose a custom system color palette or a hexadecimal input field. If you cannot find **Wallpaper & style**, use the device's available Display and Wallpaper menus instead.

Lawnchair changes the home screen, not the entire Android interface. System-wide recoloring depends on firmware support and cannot be guaranteed without a compatible theme engine.

## Troubleshooting

- **Hex color accepted but nothing looks different:** the accent may apply only to specific launcher controls.
- **Icons keep their original colors:** an accent color does not replace icons; a compatible icon pack or per-icon customization is needed.
- **No custom color option:** choose the closest available preset, or keep the dark wallpaper and layout.
- **A setting is missing:** your Lawnchair version may organize it differently. Share a screenshot of the settings page to identify the right route.
- **Widgets do not match:** adjust each widget through its own app settings.

## Current project status

This is a manual setup guide. The repository does not yet include an installable theme APK, a finished wallpaper, or its own icon pack. See the [asset specification](ASSET-SPEC.md) for what remains.
