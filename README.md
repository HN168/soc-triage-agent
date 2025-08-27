# 🚨 SOC Triage Agent

AI-powered automation for AWS GuardDuty alert triage with VirusTotal enrichment and intelligent risk scoring.

## What It Does

1. **Fetches** AWS GuardDuty findings automatically
2. **Extracts** IPs, domains, and hashes from alerts  
3. **Enriches** IoCs with VirusTotal threat intelligence
4. **Generates** AI-powered analyst summaries
5. **Scores** risk based on SOC analyst experience

**Problem Solved**: Manual GuardDuty alert triage takes 15-30 minutes per alert. This agent does it in under 3 seconds.

## Quick Start

```bash
# Setup
git clone https://github.com/HN168/huy-soc-triage-agent.git
cd huy-soc-triage-agent
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
# Add your VirusTotal and OpenAI keys to .env

# Run demo (no AWS account needed)
python src/main.py --demo

# Run live (requires AWS GuardDuty access)
python src/main.py --hours 24
```

## Sample Output

```
🚨 HIGH RISK - Score: 78/100

ALERT: Cryptocurrency Mining Activity 
IP: 185.220.101.32 (🔴 14/70 AV detections)
INSTANCE: i-1234567890abcdef0

AI SUMMARY: High-confidence mining detection with C2 communication.
Immediate isolation recommended.

ACTIONS: Isolate instance → Investigate similar IoCs → Create IR ticket
```

## Architecture

```
GuardDuty → IoC Extractor → VirusTotal API → Risk Scorer → AI Summary → Output
```

**Key Components:**
- `main.py` - Entry point and CLI interface
- `soc_triage_agent.py` - Core orchestration logic
- `guardduty_client.py` - AWS GuardDuty integration
- `virustotal_client.py` - VirusTotal API client
- `ioc_extractor.py` - Extract indicators from findings
- `risk_scorer.py` - Calculate threat scores
- `ai_summarizer.py` - OpenAI integration for analysis

## Configuration

**Required Environment Variables:**
```bash
VIRUSTOTAL_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
AWS_DEFAULT_REGION=us-west-2  # optional
```

**AWS Permissions Needed:**
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "guardduty:ListDetectors",
                "guardduty:ListFindings",
                "guardduty:GetFindings"
            ],
            "Resource": "*"
        }
    ]
}
```

## Learning Objectives

**What I'm applying from SOC experience:**
- Alert triage decision-making logic
- IoC prioritization and risk assessment
- False positive reduction techniques
- Analyst workflow automation

**What I'm learning with AI assistance:**
- Python automation and error handling
- AWS API integration patterns
- AI prompt engineering for security analysis
- Extensible architecture design

## Future Enhancements

- **Phase 1.5**: Add AbuseIPDB and GreyNoise integration
- **Phase 1.6**: Slack notifications and JIRA ticket creation
- **Phase 2.0**: SIEM integration and automated response actions

## Results

**Target Performance:**
- Processing time: <3 seconds per finding
- False positive reduction: 40% improvement
- Coverage: 90%+ IoC enrichment rate
- Cost: <$20/month for typical SMB SOC

---

*Part of [Huy's AI Cloud Security Bootcamp](https://github.com/HN168/huy-ai-cloudsec-agent-bootcamp)*
