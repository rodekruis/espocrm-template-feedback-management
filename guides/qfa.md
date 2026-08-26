

# Qualitative Feedback Analysis 

 

## What is it? 

Within the Feedback Management Template, Qualitative Feedback Analysis (QFA) can be enabled to support structured, actionable analysis of free-text feedback in EspoCRM. 

QFA is a backend service that receives qualitative feedback records from EspoCRM, processes them using large language models, and returns the results to EspoCRM. Depending on the configured flowcharts and interface, QFA can support: 

 

1. Automated summarisation of individual feedback records 
2. Automated coding and classification 
3. Automated sensitive feedback detection 
4. Analysis and insight generation across multiple feedback records 
5. Bulk summarisation of multiple feedback records 

QFA provides suggestions and draft analyses. Users remain responsible for reviewing the output and making operational decisions. 

## Why?  

Working with qualitative feedback, such as open-ended, text-based input from communities, is powerful but complex. Key challenges include:
 

- **Overload of information:** Large volumes of feedback make it difficult to identify patterns, minority perspectives, or urgent concerns. 
- **Unstructured data:** Free text does not contain built-in categories, which makes analysis slower and less consistent. 
- **Manual work:** Traditional qualitative analysis requires people to read, summarise, tag, and sort individual feedback records. This is time-consuming and can be affected by human error or bias. 
- **Lack of consistency:** Different people may interpret and classify the same feedback differently, reducing reliability and comparability. 
- **Delayed insights:** Manual processing can delay action on important community feedback. 

QFA can help address these challenges by: 

- Turning free-text feedback into structured data 
- Producing draft summaries and suggested codes more quickly 
- Supporting analysis of larger volumes of feedback 
- Helping users identify recurring themes, concerns, gaps, and suggested actions 
- Allowing staff to spend more time reviewing, interpreting, and responding to feedback 
 
QFA should support human judgement, not replace it. 


## How to Use 

 

The available QFA functions depend on the flowcharts and user interface configured in the Feedback Management Template. 

 

### Automated Summarisation 

 

Automated summarisation creates a short summary of an individual feedback record. This can help users understand the main message without first reading the complete description. 

 

#### Prerequisites 

 

- A free-text feedback field is configured in the Feedback entity. 
- The relevant QFA summarisation flowchart or script is enabled. 

- Authentication between EspoCRM and the QFA backend is configured. 

- User permissions allow relevant users to view the generated summary. 

 

#### Process 

 

1. **Feedback collection:** A qualitative feedback record is created or updated in EspoCRM. 

2. **Flowchart trigger:** An EspoCRM flowchart collects the required feedback text and sends it to the QFA backend. 

3. **Processing:** QFA generates a concise summary. 

4. **Result:** The summary is returned to EspoCRM and stored in the configured field. 

5. **Review:** A user checks the generated summary against the original feedback and corrects it if necessary. 

 

**Example** 

 

> **Feedback:**   

> “We registered three weeks ago but have still not received the hygiene kits that were promised.”   

> **Generated summary:**   

> “The community member reports a three-week delay in receiving promised hygiene kits.” 

 

### Automated Coding and Classification 

 

Automated coding and classification analyses incoming qualitative feedback and suggests predefined categories, topics, or codes without requiring users to tag every record manually. 

 

#### Prerequisites 

 

- The coding framework is configured in EspoCRM, for example as Type, Category, and Topic fields. 

- If hierarchical coding is needed, the fields and relationships required for [cascading selects in EspoCRM](https://github.com/rodekruis/EspoCRM-knowledge-base/wiki/Customization#cascading-select-with-automatic-filters) are configured. 

- The relevant classification flowchart or EspoCRM connector script is configured. 

- Authentication between EspoCRM and the QFA backend is configured. 

- User permissions allow relevant users to view and edit the coding fields. 

 

Coding framework labels and descriptions should be clear, distinct, and sufficiently detailed. Overlapping or ambiguous codes can reduce the usefulness of automated suggestions. 

 

#### Process 

 

1. **Feedback collection:** Qualitative feedback is collected and saved in EspoCRM. 

2. **Automated classification:** 

   - New or edited feedback triggers an EspoCRM flowchart. 

   - The flowchart sends the required feedback text and configured coding framework information to the QFA backend. 

   - QFA returns suggested labels or codes. 

   - The flowchart stores the suggestions in EspoCRM. 

3. **Review and correction:** Users review the suggested codes and update them where necessary. 

4. **Reporting:** Approved coded data can be filtered, aggregated, and visualised through EspoCRM reports and dashboards. 

 

**Example** 

 

> **Feedback:**   

> “I have trouble getting to the vaccination site.”   

> **Suggested classification:**   

> - Type: Problem   

> - Category: Access   

> - Topic: Vaccination 

 

### Sensitive Feedback Detection 

 

Sensitive feedback detection checks whether a feedback record may contain content that requires additional protection, restricted access, or referral under the applicable organisational procedures. 

 

Depending on the configured implementation, QFA can return: 

 

- A suggestion that the record may be sensitive 

- An explanation of why it may be sensitive 

- Supporting information for human review 

 

A QFA sensitivity flag is not a final decision. Sensitive feedback must always be handled according to the National Society's approved procedures, role-based access model, referral pathways, and data-protection requirements. 

 

#### Prerequisites 

 

- The organisation has an agreed definition of sensitive feedback. 

- Sensitive-feedback fields and restricted-access roles are configured in EspoCRM. 

- The relevant QFA detection flowchart or script is enabled. 

- A human review and referral process is documented. 

 

#### Process 

 

1. A feedback record is created or updated. 

2. The configured flowchart sends the required text to QFA. 

3. QFA returns a sensitivity suggestion and, where configured, an explanation. 

4. EspoCRM stores the result in the configured fields. 

5. An authorised user reviews the suggestion and follows the organisation's sensitive-feedback procedure. 

 

> **Important:** QFA must not be used as the only safeguard for protection, safeguarding, or PSEA concerns. Human review and established referral procedures remain essential. 

 

### Insight Generation and Bulk Analysis 

 

An **Insight** is a generated summary, finding, or analysis based on multiple feedback records. It helps users identify themes, issues, differences, or possible actions across a selected set of feedback. 

 

#### Prerequisites 

 

- Relevant feedback data exists in EspoCRM. 

- The Insight entity and the relevant insight-generation flowchart or connector are configured. 

- Authentication between EspoCRM and the QFA backend is configured. 

- User permissions allow the user to select feedback, generate an insight, and view the result. 

- The selected records are appropriate for the intended analysis. 

 

#### Process 

 

1. **Define the question:** The user creates an Insight record and writes a clear question or instruction. 

2. **Select feedback:** The user selects or filters the relevant feedback records, for example feedback about health services collected during a specified period. 

3. **Trigger generation:** The configured process sends the selected feedback text and user instruction to QFA. 

4. **Review the result:** QFA returns a generated analysis or summary, which is stored in EspoCRM. 

5. **Validate:** The user checks the result against the underlying feedback, paying particular attention to urgent issues, minority views, conflicting evidence, and unsupported conclusions. 

6. **Use responsibly:** The reviewed result can support reporting, discussion, programme adaptation, or further analysis. 

 

**Example** 

 

> **User prompt:** “Summarise the main concerns about access to vaccination services and indicate whether concerns differ by location.”   

> **Generated insight:** “The selected feedback most often mentions distance to health centres, insufficient information, and limited transport. Some locations also report inconvenient opening hours.” 

 

The example output above is illustrative. Actual QFA output depends on the selected feedback and the instruction provided. 

 

#### Prompt-writing guidance 

 

For more useful results: 

 

- State clearly what QFA should identify, compare, summarise, or assess. 

- Define the scope, such as service, location, population group, or reporting period. 

- Ask QFA to distinguish frequent themes from less common but important concerns. 

- Ask for uncertainty or contradictory feedback to be made visible. 

- Avoid leading questions that assume a conclusion. 

- Review important claims against the original feedback records. 

 

Example prompts: 

 

- “Summarise the main themes raised across these feedback records and group them by frequency.” 

- “Identify feedback that may indicate a protection, safeguarding, or PSEA concern requiring urgent human review.” 

- “Highlight recurring complaints about a specific service or activity.” 

- “Identify positive feedback and describe what people appreciated.” 

- “Identify feedback that suggests a gap between what was promised and what was delivered.” 

- “Summarise suggestions made by community members for improving the programme.” 

- “Identify feedback where a response or follow-up appears to be expected but has not yet been provided.” 

 

## Human Review and Responsible Use 

 

QFA recommends, summarises, and supports analysis. It does not make operational decisions. 

 

Users are responsible for: 

 

- Checking summaries against the original feedback 

- Reviewing and correcting suggested codes 

- Reviewing sensitivity flags and applying approved referral procedures 

- Verifying generated insights before using or sharing them 

- Considering context that may not be present in the selected feedback 

- Avoiding decisions based solely on AI-generated output 

- Protecting confidential or restricted information 

 

Where QFA provides a quality or confidence indicator, treat it as supporting information rather than proof that the output is correct. 

 

## Data Privacy and Security 

 

QFA is designed to minimise the exposure and retention of feedback data. 

 

The current QFA architecture includes the following safeguards: 

 

- Bearer-token authentication is required for protected endpoints. 

- API keys are scoped per organisation and are stored as hashes rather than in plain text. 

- Personally identifiable information is anonymised before text is sent to the language model. 

- Names and identifying details are processed in memory and are not permanently retained for analysis. 

- Feedback text, prompts, and model responses are not written to the QFA database. 

- Operational metadata, such as organisation, operation type, record counts, cost, and timing, may be retained for usage monitoring. 

- Feedback content, prompts, model output, and key values are excluded from application logs. 

- Credentials and application secrets are managed outside the source code. 

- Requests use correlation identifiers to support monitoring and troubleshooting without logging feedback content. 

 

In EspoCRM: 

 

- Roles and field-level permissions determine who can trigger QFA processes and who can view or edit the results. 

- Sensitive-feedback access must be restricted according to the organisation's approved access model. 

- Manual changes should be traceable through the configured audit or activity mechanisms. 

 

> **Note:** National Societies remain responsible for confirming that their QFA configuration, access model, processing activities, and retention practices meet applicable RCRC and local data-protection requirements. 

 

## AI Limitations and Risks 

 

QFA output can be incomplete or incorrect. Known risks when using AI for qualitative analysis include: 

 

- **Hallucination:** The system may generate a statement that is not supported by the selected feedback. 

- **Misclassification:** A suggested code or sensitivity flag may be wrong. 

- **Bias amplification:** Patterns in the model, prompts, coding framework, or source data may influence the result. 

- **Loss of nuance:** Summaries may simplify complex experiences or remove contextual details. 

- **Loss of outliers:** Less frequent views may be overlooked even when they are important. 

- **Misrepresentation:** Generated text may overstate certainty or combine distinct experiences. 

- **Translation limitations:** Meaning can be reduced or changed, especially for local languages, mixed-language text, spelling variants, or culturally specific expressions. 

- **Ambiguity and contradiction:** QFA may not correctly interpret unclear, conflicting, ironic, or indirect statements. 

- **Selection bias:** An insight only reflects the records selected for analysis. It does not automatically represent the wider community. 

- **Automation bias:** Users may trust a generated result because it appears confident or well written. 

 

Risk-reduction measures include clear prompts, appropriate record selection, human review, comparison with the original feedback, documentation of corrections, and escalation through established safeguarding and referral processes. 

 

## Troubleshooting and FAQ 

 

**Q: What if an automated summary or classification is wrong?**   

A: Review the original feedback and manually correct the relevant EspoCRM field. Where auditing is configured, the change remains traceable. 

 

**Q: Can I run QFA on existing feedback?**   

A: This depends on the configured flowchart. An administrator can configure a process for selected existing records. Avoid changing feedback text only to force a trigger, because this can create unnecessary audit changes and may affect data quality. 

 

**Q: Who can see or edit QFA results?**   

A: Access is controlled through EspoCRM roles, teams, and field-level permissions. Sensitive results may require additional restrictions. 

 

**Q: What happens if the QFA backend is unavailable or returns an error?**   

A: The EspoCRM process should not overwrite existing human-entered values. Check the configured flowchart error path, EspoCRM job and application logs, and the QFA monitoring information. Manual processing should remain possible. 

 

**Q: Is multi-language analysis supported?**   

A: QFA can process feedback in multiple languages, but performance can vary by language and context. Results for local or less widely represented languages require additional review and testing. 

 

**Q: Is a QFA suggestion final?**   

A: No. QFA output is a recommendation or draft. A user remains responsible for reviewing it. 

 

**Q: Can QFA replace qualitative research or programme judgement?**   

A: No. QFA can support summarisation and exploratory analysis, but it does not replace contextual knowledge, triangulation, qualitative research methods, or accountable decision-making. 

 

## Accessibility and Internationalisation 

 

- Use clear field labels, instructions, and error messages in the languages required by users. 

- Test QFA with representative examples from each operational language before rollout. 

- Treat performance in local and less widely represented languages as a specific testing requirement. 

- Ensure users can access the original feedback alongside generated summaries, codes, and insights. 

- Provide training on reviewing AI-generated output and reporting incorrect results. 

 

## How to Install and Configure 

 

> **Important:** Flowchart names, import files, field names, and App Secret names may change as the Feedback Management Template and QFA integration evolve. Verify these values against the current template repository and the current QFA EspoCRM integration documentation before production deployment. 

 

The flowchart-based integration requires the [EspoCRM Advanced Pack](https://www.espocrm.com/extensions/advanced-pack/). 

 

### General configuration 

 

1. Deploy or obtain access to a QFA backend environment. 

2. Configure an organisation-scoped API key for the EspoCRM integration. 

3. Store the API key in EspoCRM App Secrets. Do not hard-code it in a flowchart or formula script. 

4. Import or configure the required QFA flowcharts and connector scripts. 

5. Map the EspoCRM input fields, output fields, and relationships used by each QFA function. 

6. Configure roles, teams, field-level security, and sensitive-feedback access. 

7. Configure success, error, and retry paths without exposing feedback text or secret values in logs or notifications. 

8. Test each function with non-sensitive test data before enabling it for operational records. 

9. Validate multi-language behaviour with representative examples. 

10. Document ownership, monitoring, key rotation, incident handling, and the fallback process for manual processing. 

 

### Automated summarisation 

 

1. Configure the flowchart or connector that triggers summarisation. 

2. Map the free-text source field and generated-summary output field. 

3. Define when summarisation should run, for example after record creation or a relevant text update. 

4. Test that human-entered summaries are not overwritten unexpectedly. 

 

### Automated coding and classification 

 

1. Configure the coding framework fields and, where required, cascading relationships. 

2. Import or configure the classification flowchart or EspoCRM connector script. 

3. Map the source text, coding framework definitions, and output fields. 

4. Define how suggested codes are distinguished from reviewed or approved codes. 

5. Test ambiguous, multilingual, sensitive, and out-of-framework examples. 

 

### Sensitive feedback detection 

 

1. Agree the operational definition of sensitive feedback. 

2. Configure sensitivity fields and restricted-access roles in EspoCRM. 

3. Configure the detection flowchart or connector. 

4. Define the human-review and referral process. 

5. Test false-positive and false-negative scenarios using safe, synthetic examples. 

 

### Insight generation and bulk analysis 

 

1. Configure the Insight entity and its relationship to Feedback records. 

2. Configure the process that collects selected feedback and sends it with the user's instruction to QFA. 

3. Define limits for the number and size of selected records. 

4. Configure where generated output, processing status, and errors are stored. 

5. Test representative prompts and review the output against the selected records. 

 

For current implementation details, use the [QFA EspoCRM integration documentation](https://github.com/rodekruis/qualitative-feedback-analysis/blob/main/docs/integrations/espo-crm.md) and the [QFA REST API documentation](https://github.com/rodekruis/qualitative-feedback-analysis/blob/main/docs/rest-api/index.md). 

 

## Related Resources 

 

- [Qualitative Feedback Analysis repository](https://github.com/rodekruis/qualitative-feedback-analysis) 

- [Rendered QFA documentation](https://rodekruis.github.io/qualitative-feedback-analysis/) 

- [QFA EspoCRM integration documentation](https://github.com/rodekruis/qualitative-feedback-analysis/blob/main/docs/integrations/espo-crm.md) 

- [QFA REST API documentation](https://github.com/rodekruis/qualitative-feedback-analysis/blob/main/docs/rest-api/index.md) 

- [QFA architecture documentation](https://github.com/rodekruis/qualitative-feedback-analysis/blob/main/docs/architecture/index.md) 

- [QFA operations documentation](https://github.com/rodekruis/qualitative-feedback-analysis/blob/main/docs/operations/index.md) 

- [QFA settings reference](https://github.com/rodekruis/qualitative-feedback-analysis/blob/main/docs/operations/settings-reference.md) 

- [EspoCRM documentation](https://docs.espocrm.com/) 

- [EspoCRM Advanced Pack](https://www.espocrm.com/extensions/advanced-pack/) 

- [Cascading selects in EspoCRM](https://github.com/rodekruis/EspoCRM-knowledge-base/wiki/Customization#cascading-select-with-automatic-filters) 

 

## Improvements and Future Plans 

 

Potential improvements should be tracked against the QFA and Feedback Management Template roadmaps. Relevant areas include: 

 

- Continued testing and improvement for multiple languages and local-language use cases 

- Clearer status, progress, and error information in the EspoCRM user interface 

- Better separation between AI suggestions and human-reviewed or approved values 

- Improved support for quality review and correction feedback 

- Additional controls for bulk analysis and large input sets 

- Support for additional qualitative sources, such as focus group discussion notes and other group-meeting notes, while clearly distinguishing these from individual feedback records 

- Better guidance for triangulation, prompt design, representative record selection, and responsible interpretation 

- Continued security, privacy, monitoring, and operational documentation 

 
