# Roadmap

Status labels describe repository deliverables, not features already installed on a phone.

## v0.1.0 — Documentation foundation

- [x] Create repository structure
- [x] Document the source color palette
- [x] Add machine-readable color tokens
- [x] Add Android installation notes
- [x] Add Lawnchair manual setup guide
- [x] Document target-device limitations and missing assets
- [x] Define requirements for future assets
- [x] Add a Python validator for palette metadata and color values
- [x] Add a GitHub Actions workflow for pushes, pull requests, and manual runs
- [x] Add an original portrait SVG wallpaper source
- [x] Add a GitHub Actions workflow to render a 1080 × 2400 PNG artifact
- [ ] Confirm the wallpaper workflow succeeds on GitHub
- [ ] Test the wallpaper on the target phone
- [ ] Create home-screen preview mockups
- [ ] Test a specific compatible icon pack on the target device

## v0.2.0 — Visual assets

- [x] Add an original geometric wallpaper master
- [x] Provide a workflow for a phone-ready PNG export
- [ ] Add before/after preview images with no fake device screenshots
- [ ] Record final asset validation and phone test results

## v0.3.0 — Icon options

- [ ] Select an icon-pack format supported by the target launcher
- [ ] Create original icons for a clearly listed set of common apps
- [ ] Document missing-app fallback behavior
- [ ] Test icon labels, adaptive masks, and monochrome behavior on the target device

## Later

- [ ] Record verified installation steps with the exact Lawnchair version and device firmware
- [ ] Consider a launcher-specific theme package only if its supported format is confirmed
- [ ] Add release notes and versioned downloadable assets when the project has real deliverables

## Release criteria

Do not label the project as a complete theme or publish an APK until an installable artifact exists and its installation has been tested. A color JSON file, wallpaper, and manual setup instructions do not constitute an installable theme.
