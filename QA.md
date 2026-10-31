# Verification

- Eight domain tests pass for equipment search, reciprocal OPC resolution, blocked broken
  connectors, validation, object-level revision differences, deep links and review persistence.
- Actual XML parsing of all seven generated SVG files passes. Released samples conform;
  the draft exposes exactly five expected violations. No embedded scripts/event handlers.
- Browser: clicked AHU-SUP on pump sheet; opened UT-PID-0103 revision B at OPC-301.
- Browser: Title block extracts the actual air-handling drawing ID, revision and fields.
- Browser: Back returns to pump sheet; comparison shows one added object (P-144), one
  changed object (PT-101) and no removals, with previous/current side-by-side drawings.
- Static source is prepared at root for main / (root) Pages deployment.
- Findings focus/zoom their SVG objects; Next issue cycles nonconforming objects;
  title-only findings switch to extracted title fields.
- Physical-device testing and production CAD conversion/security testing are outside scope.
