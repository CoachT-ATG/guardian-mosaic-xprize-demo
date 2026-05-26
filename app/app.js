const sampleUsersEl = document.getElementById("sampleUsers");
const sampleCheckinsEl = document.getElementById("sampleCheckins");
const pilotLeadsEl = document.getElementById("pilotLeads");
const betaSignupsEl = document.getElementById("betaSignups");
const evidenceFilesEl = document.getElementById("evidenceFiles");
const briefOutput = document.getElementById("briefOutput");
const leadOutput = document.getElementById("leadOutput");
const betaOutput = document.getElementById("betaOutput");
const agencyTable = document.getElementById("agencyTable");
const proofJson = document.getElementById("proofJson");
const pillarRail = document.getElementById("pillarRail");
const sensoriumRail = document.getElementById("sensoriumRail");
const statusPill = document.getElementById("statusPill");
const checkinForm = document.getElementById("checkinForm");
const betaForm = document.getElementById("betaForm");
const pilotForm = document.getElementById("pilotForm");

const PILLARS = [
  {
    name: "Flow State Access",
    status: "phase one",
    detail: "Daily check-ins and short prompts to improve focus, recovery, and usable flow under load."
  },
  {
    name: "Foundational Purpose / Transcendence",
    status: "phase one",
    detail: "A purpose lens that keeps the user anchored to meaning, coherence, and resilient habits."
  },
  {
    name: "Cognitive Optimization",
    status: "later",
    detail: "Private future lane for more advanced cognitive support, held outside the public demo."
  },
  {
    name: "Recovery / Aging",
    status: "later",
    detail: "Private future lane for slower calibration signals and deeper longitudinal analysis."
  },
  {
    name: "Dementia Risk / Long Horizon",
    status: "later",
    detail: "Private future lane reserved for separate governed research and clinical partnerships."
  }
];

const SENSORIUM_INTERFACES = [
  {
    name: "Apple Watch",
    signals: "heart rate, HRV, sleep, activity",
    use: "daily resilience routing"
  },
  {
    name: "Fitbit",
    signals: "heart rate, sleep, activity, EDA on supported models",
    use: "trend monitoring"
  },
  {
    name: "Oura Ring",
    signals: "sleep, readiness, HRV, temperature",
    use: "recovery support"
  },
  {
    name: "Garmin",
    signals: "activity, sleep, HRV, stress",
    use: "load-aware prompts"
  },
  {
    name: "WHOOP",
    signals: "strain, recovery, sleep, HRV",
    use: "training/recovery balance"
  },
  {
    name: "HeartMath",
    signals: "coherence, paced breathing, HRV",
    use: "foundational purpose and breath work"
  },
  {
    name: "Muse",
    signals: "EEG-derived meditation feedback",
    use: "mindfulness practice support"
  }
];

const SAMPLE_AGENCY_DATA = [
  {
    agency: "demo-agency-001",
    active_users: "12",
    completed_checkins: "274",
    retention_rate: "0.83",
    qualitative_outcome: "Users report easier shift transitions and better recovery habits."
  },
  {
    agency: "demo-agency-002",
    active_users: "8",
    completed_checkins: "141",
    retention_rate: "0.76",
    qualitative_outcome: "Peer-support lead notes improved engagement with short daily prompts."
  }
];
const storageKey = "guardian_mosaic_demo_state_v1";

function loadState() {
  try {
    return JSON.parse(localStorage.getItem(storageKey)) || { briefs: [], leads: [], beta_signups: [] };
  } catch {
    return { briefs: [], leads: [], beta_signups: [] };
  }
}

function saveState(next) {
  localStorage.setItem(storageKey, JSON.stringify(next));
}

function readState() {
  return loadState();
}

function getFormValues(form) {
  const data = new FormData(form);
  return Object.fromEntries(data.entries());
}

function classify(row) {
  const mood = Number(row.mood);
  const sleep = Number(row.sleep);
  const stress = Number(row.stress);
  if (stress >= 8 || sleep < 5) {
    return {
      status: "recovery_first",
      summary: "The day is demanding; the goal is recovery, not optimization.",
      suggestion: "Take a 10-minute walk, hydrate, and plan a brief peer check-in.",
      note: "Elevated stress and short sleep; recommend recovery-focused support."
    };
  }
  if (mood >= 7 && stress <= 5) {
    return {
      status: "flow_ready",
      summary: "The current state supports a light flow block.",
      suggestion: "Do one focused work block, then stop and reset.",
      note: "Stable state; light challenge is appropriate."
    };
  }
  return {
    status: "steady",
    summary: "A stable day with room for short resilience practices.",
    suggestion: "Use a 4-minute breathing reset and a short transition walk.",
    note: "Moderate load; maintain basic coherence habits."
  };
}

function renderBrief(brief) {
  briefOutput.innerHTML = `
    <div class="brief-status">${brief.status}</div>
    <h4 class="brief-title">Responder Coherence Brief</h4>
    <p><strong>Summary:</strong> ${brief.summary}</p>
    <p><strong>Suggestion:</strong> ${brief.suggestion}</p>
    <p><strong>Dashboard note:</strong> ${brief.note}</p>
  `;
}

function renderLead(lead) {
  leadOutput.innerHTML = `
    <div class="brief-status">pilot lead saved</div>
    <h4 class="brief-title">${lead.agency}</h4>
    <p><strong>Contact:</strong> ${lead.email}</p>
    <p><strong>Seats:</strong> ${lead.seats}</p>
    <p><strong>Goal:</strong> ${lead.goal || "No goal provided."}</p>
  `;
}

function renderBeta(beta) {
  betaOutput.innerHTML = `
    <div class="brief-status">beta signup saved</div>
    <h4 class="brief-title">${beta.name}</h4>
    <p><strong>Email:</strong> ${beta.email}</p>
    <p><strong>Role:</strong> ${beta.role}</p>
    <p><strong>Source:</strong> ${beta.source_channel}</p>
    <p><strong>Pilot interest:</strong> ${beta.pilot_interest ? "yes" : "no"}</p>
    <p><strong>Notes:</strong> ${beta.notes || "No notes provided."}</p>
  `;
}

function renderDashboard(rows) {
  agencyTable.innerHTML = rows.map(row => `
    <tr>
      <td>${row.agency}</td>
      <td>${row.active_users}</td>
      <td>${row.completed_checkins}</td>
      <td>${Number(row.retention_rate).toFixed(2)}</td>
      <td>${row.qualitative_outcome}</td>
    </tr>
  `).join("");
}

function renderPillars() {
  pillarRail.innerHTML = PILLARS.map((pillar, index) => `
    <article class="pillar-card ${index < 2 ? "active" : "locked"}">
      <div class="pillar-index">${index + 1}</div>
      <div>
        <h4>${pillar.name}</h4>
        <span>${pillar.status}</span>
        <p>${pillar.detail}</p>
      </div>
    </article>
  `).join("");
}

function renderSensorium() {
  sensoriumRail.innerHTML = SENSORIUM_INTERFACES.map((sensor) => `
    <article class="sensor-card">
      <h4>${sensor.name}</h4>
      <p><strong>Signals:</strong> ${sensor.signals}</p>
      <p><strong>Use:</strong> ${sensor.use}</p>
    </article>
  `).join("");
}

function exportEvidence() {
  const state = readState();
  const blob = new Blob([JSON.stringify({
    generated_at: new Date().toISOString(),
    briefs: state.briefs,
    leads: state.leads,
    beta_signups: state.beta_signups || [],
    sample_agency_count: SAMPLE_AGENCY_DATA.length,
    demo_mode: "local_first_workspace_mock"
  }, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "guardian-mosaic-evidence-bundle.json";
  a.click();
  URL.revokeObjectURL(url);
}

function copyPilotEmail() {
  const text = [
    "Subject: 30-day resilience pilot for your team",
    "",
    "I’m launching a 30-day Responder Coherence Pilot for public-safety teams.",
    "It is wellness-only: daily check-ins, short recovery prompts, sponsor dashboard, and a final report.",
    "If you’re open to a small pilot, I can send the one-page scope and pricing."
  ].join("\n");
  navigator.clipboard.writeText(text);
  statusPill.textContent = "Pilot email copied";
  setTimeout(() => statusPill.textContent = "Local demo ready", 1500);
}

function exportFunnelPacket() {
  const state = readState();
  const blob = new Blob([JSON.stringify({
    generated_at: new Date().toISOString(),
    beta_signups: state.beta_signups || [],
    lead_count: state.leads.length,
    beta_count: (state.beta_signups || []).length,
    workspace_mode: "local_first_workspace_mock"
  }, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "guardian-mosaic-funnel-packet.json";
  a.click();
  URL.revokeObjectURL(url);
}

async function main() {
  renderPillars();
  renderSensorium();
  renderDashboard(SAMPLE_AGENCY_DATA);

  const state = readState();
  sampleUsersEl.textContent = SAMPLE_AGENCY_DATA.reduce((sum, row) => sum + Number(row.active_users), 0);
  sampleCheckinsEl.textContent = SAMPLE_AGENCY_DATA.reduce((sum, row) => sum + Number(row.completed_checkins), 0);
  pilotLeadsEl.textContent = state.leads.length;
  betaSignupsEl.textContent = (state.beta_signups || []).length;
  evidenceFilesEl.textContent = 3 + state.briefs.length + state.leads.length + (state.beta_signups || []).length;

  const latestLead = state.leads[state.leads.length - 1];
  if (latestLead) renderLead(latestLead);
  if (state.briefs[state.briefs.length - 1]) renderBrief(state.briefs[state.briefs.length - 1]);
  const latestBeta = (state.beta_signups || [])[state.beta_signups.length - 1];
  if (latestBeta) renderBeta(latestBeta);

  proofJson.textContent = JSON.stringify({
    workspace: true,
    appsheet_config: "../appsheet/appsheet-config.json",
    gemini_payload: "../gemini/api-call-example.json",
    disclosure: "../docs/preexisting-work-disclosure.md",
    grant_matrix: "../docs/grant-requirements-matrix.md",
    beta_pipeline: "../docs/beta-to-pilot-pipeline.md",
    sensorium_interfaces: "../docs/sensorium-interfaces.md",
    revenue_gate: "blocked_until_paid_receipt"
  }, null, 2);

  checkinForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const values = getFormValues(checkinForm);
    const brief = { ...values, ...classify(values), created_at: new Date().toISOString() };
    const next = readState();
    next.briefs.push(brief);
    saveState(next);
    renderBrief(brief);
    sampleUsersEl.textContent = SAMPLE_AGENCY_DATA.reduce((sum, row) => sum + Number(row.active_users), 0);
    sampleCheckinsEl.textContent = SAMPLE_AGENCY_DATA.reduce((sum, row) => sum + Number(row.completed_checkins), 0) + next.briefs.length;
    betaSignupsEl.textContent = (next.beta_signups || []).length;
    evidenceFilesEl.textContent = 3 + next.briefs.length + next.leads.length + (next.beta_signups || []).length;
  });

  betaForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const values = getFormValues(betaForm);
    const beta = {
      ...values,
      beta_consent: Boolean(values.beta_consent),
      pilot_interest: Boolean(values.pilot_interest),
      created_at: new Date().toISOString()
    };
    const next = readState();
    next.beta_signups = next.beta_signups || [];
    next.beta_signups.push(beta);
    saveState(next);
    renderBeta(beta);
    betaSignupsEl.textContent = next.beta_signups.length;
    evidenceFilesEl.textContent = 3 + next.briefs.length + next.leads.length + next.beta_signups.length;
    statusPill.textContent = "Beta signup saved";
    setTimeout(() => statusPill.textContent = "Local demo ready", 1500);
  });

  pilotForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const values = getFormValues(pilotForm);
    const lead = { ...values, created_at: new Date().toISOString() };
    const next = readState();
    next.leads.push(lead);
    saveState(next);
    renderLead(lead);
    pilotLeadsEl.textContent = next.leads.length;
    betaSignupsEl.textContent = (next.beta_signups || []).length;
    evidenceFilesEl.textContent = 3 + next.briefs.length + next.leads.length + (next.beta_signups || []).length;
    statusPill.textContent = "Pilot lead saved";
    setTimeout(() => statusPill.textContent = "Local demo ready", 1500);
  });

  document.getElementById("exportBtn").addEventListener("click", exportEvidence);
  document.getElementById("exportFunnelBtn").addEventListener("click", exportFunnelPacket);
  document.getElementById("copyEmailBtn").addEventListener("click", copyPilotEmail);
}

main().catch((err) => {
  console.error(err);
  statusPill.textContent = "Demo failed to load";
  statusPill.style.background = "rgba(255,107,107,.12)";
});
