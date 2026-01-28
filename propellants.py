# propellants.py
# Clean propellant database - NO ERRORS

PROPELLANTS = {
    # LIQUIDS
    'RP-1/LOX': {'type': 'Kerosene', 'optimal_of': 2.3, 'c_star': 1800},
    'LH2/LOX': {'type': 'Hydrogen', 'optimal_of': 6.0, 'c_star': 2300},
    'Slush Hydrogen/LOX': {'type': 'Hydrogen', 'optimal_of': 6.0, 'c_star': 2350},
    'MMH/NTO': {'type': 'Hypergolic', 'optimal_of': 1.65, 'c_star': 1740},
    'UDMH/NTO': {'type': 'Hypergolic', 'optimal_of': 2.0, 'c_star': 1720},
    'Aerozine-50/NTO': {'type': 'Hypergolic', 'optimal_of': 1.9, 'c_star': 1760},
    'H2O2/Kerosene': {'type': 'Green', 'optimal_of': 7.0, 'c_star': 1600},
    'LNG/LOX': {'type': 'Methane', 'optimal_of': 3.4, 'c_star': 1850},
    'Aluminum/Ice (ALICE)': {'type': 'Experimental', 'optimal_of': 1.2, 'c_star': 1400},
    'Hydrogen Peroxide (98%)': {'type': 'Monopropellant', 'optimal_of': 0.0, 'c_star': 1200},
    'Hydrazine (N2H4)': {'type': 'Monopropellant', 'optimal_of': 0.0, 'c_star': 1300},
    
    # SOLIDS
    'HTPB/AP (Solid)': {'type': 'Solid', 'optimal_of': 0.0, 'c_star': 1580, 'burn_rate': 8.0},
    'PBAN/AP (Solid)': {'type': 'Solid', 'optimal_of': 0.0, 'c_star': 1600, 'burn_rate': 7.5},
    'Double-Base (Solid)': {'type': 'Solid', 'optimal_of': 0.0, 'c_star': 1550, 'burn_rate': 10.0},
    'APCP (Solid)': {'type': 'Solid', 'optimal_of': 0.0, 'c_star': 1620, 'burn_rate': 9.0},
    
    # HYBRIDS
    'HTPB/N2O (Hybrid)': {'type': 'Hybrid', 'optimal_of': 7.5, 'c_star': 1450, 'regression_rate': 1.2},
    'HTPB/LOX (Hybrid)': {'type': 'Hybrid', 'optimal_of': 2.4, 'c_star': 1700, 'regression_rate': 0.8},
    'Paraffin/N2O (Hybrid)': {'type': 'Hybrid', 'optimal_of': 8.0, 'c_star': 1480, 'regression_rate': 2.5},
    'PE/LOX (Hybrid)': {'type': 'Hybrid', 'optimal_of': 2.6, 'c_star': 1680, 'regression_rate': 0.7},
}

# Test the file
if __name__ == "__main__":
    print(f"✅ propellants.py: {len(PROPELLANTS)} propellants loaded")
    print("First 5:", list(PROPELLANTS.keys())[:5])
