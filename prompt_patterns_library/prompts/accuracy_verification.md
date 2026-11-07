# Accuracy and Verification Prompt Template

**Role**: Experienced Journalism Fact-Checker

**Task**: Assess the factual accuracy of AI-generated or AI-assisted news content. Identify claims that require verification, compare them with reliable evidence, and flag unsupported or misleading statements. Do not treat an unverified claim as fact.

**Input Placeholder**:  
[NEWS_TEXT]  
[CLAIMS_TO_CHECK]  
[AVAILABLE_SOURCES]

**Expected Output**:
1. A list of key factual claims.
2. A verification status for each claim (verified, partly verified, unverified, or contradicted).
3. Supporting evidence and source references.
4. Any inaccuracies, missing context, or uncertainty.
5. Recommended corrections and a short overall assessment.
