def calculate_sales():
    total_land = 80
    segment_land = total_land / 5

    tomato_land = segment_land
    potato_land = segment_land
    cabbage_land = segment_land
    sunflower_land = segment_land
    sugarcane_land = segment_land

    tomato_yield = (0.3 * tomato_land * 10 + 0.7 * tomato_land * 12) * 1000 * 7
    potato_yield = potato_land * 10 * 1000 * 20
    cabbage_yield = cabbage_land * 14 * 1000 * 24
    sunflower_yield = sunflower_land * 0.7 * 1000 * 200
    sugarcane_yield = sugarcane_land * 45 * 4000

    total_sales = (
        tomato_yield
        + potato_yield
        + cabbage_yield
        + sunflower_yield
        + sugarcane_yield
    )

    chemical_free_sales = (
        tomato_yield
        + potato_yield
        + cabbage_yield
        + sunflower_yield
    )

    return total_sales, chemical_free_sales


def run_tests():
    print("\nRunning Test Cases...\n")

    total_sales, chemical_free_sales = calculate_sales()

    assert total_sales == 30944000.0
    assert chemical_free_sales == 25184000.0

    print(" All test cases passed successfully!")


if __name__ == "__main__":
    run_tests()

    total, chemical_free = calculate_sales()

    print("\nOverall Sales from 80 acres: Rs.", total)
    print("Sales from Chemical-Free Farming after 11 months: Rs.", chemical_free)
