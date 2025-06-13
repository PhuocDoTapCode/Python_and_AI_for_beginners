import math

# Conditional structure example
def conditional_structure(x = 10):
    if x > 0:
        print(f"{x} is a positive number")
    elif x == 0:
        print(f"{x} is zero")
    else:
        print(f"{x} is negative number")
    
        
# Calculate Vietnamese Can-Chi calendar
def calculate_can_chi_calendar(year):
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mẹo", "Thìn", "Tỵ", "Ngọ", "Mùi"]
    can_index = (year % 10)
    chi_index = (year % 12)
    return f"{can[can_index]} {chi[chi_index]}"


# Activation function
def relu(x):
    return x if x > 0 else 0

def leaky_relu(x, alpha=0.01):
    return x if x > 0 else alpha * x

def sigmoid(x):
    return round(1 / (1 + math.exp(-x)), 4)

def tanh(x):
    return round((math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x)), 4) 

def elu(x, alpha=1.0):
    return x if x > 0 else round(alpha * (math.exp(x) - 1), 4)


# New unit test function
def run_tests():
 
    assert calculate_can_chi_calendar(2000) == "Canh Thìn"
    assert calculate_can_chi_calendar(2012) == "Nhâm Thìn"
    assert calculate_can_chi_calendar(1979) == "Kỷ Mùi"
    
    assert relu(5) == 5
    assert relu(-10) == 0
    assert relu(0.001) == 0.001
    
    assert leaky_relu(5) == 5
    assert leaky_relu(-5) == -0.05
    assert leaky_relu(0.001) == 0.001
    
    assert sigmoid(1) == 0.7311
    assert sigmoid(-1) == 0.2689
    assert sigmoid(10) == 1.0

    assert tanh(1) == 0.7616
    assert tanh(-1) == -0.7616
    assert tanh(0.5) == 0.4621

    assert elu(-2) == -0.8647
    assert elu(-0.5) == -0.3935
    assert elu(0) == 0
    print("✅ All new tests passed successfully!")

# Activation function demo
def show_demo():
    x_vals = [-1, 0, 1]
    for x in x_vals:
        print(f"x = {x}")
        print(f"ReLU: {relu(x)}")
        print(f"Leaky ReLU: {leaky_relu(x)}")
        print(f"Sigmoid: {sigmoid(x)}")
        print(f"Tanh: {tanh(x)}")
        print(f"ELU: {elu(x)}")
        print("-" * 30)

# Main program
def main():
    print("\n\t\t------Start the program------\n")
    
    print("🔹 Conditional Structure Example:")
    conditional_structure(-5)
    
    print("\n🔹 Vietnamese Can-Chi Calendar:")
    for year in [1997, 2024, 2025]:
        print(f"{year} → {calculate_can_chi_calendar(year)}")
    
    print("\n🔹 Activation Function Demo:")
    show_demo()

    print("\n🔹 Running Unit Tests:")
    run_tests()
    
    print("\n\t\t------End the program------\n")


if __name__ == "__main__":
    main()