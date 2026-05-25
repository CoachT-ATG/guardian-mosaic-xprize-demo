export function writeProvenanceLog(entry) {
  const record = {
    timestamp: new Date().toISOString(),
    ...entry,
  };
  return JSON.stringify(record);
}

