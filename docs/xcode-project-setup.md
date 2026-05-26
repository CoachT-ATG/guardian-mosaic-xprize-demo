# Xcode Project Setup

Use this exact sequence to turn the SwiftUI scaffold into a buildable iOS app for TestFlight.

## 1. Create The Project

In Xcode:

1. File -> New -> Project.
2. Choose `iOS` -> `App`.
3. Product Name: `Guardian Mosaic`.
4. Interface: `SwiftUI`.
5. Language: `Swift`.
6. Lifecycle: `SwiftUI App`.
7. Organization Identifier: `com.abovethegenes`.
8. Bundle Identifier: `com.abovethegenes.guardianmosaic`.
9. Team: your Apple Developer team.
10. User Interface: default SwiftUI.

## 2. Add The Scaffold Files

Add these files to the app target:

- `ios/GuardianMosaic/GuardianMosaicApp.swift`
- `ios/GuardianMosaic/RootView.swift`
- `ios/GuardianMosaic/Models.swift`
- `ios/GuardianMosaic/LocalBetaStore.swift`

Use the `Info.plist` in `ios/GuardianMosaic/Info.plist` if you want to override the defaults.

## 3. Signing Settings

In the target settings:

- Team: your Apple Developer team
- Bundle Identifier: `com.abovethegenes.guardianmosaic`
- Automatically manage signing: enabled
- Signing certificate: Apple Development for local runs
- Signing certificate for archive: Apple Distribution

## 4. Deployment Target

Use the default deployment target offered by your installed Xcode unless you intentionally want to support an older iPhone baseline.

Keep the minimum version consistent across:

- the Xcode target
- the App Store Connect build
- the beta release notes

## 5. App Capabilities

Keep capabilities minimal for the first beta:

- no HealthKit
- no background processing unless later needed
- no push notifications unless required
- no iCloud entitlement unless required

## 6. App Store Connect Fields

Use the drafts in `docs/apple-release-assets.md`.

Required fields:

- app name
- subtitle
- bundle ID
- category
- support URL
- privacy policy URL
- marketing URL
- description
- keywords

## 7. TestFlight Setup

1. Upload the first build from Xcode.
2. Wait for App Store Connect processing to complete.
3. In the app record, open the `TestFlight` tab.
4. Add internal testers first.
5. Add external testers after beta review approval.
6. Add the beta feedback email from your account.

## 8. Beta Review Notes

Use this language:

- wellness-only responder support
- daily check-ins
- beta signup
- pilot lead capture
- aggregate reporting
- no diagnosis
- no treatment
- no PHI
- no fitness-for-duty claims

## 9. First Upload Sanity Check

Before archiving:

- verify bundle ID matches App Store Connect
- verify version and build number are unique
- verify the app launches on your device
- verify the beta signup and pilot forms work
- verify the sensorium tab renders

## 10. What To Do After Upload

- create the TestFlight internal group
- add yourself as a tester
- install via TestFlight
- capture screenshots of the test run
- record the build version and upload timestamp in the evidence log

