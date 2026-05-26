import SwiftUI

struct RootView: View {
    @EnvironmentObject private var store: LocalBetaStore

    var body: some View {
        TabView {
            DashboardView()
                .tabItem { Label("Today", systemImage: "heart.text.square") }
            BetaView()
                .tabItem { Label("Beta", systemImage: "paperplane") }
            PilotView()
                .tabItem { Label("Pilot", systemImage: "building.2") }
            SensoriumView()
                .tabItem { Label("Sensors", systemImage: "waveform.path.ecg") }
        }
        .tint(.mint)
    }
}

struct DashboardView: View {
    @EnvironmentObject private var store: LocalBetaStore
    @State private var role = "law_enforcement"
    @State private var mood = 6
    @State private var sleepHours = 5.5
    @State private var stress = 7
    @State private var notes = ""

    var brief: CoherenceBrief {
        classify(DailyCheckIn(role: role, mood: mood, sleepHours: sleepHours, stress: stress, notes: notes))
    }

    var body: some View {
        NavigationStack {
            Form {
                Section("Daily Check-In") {
                    Picker("Role", selection: $role) {
                        Text("Law enforcement").tag("law_enforcement")
                        Text("Fire / EMS").tag("fire_ems")
                        Text("Dispatch").tag("dispatch")
                        Text("Academy").tag("academy")
                    }
                    Stepper("Mood: \(mood)", value: $mood, in: 1...10)
                    Stepper("Sleep: \(sleepHours, specifier: "%.1f") h", value: $sleepHours, in: 0...12, step: 0.5)
                    Stepper("Stress: \(stress)", value: $stress, in: 1...10)
                    TextField("Notes", text: $notes, axis: .vertical)
                    Button("Save Check-In") {
                        store.saveBrief(DailyCheckIn(role: role, mood: mood, sleepHours: sleepHours, stress: stress, notes: notes))
                    }
                }
                Section("Responder Coherence Brief") {
                    Text(brief.status).font(.headline)
                    Text(brief.summary)
                    Text(brief.suggestion)
                    Text(brief.note).foregroundStyle(.secondary)
                }
            }
            .navigationTitle("Guardian Mosaic")
        }
    }
}

struct BetaView: View {
    @EnvironmentObject private var store: LocalBetaStore
    @State private var name = ""
    @State private var email = ""
    @State private var role = "law_enforcement"
    @State private var organizationType = "individual"
    @State private var sourceChannel = "linkedin"
    @State private var wantsPilot = true
    @State private var notes = ""

    var body: some View {
        NavigationStack {
            Form {
                Section("Beta Signup") {
                    TextField("Name", text: $name)
                    TextField("Email", text: $email)
                    Picker("Role", selection: $role) {
                        Text("Law enforcement").tag("law_enforcement")
                        Text("Fire / EMS").tag("fire_ems")
                        Text("Military").tag("military")
                        Text("Veteran").tag("veteran")
                        Text("First responder").tag("first_responder")
                    }
                    Picker("Organization", selection: $organizationType) {
                        Text("Individual").tag("individual")
                        Text("Agency").tag("agency")
                        Text("Union / association").tag("union")
                        Text("Nonprofit").tag("nonprofit")
                    }
                    Picker("Source", selection: $sourceChannel) {
                        Text("LinkedIn").tag("linkedin")
                        Text("Referral").tag("referral")
                        Text("Email").tag("email")
                    }
                    Toggle("Open to pilot after beta", isOn: $wantsPilot)
                    TextField("Notes", text: $notes, axis: .vertical)
                    Button("Save Beta Signup") {
                        store.saveBeta(BetaSignup(name: name, email: email, role: role, organizationType: organizationType, sourceChannel: sourceChannel, wantsPilot: wantsPilot, notes: notes))
                    }
                }
                Section("Saved Beta Count") {
                    Text("\(store.betaSignups.count)")
                }
            }
            .navigationTitle("Beta")
        }
    }
}

struct PilotView: View {
    @EnvironmentObject private var store: LocalBetaStore
    @State private var agency = ""
    @State private var email = ""
    @State private var seats = 10
    @State private var goal = ""

    var body: some View {
        NavigationStack {
            Form {
                Section("Agency Pilot") {
                    TextField("Agency", text: $agency)
                    TextField("Email", text: $email)
                    Stepper("Seats: \(seats)", value: $seats, in: 5...100, step: 5)
                    TextField("Goal", text: $goal, axis: .vertical)
                    Button("Save Pilot Lead") {
                        store.saveLead(PilotLead(agency: agency, email: email, seats: seats, goal: goal))
                    }
                }
                Section("Saved Pilot Leads") {
                    Text("\(store.leads.count)")
                }
            }
            .navigationTitle("Pilot")
        }
    }
}

struct SensoriumView: View {
    private let sensors: [(String, String, String)] = [
        ("Apple Watch", "heart rate, HRV, sleep, activity", "daily resilience routing"),
        ("Fitbit", "heart rate, sleep, activity, EDA on supported models", "trend monitoring"),
        ("Oura Ring", "sleep, readiness, HRV, temperature", "recovery support"),
        ("Garmin", "activity, sleep, HRV, stress", "load-aware prompts"),
        ("WHOOP", "strain, recovery, sleep, HRV", "training/recovery balance"),
        ("HeartMath", "coherence, paced breathing, HRV", "breath work"),
        ("Muse", "EEG-derived meditation feedback", "mindfulness practice support")
    ]

    var body: some View {
        NavigationStack {
            List {
                Section("Trend-only sensors") {
                    ForEach(sensors, id: \.0) { sensor in
                        VStack(alignment: .leading, spacing: 4) {
                            Text(sensor.0).font(.headline)
                            Text(sensor.1)
                            Text(sensor.2).foregroundStyle(.secondary)
                        }
                    }
                }
            }
            .navigationTitle("Sensorium")
        }
    }
}
