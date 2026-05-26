# MO/Hermes /goal: Guardian Mosaic iPhone Release

## Mission

Ship the first iPhone-accessible Guardian Mosaic beta through App Store Connect and TestFlight with the smallest reliable sequence of work.

## Canonical App Identity

- App name: Guardian Mosaic
- Platform: iOS
- Bundle ID: `com.abovethegenes.guardianmosaic`
- Local scaffold: `ios/GuardianMosaic/`
- Metadata: `docs/apple-release-assets.md`
- Launch kit: `docs/apple-launch-kit.md`
- Beta checklist: `docs/ios-beta-launch-checklist.md`

## Current Local State

- SwiftUI source exists.
- `Info.plist` already declares `com.abovethegenes.guardianmosaic`.
- No `.xcodeproj` is present in this repo yet.

## MO/Hermes Directives

1. Preserve the wellness-only boundary.
2. Keep all Apple-facing copy aligned to `docs/apple-release-assets.md`.
3. Use `ABSTAIN` for medical, clinical, crisis, medication, diagnosis, or fitness-for-duty claims.
4. Route beta onboarding toward observe-and-dialogue wellness support only.
5. Do not create duplicate bundle IDs, duplicate app records, or duplicate TestFlight groups.
6. Treat App Store Connect Account Holder agreement acceptance as a blocking manual gate.

## Apple Execution Sequence

1. App Store Connect
   - Open Apps -> `+` -> New App.
   - Select iOS.
   - Name: `Guardian Mosaic`.
   - Bundle ID: `com.abovethegenes.guardianmosaic`.
   - If prompted, Account Holder accepts the latest Apple agreement first.

2. Xcode
   - Create a new iOS App project if one is not already present.
   - Product Name: `Guardian Mosaic`.
   - Interface: SwiftUI.
   - Language: Swift.
   - Team: Above the Genes Apple developer account.
   - Bundle Identifier: `com.abovethegenes.guardianmosaic`.
   - Copy files from `ios/GuardianMosaic/` into the app target.
   - Run once on Terry's iPhone to verify signing.

3. Archive
   - Xcode -> Product -> Archive.
   - Distribute App -> App Store Connect -> Upload.
   - Confirm version `0.1.0`, build `1`.

4. TestFlight
   - Create internal tester group.
   - Add Terry first.
   - After processing, install through TestFlight.
   - Create external group only after Apple beta review is ready.

5. Funnel
   - LinkedIn copy: `docs/linkedin-launch-copy.md`.
   - Beta-to-pilot flow: `docs/beta-to-pilot-pipeline.md`.
   - App intake: `app/`.
   - Google/Workspace evidence: `scripts/google_ops_runner.py`.
   - XPRIZE boundary: `scripts/doc_strange_adversarial_loop.py`.

## Acceptance Criteria

- App record exists in App Store Connect.
- Local Xcode app signs under the correct Team.
- First build uploads successfully.
- Terry is an internal TestFlight tester.
- External TestFlight is staged for review.
- No medical-device or clinical claims appear in Apple metadata.
