# Kali Red Dark for Android

A no-root Android personalization project inspired by the **Kali Red Dark** color palette. The goal is to bring its dark surfaces, bright red accents, and readable contrast to compatible Android launchers and customization apps.

> **Device target:** Cubot KINGKONG ACE 2 running Android 14. Compatibility depends on the launcher and customization tools installed.

## Color palette

| Role | Color | Hex |
|---|---|---|
| Accent / primary red | <span style="color:#ec0101">Red</span> | `#ec0101` |
| Main background | Near-black | `#0b0b0d` |
| Secondary background | Deep black | `#09090b` |
| Main text | Soft white | `#e8e8e8` |
| Muted text | Gray | `#777777` |
| Strings / positive accent | Green | `#7ee787` |
| Variables / links | Blue | `#79c0ff` |
| Functions | Orange | `#ff9f43` |
| Classes / types | Yellow | `#ffd166` |
| Built-in support | Cyan | `#67e8f9` |
| Constants | Purple | `#c084fc` |

The source palette comes from the Kali Red Dark theme for Visual Studio Code. This repository is a separate Android-focused project and does not modify that original project.

## Included documentation

- Color palette in `theme/colors.json`
- Android 14 installation guide
- Step-by-step [Lawnchair setup guide](docs/LAWNCHAIR-SETUP.md)
- Roadmap for the wallpaper, icon options, and preview mockups

Wallpaper artwork, a real icon pack, and preview images are still pending; placeholder folders are documented but do not contain installable assets yet.

## Android limitations

Without root or a compatible system theme engine, an ordinary theme cannot recolor every Android system surface. Quick Settings, notifications, Settings, and status-bar elements may keep the colors supplied by the device manufacturer. This project focuses on supported wallpaper, launcher, icon, widget, and color settings.

## Getting started

See [Installation guide](docs/INSTALL.md) and [project roadmap](docs/ROADMAP.md).

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE).
