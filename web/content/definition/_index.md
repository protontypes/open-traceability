
---
title: Open Traceability Definition
version: "1.0"
date: 2026-05-30
---

**Open Traceability** is the externally inspectable link between an environmental claim and the evidence, methods, assumptions, computations, review processes, and publications on which that claim is based. It enables consistent assessment across claim types by breaking the knowledge-creation process into five processing steps, plus a cross-cutting verifiability dimension that links claims to the exact evidence chain behind them.

An environmental claim is any statement about environmental state, impact, change, risk, performance, attribution, history, or forecast. Open Traceability makes it possible to trace how information moves from source evidence to claim.

1. **Open Input Data and Measurement Evidence**: whether the relevant inputs are identifiable, documented, attributable, reusable, verifiable, and versioned; whether their measurement methods, uncertainty, quality controls, licensing, and transformations are clear; and whether the origin and quality of the data can be externally verified. Strong input-data traceability exists where external actors can inspect where the data came from, how it was produced or collected, how it was processed, and under what conditions it may be reused. Any secondary data should be traceable back to the underlying primary data. All primary datasets should include quantified errors and uncertainties where feasible.

2. **Open-Source Models, Methods, and Software**: whether the analytical logic can be inspected through code, models, methods, dependencies, documentation, and licensing. Ideally, open-source models and software should be released in version-controlled repositories and come with a recognised open-source licence, such as one approved by the [Open Source Initiative](https://opensource.org/licenses). This should also include the dependencies, documentation, and configuration needed to understand and run the software or model. It should further include the infrastructure software needed to operate the software and provide user-facing front ends. The software infrastructure should be capable of operating independently of any single company.

3. **Open Execution and Reproducibility**: whether workflows, scripts, parameters, outputs, and computational environments make the path from inputs to outputs inspectable. Strong execution traceability exists where an external actor can understand and, ideally, repeat the computational process that produced the result. The highest standard requires more than the existence of code: the specific run connecting the input data to the reported output should be inspectable and, where feasible, re-executable using standardised and accessible computational infrastructure.

4. **Open Community and Review**: whether critique, issue tracking, review, correction processes, and responses to challenges are sufficiently visible to show how claims were tested, questioned, corrected, or improved. Strong review traceability exists where external users can inspect not only the final claim, but also the record of scrutiny around it. This may include peer review, public comments, public issue trackers, correction notices, open methodological discussions, replication attempts, governance records, or community forums. Ideally, the evidence-producing process includes open channels where users, contributors, reviewers, and affected communities can raise questions, report errors, and discuss interpretations.

5. **Open Publications and Communication**: whether resulting reports, papers, dashboards, policy outputs, or explanatory materials are accessible and documented clearly enough to support scrutiny. Strong publication traceability exists where public outputs clearly state the claim, describe the methods and evidence base, cite the specific supporting artifacts, and preserve enough context for external inspection. Ideally, publications are openly accessible, released under standardised open licences such as Creative Commons licences, and subject to appropriate review. For dashboards and other dynamic outputs, this also includes clear documentation of update cycles, data sources, indicator definitions, and version history.

6. **Open Linkage**: whether the chain of evidence across open input data and measurement evidence (1), models, methods, and software (2), execution (3), community and review (4), and publication (5) is inspectable in an explicit, specific, versioned, and externally verifiable way. This includes links between claims and the exact datasets, code versions, model configurations, workflow runs, review records, publications, and supporting documents on which they depend. This dimension is critical because openness without explicit linkage does not produce traceability.

Open Traceability does not by itself prove that an environmental claim is correct, unbiased, or scientifically valid. Rather, it makes the basis of the claim inspectable, so that its evidence, assumptions, methods, limitations, uncertainty, and possible errors can be examined by others. A claim can be highly traceable and still be wrong; Open Traceability makes such problems easier to detect, evaluate, and correct.



