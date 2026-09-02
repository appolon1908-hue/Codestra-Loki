# Backup, restore, and rollback

Before a runtime change, capture the active image digest, signed configuration
artifact digest, expanded configuration checksum, object-store recovery evidence,
WAL and volume locations, and the previous approved bundle. Restore or rollback
one instance at a time and prove cluster health before continuing.

This document does not execute a backup, restore, deployment, or rollback.
