# Upgrade policy

Resolve the upstream version tag to its exact source commit, multi-platform image
digest, and linux/amd64 child digest. Update the runtime lock and deterministic
configuration manifest in one reviewed change. Validate the exact image against
the configuration, then promote the same protected source through development,
test, staging, production, and main. Never rebuild on a production host.
