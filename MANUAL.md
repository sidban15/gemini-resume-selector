# Gemini Resume Selector - User Manual

## Overview
Gemini Resume Selector is an automated recruitment agent pipeline designed to parse, analyze, rank, and process job applications (resumes) against specific Job Descriptions (JDs). It automates the workflow from initial receipt to final shortlisting or rejection, including email drafting.

---

## 🛠 Project Structure

- **`Unread/`**: The entry point for new resumes (PDF/DOCX).
- **`JD/`**: Contains Job Description files used for matching.
- **`ShortListed/`**: Candidates who meet the criteria.
- **`Reject/`**: Candidates who do not meet the criteria.
- **`Referred/`**: Candidates for other potential roles.
- **`Drafts/`**: Generated email drafts for candidates.
- **`SKILLS/`**: Definitions for specialized AI agents:
    - `AgentOrchestrator`: Manages the overall workflow.
    - `ResumeParser`: Extracts text and structured data from resumes.
    - `ResumeAnalyst`: Evaluates resumes against JD requirements.
    - `ResumeRanker`: Scores candidates numerically.
    - `EmailDrafter`: Prepares communication based on outcomes.
    - `SessionSummarizer`: Creates logs of the recruitment session.
- **`TEMPLATES/`**: Markdown templates for shortlist and rejection emails.
- **`AnalysisSummary/`**: CSV logs of all processed candidates and their scores.

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- Gemini CLI with access to the `gemini-resume-selector` workspace.
- (Optional) Gmail MCP configured for email automation.

### 2. Installation
```bash
git clone https://github.com/sidban15/gemini-resume-selector.git
cd gemini-resume-selector
git checkout dev
# Install dependencies (if any, e.g., for docx parsing)
# pip install -r requirements.txt
```

---

## 📖 How to Use

### Step 1: Prepare the Input
1. Place a Job Description in the `JD/` folder (e.g., `JD/software_engineer.md`).
2. Place all new resumes in the `Unread/` folder.

### Step 2: Run the Pipeline
Invoke the **Agent Orchestrator** to begin the process. The agent will:
1. Parse the resumes in `Unread/` using `extract_docx.py` or native PDF reading.
2. Analyze and rank them against the JD.
3. Move files to `ShortListed/` or `Reject/`.
4. Generate email drafts in the `Drafts/` folder.

### Step 3: Review & Finalize
- Check the `AnalysisSummary/` CSV for a quick overview of scores.
- Review the drafted emails in `Drafts/`.
- If Gmail MCP is active, you can instruct the agent to send the drafts.

---

## ⚙️ Customization
- **Email Templates**: Edit files in `TEMPLATES/` to match your company's voice.
- **Agent Instructions**: Modify `SKILLS/*/SKILL.md` to adjust how agents evaluate candidates.

---

## 📝 Utility Scripts
- **`extract_docx.py`**: A utility to convert `.docx` files to plain text for processing.
- **`generate_resumes.py`**: (Used for testing) Generates dummy resumes to verify pipeline flow.
