import subprocess
import sys


def run_command(command):
    print("\n" + "=" * 80)
    print(f"Running: {command}")
    print("=" * 80)

    result = subprocess.run(
        command,
        shell=True
    )

    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {command}")


def main():
    sessions = [
        "session_01",
        "session_02",
        "session_03"
    ]

    # 1. Run main pipeline for all sessions
    for session in sessions:
        run_command(
            f"{sys.executable} -m src.main {session}"
        )

    # 2. Run Experiment 1
    run_command(
        f"{sys.executable} tests/experiment_delta_offset.py"
    )

    # 3. Run Experiment 2
    run_command(
        f"{sys.executable} tests/experiment_signal_comparison.py"
    )

    # 4. Collect results
    run_command(
        f"{sys.executable} tests/collect_delta_experiment.py"
    )

    run_command(
        f"{sys.executable} tests/collect_signal_experiment.py"
    )

    run_command(
        f"{sys.executable} tests/collect_all_experiments.py"
    )

    print("\nALL PIPELINES AND EXPERIMENTS COMPLETED SUCCESSFULLY.")


if __name__ == "__main__":
    main()