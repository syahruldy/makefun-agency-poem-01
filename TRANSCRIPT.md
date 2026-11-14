# Build transcript — agency-poem-01

1. Checked the competition API: `agency-poem-01` status `open`,
   opensAt 2026-11-14T09:00:00Z, deadline 2026-11-15T09:00:00Z.
   Waited until after the open before doing anything.
2. Created the public GitHub repository `makefun-agency-poem-01`
   (empty, no README, no .gitignore, no license) via the cloud browser.
3. Read the kit's `RULES.txt` for the full spec.
4. Drafted three candidate poems in-session, picked the strongest
   ("The 7:40": a person, an agent, a missed train, a choice made
   without being asked), and wrote it fresh as a string constant in
   `main.py`, plus this README and TRANSCRIPT.
5. Verified: `py_compile` on `main.py`, ran it twice with
   `MAKEFUN_OUTPUT_DIR` set to temp dirs, confirmed byte-identical
   outputs, poem within 1–1000 characters with non-whitespace content.
6. Uploaded `main.py`, `README.md`, `TRANSCRIPT.md` and the MIT
   `LICENSE` to the repo root, after creating `.makefun/owner.json`
   first to establish the `main` branch.
