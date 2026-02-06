import os
import json
from openai import OpenAI
import jiwer

AUDIO_FILE = "april_whisper_test.m4a"
GROUND_TRUTH_FILE = "ground_truth.txt"
WHISPER_JSON_OUT = "whisper_transcription.json"
WER_JSON_OUT = "wer_results.json"

client = OpenAI()


def transcribe_audio(file_path: str) -> str:
    print("🎧 Transcribing audio with Whisper...")

    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=audio_file
        )

    print("✅ Transcription complete!")
    return transcription.text


def load_text_file(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing file: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


def calculate_wer(reference: str, hypothesis: str) -> dict:
    """
    WER = (Substitutions + Insertions + Deletions) / Total reference words
    """

    transform = jiwer.Compose([
        jiwer.ToLowerCase(),
        jiwer.RemovePunctuation(),
        jiwer.RemoveMultipleSpaces(),
        jiwer.Strip(),
    ])

    reference_clean = transform(reference)
    hypothesis_clean = transform(hypothesis)

    # jiwer 4.x method
    output = jiwer.process_words(reference_clean, hypothesis_clean)

    wer = output.wer

    return {
        "wer": wer,
        "accuracy": 1 - wer,
        "substitutions": output.substitutions,
        "insertions": output.insertions,
        "deletions": output.deletions,
        "hits": output.hits,
        "reference_words": len(reference_clean.split()),
        "hypothesis_words": len(hypothesis_clean.split()),
    }


if __name__ == "__main__":

    # 1️⃣ Check files exist
    if not os.path.exists(AUDIO_FILE):
        raise FileNotFoundError(f"Audio file not found: {AUDIO_FILE}")

    ground_truth_text = load_text_file(GROUND_TRUTH_FILE)

    # 2️⃣ Transcribe with Whisper
    whisper_text = transcribe_audio(AUDIO_FILE)

    print("\n--- WHISPER TRANSCRIPTION ---")
    print(whisper_text)

    with open(WHISPER_JSON_OUT, "w", encoding="utf-8") as f:
        json.dump({"text": whisper_text}, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Saved to {WHISPER_JSON_OUT}")

    # 3️⃣ Calculate WER
    wer_results = calculate_wer(ground_truth_text, whisper_text)

    print("\n" + "=" * 50)
    print("WER EVALUATION")
    print("=" * 50)
    print(f"WER: {wer_results['wer']:.4f} ({wer_results['wer']*100:.2f}%)")
    print(f"Accuracy: {wer_results['accuracy']:.4f} ({wer_results['accuracy']*100:.2f}%)")

    print("\nError breakdown:")
    print(f"  Substitutions: {wer_results['substitutions']}")
    print(f"  Insertions:    {wer_results['insertions']}")
    print(f"  Deletions:     {wer_results['deletions']}")
    print(f"  Correct words: {wer_results['hits']}")

    print("\nWord counts:")
    print(f"  Reference words:  {wer_results['reference_words']}")
    print(f"  Hypothesis words: {wer_results['hypothesis_words']}")

    with open(WER_JSON_OUT, "w", encoding="utf-8") as f:
        json.dump(wer_results, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Saved to {WER_JSON_OUT}")
