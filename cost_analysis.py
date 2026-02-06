import json

DURATION_SECONDS = 86.014667

# ✅ Set this to the price-per-minute your course wants you to use
# Example: 0.006 means $0.006 per minute
PRICE_PER_MIN_USD = 0.006
MONTHLY_HOURS_SCENARIOS = [10, 50, 100, 300]  # adjust if your lab suggests different volumes


def estimate_cost(duration_seconds: float, price_per_min_usd: float) -> dict:
    minutes = duration_seconds / 60.0
    cost = minutes * price_per_min_usd

    return {
        "duration_seconds": duration_seconds,
        "duration_minutes": minutes,
        "price_per_min_usd": price_per_min_usd,
        "estimated_cost_usd": cost,
        "estimated_cost_usd_rounded": round(cost, 6),
    }

if __name__ == "__main__":
    per_file = estimate_cost(DURATION_SECONDS, PRICE_PER_MIN_USD)

    # Monthly scenarios (cost scales linearly by minutes)
    scenarios = []
    for hours in MONTHLY_HOURS_SCENARIOS:
        minutes = hours * 60
        scenarios.append({
            "monthly_hours": hours,
            "monthly_minutes": minutes,
            "estimated_cost_usd": round(minutes * PRICE_PER_MIN_USD, 2),
        })

    result = {
        "single_file": per_file,
        "monthly_scenarios": scenarios
    }

    print("COST ANALYSIS")
    print(f"Single file: {per_file['duration_minutes']:.3f} min → ${per_file['estimated_cost_usd']:.6f}")

    print("\nMonthly scenarios:")
    for s in scenarios:
        print(f"  {s['monthly_hours']} hours/month → ${s['estimated_cost_usd']}/month")

    with open("cost_analysis.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print("\n✅ Saved to cost_analysis.json")
