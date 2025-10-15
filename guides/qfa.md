# Qualitative Feedback Analysis

## What is it?
Within the Feedback Management Template there is the possibility to enable qualitative feedback analysis (QFA). This enables structured, actionable analysis of free-text feedback within EspoCRM. It consists of two parts:
1. Automated Classification  
2. Insight Generation


## Why?

Working with qualitative feedback—open-ended, text-based input from communities—is powerful but complex. Some of the key challenges include:

- **Overload of Information:** Large volumes of feedback make it hard to see patterns or urgent needs.
- **Unstructured Data:** Free text lacks built-in categories, making analysis slow and inconsistent.
- **Manual Work:** Traditional qualitative analysis requires people to read, tag, and sort each piece of feedback. This is slow, repetitive, and prone to human error or bias.
- **Lack of Consistency:** Different people may interpret and classify the same feedback in different ways, reducing reliability and comparability.
- **Delayed Insights:** Manual processing takes time, delaying action on important community feedback.

**Automated classification and insight generation address these challenges by:**
- Turning text feedback into structured, actionable data
- Providing faster, more consistent insights
- Freeing up staff to focus on responding, not sorting


## How to Use?

QFA consists of two components: [Automated Classification](#automated-classification) and [Insight Generation](#insight-generation).

### Automated Classification

**Automated classification** is the process by which incoming qualitative feedback (free text) is analyzed and assigned to pre-defined categories, topics, or codes without manual human tagging.

#### Prerequisites

- **Coding framework levels** (e.g., Type, Category, Topic) are set up as fields within the Feedback entity, or as foreign fields of a related entity if [cascading select](https://github.com/rodekruis/EspoCRM-knowledge-base/wiki/Customization#cascading-select-with-automatic-filters) is needed.
    - Fields should be clearly named, of type text or string, and structured to allow cascading/nested selection (where possible).
- **Classification Flowchart** is configured (see [QFA-API Setup](https://github.com/rodekruis/qfa-api?tab=readme-ov-file#setup-classification-with-espocrm))
- **User permissions** are set so that relevant users can view and edit classification fields.

#### Steps

1. **Feedback Collection:** Qualitative (free text) feedback is collected and saved in EspoCRM.
2. **Automated Classification:**
    - New feedback (or edited feedback) triggers an EspoCRM flowchart.
    - The flowchart sends the feedback text (and up to 3 coding framework levels) to the QFA-API.
    - The QFA-API returns suggested labels for each level.
    - The flowchart saves these results in EspoCRM.
3. **Review and Edit:** Users can see the classified levels and correct them if needed. All manual changes are logged for transparency.
4. **Reporting:** Classified qualitative data can now be handled as quantitative data and visualized using Reports and Dashboards for meaningful insights.

**Example**

> **Feedback:**  
> “I have trouble getting to the vaccination site.”  
> **Classification:**  
> - Type: Problem  
> - Category: Access  
> - Topic: Vaccination


### Insight Generation

An **Insight** is an automatically generated summary, recommendation, or key finding created from analyzing multiple feedback entries. Insights help users quickly understand key themes, issues, or suggested actions based on community feedback.

#### Prerequisites

- **Feedback data** exists in EspoCRM (ideally classified).
- **Insight Generation Flowchart** (e.g., via QFA-API or a connected LLM) is set up and configured with correct API keys.
- **User permissions** are in place for generating and viewing insights.

#### Steps

1. **Create Insight:** User creates a new Insight record, specifying the topic or question to explore.
2. **Select Feedback:** User selects or filters relevant feedback (e.g., all feedback about “Health Services” in June).
3. **Trigger Generation:** A flowchart collects feedback text and the user’s prompt, sending both to the insight generation backend.
4. **View Insight:** The resulting summary, recommendation, or narrative is returned and saved in EspoCRM, visible to the user.
5. **Use in Decision-making:** Insights can be copied into reports, shared, or used for program decision-making.

**Example**

> **User prompt:** “Summarize main concerns about vaccination access.”  
> **Generated Insight:** “The most common barriers reported were distance to health centers, lack of information, and limited transportation.”


## Data Privacy & Security

- All data sent to external APIs is handled securely (following IFRC and RCRC data protection policies)
- User permissions determine who can trigger classifications or insights and who can view/edit results.
- All edits and classification overrides are logged in the activity stream for transparency.


## Troubleshooting & FAQ

**Q: What if a classification is wrong?**  
A: You can manually update any coding framework field. All changes are tracked in the activity log.

**Q: Can I re-run the classifier on old feedback?**  
A: Yes. Use the mass-update or change the feedback description slightly to trigger automated classification again on selected records.

**Q: Who can see or edit insights?**  
A: Access is controlled by EspoCRM permissions. Check with your administrator if unsure.

**Q: What if the QFA-API is down or errors occur?**  
A: You will receive a notification in EspoCRM. Manual classifications are still possible.

**Q: Is multi-language analysis supported?**  
A: Insight generation in most-common multiple languages is supported or planned, depending on the connected backend and local setup.


## Accessibility & Internationalization

- The system is designed to be accessible and usable for staff in different countries and contexts.
- Support for multiple languages is planned/ongoing to ensure inclusivity.


## How to Install & Configure

**Both components require the [EspoCRM Advanced Pack extension](https://www.espocrm.com/extensions/advanced-pack/) to be installed first.**

### Insight Generation
1. Import [Insight Generation](/import/qfa-classify-feedback-flowchart.csv) Flowchart.
2. Add your API Key to the App Secrets page under Administration with name `API_Key_Insight_Generation`.

### Classification
1. Import the [Classify Feedback](/import/qfa-classify-feedback-flowchart.csv) Flowchart.
2. Add your API Key to the App Secrets page under Administration with name `API_Key_Classify_Feedback`.
3. Follow the [QFA-API setup instructions](https://github.com/rodekruis/qfa-api?tab=readme-ov-file#setup-classification-with-espocrm).


## Related Resources

- [EspoCRM Documentation](https://docs.espocrm.com/)
- [QFA-API Documentation](https://github.com/rodekruis/qfa-api)
- [EspoCRM Advanced Pack](https://www.espocrm.com/extensions/advanced-pack/)
- [Cascading Selects in EspoCRM](https://github.com/rodekruis/EspoCRM-knowledge-base/wiki/Customization#cascading-select-with-automatic-filters)


## Improvements and Future Plans

- Ongoing work to improve multi-language support for both classification and insight generation.
- Planned enhancements for UI and UX
- Better error handling and user notifications.
- Improve classification accuracy and insight usefulness.
- Add a section on the risks of using AI for analysis (bias amplification, misrepresentation, hallucination, loss of outliers, context & nuance, difficulty handling ambiguity & contradiction, etc.) 

