# Polyglot Medicine — phone interface

Mobile web interface for the Polyglot Medicine knowledge graph (https://kgraph.sg/polyglot/).

Live: https://xuyuan71.github.io/polyglot-phone/

Plant scanning uses the Pl@ntNet API. No API key is stored in this repository. The GitHub Action inserts the `PLANTNET_KEY` repository secret at publish time (Settings → Secrets and variables → Actions). Without it, users can enter a key in the app settings.
