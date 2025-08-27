#!/usr/bin/env python3
"""
SOC Triage Agent - Main Entry Point
Author: Huy Ngo (with AI coding assistance)
"""

import sys
import argparse
import logging
import time
from datetime import datetime
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent))

try:
    from config.settings import LOG_LEVEL, DEMO_MODE, validate_required_settings
except ImportError as e:
    print(f"❌ Configuration import failed: {e}")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper()),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def run_demo_mode():
    """Run agent with simulated GuardDuty findings."""
    print("🎯 SOC TRIAGE AGENT - DEMO MODE")
    print("=" * 50)
    print("Running with simulated GuardDuty findings...")
    print("No real API keys required for demo.\n")
    
    # Sample findings (based on real GuardDuty alert types)
    demo_findings = [
        {
            'Id': 'demo-001',
            'Type': 'CryptoCurrency:EC2/BitcoinTool.B!DNS',
            'Title': 'Cryptocurrency mining activity detected',
            'Severity': 7.2,
            'RemoteIP': '185.220.101.32'
        },
        {
            'Id': 'demo-002',
            'Type': 'UnauthorizedAPICall:IAM/ConsoleLogin',
            'Title': 'Unusual console login activity',
            'Severity': 5.8,
            'RemoteIP': '203.0.113.42'
        },
        {
            'Id': 'demo-003',
            'Type': 'Recon:EC2/PortProbeUnprotectedPort',
            'Title': 'Unprotected port being probed',
            'Severity': 4.1,
            'RemoteIP': '198.51.100.100'
        }
    ]
    
    print(f"📋 Processing {len(demo_findings)} simulated findings...\n")
    
    for i, finding in enumerate(demo_findings, 1):
        print(f"--- FINDING {i}/{len(demo_findings)} ---")
        print(f"🚨 Type: {finding['Type']}")
        print(f"📊 Severity: {finding['Severity']}/10")
        print(f"🎯 IP: {finding['RemoteIP']}")
        
        # Simulate processing
        print("🔍 Extracting IoCs...")
        time.sleep(0.5)
        print("🌐 Enriching with VirusTotal (simulated)...")
        time.sleep(0.3)
        print("📊 Calculating risk score...")
        
        # Simple risk calculation
        risk_score = min(finding['Severity'] * 12, 100)
        print(f"   • Risk score: {risk_score:.0f}/100")
        
        # Recommendation
        if risk_score >= 70:
            recommendation = "🚨 IMMEDIATE ACTION REQUIRED"
        elif risk_score >= 50:
            recommendation = "⚠️ INVESTIGATE FURTHER"
        else:
            recommendation = "✅ CONTINUE MONITORING"
        
        print(f"💡 Recommendation: {recommendation}")
        print("-" * 50)
        
        if i < len(demo_findings):
            time.sleep(1)
    
    print("\n🎉 DEMO COMPLETED!")
    print("✅ All simulated findings processed successfully")
    print("🚀 Ready to configure real API keys for live mode")


def main():
    """Main entry point with CLI argument parsing."""
    parser = argparse.ArgumentParser(description='SOC Triage Agent')
    parser.add_argument('--demo', action='store_true', help='Run demo mode')
    parser.add_argument('--hours', type=int, default=1, help='Hours back to search')
    
    args = parser.parse_args()
    
    print("🛡️ SOC TRIAGE AGENT")
    print("Learning Project by Huy Ngo")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    try:
        if args.demo or DEMO_MODE:
            run_demo_mode()
        else:
            print("⚠️ Live mode not implemented yet")
            print("🎯 Try: python src/main.py --demo")
    
    except KeyboardInterrupt:
        print("\n👋 SOC Triage Agent stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()