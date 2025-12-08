from app2.xp_system import calculate_level_stats

def test_linear_formula():
    print("--- Testing Linear Level Formula: Level = (XP // 100) + 1 ---")
    
    test_cases = [
        0,    # Level 1
        50,   # Level 1
        90,   # Level 1
        100,  # Level 2 (Boundary)
        110,  # Level 2
        190,  # Level 2
        200,  # Level 3 (Boundary)
        990,  # Level 10
        1000  # Level 11
    ]
    
    for xp in test_cases:
        stats = calculate_level_stats(xp)
        level = stats['current_level']
        print(f"XP: {xp:4} -> Level: {level} | Next Level at: {stats['xp_target_next_level']}")

if __name__ == "__main__":
    test_linear_formula()
