import random

def simulate_tech_bubble(days=100, initial_intrinsic_value=10.0, intrinsic_growth_rate=0.01,
                         speculation_start_day=20, speculation_intensity=0.04,
                         burst_threshold_factor=2.0, burst_chance_per_day=0.15,
                         post_burst_recovery_factor=0.05):
    """
    Simulates the price of a hypothetical tech asset over time, demonstrating
    the formation and bursting of a technology bubble.
    """
    intrinsic_value = initial_intrinsic_value
    market_price = initial_intrinsic_value * random.uniform(0.95, 1.05) # Start with slight variation
    bubble_phase = False
    burst_occurred = False
    burst_day = -1

    print(f"{'Day':<5} {'Intrinsic Value':<18} {'Market Price':<18} {'Status':<15}")
    print("-" * 56)

    for day in range(1, days + 1):
        # Intrinsic Value always grows steadily, representing the long-term value of the technology
        # (Teknolojinin uzun vadeli, gerçek değeri sürekli artar)
        intrinsic_value *= (1 + intrinsic_growth_rate)

        if not burst_occurred:
            # Phase 1: Pre-Speculation
            if day < speculation_start_day:
                # Market price tracks intrinsic value with minor fluctuations
                market_price = intrinsic_value * random.uniform(0.98, 1.02)
                status = "Pre-Speculation"
            # Phase 2: Bubble Formation
            else:
                bubble_phase = True
                # Market price is driven by speculation and herd mentality
                # It grows faster than intrinsic value, detaching from it.
                # (Piyasa fiyatı, spekülasyon ve sürü psikolojisi ile gerçek değerinden koparak hızla yükselir)
                speculative_growth = market_price * speculation_intensity * random.uniform(0.9, 1.1)
                market_price += speculative_growth
                market_price += random.uniform(-0.2, 0.2) # Small daily noise

                status = "Bubble Active"

                # Check for bubble burst condition
                # A bubble bursts if the market price is significantly higher than intrinsic value
                # and a random chance occurs.
                # (Piyasa fiyatı, gerçek değerinden çok uzaklaştığında balon patlama riski artar)
                if market_price > intrinsic_value * burst_threshold_factor:
                    if random.random() < burst_chance_per_day:
                        burst_occurred = True
                        burst_day = day
                        print(f"--- BUBBLE BURST ON DAY {day}! Market price was {market_price:.2f}, Intrinsic was {intrinsic_value:.2f} ---")
        else:
            # Phase 3: Post-Burst Crash and Recovery
            # Immediately after burst, price crashes significantly
            # (Balon patladıktan sonra piyasa fiyatı hızla düşer)
            if day == burst_day + 1: # The day after the burst
                crash_percentage = random.uniform(0.4, 0.7) # Lose 40-70% of its value
                market_price *= (1 - crash_percentage)
                if market_price < intrinsic_value * 0.5: # Ensure it doesn't go too low initially
                    market_price = intrinsic_value * 0.5
            else:
                # Gradual recovery/stabilization towards intrinsic value, but with volatility
                # The market price is pulled towards the intrinsic value
                # (Piyasa fiyatı, zamanla gerçek değerine doğru toparlanır veya stabilize olur)
                market_price = (market_price * (1 - post_burst_recovery_factor) +
                                intrinsic_value * post_burst_recovery_factor)
                market_price *= random.uniform(0.98, 1.02) # Add some post-burst volatility

            status = "Post-Burst Recovery"

        # Ensure market price doesn't go below zero
        if market_price < 0.1:
            market_price = 0.1

        print(f"{day:<5} {intrinsic_value:<18.2f} {market_price:<18.2f} {status:<15}")

# Run the simulation
simulate_tech_bubble()
