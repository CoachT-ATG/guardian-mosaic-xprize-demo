import Foundation

struct DailyCheckIn: Identifiable, Codable {
    var id = UUID()
    var role: String
    var mood: Int
    var sleepHours: Double
    var stress: Int
    var notes: String
    var createdAt = Date()
}

struct BetaSignup: Identifiable, Codable {
    var id = UUID()
    var name: String
    var email: String
    var role: String
    var organizationType: String
    var sourceChannel: String
    var wantsPilot: Bool
    var notes: String
    var createdAt = Date()
}

struct PilotLead: Identifiable, Codable {
    var id = UUID()
    var agency: String
    var email: String
    var seats: Int
    var goal: String
    var createdAt = Date()
}

struct CoherenceBrief: Codable {
    var status: String
    var summary: String
    var suggestion: String
    var note: String
}

enum ResonanceState: String, CaseIterable, Identifiable {
    case recoveryFirst = "Recovery First"
    case steady = "Steady"
    case flowReady = "Flow Ready"

    var id: String { rawValue }
}

func classify(_ checkIn: DailyCheckIn) -> CoherenceBrief {
    if checkIn.stress >= 8 || checkIn.sleepHours < 5 {
        return CoherenceBrief(
            status: ResonanceState.recoveryFirst.rawValue,
            summary: "The day is demanding; the goal is recovery, not optimization.",
            suggestion: "Take a 10-minute walk, hydrate, and plan a brief peer check-in.",
            note: "Elevated stress and short sleep; recommend recovery-focused support."
        )
    }
    if checkIn.mood >= 7 && checkIn.stress <= 5 {
        return CoherenceBrief(
            status: ResonanceState.flowReady.rawValue,
            summary: "The current state supports a light flow block.",
            suggestion: "Do one focused work block, then stop and reset.",
            note: "Stable state; light challenge is appropriate."
        )
    }
    return CoherenceBrief(
        status: ResonanceState.steady.rawValue,
        summary: "A stable day with room for short resilience practices.",
        suggestion: "Use a 4-minute breathing reset and a short transition walk.",
        note: "Moderate load; maintain basic coherence habits."
    )
}
