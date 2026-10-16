# Installation guide

This repository is currently a **manual personalization kit**, not a flashable ROM, installable theme APK, or system-wide Android theme. No root access is required.

## 1. Get and set the wallpaper

The vector master is included at [`assets/wallpapers/kali-red-dark-wallpaper-portrait.svg`](../assets/wallpapers/kali-red-dark-wallpaper-portrait.svg). A PNG export is produced by GitHub Actions.

1. Open the repository's **Actions** tab.
2. Select **Build wallpaper PNG** and open a successful run.
3. Download the `kali-red-dark-wallpaper-1080x2400` artifact.
4. Extract the ZIP so the PNG is available in your Downloads folder.
5. Open the PNG in Gallery or Photos.
6. Choose **Set as wallpaper** and select the home screen, lock screen, or both.

Workflow artifacts are temporary and retained for 30 days. If no successful run is available yet, run **Build wallpaper PNG** manually from the Actions tab. The SVG source can also be converted to PNG on a computer with a compatible SVG renderer.

## 2. Enable dark mode

Open the phone's **Settings → Display** (menu names vary by manufacturer) and enable dark theme if available. Wallpaper controls may be under **Wallpaper**, **Home screen**, or **Display**; some Cubot firmware versions may not show a separate **Wallpaper & style** page.

Android system color palettes are separate from Lawnchair's accent setting. Some firmware does not expose custom hexadecimal colors.

## 3. Configure Lawnchair

Follow the [Lawnchair setup guide](LAWNCHAIR-SETUP.md) for a suggested grid, icon settings, accent options, and widgets. Use only options visible in the installed version. Settings are reversible; do not clear app data or reset the launcher just to test a color.

The original theme red is `#EC0101`. A brighter optional mobile accent is `#FF0000`, if custom hex input is supported. Entering a color does not guarantee that every launcher control changes.

## 4. Icons and widgets

The project does not yet include its own icon pack. Icon replacement and widget colors depend on the launcher and apps installed. Lawnchair can customize the home screen but cannot force every third-party widget or system app to use the same colors.

Only install icon packs from trusted sources and verify the package supports your launcher. Avoid apps that request Accessibility, device administrator, or other powerful permissions without a clear need.

## 5. Limitations

- No installable APK or theme package is currently available.
- The wallpaper has not yet been tested on the target Cubot device.
- This project does not flash firmware or modify the Android system partition.
- Quick Settings, notifications, Settings, and status-bar colors may remain controlled by the device manufacturer.
- The exact menu names depend on Lawnchair version and device firmware.

## Related documentation

- [Lawnchair setup guide](LAWNCHAIR-SETUP.md)
- [Asset specifications](ASSET-SPEC.md)
- [Roadmap](ROADMAP.md)
