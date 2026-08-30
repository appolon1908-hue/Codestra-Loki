# Repository Profile — `Codestra-Loki`

## Identity

- **Repository:** `appolon1908-hue/Codestra-Loki`
- **Category:** Observability backend — logs
- **Visibility:** `public`
- **Default branch:** `main`
- **Canonical hostname:** `loki.codestra.media`
- **Exposure:** Internal/private only; no public native API
- **Authority:** Primary log ingestion, storage, retention, compaction, querying, tenancy, and label-policy authority

## Purpose

Stores and serves approved application and infrastructure logs for Grafana while enforcing redaction, tenant/business attribution, retention, and cardinality controls.

## Owns

- Loki ingestion, storage, retention, compaction, limits, tenancy, query, and label policy
- Log schema and storage configuration
- Loki validation, backup/restore, upgrade, and rollback source

## Does not own

- Log collection agents or application logging implementation
- Secrets, tokens, credentials, customer payloads, or raw sensitive business data in logs
- Public exposure of the native listener

## Key integrations

- Alloy and OpenTelemetry Collector
- Grafana
- Object/local storage according to accepted environment design
- Alerting and runbook links through approved observability contracts

## Current priorities

1. Finalize storage, schema, retention, compaction, and resource limits
2. Enforce log-field redaction and bounded labels
3. Prove ingestion backpressure, outage recovery, querying, and tenant isolation
4. Add backup/restore, upgrade, downgrade, and rollback evidence

## Governance and safety

- Promotion model: `feature/docs/fix/security/upgrade -> development -> test -> staging -> production -> main`.
- Native port `3100` must remain private; `loki.codestra.media` must not expose the API publicly.
- Never commit storage credentials, private keys, tokens, customer data, or secret-bearing sample logs.
- New log sources require redaction, retention, cardinality, and ownership review.
- Merge does not start Loki, activate ingestion, change storage, expose ports, or deploy software.

## Account-wide catalog

See `appolon1908-hue/documentaions/REPOSITORY_CATALOG.md`.
