#!/usr/bin/env python3
import json, os, pathlib, sys

REQUIRED = {"codestra","moneybee","beyvra","breero","larim-a","transportation","booked4seasons","social","klyrow","telnexa","kyqra","restaurant","provisioning"}
EXPECTED_HOSTS = {
    "appolon1908-hue/Codestra-Loki": "loki.codestra.media",
    "appolon1908-hue/Codestra-Prometheus": "prom.codestra.media",
    "appolon1908-hue/Codestra-Tempo": "temp.codestra.media",
    "appolon1908-hue/Codestra-Telemetry": "otel.codestra.media",
    "appolon1908-hue/Codestra-Alloy": "allo.codestra.media",
    "appolon1908-hue/Codestra-Node-Exporter": "node.codestra.media",
    "appolon1908-hue/Codestra-cAdvisor": "cadv.codestra.media",
    "appolon1908-hue/Codestra-Redis-Exporter": "rdex.codestra.media",
    "appolon1908-hue/Codestra-Blackbox-Exporter": "blac.codestra.media",
    "appolon1908-hue/Superset": "supe.codestra.media",
    "appolon1908-hue/Codestra-OpenBao": "bao.codestra.media"
}

def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)

p = pathlib.Path("codestra/enterprise-profile.v1.json")
if not p.exists(): fail("missing enterprise profile")
data = json.loads(p.read_text())
repo = os.environ.get("GITHUB_REPOSITORY", "appolon1908-hue/Codestra-Loki")
expected = EXPECTED_HOSTS.get(repo)
if expected and data.get("canonicalHostname") != expected: fail(f"canonical hostname must be {expected}")
if data.get("schemaVersion") != "1.0": fail("schemaVersion must be 1.0")
if data.get("status") != "SOURCE_PREPARED_NOT_DEPLOYED": fail("profile must remain source-prepared/not-deployed")
businesses = set(data.get("businessScope", []))
missing = REQUIRED - businesses
if missing: fail("missing Codestra businesses: " + ", ".join(sorted(missing)))
if len(data.get("businessScope", [])) != len(businesses): fail("duplicate business IDs")
if not data.get("features"): fail("features must not be empty")
if data.get("exposure") == "public_native": fail("native observability/security service exposure may not be public")

def walk(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            key = k.lower().replace("_", "")
            if any(x in key for x in ("password","apikey","clientsecret","privatekey","roottoken")) and isinstance(v, str) and v.strip():
                fail(f"credential-like value committed at {path + k}")
            walk(v, path + k + ".")
    elif isinstance(obj, list):
        for i, v in enumerate(obj): walk(v, f"{path}{i}.")
walk(data)
print(f"Codestra enterprise profile validation PASS: {repo}")
