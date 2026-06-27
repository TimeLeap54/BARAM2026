"""Entry point for the BARAM2026 forecasting pipeline."""


def main() -> None:
    """Run the end-to-end pipeline.

    Planned stages:
    1. raw data load
    2. schema check
    3. cutoff filtering
    4. feature engineering
    5. train/valid split
    6. model training
    7. prediction
    8. postprocess
    9. local metric scoring
    10. submission generation
    """
    raise NotImplementedError("Pipeline implementation is pending.")


if __name__ == "__main__":
    main()
