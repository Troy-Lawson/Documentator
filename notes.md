# 2026-07-29

## Goal

Render the Red Hat operator catalog.

## Findings

- `podman login` stores credentials in `/run/user/<uid>/containers/auth.json` on Fedora.
- Successfully pulled `registry.redhat.io/redhat/redhat-operator-index:v4.20`.
- `opm render` still returns a 401 Unauthorized.
- Hypothesis: `opm` is not discovering the Podman authentication file.

## Next experiment

Set `REGISTRY_AUTH_FILE` to the Podman auth file and retry.

## Findings
- Downloaded and installed a old version of opm from 2023
- Accidently used 4.9 mirror when we are trying to examine 4.20 images. Too much of a gap in versions.
- Discovered opm exisits in the catalog image itself. Meaning I have opm available with in a pod.

## Next experiment

Try using the opm image in podman to run the opm render test.


