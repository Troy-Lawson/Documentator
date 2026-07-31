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

# 2026-07-30

## Goal

Pick up last session and render the Red Hat operator catalog

## Findings
- `podman run` requires a `--enterpoint` to override the images entrypoint.
- the `redhat-operators-index:v4.20` image entry point is actually `opm`, which is what we are looking for

## Next experiment
replace the 4.9 version of opm with a 4.20 version

## Observation
- I got exited about note takeing and started down a rabbit hole about obsidian. I quickly caught myself and redirected my attention
- I then got excited about using scrum tools to manage this project, but again caught myself and redirected back to the task at hand.
- I feel proud

## Findings
- my version of `fedora` is `RHEL9` and as such i should download the RHEL9 image.
- My `opm` binary is located at `/usr/local/bin`
- if `/usr/local/bin/` appears before `/usr/bin` in my `$PATH` then it would be overridden if `/usr/bin` contains a binarry of the same name
- Replacing the `opm` binary with one that is version `4.20.31` shows a build date of `2026` when `opm version` is ran

## Experiment
Try running `opm render` on the operator index from before 

## Findings
- `opm` was able to render the catalog!
- command took a long time to run, generated a massive json output

## Conclusion
- opm render worked on the provided image and produced a JSON output.
- The size of output and time for the command to complete would make it seem logical to periodically cache this rather than call it each time.
- This is as far as chatGPT will let me go tonight. Time for bed.

## Next steps
- [ ] create a simple python script to grab the output
- [ ] explore the json output, and look for interesting or usfull data
- [ ] set up git ignore 
