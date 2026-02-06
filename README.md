# Speech-to-Text Evaluation Pipeline (Whisper)
This project implements an end-to-end evaluation pipeline for AI speech-to-text systems using OpenAI Whisper. The workflow evaluates transcription accuracy using Word Error Rate (WER), compares model output against human-verified ground truth, and analyzes cost-performance tradeoffs for production deployment scenarios.

The project demonstrates a practical evaluation approach used when assessing AI services prior to large-scale adoption, combining accuracy measurement, cost estimation, and deployment recommendations.

## Project Structure

- `whisper_evaluation.py` – Whisper transcription and WER evaluation
- `cost_analysis.py` – Cost estimation and usage scenarios
- `evaluation_report.md` – Accuracy and performance analysis
- `pair_comparison_summary.md` – Comparative evaluation analysis
- `ground_truth.txt` – Human-verified transcription
- `*.json` – Generated evaluation outputs
