import Foundation
import Combine
import SwiftUI

final class LocalBetaStore: ObservableObject {
    @Published var briefs: [DailyCheckIn] = []
    @Published var betaSignups: [BetaSignup] = []
    @Published var leads: [PilotLead] = []

    private let defaults = UserDefaults.standard
    private let prefix = "guardian_mosaic_ios_"

    init() {
        briefs = load([DailyCheckIn].self, key: "briefs") ?? []
        betaSignups = load([BetaSignup].self, key: "beta_signups") ?? []
        leads = load([PilotLead].self, key: "leads") ?? []
    }

    func saveBrief(_ brief: DailyCheckIn) {
        briefs.append(brief)
        persist(briefs, key: "briefs")
    }

    func saveBeta(_ beta: BetaSignup) {
        betaSignups.append(beta)
        persist(betaSignups, key: "beta_signups")
    }

    func saveLead(_ lead: PilotLead) {
        leads.append(lead)
        persist(leads, key: "leads")
    }

    private func persist<T: Encodable>(_ value: T, key: String) {
        guard let data = try? JSONEncoder().encode(value) else { return }
        defaults.set(data, forKey: prefix + key)
    }

    private func load<T: Decodable>(_ type: T.Type, key: String) -> T? {
        guard let data = defaults.data(forKey: prefix + key) else { return nil }
        return try? JSONDecoder().decode(type, from: data)
    }
}
