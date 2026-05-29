# Underlying models

This is a work in progress (based upon [preliminary work in Mistral](https://chat.mistral.ai/chat/c8823a96-5173-4116-8cdc-776a8ec226b0))

The envisioned structure is the following:

- `ontology/` contains the [ontology](https://en.wikipedia.org/wiki/Ontology_(information_science)) definition,
- `knowledge_graph/` contains the PoC code to generate knowledge graphs using Python,
- `prompts/`contains a collection of prompts to carry out LLM interactions aligned with OT.


Notes:
- The TTL ontology is a rough first autogeneration using Mistral AI starting from the OT definition. Mistral claims:
    > Here is a formal OWL 2 ontology for Open Traceability, in Turtle (TTL) format. It aligns with PROV-O, Schema.org, and Dublin Core, while extending them for environmental traceability. The ontology is self-contained, valid, and ready for use in RDF-based systems (e.g., knowledge graphs, SPARQL endpoints).
