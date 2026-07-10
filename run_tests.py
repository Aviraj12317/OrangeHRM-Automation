"""
Test Execution Script
Run this script to execute tests with various options
"""

import os
import sys
import argparse
from datetime import datetime


def run_tests(args):
    """Execute tests based on provided arguments"""
    
    # Build pytest command
    cmd_parts = ["pytest"]
    
    # Add marker if specified
    if args.marker:
        cmd_parts.append(f"-m {args.marker}")
    
    # Add specific test file if specified
    if args.test_file:
        cmd_parts.append(f"tests/{args.test_file}")
    
    # Add parallel execution
    if args.parallel:
        cmd_parts.append(f"-n {args.workers}")
    
    # Add HTML report
    if args.html_report:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_name = f"reports/report_{timestamp}.html"
        cmd_parts.append(f"--html={report_name}")
        cmd_parts.append("--self-contained-html")
    
    # Add verbose if specified
    if args.verbose:
        cmd_parts.append("-v")
    
    # Add browser option if specified
    if args.browser:
        # This would require updating conftest to accept browser parameter
        print(f"Note: To change browser, update config.py - BROWSER = '{args.browser}'")
    
    # Execute command
    cmd = " ".join(cmd_parts)
    print(f"\nExecuting: {cmd}\n")
    print("=" * 80)
    os.system(cmd)


def main():
    """Main function to parse arguments and run tests"""
    
    parser = argparse.ArgumentParser(
        description="OrangeHRM Test Automation Execution Script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run all tests
  python run_tests.py
  
  # Run smoke tests only
  python run_tests.py -m smoke
  
  # Run specific test file
  python run_tests.py -f test_login.py
  
  # Run tests in parallel with HTML report
  python run_tests.py -p -r
  
  # Run regression tests in parallel with 4 workers
  python run_tests.py -m regression -p -w 4
        """
    )
    
    parser.add_argument(
        "-m", "--marker",
        help="Run tests with specific marker (smoke, regression, sanity)",
        choices=["smoke", "regression", "sanity"]
    )
    
    parser.add_argument(
        "-f", "--test-file",
        help="Run specific test file (e.g., test_login.py)"
    )
    
    parser.add_argument(
        "-p", "--parallel",
        action="store_true",
        help="Run tests in parallel"
    )
    
    parser.add_argument(
        "-w", "--workers",
        type=int,
        default=4,
        help="Number of parallel workers (default: 4)"
    )
    
    parser.add_argument(
        "-r", "--html-report",
        action="store_true",
        help="Generate HTML report"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )
    
    parser.add_argument(
        "-b", "--browser",
        help="Browser to use (chrome, firefox, edge)",
        choices=["chrome", "firefox", "edge"]
    )
    
    args = parser.parse_args()
    
    # Run tests
    run_tests(args)


if __name__ == "__main__":
    main()
