#!/usr/bin/env python
import sys
import os
import warnings

from datetime import datetime

from zero_day_sentinel.crew import ZeroDaySentinel

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    if len(sys.argv) > 1:
        target_software = sys.argv[1]
    else:
        target_software = "Apache Web Server"

    inputs = {
        "target_software": target_software,
        "current_year": str(datetime.now().year),
    }

    print(
        f"""
        🔍 ZERODAY SENTINEL ACTIVATED
        ═══════════════════════════════════════
        Target: {target_software}
        Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        Mission: Autonomous Vulnerability Research & Patching
        ═══════════════════════════════════════
        """
    )

    try:
        os.makedirs("reports", exist_ok=True)
        result = ZeroDaySentinel().crew().kickoff(inputs=inputs)
        print(
            f"""
            ✅ MISSION COMPLETE
            ═══════════════════════════════════════
            Results saved in: reports/security_advisory.md
            Target Secured: {target_software}
            ═══════════════════════════════════════
        """
        )
        return result
    except Exception as e:
        print(f"❌ CRITICAL MISSION FAILURE: {e}")
        raise Exception(f"ZeroDay Sentinel mission failed: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "target_software": "Apache Web Server",
        "current_year": str(datetime.now().year),
    }
    try:
        ZeroDaySentinel().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ZeroDaySentinel().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "target_software": "Apache Web Server",
        "current_year": str(datetime.now().year),
    }

    try:
        ZeroDaySentinel().crew().test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    run()
