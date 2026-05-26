import SwiftUI

@main
struct GuardianMosaicApp: App {
    @StateObject private var store = LocalBetaStore()

    var body: some Scene {
        WindowGroup {
            RootView()
                .environmentObject(store)
        }
    }
}
