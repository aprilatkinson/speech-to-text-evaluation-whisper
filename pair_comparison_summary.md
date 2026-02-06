# Whisper STT Comparison Summary (Individual Analysis) – Lab M1.08

## Participant
- Student: April Atkinson

## Test Audio Characteristics
- Duration: 86 seconds
- Speaking style: Structured professional speech
- Number of speakers: Single speaker
- Background noise: Minimal
- Recording quality: Clear microphone input

## Accuracy Results
- Word Error Rate (WER): 6.67%
- Accuracy: 93.33%
- Substitutions: 2
- Insertions: 7
- Deletions: 1

## Simulated Comparison Analysis
Since this evaluation was conducted individually, performance differences are analyzed based on expected variations commonly observed in speech recognition systems.

Based on Whisper documentation and observed results, the following factors are likely to affect transcription accuracy:

- **Accent variation:** Strong regional accents typically increase substitution errors.
- **Speaking pace:** Faster speech increases deletion errors due to word boundary ambiguity.
- **Background noise:** Environmental noise increases insertions and substitutions.
- **Multi-speaker conversations:** Speaker overlap generally increases WER compared to single-speaker recordings.
- **Domain terminology:** Specialized vocabulary may increase substitution rates.

## Performance Insights
The evaluated audio represents a best-case scenario (clear audio, single speaker, structured speech). The achieved WER of 6.67% suggests Whisper performs well under controlled meeting conditions.

In real-world deployment, accuracy may decrease when:
- multiple speakers overlap,
- audio quality varies,
- informal or conversational speech is used.

## Recommendations
- Whisper is suitable for meeting transcription where minor inaccuracies are acceptable.
- Organizations should evaluate performance across:
  - multiple speakers,
  - different accents,
  - lower-quality recordings,
  before full-scale deployment.
- Implement human review for high-stakes or externally distributed transcripts.
