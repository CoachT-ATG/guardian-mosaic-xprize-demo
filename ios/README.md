# Guardian Mosaic iOS Scaffold

This folder contains the native SwiftUI shell for the beta.

## Files

- `GuardianMosaic/GuardianMosaicApp.swift`
- `GuardianMosaic/RootView.swift`
- `GuardianMosaic/Models.swift`
- `GuardianMosaic/LocalBetaStore.swift`
- `GuardianMosaic/Info.plist`

## How To Use

1. Open Xcode.
2. Create a new iOS App project named `Guardian Mosaic`.
3. Replace the generated app entry point with `GuardianMosaicApp.swift`.
4. Add the other Swift files to the target.
5. Set the bundle identifier to your Apple Developer bundle ID.
6. Copy the metadata from `docs/apple-release-assets.md` into App Store Connect.
7. Archive and upload the first beta build to TestFlight.

## Local Behavior

- daily check-ins are stored locally
- beta signups are stored locally
- pilot leads are stored locally
- the sensorium layer is trend-only
- no network calls are required for the scaffold to render

