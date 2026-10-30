# Drawing platform contract

Canonical site: DEMO-PLANT-01. Eight shared equipment IDs match master_data and Digital Twin.
Identity is joined through assetId, never display names or file positions.

## Deep links

`?assetId=EQ-UT-00142` selects a released drawing containing the equipment.
`?drawingId=UT-PID-0102&revision=C&objectId=P-142` selects an exact sheet revision/object.
Unknown drawing references fall back to the default sample; unsupported asset IDs never
become fabricated equipment. Browser URL replacement preserves the repository subpath.

## SVG/XML structure

Each SVG has a viewBox, synthetic metadata, title-block text nodes tagged data-title-field,
and selectable groups tagged data-object-id, data-object-type, data-standard-id,
data-asset-id, data-layer and data-signature. OPC objects additionally have target drawing,
target object and connection-code attributes. Element IDs are scoped by drawing ID/revision.

Runtime extraction reads the fetched file with DOMParser. App exports contain schemaVersion,
source, synthetic flag, titleBlock and objects. They are drawing metadata, not a twin's
asset bundle or master snapshot. Add adapters rather than assuming those formats match.

OPC resolution uses the target drawing's latest catalog revision and validates the target
connector, matching service code and reciprocal reference. Prior revisions are read-only in
comparison mode. Objects remain keyed by drawingId + revision + objectId.

## Future services

Master data owns asset identity/lifecycle/specifications. Drawing management owns drawing
revisions and equipment/object relationships. Document delivery should provide accepted
releases; replace the bundled manifest through an adapter. ETL owns its processing and
operational status. The current frontend neither imports live releases nor shares review notes.

A production backend should store document hashes, released/retired revisions, extraction
jobs, validation findings, approval history and concurrency-safe review notes. CAD/PDF
conversion and arbitrary SVG uploads require a separately secured processing pipeline.

## Document handover available

The document_delivery demo at https://leetj94-lab.github.io/document_delivery/
accepts the same canonical assetId. It owns dossier submissions, structured document
checks, review/acceptance and release manifests. Links preserve equipment context;
browser-local decisions are not automatically synchronized across applications.
For equipment without a seeded dossier, create a package from the shared master list.

## ETL operations available

The etl_monitoring demo at https://leetj94-lab.github.io/etl_monitoring/
preserves assetId context and supports pipelineId/runId deep links. It processes
pinned synthetic master, observation, drawing and accepted-handover inputs, with
quarantine/retry/checkpoint evidence. It does not redefine equipment standards,
release drawings, accept handovers or synchronize browser-local edits across sites.
