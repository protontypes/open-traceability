# /// script
# dependencies = [
#   "ontolearner",
# ]
# ///
""" 
This script is meant to be run as a [UV script](https://docs.astral.sh/uv/guides/scripts/) with:
> uv run kg_poc.py
"""

from pathlib import Path

# Pointing to the ontology in the repo
ontology_file = Path(__file__).parent.parent / "ontology" / "open-traceability-ontology.ttl"
