# Whisper STT Evaluation Report (Lab M1.08)

## 1) Test Setup
- Audio file: `april_whisper_test.m4a`
- Duration: 86.015 seconds (1.434 minutes)
- Environment: Local Python script using OpenAI Whisper transcription API
- Evaluation metric: Word Error Rate (WER) using `jiwer`
- Ground truth: Human-verified transcript stored in `ground_truth.txt`

## 2) Whisper Transcription Output (Summary)
Whisper successfully produced a full transcription with strong overall readability and correct intent.
Notable observation: Whisper included an extra intro line (“Hi, my name is April Atkinson.”) which may not be present in the ground truth depending on what was actually spoken.

Files saved:
- `whisper_transcription.json` (model output)

## 3) Accuracy Results (WER)
**WER:** 0.0667 (6.67%)  
**Accuracy:** 0.9333 (93.33%)

Error breakdown:
- Substitutions: 2
- Insertions: 7
- Deletions: 1
- Correct words (hits): 147
- Reference words: 150
- Hypothesis words: 156

File saved:
- `wer_results.json` (WER metrics)

## 4) Cost Analysis
Pricing model: cost per minute of audio processed.

Single file estimate:
- 1.434 minutes → **$0.0086** (at $0.006/min)

Monthly scenarios:
- 10 hours/month → **$3.60/month**
- 50 hours/month → **$18.00/month**
- 100 hours/month → **$36.00/month**
- 300 hours/month → **$108.00/month**

File saved:
- `cost_analysis.json` (cost metrics)

## 5) Performance Insights
- Whisper achieved high accuracy on clean speech with minimal background noise.
- Most observed errors were insertions rather than substitutions, suggesting occasional over-generation or filler additions.
- For meeting transcription use cases, this level of accuracy is generally acceptable, but higher-stakes use (legal/medical) would require stricter QA.

## 6) Recommendations
- **Deploy recommendation:** Yes, Whisper is suitable for meeting transcription in this tested condition (clean single-speaker audio).
- **Quality controls recommended:**
  - Establish a review workflow for high-importance meetings (spot-check or human QA on critical segments).
  - Track WER across multiple speakers and audio conditions before scaling.
- **Cost recommendation:** Whisper is cost-effective at the tested pricing; even at 300 hours/month estimated cost remains relatively low.

## 7) Next Steps (Pair Work)
- Compare results with partner across a different voice/accent/audio quality sample.
- Document patterns:
  - Does WER increase with accents or faster speech?
  - Are errors mainly insertions or substitutions?
  - Any consistent failure modes (names, acronyms, domain terms)?
