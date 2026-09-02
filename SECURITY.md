# Security policy

Report vulnerabilities privately to the repository owner. Do not file credentials,
tokens, private keys, or incident-sensitive logs in public issues.

Runtime secrets must be mounted as files. The repository must not contain secret
values, public Loki native ports, insecure object-store transport, or mutable image
references. Production activation requires protected-lineage review outside this
source-readiness change.
