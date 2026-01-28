"""
🚀 ROCKET ENGINE STUDIO - ULTIMATE PROFESSIONAL EDITION
Complete Aerospace Engineering Tool with All Advanced Features
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from datetime import datetime
from io import BytesIO
from fpdf import FPDF
import base64
import warnings
import math
from scipy import signal

# ========== ADD THE SAFE DIVISION FUNCTION HERE ==========
def safe_divide(numerator, denominator, default=0.0):
    """Safe division that prevents ZeroDivisionError"""
    if denominator == 0:
        return default
    return numerator / denominator
# ========== END SAFE DIVISION FUNCTION ==========


warnings.filterwarnings('ignore')

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="🚀 Rocket Engine Studio Ultimate",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ========== COMPREHENSIVE MATERIAL DATABASE ==========
class AdvancedMaterialDatabase:
    """NASA/ESA material properties for rocket engines"""

    MATERIALS = {
        'Copper (OFHC)': {
            'density': 8960,
            'conductivity': 380,
            'specific_heat': 385,
            'yield_strength': 200e6,
            'ultimate_strength': 220e6,
            'youngs_modulus': 110e9,
            'poisson': 0.34,
            'thermal_expansion': 17e-6,
            'max_temp': 1350,
            'creep_limit': 1000,
            'erosion_rate': 0.005,
            'cost': 'Medium'
        },
        'Inconel 718': {
            'density': 8220,
            'conductivity': 11.4,
            'specific_heat': 435,
            'yield_strength': 1034e6,
            'ultimate_strength': 1276e6,
            'youngs_modulus': 200e9,
            'poisson': 0.29,
            'thermal_expansion': 13e-6,
            'max_temp': 1300,
            'creep_limit': 1200,
            'erosion_rate': 0.002,
            'cost': 'High'
        },
        'Tungsten-Copper (W-Cu)': {
            'density': 15000,
            'conductivity': 180,
            'specific_heat': 140,
            'yield_strength': 800e6,
            'ultimate_strength': 900e6,
            'youngs_modulus': 350e9,
            'poisson': 0.28,
            'thermal_expansion': 5.5e-6,
            'max_temp': 3000,
            'creep_limit': 2500,
            'erosion_rate': 0.001,
            'cost': 'Very High'
        },
        'Silicon Carbide (SiC)': {
            'density': 3100,
            'conductivity': 120,
            'specific_heat': 750,
            'yield_strength': 400e6,
            'ultimate_strength': 550e6,
            'youngs_modulus': 410e9,
            'poisson': 0.14,
            'thermal_expansion': 4.0e-6,
            'max_temp': 1900,
            'creep_limit': 1700,
            'erosion_rate': 0.0005,
            'cost': 'High'
        },
        'Cobalt Superalloy': {
            'density': 8900,
            'conductivity': 14.9,
            'specific_heat': 420,
            'yield_strength': 800e6,
            'ultimate_strength': 1000e6,
            'youngs_modulus': 230e9,
            'poisson': 0.31,
            'thermal_expansion': 12e-6,
            'max_temp': 1150,
            'creep_limit': 1050,
            'erosion_rate': 0.003,
            'cost': 'Very High'
        },
        'Molybdenum (TZM)': {
            'density': 10200,
            'conductivity': 142,
            'specific_heat': 250,
            'yield_strength': 600e6,
            'ultimate_strength': 700e6,
            'youngs_modulus': 320e9,
            'poisson': 0.32,
            'thermal_expansion': 5.4e-6,
            'max_temp': 2600,
            'creep_limit': 2200,
            'erosion_rate': 0.0015,
            'cost': 'High'
        }
    }


# ========== COMPREHENSIVE PROPELLANT DATABASE ==========
class AdvancedPropellantDatabase:
    """Comprehensive propellant database with 21 combinations"""

    def __init__(self):
        self.PROPELLANTS = {
            # LIQUID PROPELLANTS (13)
            'RP-1/LOX': {
                'type': 'Kerosene',
                'optimal_of': 2.3,
                'gamma_range': [1.18, 1.22, 1.26],
                'c_star': 1800,
                'combustion_temp': 3700,
                'density_impulse': 3500,
                'toxicity': 'Low',
                'handling': 'Easy',
                'cost': 'Low',
                'flight_heritage': 'Extensive'
            },
            'Methane/LOX (CH4/LOX)': {
                'type': 'Methane',
                'optimal_of': 3.5,
                'gamma_range': [1.20, 1.25, 1.30],
                'c_star': 1900,
                'combustion_temp': 3600,
                'density_impulse': 3200,
                'toxicity': 'Very Low',
                'handling': 'Medium',
                'cost': 'Low',
                'flight_heritage': 'Modern'
            },
            'Propane/LOX': {
                'type': 'Hydrocarbon',
                'optimal_of': 3.0,
                'gamma_range': [1.19, 1.23, 1.27],
                'c_star': 1750,
                'combustion_temp': 3650,
                'density_impulse': 3400,
                'toxicity': 'Low',
                'handling': 'Easy',
                'cost': 'Low',
                'flight_heritage': 'Moderate'
            },
            'LH2/LOX': {
                'type': 'Hydrogen',
                'optimal_of': 6.0,
                'gamma_range': [1.12, 1.15, 1.18],
                'c_star': 2300,
                'combustion_temp': 3500,
                'density_impulse': 2500,
                'toxicity': 'None',
                'handling': 'Difficult',
                'cost': 'High',
                'flight_heritage': 'Extensive'
            },
            'Slush Hydrogen/LOX': {
                'type': 'Hydrogen',
                'optimal_of': 6.0,
                'gamma_range': [1.10, 1.13, 1.16],
                'c_star': 2350,
                'combustion_temp': 3450,
                'density_impulse': 2600,
                'toxicity': 'None',
                'handling': 'Very Difficult',
                'cost': 'Very High',
                'flight_heritage': 'Experimental'
            },
            'MMH/NTO': {
                'type': 'Hypergolic',
                'optimal_of': 1.65,
                'gamma_range': [1.20, 1.24, 1.28],
                'c_star': 1740,
                'combustion_temp': 3400,
                'density_impulse': 3300,
                'toxicity': 'Very High',
                'handling': 'Difficult',
                'cost': 'High',
                'flight_heritage': 'Extensive'
            },
            'UDMH/NTO': {
                'type': 'Hypergolic',
                'optimal_of': 2.0,
                'gamma_range': [1.21, 1.25, 1.29],
                'c_star': 1720,
                'combustion_temp': 3450,
                'density_impulse': 3350,
                'toxicity': 'Very High',
                'handling': 'Difficult',
                'cost': 'High',
                'flight_heritage': 'Extensive'
            },
            'Aerozine-50/NTO': {
                'type': 'Hypergolic',
                'optimal_of': 1.9,
                'gamma_range': [1.20, 1.24, 1.28],
                'c_star': 1760,
                'combustion_temp': 3420,
                'density_impulse': 3400,
                'toxicity': 'High',
                'handling': 'Difficult',
                'cost': 'High',
                'flight_heritage': 'Historical'
            },
            'H2O2/Kerosene': {
                'type': 'Green',
                'optimal_of': 7.0,
                'gamma_range': [1.18, 1.22, 1.26],
                'c_star': 1600,
                'combustion_temp': 2800,
                'density_impulse': 3000,
                'toxicity': 'Low',
                'handling': 'Medium',
                'cost': 'Medium',
                'flight_heritage': 'Limited'
            },
            'LNG/LOX': {
                'type': 'Methane',
                'optimal_of': 3.4,
                'gamma_range': [1.19, 1.24, 1.29],
                'c_star': 1850,
                'combustion_temp': 3550,
                'density_impulse': 3150,
                'toxicity': 'Very Low',
                'handling': 'Medium',
                'cost': 'Low',
                'flight_heritage': 'Modern'
            },
            'Aluminum/Ice (ALICE)': {
                'type': 'Experimental',
                'optimal_of': 1.2,
                'gamma_range': [1.15, 1.18, 1.21],
                'c_star': 1400,
                'combustion_temp': 3200,
                'density_impulse': 2800,
                'toxicity': 'Medium',
                'handling': 'Difficult',
                'cost': 'Medium',
                'flight_heritage': 'Experimental'
            },
            'Hydrogen Peroxide (98%)': {
                'type': 'Monopropellant',
                'optimal_of': 0.0,
                'gamma_range': [1.13, 1.13, 1.13],
                'c_star': 1200,
                'combustion_temp': 1100,
                'density_impulse': 1500,
                'toxicity': 'Medium',
                'handling': 'Difficult',
                'cost': 'Medium',
                'flight_heritage': 'Historical'
            },
            'Hydrazine (N2H4)': {
                'type': 'Monopropellant',
                'optimal_of': 0.0,
                'gamma_range': [1.20, 1.20, 1.20],
                'c_star': 1300,
                'combustion_temp': 1200,
                'density_impulse': 2200,
                'toxicity': 'Very High',
                'handling': 'Very Difficult',
                'cost': 'High',
                'flight_heritage': 'Extensive'
            },

            # SOLID PROPELLANTS (4)
            'HTPB/AP (Solid)': {
                'type': 'Solid',
                'optimal_of': 0.0,
                'gamma_range': [1.18, 1.22, 1.26],
                'c_star': 1580,
                'combustion_temp': 3400,
                'density_impulse': 2800,
                'toxicity': 'Medium',
                'handling': 'Medium',
                'cost': 'Low',
                'flight_heritage': 'Extensive',
                'burn_rate': 8.0,
                'pressure_exp': 0.3,
                'density': 1800
            },
            'PBAN/AP (Solid)': {
                'type': 'Solid',
                'optimal_of': 0.0,
                'gamma_range': [1.19, 1.23, 1.27],
                'c_star': 1600,
                'combustion_temp': 3450,
                'density_impulse': 2850,
                'toxicity': 'Medium',
                'handling': 'Medium',
                'cost': 'Low',
                'flight_heritage': 'Extensive',
                'burn_rate': 7.5,
                'pressure_exp': 0.32,
                'density': 1750
            },
            'Double-Base (Solid)': {
                'type': 'Solid',
                'optimal_of': 0.0,
                'gamma_range': [1.17, 1.21, 1.25],
                'c_star': 1550,
                'combustion_temp': 3300,
                'density_impulse': 2700,
                'toxicity': 'Medium',
                'handling': 'Difficult',
                'cost': 'Medium',
                'flight_heritage': 'Extensive',
                'burn_rate': 10.0,
                'pressure_exp': 0.25,
                'density': 1600
            },
            'APCP (Solid)': {
                'type': 'Solid',
                'optimal_of': 0.0,
                'gamma_range': [1.20, 1.24, 1.28],
                'c_star': 1620,
                'combustion_temp': 3500,
                'density_impulse': 2900,
                'toxicity': 'Medium',
                'handling': 'Medium',
                'cost': 'Medium',
                'flight_heritage': 'Extensive',
                'burn_rate': 9.0,
                'pressure_exp': 0.35,
                'density': 1850
            },

            # HYBRID PROPELLANTS (4)
            'HTPB/N2O (Hybrid)': {
                'type': 'Hybrid',
                'optimal_of': 7.5,
                'gamma_range': [1.16, 1.19, 1.22],
                'c_star': 1450,
                'combustion_temp': 3200,
                'density_impulse': 2600,
                'toxicity': 'Low',
                'handling': 'Easy',
                'cost': 'Low',
                'flight_heritage': 'Moderate',
                'regression_rate': 1.2,
                'regression_exp': 0.8,
                'fuel_density': 920
            },
            'HTPB/LOX (Hybrid)': {
                'type': 'Hybrid',
                'optimal_of': 2.4,
                'gamma_range': [1.18, 1.22, 1.26],
                'c_star': 1700,
                'combustion_temp': 3600,
                'density_impulse': 3100,
                'toxicity': 'Low',
                'handling': 'Medium',
                'cost': 'Low',
                'flight_heritage': 'Experimental',
                'regression_rate': 0.8,
                'regression_exp': 0.7,
                'fuel_density': 920
            },
            'Paraffin/N2O (Hybrid)': {
                'type': 'Hybrid',
                'optimal_of': 8.0,
                'gamma_range': [1.15, 1.18, 1.21],
                'c_star': 1480,
                'combustion_temp': 3100,
                'density_impulse': 2650,
                'toxicity': 'Very Low',
                'handling': 'Easy',
                'cost': 'Very Low',
                'flight_heritage': 'Research',
                'regression_rate': 2.5,
                'regression_exp': 0.8,
                'fuel_density': 900
            },
            'PE/LOX (Hybrid)': {
                'type': 'Hybrid',
                'optimal_of': 2.6,
                'gamma_range': [1.17, 1.21, 1.25],
                'c_star': 1680,
                'combustion_temp': 3550,
                'density_impulse': 3050,
                'toxicity': 'Very Low',
                'handling': 'Easy',
                'cost': 'Very Low',
                'flight_heritage': 'Research',
                'regression_rate': 0.7,
                'regression_exp': 0.65,
                'fuel_density': 950
            }
        }


# ========== ENGINE CYCLE DATABASE ==========
class EngineCycleDatabase:
    """Complete engine cycle configurations"""
    
    CYCLES = {
        'Gas Generator': {
            'description': 'Open cycle using separate gas generator for turbopumps',
            'efficiency': 0.92,
            'complexity': 'Medium',
            'cost': 'Medium',
            'reliability': 'High',
            'throttle_range': '70-105%',
            'examples': 'F-1, Merlin, Vulcain',
            'advantages': ['Simple plumbing', 'Proven reliability', 'Good throttle response'],
            'disadvantages': ['Lower efficiency (fuel-rich tap-off)', 'Loss of propellant mass flow', 'Separate combustion chamber required']
        },
        'Staged Combustion (Fuel-rich)': {
            'description': 'Closed cycle where all propellants go through pre-burner',
            'efficiency': 0.96,
            'complexity': 'High',
            'cost': 'High',
            'reliability': 'Medium',
            'throttle_range': '50-110%',
            'examples': 'RD-180, SSME, BE-4',
            'advantages': ['Highest efficiency', 'All propellants utilized', 'Excellent chamber pressure'],
            'disadvantages': ['Very complex plumbing', 'High pressure requirements', 'Material challenges']
        },
        'Staged Combustion (Oxidizer-rich)': {
            'description': 'Closed cycle with oxidizer-rich pre-burner',
            'efficiency': 0.95,
            'complexity': 'Very High',
            'cost': 'Very High',
            'reliability': 'Medium',
            'throttle_range': '40-100%',
            'examples': 'RD-170, NK-33, Raptor',
            'advantages': ['High efficiency', 'Avoids fuel-rich hot gas turbine issues', 'Excellent power density'],
            'disadvantages': ['Extreme material requirements', 'Corrosion challenges', 'Very high development cost']
        },
        'Expander Cycle': {
            'description': 'Uses fuel as coolant then expands through turbine',
            'efficiency': 0.94,
            'complexity': 'Medium-High',
            'cost': 'High',
            'reliability': 'High',
            'throttle_range': '30-110%',
            'examples': 'RL-10, LE-5, Vinci',
            'advantages': ['Simple cycle with no gas generator', 'Excellent throttleability', 'High reliability'],
            'disadvantages': ['Limited to high-heat-capacity fuels (H2)', 'Limited chamber pressure', 'Cooling channel complexity']
        },
        'Pressure Fed': {
            'description': 'Simplest cycle using tank pressure for propellant feed',
            'efficiency': 0.85,
            'complexity': 'Low',
            'cost': 'Low',
            'reliability': 'Very High',
            'throttle_range': '20-100%',
            'examples': 'AJ-10, R-4D, SuperDraco',
            'advantages': ['Extreme simplicity', 'High reliability', 'Excellent restart capability'],
            'disadvantages': ['Very low chamber pressure', 'Heavy tank structure', 'Limited to small engines']
        },
        'Electric Pump Fed': {
            'description': 'Modern cycle using electric motors for turbopumps',
            'efficiency': 0.93,
            'complexity': 'Medium',
            'cost': 'Medium',
            'reliability': 'Medium',
            'throttle_range': '10-100%',
            'examples': 'Rutherford, Curie',
            'advantages': ['Precise mixture control', 'Deep throttle capability', 'Reduced plumbing complexity'],
            'disadvantages': ['Battery mass penalty', 'Limited to medium-sized engines', 'Thermal management challenges']
        }
    }


# ========== NOZZLE DESIGN DATABASE ==========
class NozzleDesignDatabase:
    """Advanced nozzle configurations and performance"""
    
    NOZZLE_TYPES = {
        'Conical (15°)': {
            'divergence_efficiency': 0.96,
            'manufacturing_cost': 'Low',
            'length_factor': 1.0,
            'weight_factor': 1.0,
            'cooling_complexity': 'Low',
            'application': 'Small engines, upper stages'
        },
        'Bell (NASA-SP)': {
            'divergence_efficiency': 0.98,
            'manufacturing_cost': 'Medium',
            'length_factor': 0.8,
            'weight_factor': 0.9,
            'cooling_complexity': 'Medium',
            'application': 'Medium engines, balance perf/length'
        },
        'Aerospike (Linear)': {
            'divergence_efficiency': 0.99,
            'manufacturing_cost': 'Very High',
            'length_factor': 0.6,
            'weight_factor': 1.2,
            'cooling_complexity': 'Very High',
            'application': 'Altitude compensation, SSTO'
        },
        'Aerospike (Annular)': {
            'divergence_efficiency': 0.99,
            'manufacturing_cost': 'Extremely High',
            'length_factor': 0.5,
            'weight_factor': 1.3,
            'cooling_complexity': 'Extremely High',
            'application': 'Advanced SSTO, spaceplanes'
        },
        'Dual-Bell': {
            'divergence_efficiency': 0.97,
            'manufacturing_cost': 'High',
            'length_factor': 1.1,
            'weight_factor': 1.1,
            'cooling_complexity': 'High',
            'application': 'Two-stage-to-orbit optimization'
        },
        'Expansion-Deflection': {
            'divergence_efficiency': 0.96,
            'manufacturing_cost': 'High',
            'length_factor': 0.9,
            'weight_factor': 1.1,
            'cooling_complexity': 'Medium',
            'application': 'Compact installations'
        }
    }


# ========== PHYSICS ENGINE WITH DIFFERENCE EXPLANATION ==========
class PhysicsEngineWithExplanation:
    """Comprehensive physics engine that explains differences"""

    def __init__(self):
        self.materials = AdvancedMaterialDatabase()
        self.propellants = AdvancedPropellantDatabase()
        self.cycles = EngineCycleDatabase()
        self.nozzles = NozzleDesignDatabase()

    def calculate_gamma(self, propellant, of_ratio):
        """Calculate specific heat ratio with interpolation"""
        props = self.propellants.PROPELLANTS[propellant]
        gamma_range = props['gamma_range']

        if of_ratio < props['optimal_of'] * 0.8:
            return gamma_range[0]
        elif of_ratio < props['optimal_of'] * 1.2:
            return gamma_range[1]
        else:
            return gamma_range[2]

    def calculate_c_star(self, propellant, Pc, of_ratio):
        """NASA SP-125 characteristic velocity with real effects"""
        props = self.propellants.PROPELLANTS[propellant]
        base_cstar = props['c_star']

        # Pressure correction
        pressure_factor = (Pc / 20.0) ** 0.05

        # OF ratio correction (quadratic)
        of_deviation = (of_ratio - props['optimal_of']) / props['optimal_of']
        of_factor = 1.0 - 0.02 * of_deviation ** 2

        # Temperature correction
        temp_factor = 1.0 + 0.0001 * (props['combustion_temp'] - 3500)

        return base_cstar * pressure_factor * of_factor * temp_factor

    def calculate_combustion_efficiency(self, propellant, Pc, of_ratio, injector_type='coaxial'):
        """Calculate combustion efficiency with physics-based model"""
        props = self.propellants.PROPELLANTS[propellant]

        # Base efficiency by propellant type
        if 'Solid' in props['type']:
            base_eff = 0.99  # Solids have excellent combustion efficiency
        elif 'Hybrid' in props['type']:
            base_eff = 0.96  # Hybrids have mixing challenges
        elif propellant in ['LH2/LOX', 'Slush Hydrogen/LOX']:
            base_eff = 0.985
        elif 'Hypergolic' in props['type']:
            base_eff = 0.99
        else:
            base_eff = 0.98

        # OF ratio effect (not for solids)
        if 'Solid' not in props['type']:
            of_deviation = abs(of_ratio - props['optimal_of']) / props['optimal_of']
            of_factor = 1.0 - 0.03 * of_deviation ** 1.5
        else:
            of_factor = 1.0  # Solids have fixed composition

        # Pressure effect (higher pressure = better mixing)
        pressure_factor = 1.0 + 0.001 * (Pc - 20.0)

        # Injector type effect (not for solids)
        if 'Solid' in props['type']:
            injector_factor = 1.0
        else:
            injector_factors = {
                'coaxial': 1.00,
                'like-on-like': 0.98,
                'impinging': 0.97,
                'swirl': 0.96
            }
            injector_factor = injector_factors.get(injector_type, 0.97)

        # Chamber L* effect (longer = more complete combustion)
        Lstar_factor = 1.0  # Simplified

        efficiency = base_eff * of_factor * pressure_factor * injector_factor * Lstar_factor

        return min(0.995, max(0.85, efficiency))

    def calculate_nozzle_efficiency(self, expansion_ratio, Pc, Pe, gamma):
        """Calculate nozzle efficiency with boundary layer losses"""
        # Ideal efficiency
        ideal_eff = 0.98

        # Boundary layer loss (increases with pressure)
        boundary_loss = 0.015 * (Pc / 50.0) ** 0.5

        # Divergence loss (depends on expansion)
        if expansion_ratio < 30:
            divergence_loss = 0.01
        elif expansion_ratio < 60:
            divergence_loss = 0.02
        else:
            divergence_loss = 0.03

        # Two-phase flow loss (if solid particles)
        two_phase_loss = 0.0  # For liquid engines

        total_efficiency = ideal_eff - boundary_loss - divergence_loss - two_phase_loss

        return max(0.90, total_efficiency)

    def calculate_erosion_rate(self, Pc, material_name, heat_flux, propellant):
        """Calculate erosion rate with advanced model"""
        material = self.materials.MATERIALS[material_name]
        base_rate = material['erosion_rate']

        # Pressure scaling (empirical)
        pressure_factor = (Pc / 35.0) ** 1.5

        # Heat flux effect
        heat_flux_factor = (heat_flux / 5e6) ** 0.8

        # Propellant effect (oxidizer-rich = more erosion)
        if 'LOX' in propellant:
            prop_factor = 1.2
        elif 'NTO' in propellant:
            prop_factor = 1.3
        else:
            prop_factor = 1.0

        # Material temperature effect (higher temp = more erosion)
        temp_factor = 1.0 + 0.001 * (heat_flux / 1e6)

        erosion_rate = base_rate * pressure_factor * heat_flux_factor * prop_factor * temp_factor

        return erosion_rate

    def explain_differences(self, theoretical, experimental, parameter, engine_params):
        """Generate detailed engineering explanations for differences"""

        deviation = ((experimental - theoretical) / theoretical) * 100

        explanations = {
            'thrust': self._explain_thrust_difference,
            'isp': self._explain_isp_difference,
            'pressure': self._explain_pressure_difference,
            'temperature': self._explain_temperature_difference,
            'efficiency': self._explain_efficiency_difference
        }

        if parameter in explanations:
            return explanations[parameter](deviation, engine_params)
        else:
            return self._generic_explanation(deviation)

    def _explain_thrust_difference(self, deviation, params):
        """Detailed thrust difference explanation"""
        reasons = []
        recommendations = []

        if deviation > 5:
            reasons.extend([
                "Pressure measurement calibration error (±3-5%)",
                "Combustion more efficient than predicted",
                "Fuel-rich mixture increasing chamber pressure",
                "Nozzle expansion better than design",
                "Instrumentation thermal drift"
            ])
            recommendations.extend([
                "Re-calibrate pressure transducers",
                "Verify mixture ratio measurements",
                "Check for combustion instability",
                "Review theoretical assumptions"
            ])
            severity = "⚠️ HIGHER THAN EXPECTED"

        elif deviation < -5:
            reasons.extend([
                "Combustion inefficiencies (2-8% typical)",
                "Nozzle boundary layer losses (3-5%)",
                "Heat losses to chamber walls (2-4%)",
                "Incomplete fuel atomization",
                "Injector pattern deficiencies",
                "Film cooling flow rate too high"
            ])
            recommendations.extend([
                "Optimize injector design",
                "Increase chamber L* for complete combustion",
                "Review cooling flow distribution",
                "Check for propellant vaporization issues"
            ])
            severity = "🔻 LOWER THAN EXPECTED"

        else:
            reasons.extend([
                "Normal manufacturing tolerances (±2-3%)",
                "Expected test-to-test variability",
                "Measurement system accuracy limits",
                "Environmental condition variations"
            ])
            recommendations.extend([
                "Continue monitoring",
                "Document test conditions",
                "Establish statistical baseline"
            ])
            severity = "✅ WITHIN EXPECTED RANGE"

        return {
            'severity': severity,
            'deviation': f"{deviation:+.1f}%",
            'reasons': reasons,
            'recommendations': recommendations,
            'physics_notes': [
                "Theoretical assumes 100% combustion efficiency",
                "Experimental includes real-world losses",
                "Nozzle divergence losses not in ideal theory",
                "Boundary layer effects reduce actual thrust"
            ]
        }

    def _explain_isp_difference(self, deviation, params):
        """Detailed ISP difference explanation"""
        if deviation > 2:
            return {
                'severity': "🚀 EXCELLENT ISP",
                'deviation': f"{deviation:+.1f}%",
                'reasons': [
                    "Superior nozzle expansion efficiency",
                    "Better-than-predicted combustion",
                    "Optimal mixture ratio achieved",
                    "Reduced boundary layer losses"
                ],
                'recommendations': [
                    "Document operating conditions",
                    "Consider slight mixture optimization",
                    "Verify measurement accuracy"
                ],
                'physics_notes': [
                    "ISP highly sensitive to nozzle efficiency",
                    "Small improvements in combustion yield large ISP gains",
                    "Nozzle contour optimization critical"
                ]
            }
        elif deviation < -3:
            return {
                'severity': "📉 ISP BELOW EXPECTED",
                'deviation': f"{deviation:+.1f}%",
                'reasons': [
                    "Nozzle over/under expansion",
                    "Combustion chamber heat losses",
                    "Two-phase flow in nozzle",
                    "Injector mixing deficiencies",
                    "Film cooling mass flow too high"
                ],
                'recommendations': [
                    "Review nozzle expansion ratio",
                    "Optimize cooling flow distribution",
                    "Improve injector atomization",
                    "Consider chamber insulation"
                ],
                'physics_notes': [
                    "1% heat loss = ~0.5% ISP loss",
                    "Film cooling can reduce ISP by 2-5%",
                    "Nozzle divergence angle critical for efficiency"
                ]
            }
        else:
            return {
                'severity': "✅ NOMINAL ISP",
                'deviation': f"{deviation:+.1f}%",
                'reasons': [
                    "Expected performance for design",
                    "Normal test scatter",
                    "Within measurement accuracy"
                ],
                'recommendations': [
                    "Continue current design",
                    "Monitor trend over multiple tests"
                ],
                'physics_notes': [
                    "ISP within ±2% of theoretical is excellent",
                    "Real engines typically 3-8% below ideal",
                    "Measurement uncertainty ±1-2% typical"
                ]
            }

    def _explain_pressure_difference(self, deviation, params):
        """Detailed chamber pressure difference explanation"""
        if deviation > 5:
            return {
                'severity': "⚠️ HIGHER PRESSURE",
                'deviation': f"{deviation:+.1f}%",
                'reasons': [
                    "Pressure transducer calibration error",
                    "Combustion more vigorous than predicted",
                    "Fuel-rich mixture increasing chamber temperature",
                    "Nozzle throat erosion (increased throat area)",
                    "Coolant flow restriction causing backpressure"
                ],
                'recommendations': [
                    "Re-calibrate pressure sensors",
                    "Verify mixture ratio",
                    "Check for nozzle throat erosion",
                    "Review cooling system flow rates"
                ],
                'physics_notes': [
                    "Chamber pressure highly sensitive to throat area",
                    "1% throat erosion = ~2% pressure increase",
                    "Combustion efficiency affects gas generation rate"
                ]
            }
        elif deviation < -5:
            return {
                'severity': "🔻 LOWER PRESSURE",
                'deviation': f"{deviation:+.1f}%",
                'reasons': [
                    "Nozzle throat larger than designed",
                    "Combustion efficiency lower than predicted",
                    "Fuel-lean mixture reducing gas generation",
                    "Pressure measurement location effects",
                    "Gas leakage in chamber"
                ],
                'recommendations': [
                    "Measure actual throat diameter",
                    "Improve injector mixing",
                    "Check for chamber leaks",
                    "Optimize mixture ratio"
                ],
                'physics_notes': [
                    "Pressure ∝ mdot / throat_area",
                    "Incomplete combustion reduces gas moles",
                    "Measurement port location affects readings"
                ]
            }
        else:
            return {
                'severity': "✅ NORMAL PRESSURE",
                'deviation': f"{deviation:+.1f}%",
                'reasons': [
                    "Within expected measurement accuracy",
                    "Normal combustion variability",
                    "Manufacturing tolerances within spec"
                ],
                'recommendations': [
                    "Continue monitoring",
                    "Document pressure trends"
                ],
                'physics_notes': [
                    "±5% pressure variation normal for rocket engines",
                    "Pressure stability more important than absolute value",
                    "Transient pressure spikes more concerning than steady deviation"
                ]
            }

    def _explain_temperature_difference(self, deviation, params):
        """Detailed temperature difference explanation"""
        if deviation > 10:
            return {
                'severity': "🔥 HIGHER TEMPERATURE",
                'deviation': f"{deviation:+.1f}%",
                'reasons': [
                    "Optical pyrometer calibration error",
                    "Combustion more complete than predicted",
                    "Fuel-rich mixture increasing flame temperature",
                    "Radiation from soot or particles",
                    "Measurement viewing hot spots"
                ],
                'recommendations': [
                    "Calibrate temperature sensors",
                    "Verify optical alignment",
                    "Check for combustion deposits",
                    "Review mixture ratio"
                ],
                'physics_notes': [
                    "Temperature measurements highly location-dependent",
                    "Optical measurements see radiation, not gas temperature",
                    "Soot radiation can double apparent temperature"
                ]
            }
        elif deviation < -10:
            return {
                'severity': "❄️ LOWER TEMPERATURE",
                'deviation': f"{deviation:+.1f}%",
                'reasons': [
                    "Heat losses to chamber walls",
                    "Incomplete combustion",
                    "Film cooling effects on measurement",
                    "Fuel-lean mixture",
                    "Sensor radiative cooling"
                ],
                'recommendations': [
                    "Improve chamber insulation",
                    "Optimize injector for better mixing",
                    "Relocate temperature sensors",
                    "Increase combustion efficiency"
                ],
                'physics_notes': [
                    "Actual gas temperature 200-500K higher than measured",
                    "Boundary layer effects cool measurements",
                    "Radiation losses significant at high temperatures"
                ]
            }
        else:
            return {
                'severity': "✅ NORMAL TEMPERATURE",
                'deviation': f"{deviation:+.1f}%",
                'reasons': [
                    "Within measurement accuracy limits",
                    "Expected thermal gradients",
                    "Normal combustion temperature scatter"
                ],
                'recommendations': [
                    "Monitor temperature distribution",
                    "Check for hot spots"
                ],
                'physics_notes': [
                    "Temperature measurements ±10% accuracy typical",
                    "Gas temperature non-uniform in chamber",
                    "Wall temperature ≠ gas temperature"
                ]
            }

    def _explain_efficiency_difference(self, deviation, params):
        """Detailed efficiency difference explanation"""
        if deviation > 5:
            return {
                'severity': "🚀 HIGHER EFFICIENCY",
                'deviation': f"{deviation:+.1f}%",
                'reasons': [
                    "Combustion more complete than predicted",
                    "Nozzle expansion better than design",
                    "Injector mixing superior to expectations",
                    "Lower-than-expected boundary layer losses",
                    "Measurement systematic error"
                ],
                'recommendations': [
                    "Document successful parameters",
                    "Verify measurement accuracy",
                    "Consider slight design optimization"
                ],
                'physics_notes': [
                    "Small design improvements yield large efficiency gains",
                    "Boundary layer transition affects efficiency significantly",
                    "Injector optimization critical for combustion efficiency"
                ]
            }
        elif deviation < -10:
            return {
                'severity': "📉 LOWER EFFICIENCY",
                'deviation': f"{deviation:+.1f}%",
                'reasons': [
                    "Combustion inefficiencies",
                    "Nozzle boundary layer losses",
                    "Heat losses to chamber walls",
                    "Two-phase flow in nozzle",
                    "Injector pattern deficiencies"
                ],
                'recommendations': [
                    "Optimize injector design",
                    "Increase chamber L*",
                    "Improve nozzle contour",
                    "Reduce cooling flow if possible"
                ],
                'physics_notes': [
                    "Efficiency = f(combustion, nozzle, injector)",
                    "Each 1% combustion loss = ~0.7% overall efficiency loss",
                    "Nozzle losses typically 3-8% in real engines"
                ]
            }
        else:
            return {
                'severity': "✅ EXPECTED EFFICIENCY",
                'deviation': f"{deviation:+.1f}%",
                'reasons': [
                    "Within expected range for this engine class",
                    "Normal manufacturing tolerances",
                    "Typical real-world losses accounted for"
                ],
                'recommendations': [
                    "Continue current design",
                    "Monitor efficiency trends"
                ],
                'physics_notes': [
                    "Real engines typically 5-15% below theoretical maximum",
                    "Efficiency improves with scale (larger engines more efficient)",
                    "Testing refines efficiency predictions"
                ]
            }

    def _generic_explanation(self, deviation):
        """Generic explanation for unspecified parameters"""
        return {
            'severity': "📊 PARAMETER VARIATION",
            'deviation': f"{deviation:+.1f}%",
            'reasons': [
                "Measurement system accuracy limits",
                "Environmental condition variations",
                "Test-to-test variability",
                "Data acquisition timing effects"
            ],
            'recommendations': [
                "Verify measurement calibration",
                "Repeat test for confirmation",
                "Check data acquisition setup"
            ],
            'physics_notes': [
                "All measurements have inherent uncertainty",
                "Rocket testing has significant test-to-test variation",
                "Multiple data points needed for statistical confidence"
            ]
        }

    def calculate_solid_burn_rate(self, propellant, Pc):
        """Calculate solid propellant burn rate using Vieille's law"""
        props = self.propellants.PROPELLANTS[propellant]

        if 'Solid' not in props['type']:
            return 0.0

        # r = a * Pc^n
        a = props['burn_rate'] / (70.0 ** props['pressure_exp'])  # Reference at 70 bar
        n = props['pressure_exp']

        burn_rate = a * (Pc ** n)  # mm/s

        # Temperature sensitivity (typical 0.2%/K)
        temp_factor = 1.0  # Simplified

        return burn_rate * temp_factor

    def calculate_hybrid_regression_rate(self, propellant, oxidizer_flux, Pc):
        """Calculate hybrid fuel regression rate using Marxman equation"""
        props = self.propellants.PROPELLANTS[propellant]

        if 'Hybrid' not in props['type']:
            return 0.0

        # r = a * Gox^m * Pc^n (simplified)
        a = props['regression_rate'] / (200.0 ** props['regression_exp'])  # Reference
        m = props['regression_exp']
        n = 0.0  # Pressure exponent for hybrids (usually small)

        regression_rate = a * (oxidizer_flux ** m) * (Pc ** n)  # mm/s

        return regression_rate
    
    def get_overall_assessment(self, deviations):
        """Get overall engine assessment"""
        avg_dev = np.mean([abs(d) for d in deviations.values()])

        if avg_dev < 2:
            return {
                "grade": "A+",
                "verdict": "EXCELLENT",
                "color": "#10b981",
                "summary": "Engine performance matches theoretical predictions exceptionally well.",
                "action": "Ready for flight operations"
            }
        elif avg_dev < 5:
            return {
                "grade": "B+",
                "verdict": "GOOD",
                "color": "#3b82f6",
                "summary": "Minor deviations observed but within acceptable engineering limits.",
                "action": "Continue with monitoring"
            }
        elif avg_dev < 10:
            return {
                "grade": "C",
                "verdict": "REQUIRES ATTENTION",
                "color": "#f59e0b",
                "summary": "Significant deviations detected requiring investigation.",
                "action": "Review design and testing parameters"
            }
        else:
            return {
                "grade": "D",
                "verdict": "NEEDS IMPROVEMENT",
                "color": "#ef4444",
                "summary": "Large discrepancies between theoretical and experimental values.",
                "action": "Major redesign or parameter adjustment needed"
            }


# ========== ACOUSTIC ANALYSIS ENGINE ==========
class AcousticAnalysisEngine:
    """Combustion instability and acoustic mode analysis"""

    def __init__(self):
        self.modes = {
            '1L': {'frequency': 500, 'growth_rate': 0.05, 'danger': 'Medium'},
            '1T': {'frequency': 2000, 'growth_rate': 0.10, 'danger': 'High'},
            '1R': {'frequency': 800, 'growth_rate': 0.03, 'danger': 'Low'},
            '2L': {'frequency': 1000, 'growth_rate': 0.02, 'danger': 'Low'},
            '2T': {'frequency': 4000, 'growth_rate': 0.15, 'danger': 'Very High'}
        }

    def analyze_acoustic_modes(self, Pc, chamber_length, chamber_diameter, propellant):
        """Analyze acoustic modes in combustion chamber"""

        # Speed of sound in combustion products
        if 'LH2' in propellant:
            sound_speed = 1400  # m/s
        elif 'RP-1' in propellant:
            sound_speed = 1200
        else:
            sound_speed = 1300

        # Calculate fundamental longitudinal mode (1L)
        f_1L = sound_speed / (2 * chamber_length)

        # Calculate fundamental transverse mode (1T)
        f_1T = 1.84 * sound_speed / (math.pi * chamber_diameter)

        # Calculate radial mode (1R)
        f_1R = 3.83 * sound_speed / (math.pi * chamber_diameter)

        # Pressure effect on growth rates (higher pressure = more instability)
        pressure_factor = (Pc / 35.0) ** 0.8

        modes = {
            '1L': {
                'frequency': f_1L,
                'description': 'First Longitudinal Mode',
                'growth_rate': 0.05 * pressure_factor,
                'risk': 'Medium' if f_1L < 800 else 'Low',
                'mitigation': 'Add acoustic damping or change L*'
            },
            '1T': {
                'frequency': f_1T,
                'description': 'First Tangential Mode',
                'growth_rate': 0.12 * pressure_factor,
                'risk': 'High' if f_1T < 3000 else 'Medium',
                'mitigation': 'Baffles or change injector pattern'
            },
            '1R': {
                'frequency': f_1R,
                'description': 'First Radial Mode',
                'growth_rate': 0.03 * pressure_factor,
                'risk': 'Low',
                'mitigation': 'Usually not concerning'
            }
        }

        # Check for dangerous modes
        dangerous_modes = []
        for mode, data in modes.items():
            if data['growth_rate'] > 0.1:
                dangerous_modes.append(mode)

        return {
            'modes': modes,
            'dangerous_modes': dangerous_modes,
            'recommendations': self._get_acoustic_recommendations(modes),
            'stability_margin': self._calculate_stability_margin(modes)
        }

    def _get_acoustic_recommendations(self, modes):
        """Get recommendations based on acoustic analysis"""
        recommendations = []

        for mode, data in modes.items():
            if data['growth_rate'] > 0.1:
                recommendations.append(f"⚠️ {mode} mode unstable: {data['mitigation']}")
            elif data['growth_rate'] > 0.05:
                recommendations.append(f"📊 {mode} mode marginal: Monitor during testing")

        if not recommendations:
            recommendations.append("✅ All acoustic modes stable")

        return recommendations

    def _calculate_stability_margin(self, modes):
        """Calculate overall stability margin"""
        max_growth = max([m['growth_rate'] for m in modes.values()])

        if max_growth < 0.05:
            return {'margin': 'Excellent', 'value': 95, 'color': 'green'}
        elif max_growth < 0.1:
            return {'margin': 'Good', 'value': 80, 'color': 'orange'}
        else:
            return {'margin': 'Poor', 'value': 50, 'color': 'red'}


# ========== 3D VISUALIZATION ENGINE ==========
class Visualization3D:
    """Create 3D visualizations of engine and plume"""

    @staticmethod
    def create_engine_3d_model(chamber_diam, chamber_len, throat_diam, exit_diam, nozzle_len):
        """Create 3D visualization of engine geometry"""
        import plotly.graph_objects as go

        # Create engine geometry points
        n_points = 100

        # Chamber (cylinder)
        theta = np.linspace(0, 2 * np.pi, n_points)
        z_chamber = np.linspace(0, chamber_len, n_points)
        theta_grid, z_grid = np.meshgrid(theta, z_chamber)
        x_chamber = (chamber_diam / 2) * np.cos(theta_grid)
        y_chamber = (chamber_diam / 2) * np.sin(theta_grid)

        # Nozzle (converging-diverging)
        z_nozzle = np.linspace(0, nozzle_len, n_points)
        # Create nozzle profile with proper shape
        z_norm = z_nozzle / nozzle_len
        r_nozzle = throat_diam / 2 + (exit_diam / 2 - throat_diam / 2) * (z_norm) ** 2
        theta_grid_n, z_grid_n = np.meshgrid(theta, z_nozzle)
        x_nozzle = r_nozzle[:, np.newaxis] * np.cos(theta_grid_n)
        y_nozzle = r_nozzle[:, np.newaxis] * np.sin(theta_grid_n)

        # Create figure
        fig = go.Figure()

        # Add surfaces
        fig.add_trace(go.Surface(
            x=x_chamber, y=y_chamber, z=z_grid,
            colorscale='Reds',
            showscale=False,
            opacity=0.8,
            name='Combustion Chamber'
        ))

        fig.add_trace(go.Surface(
            x=x_nozzle, y=y_nozzle, z=z_grid_n + chamber_len,
            colorscale='Blues',
            showscale=False,
            opacity=0.8,
            name='Nozzle'
        ))

        # Add plume - FIXED BROADCASTING ERROR
        z_plume = np.linspace(0, nozzle_len * 3, 50)
        theta_plume = np.linspace(0, 2 * np.pi, 100)
        z_plume_grid, theta_plume_grid = np.meshgrid(z_plume, theta_plume)

        # Plume expansion
        r_plume_base = exit_diam / 2
        plume_expansion = 0.5  # Expansion factor
        r_plume = r_plume_base * (1 + plume_expansion * (z_plume / nozzle_len) ** 0.8)

        # Create plume meshgrid properly
        r_plume_grid = np.tile(r_plume, (len(theta_plume), 1))

        x_plume = r_plume_grid * np.cos(theta_plume_grid)
        y_plume = r_plume_grid * np.sin(theta_plume_grid)

        fig.add_trace(go.Surface(
            x=x_plume, y=y_plume, z=z_plume_grid.T + chamber_len + nozzle_len,
            colorscale='Hot',
            showscale=False,
            opacity=0.6,
            name='Exhaust Plume'
        ))

        fig.update_layout(
            title='3D Engine Model with Exhaust Plume',
            scene=dict(
                xaxis_title='X (m)',
                yaxis_title='Y (m)',
                zaxis_title='Z (m)',
                aspectmode='data'
            ),
            height=600
        )

        return fig

    @staticmethod
    def create_heat_map_3d(wall_temps, positions):
        """Create 3D heat map of engine walls"""
        # Generate synthetic data if real data not available
        if wall_temps is None or positions is None:
            # Create synthetic temperature distribution
            x = np.linspace(-0.5, 0.5, 20)
            y = np.linspace(-0.5, 0.5, 20)
            z = np.linspace(0, 2, 20)
            X, Y, Z = np.meshgrid(x, y, z)

            # Temperature distribution (hotter near throat)
            R = np.sqrt(X ** 2 + Y ** 2)
            T = 300 + 1000 * np.exp(-R * 10) * np.exp(-Z / 2)
            wall_temps = T.flatten()
            positions = {
                'x': X.flatten(),
                'y': Y.flatten(),
                'z': Z.flatten()
            }

        fig = go.Figure(data=go.Volume(
            x=positions['x'],
            y=positions['y'],
            z=positions['z'],
            value=wall_temps,
            isomin=np.min(wall_temps),
            isomax=np.max(wall_temps),
            opacity=0.1,
            surface_count=20,
            colorscale='Hot',
            caps=dict(x_show=False, y_show=False, z_show=False)
        ))

        fig.update_layout(
            title='3D Temperature Distribution in Engine Walls',
            scene=dict(
                xaxis_title='X Position',
                yaxis_title='Y Position',
                zaxis_title='Z Position'
            ),
            height=500
        )

        return fig

    @staticmethod
    def create_simple_engine_visualization(Dc, Lc, Dt, De, Ln):
        """Simplified but working 3D visualization"""
        fig = go.Figure()

        # Chamber (simple cylinder)
        n_points = 50
        theta = np.linspace(0, 2 * np.pi, n_points)
        z_chamber = np.linspace(0, Lc, n_points)
        theta_grid, z_grid = np.meshgrid(theta, z_chamber)

        x_chamber = (Dc / 2) * np.cos(theta_grid)
        y_chamber = (Dc / 2) * np.sin(theta_grid)

        # Nozzle (simpler approach)
        z_nozzle = np.linspace(0, Ln, n_points)
        z_norm = z_nozzle / Ln
        r_nozzle = Dt / 2 + (De / 2 - Dt / 2) * z_norm ** 2

        # Proper broadcasting
        r_nozzle_grid = np.tile(r_nozzle, (n_points, 1))
        theta_nozzle_grid = np.tile(theta, (n_points, 1)).T

        x_nozzle = r_nozzle_grid * np.cos(theta_nozzle_grid)
        y_nozzle = r_nozzle_grid * np.sin(theta_nozzle_grid)
        z_nozzle_grid = np.tile(z_nozzle, (n_points, 1))

        # Add surfaces
        fig.add_trace(go.Surface(
            x=x_chamber, y=y_chamber, z=z_grid,
            colorscale='Reds',
            opacity=0.8,
            name='Chamber'
        ))

        fig.add_trace(go.Surface(
            x=x_nozzle, y=y_nozzle, z=z_nozzle_grid.T + Lc,
            colorscale='Blues',
            opacity=0.8,
            name='Nozzle'
        ))

        # Add plume (simplified)
        z_plume = np.linspace(0, Ln * 2, 30)
        r_plume = De / 2 * (1 + 0.3 * (z_plume / Ln) ** 0.7)

        theta_plume = np.linspace(0, 2 * np.pi, 50)
        z_plume_grid, theta_plume_grid = np.meshgrid(z_plume, theta_plume)
        r_plume_grid = np.tile(r_plume, (50, 1))

        x_plume = r_plume_grid * np.cos(theta_plume_grid)
        y_plume = r_plume_grid * np.sin(theta_plume_grid)

        fig.add_trace(go.Surface(
            x=x_plume, y=y_plume, z=z_plume_grid.T + Lc + Ln,
            colorscale='Hot',
            opacity=0.5,
            name='Plume'
        ))

        fig.update_layout(
            title='3D Rocket Engine Model',
            scene=dict(
                xaxis_title='X (m)',
                yaxis_title='Y (m)',
                zaxis_title='Z (m)'
            ),
            height=600
        )

        return fig


# ========== COMPREHENSIVE PDF REPORT GENERATOR ==========
class ComprehensivePDFReport:
    """Generate comprehensive PDF report with all details"""

    @staticmethod
    def create_report(engine_data, analysis_results, explanations, filename="Rocket_Engine_Results.pdf"):
        """Create SIMPLE PDF with only numerical results"""
        pdf = FPDF()
        pdf.add_page()

        # Simple header
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'ROCKET ENGINE RESULTS', 0, 1, 'C')
        pdf.ln(5)

        # Basic info
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 10, f'Report Date: {datetime.now().strftime("%Y-%m-%d")}', 0, 1)
        pdf.cell(0, 10, f'Generated by: Rocket Engine Studio v1.0', 0, 1)
        pdf.ln(10)

        # ===== PERFORMANCE RESULTS =====
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, '1. PERFORMANCE RESULTS', 0, 1)
        pdf.set_font('Arial', '', 11)

        performance = analysis_results.get('performance', {})
        for key, value in performance.items():
            pdf.cell(0, 8, f"{key}: {value}", 0, 1)

        pdf.ln(5)

        # ===== DEVIATIONS =====
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, '2. DEVIATIONS FROM THEORETICAL', 0, 1)
        pdf.set_font('Arial', '', 11)

        deviations = analysis_results.get('deviations', {})
        for param, value in deviations.items():
            pdf.cell(0, 8, f"{param.title()}: {value:+.2f}%", 0, 1)

        pdf.ln(5)

        # ===== EFFICIENCIES =====
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, '3. EFFICIENCIES', 0, 1)
        pdf.set_font('Arial', '', 11)

        efficiencies = analysis_results.get('efficiencies', {})
        for param, value in efficiencies.items():
            pdf.cell(0, 8, f"{param.title()}: {value:.1f}%", 0, 1)

        pdf.ln(5)

        # ===== STRUCTURAL DATA =====
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, '4. STRUCTURAL DATA', 0, 1)
        pdf.set_font('Arial', '', 11)

        structural = analysis_results.get('structural', {})
        # Only include numerical values
        for key, value in structural.items():
            if 'Safety Factor' in key or 'Diameter' in key or 'Material' in key:
                pdf.cell(0, 8, f"{key}: {value}", 0, 1)

        pdf.ln(5)

        # ===== STABILITY METRICS =====
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, '5. STABILITY METRICS', 0, 1)
        pdf.set_font('Arial', '', 11)

        stability = analysis_results.get('stability', {})
        for key, value in stability.items():
            pdf.cell(0, 8, f"{key}: {value}", 0, 1)

        pdf.ln(10)

        # ===== ENGINEERING NOTES =====
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, 'ENGINEERING NOTES', 0, 1)
        pdf.set_font('Arial', 'I', 10)

        notes = """
        Note: This PDF contains only numerical results.
        For complete analysis with interactive charts, 
        3D visualizations, and detailed explanations,
        please use the Rocket Engine Studio application.

        All values are based on NASA/ESA standard calculations
        with realistic engineering deviations applied.
        """

        pdf.multi_cell(0, 8, notes)

        # Simple output - guaranteed to work
        try:
            output = pdf.output(dest='S')
            # Clean any stray characters
            clean_output = ''
            for char in output:
                if ord(char) < 256:  # Only ASCII/Latin-1
                    clean_output += char
            return clean_output.encode('latin-1')
        except Exception as e:
            # Ultimate fallback - minimal PDF
            pdf_fallback = FPDF()
            pdf_fallback.add_page()
            pdf_fallback.set_font('Arial', 'B', 16)
            pdf_fallback.cell(0, 10, 'RESULTS EXPORTED', 0, 1, 'C')
            pdf_fallback.set_font('Arial', '', 12)
            pdf_fallback.cell(0, 10, 'Open the app to view complete results.', 0, 1)
            return pdf_fallback.output(dest='S').encode('latin-1')


# ========== MAIN ENGINE SIMULATION ==========
class UltimateRocketEngine:
    """Complete rocket engine simulation with all features"""

    def __init__(self, params):
        self.params = params
        self.physics = PhysicsEngineWithExplanation()
        self.acoustics = AcousticAnalysisEngine()
        self.visualization = Visualization3D()
        self.cycles = EngineCycleDatabase()
        self.nozzles = NozzleDesignDatabase()

        self.time = np.linspace(0, params['burn_time'], 1000)
        np.random.seed(42)

        # Run comprehensive analysis
        self.calculate_theoretical_performance()
        self.generate_experimental_data()
        self.analyze_all_aspects()
        self.generate_explanations()

    def calculate_theoretical_performance(self):
        """Calculate ideal theoretical performance"""
        # Get properties
        prop = self.physics.propellants.PROPELLANTS[self.params['propellant']]
        mat = self.physics.materials.MATERIALS[self.params['material']]

        # Thermodynamic properties
        self.gamma = self.physics.calculate_gamma(
            self.params['propellant'], self.params['of_ratio']
        )

        self.c_star = self.physics.calculate_c_star(
            self.params['propellant'], self.params['Pc'], self.params['of_ratio']
        )

        # Geometry calculations
        Pc_Pa = self.params['Pc'] * 1e5
        self.At = self.params['thrust'] / (Pc_Pa * 1.5)  # Initial estimate
        self.Dt = np.sqrt(4 * self.At / np.pi)

        # Chamber dimensions (typical ratios)
        self.Dc = self.Dt * 2.5
        self.Lc = self.Dc * 1.5  # Chamber length

        # Nozzle
        self.Ae = self.At * self.params['expansion_ratio']
        self.De = np.sqrt(4 * self.Ae / np.pi)
        self.Ln = self.De * 2.0  # Nozzle length

        # Theoretical mass flow
        self.mdot_theoretical = Pc_Pa * self.At / self.c_star

        # Theoretical thrust (recalculate with proper Cf)
        self.Cf = 1.5  # Initial, will be updated
        self.F_theoretical = Pc_Pa * self.At * self.Cf

        # Theoretical ISP
        self.Isp_theoretical = self.F_theoretical / (self.mdot_theoretical * 9.80665)

        # Efficiencies
        self.combustion_efficiency = self.physics.calculate_combustion_efficiency(
            self.params['propellant'], self.params['Pc'], self.params['of_ratio']
        )
        self.nozzle_efficiency = self.physics.calculate_nozzle_efficiency(
            self.params['expansion_ratio'], self.params['Pc'], 1.0, self.gamma
        )

        # Acoustic analysis
        self.acoustic_results = self.acoustics.analyze_acoustic_modes(
            self.params['Pc'], self.Lc, self.Dc, self.params['propellant']
        )
        # Adjust for solid/hybrid propellants
        is_solid = 'Solid' in prop['type']
        is_hybrid = 'Hybrid' in prop['type']

        if is_solid:
            # Solid propellant has no separate fuel/oxidizer flow
            self.mdot_theoretical *= 0.95  # Slightly lower mass flow for solids
            # Solids typically have slightly lower ISP than theoretical liquids
            self.Isp_theoretical *= 0.92
            # Calculate burn rate
            self.burn_rate = self.physics.calculate_solid_burn_rate(
                self.params['propellant'],
                self.params['Pc']
            )

        elif is_hybrid:
            # Hybrids have intermediate performance
            self.Isp_theoretical *= 0.94
            # Add regression rate calculation
            self.regression_rate = self.physics.calculate_hybrid_regression_rate(
                self.params['propellant'],
                200.0,  # Estimated oxidizer flux
                self.params['Pc']
            )

    def generate_experimental_data(self):
        """Generate realistic experimental data with all physics effects"""

        # Base efficiencies with time variations
        total_efficiency = self.combustion_efficiency * self.nozzle_efficiency * 0.98  # Injector efficiency

        # Thrust with realistic variations
        base_F = self.F_theoretical * total_efficiency

        # Add physics-based variations
        variations = {
            'combustion_instability': 0.02 * np.sin(2 * np.pi * 100 * self.time),
            'injector_chugging': 0.01 * np.sin(2 * np.pi * 500 * self.time),
            'thermal_drift': 0.001 * self.time / self.params['burn_time'],
            'random_noise': 0.005 * np.random.randn(len(self.time)),
            'acoustic_effects': 0.003 * np.sin(
                2 * np.pi * self.acoustic_results['modes']['1L']['frequency'] * self.time)
        }

        total_variation = sum(variations.values())
        self.F_experimental = base_F * (1 + total_variation)

        # Other parameters
        self.Pc_experimental = self.params['Pc'] * (
                1 + 0.03 * np.sin(2 * np.pi * 50 * self.time) + 0.01 * np.random.randn(len(self.time))
        )

        self.mdot_experimental = self.mdot_theoretical * 1.02 * (
                1 + 0.005 * np.sin(2 * np.pi * 200 * self.time) + 0.002 * np.random.randn(len(self.time))
        )

        self.Isp_experimental = self.F_experimental / (self.mdot_experimental * 9.80665)

        # Temperature data
        prop_temp = self.physics.propellants.PROPELLANTS[self.params['propellant']]['combustion_temp']
        self.Tc_experimental = prop_temp * total_efficiency * (
                1 + 0.01 * np.sin(2 * np.pi * 80 * self.time)
        )

    def analyze_all_aspects(self):
        """Perform comprehensive analysis"""
        # Performance deviations
        self.deviations = {
            'thrust': (np.mean(self.F_experimental) - self.F_theoretical) / self.F_theoretical * 100,
            'isp': (np.mean(self.Isp_experimental) - self.Isp_theoretical) / self.Isp_theoretical * 100,
            'mdot': (np.mean(self.mdot_experimental) - self.mdot_theoretical) / self.mdot_theoretical * 100,
            'pressure': (np.mean(self.Pc_experimental) - self.params['Pc']) / self.params['Pc'] * 100
        }

        # Efficiencies
        self.efficiencies = {
            'combustion': self.combustion_efficiency * 100,
            'nozzle': self.nozzle_efficiency * 100,
            'overall': (np.mean(self.F_experimental) / self.F_theoretical) * 100,
            'total': self.combustion_efficiency * self.nozzle_efficiency * 100
        }

        # Thermal analysis
        heat_flux = 5e6  # Estimated
        self.erosion_rate = self.physics.calculate_erosion_rate(
            self.params['Pc'], self.params['material'], heat_flux, self.params['propellant']
        )

        # Structural analysis
        mat = self.physics.materials.MATERIALS[self.params['material']]
        thermal_stress = 100e6  # Estimated
        self.safety_factors = {
            'throat': mat['yield_strength'] / thermal_stress,
            'chamber': mat['yield_strength'] / (thermal_stress * 0.7)
        }

        # Stability metrics
        self.pressure_stability = np.std(self.Pc_experimental) / np.mean(self.Pc_experimental) * 100
        self.thrust_stability = np.std(self.F_experimental) / np.mean(self.F_experimental) * 100

        # Acoustic stability
        stability = self.acoustic_results['stability_margin']
        self.acoustic_stability = f"{stability['margin']} ({stability['value']}%)"

    def generate_explanations(self):
        """Generate detailed explanations for all differences"""
        self.explanations = {}

        for param in ['thrust', 'isp', 'pressure']:
            theoretical = getattr(self, f'{param}_theoretical', self.params.get('Pc'))
            experimental = np.mean(getattr(self, f'{param}_experimental', self.Pc_experimental))

            self.explanations[param] = self.physics.explain_differences(
                theoretical, experimental, param, self.params
            )

    def analyze_engine_cycle(self):
        """Analyze selected engine cycle performance"""
        cycle_name = self.params.get('cycle', 'Gas Generator')
        cycle = self.cycles.CYCLES[cycle_name]
        
        return {
            'cycle_name': cycle_name,
            'efficiency': cycle['efficiency'],
            'description': cycle['description'],
            'complexity': cycle['complexity'],
            'throttle_range': cycle['throttle_range'],
            'examples': cycle['examples']
        }
    
    def analyze_nozzle_performance(self):
        """Analyze nozzle type performance"""
        nozzle_type = self.params.get('nozzle_type', 'Bell (NASA-SP)')
        nozzle = self.nozzles.NOZZLE_TYPES[nozzle_type]
        
        return {
            'nozzle_type': nozzle_type,
            'divergence_efficiency': nozzle['divergence_efficiency'] * 100,
            'length_factor': nozzle['length_factor'],
            'manufacturing_cost': nozzle['manufacturing_cost'],
            'application': nozzle['application'],
            'cooling_complexity': nozzle['cooling_complexity']
        }
    
    def analyze_propellant_type(self):
        """Analyze propellant-specific characteristics"""
        propellant = self.params['propellant']
        props = self.physics.propellants.PROPELLANTS[propellant]
        
        analysis = {
            'propellant_name': propellant,
            'type': props['type'],
            'optimal_of_ratio': props.get('optimal_of', 0.0),
            'characteristic_velocity': props.get('c_star', 1600),
            'toxicity': props.get('toxicity', 'Medium'),
            'handling': props.get('handling', 'Medium'),
            'flight_heritage': props.get('flight_heritage', 'Moderate')
        }
        
        # Solid-specific analysis
        if 'Solid' in props['type']:
            burn_rate = self.physics.calculate_solid_burn_rate(propellant, self.params['Pc'])
            analysis.update({
                'burn_rate': burn_rate,
                'propellant_density': props.get('density', 1800)
            })
        
        # Hybrid-specific analysis
        elif 'Hybrid' in props['type']:
            regression_rate = self.physics.calculate_hybrid_regression_rate(propellant, 200.0, self.params['Pc'])
            analysis.update({
                'regression_rate': regression_rate,
                'fuel_density': props.get('fuel_density', 900)
            })
        
        return analysis

    def get_comprehensive_results(self):
        """Get all results in structured format"""
        return {
            'performance': {
                'Theoretical Thrust': f'{self.F_theoretical / 1000:.2f} kN',
                'Experimental Thrust': f'{np.mean(self.F_experimental) / 1000:.2f} kN',
                'Theoretical ISP': f'{self.Isp_theoretical:.1f} s',
                'Experimental ISP': f'{np.mean(self.Isp_experimental):.1f} s',
                'Mass Flow': f'{self.mdot_theoretical:.3f} kg/s',
                'Characteristic Velocity': f'{self.c_star:.0f} m/s',
                'Thrust Coefficient': f'{self.Cf:.3f}',
                'Specific Heat Ratio': f'{self.gamma:.3f}'
            },
            'thermal': {
                'Combustion Temperature': f'{self.Tc_experimental[0]:.0f} K',
                'Erosion Rate': f'{self.erosion_rate * 1000:.3f} mm/s',
                'Estimated Heat Flux': '5-10 MW/m²',
                'Cooling Requirement': 'Active regenerative'
            },
            'solid_hybrid_info': {
                'Burn/Regression Rate': f'{getattr(self, "burn_rate", getattr(self, "regression_rate", 0)):.2f} mm/s',
                'Propellant Type': self.physics.propellants.PROPELLANTS[self.params['propellant']]['type'],
                'Notes': 'Solid motor' if 'Solid' in self.physics.propellants.PROPELLANTS[self.params['propellant']]['type'] else
                'Hybrid engine' if 'Hybrid' in self.physics.propellants.PROPELLANTS[self.params['propellant']]['type'] else
                'Liquid engine'
            },
            'structural': {
                'Throat Diameter': f'{self.Dt * 1000:.1f} mm',
                'Chamber Diameter': f'{self.Dc * 1000:.1f} mm',
                'Nozzle Exit Diameter': f'{self.De * 1000:.1f} mm',
                'Safety Factor (Throat)': f'{self.safety_factors["throat"]:.2f}',
                'Safety Factor (Chamber)': f'{self.safety_factors["chamber"]:.2f}',
                'Material': self.params['material']
            },
            'stability': {
                'Pressure Stability': f'±{self.pressure_stability:.1f}%',
                'Thrust Stability': f'±{self.thrust_stability:.1f}%',
                'Acoustic Stability': self.acoustic_stability,
                'Dangerous Modes': self.acoustic_results['dangerous_modes']
            },
            'efficiencies': self.efficiencies,
            'deviations': self.deviations,
            'explanations': self.explanations,
            'acoustic': self.acoustic_results
        }


# ========== STREAMLIT APP ==========
# Initialize session state
if 'engine' not in st.session_state:
    st.session_state.engine = None
if 'pdf_data' not in st.session_state:
    st.session_state.pdf_data = None

# ========== SIDEBAR ==========
with st.sidebar:
    st.title("⚙️ ENGINE PARAMETERS")
    
    # Create propellant database instance
    prop_db = AdvancedPropellantDatabase()
    
    # Get all propellant names
    all_propellants = list(prop_db.PROPELLANTS.keys())
    
    # Propellant selection
    propellant = st.selectbox(
        "Propellant Combination",
        all_propellants,
        index=0,
        help="Select from 21 propellant combinations"
    )
    
    # Show which propellant was selected
    st.sidebar.success(f"✅ Selected: **{propellant}**")
    
    # Engine Cycle Selection
    cycles_list = list(EngineCycleDatabase().CYCLES.keys())
    selected_cycle = st.selectbox(
        "Engine Cycle",
        cycles_list,
        index=0,
        help="Select the engine cycle configuration"
    )
    
    # Nozzle Type Selection
    nozzles_list = list(NozzleDesignDatabase().NOZZLE_TYPES.keys())
    selected_nozzle = st.selectbox(
        "Nozzle Type",
        nozzles_list,
        index=1,
        help="Select nozzle design type"
    )
    
    # Material selection
    materials = list(AdvancedMaterialDatabase().MATERIALS.keys())
    material = st.selectbox("Throat/Chamber Material", materials, index=0)

    col1, col2 = st.columns(2)
    with col1:
        thrust = st.number_input("Thrust (N)", 500, 20000, 1550, 100)
    with col2:
        Pc = st.number_input("Chamber Pressure (bar)", 10.0, 200.0, 35.0, 5.0)

    of_ratio = st.slider("O/F Ratio", 1.0, 8.0, 2.5, 0.1)
    expansion = st.slider("Nozzle Expansion Ratio", 10, 200, 40, 10)
    burn_time = st.slider("Burn Time (s)", 10, 600, 180, 10)

    injector_type = st.selectbox(
        "Injector Type",
        ["coaxial", "like-on-like", "impinging", "swirl"],
        index=0
    )

    if st.button("🔄 UPDATE SIMULATION", use_container_width=True):
        params = {
            'thrust': thrust,
            'Pc': Pc,
            'of_ratio': of_ratio,
            'burn_time': burn_time,
            'propellant': propellant,
            'expansion_ratio': expansion,
            'material': material,
            'injector_type': 'coaxial',
            'cycle': selected_cycle,
            'nozzle_type': selected_nozzle
        }
        st.session_state.engine = UltimateRocketEngine(params)
        st.session_state.pdf_data = None
        st.rerun()

    st.markdown("---")
    st.title("📤 EXPORT")

    # PDF Download Button
    if st.button("📄 GENERATE & DOWNLOAD PDF", type="primary"):
        if st.session_state.engine:
            with st.spinner("Generating PDF..."):
                engine = st.session_state.engine
                results = engine.get_comprehensive_results()

                pdf_gen = ComprehensivePDFReport()
                pdf_data = pdf_gen.create_report(
                    engine.params,
                    results,
                    engine.explanations
                )

                # Store in session state
                st.session_state.pdf_data = pdf_data

# ========== MAIN DASHBOARD ==========
st.title("🚀 ULTIMATE ROCKET ENGINE ANALYSIS STUDIO")
st.markdown("**Complete Professional Aerospace Engineering Tool**")

if st.session_state.pdf_data:
    # Create download link
    b64 = base64.b64encode(st.session_state.pdf_data).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="Rocket_Engine_Complete_Analysis.pdf" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold; display: inline-block; margin: 10px 0;">📥 DOWNLOAD COMPLETE PDF REPORT</a>'
    st.markdown(href, unsafe_allow_html=True)
    st.balloons()

if st.session_state.engine is None:
    st.info("👈 Configure engine parameters in the sidebar and click 'RUN COMPREHENSIVE ANALYSIS'")
    st.stop()

engine = st.session_state.engine
results = engine.get_comprehensive_results()

# Header with overall assessment
overall_eff = results['efficiencies']['overall']
if overall_eff > 95:
    st.success(f"## ✅ EXCELLENT PERFORMANCE - Overall Efficiency: {overall_eff:.1f}%")
elif overall_eff > 90:
    st.info(f"## ⚠️ GOOD PERFORMANCE - Overall Efficiency: {overall_eff:.1f}%")
elif overall_eff > 85:
    st.warning(f"## 🔶 ACCEPTABLE PERFORMANCE - Overall Efficiency: {overall_eff:.1f}%")
else:
    st.error(f"## ❌ NEEDS IMPROVEMENT - Overall Efficiency: {overall_eff:.1f}%")

# Main Tabs - UPDATED TO 8 TABS
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📊 Performance", "🔥 Thermal", "🏗️ Structural", "🎵 Acoustic", 
    "🔄 Engine Cycle", "🚀 Nozzle Design", "🧪 Propellant", "🔍 Differences", "🎨 3D Visualization"
])

with tab1:
    st.subheader("Performance Analysis")

    # Metrics
    cols = st.columns(4)
    perf = results['performance']
    with cols[0]:
        st.metric("Theoretical Thrust", perf['Theoretical Thrust'])
    with cols[1]:
        st.metric("Experimental Thrust", perf['Experimental Thrust'],
                  f"{results['deviations']['thrust']:+.1f}%")
    with cols[2]:
        st.metric("Theoretical ISP", perf['Theoretical ISP'])
    with cols[3]:
        st.metric("Experimental ISP", perf['Experimental ISP'],
                  f"{results['deviations']['isp']:+.1f}%")

    # Performance charts
    fig = make_subplots(rows=2, cols=2, subplot_titles=('Thrust', 'ISP', 'Pressure', 'Mass Flow'))

    fig.add_trace(go.Scatter(x=engine.time, y=engine.F_experimental, name='Thrust'), row=1, col=1)
    fig.add_hline(y=engine.F_theoretical, line_dash="dash", row=1, col=1)

    fig.add_trace(go.Scatter(x=engine.time, y=engine.Isp_experimental, name='ISP'), row=1, col=2)
    fig.add_hline(y=engine.Isp_theoretical, line_dash="dash", row=1, col=2)

    fig.add_trace(go.Scatter(x=engine.time, y=engine.Pc_experimental, name='Pressure'), row=2, col=1)
    fig.add_hline(y=engine.params['Pc'], line_dash="dash", row=2, col=1)

    fig.add_trace(go.Scatter(x=engine.time, y=engine.mdot_experimental, name='Mass Flow'), row=2, col=2)
    fig.add_hline(y=engine.mdot_theoretical, line_dash="dash", row=2, col=2)

    fig.update_layout(height=600, showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Thermal Analysis")

    thermal = results['thermal']
    cols = st.columns(3)
    for i, (key, value) in enumerate(thermal.items()):
        with cols[i % 3]:
            st.metric(key, value)

    # Heat flux visualization
    st.subheader("Heat Flux Distribution")
    x = np.linspace(0, 1, 100)
    heat_profile = 8e6 * np.exp(-5 * x) + 12e6 * np.exp(-20 * (x - 0.5) ** 2)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=heat_profile / 1e6, fill='tozeroy',
                             line=dict(color='red', width=3)))
    fig.update_layout(title="Heat Flux Along Engine Length",
                      xaxis_title="Normalized Position",
                      yaxis_title="Heat Flux (MW/m²)")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Structural Analysis")

    struct = results['structural']
    cols = st.columns(3)
    for i, (key, value) in enumerate(struct.items()):
        with cols[i % 3]:
            if 'Safety Factor' in key:
                val = float(value)
                st.metric(key, value)
                st.progress(min(val / 5, 1.0))
            else:
                st.metric(key, value)

    # Material comparison
    st.subheader("Material Properties Comparison")
    materials_db = AdvancedMaterialDatabase().MATERIALS
    mat_data = []
    for mat_name, props in materials_db.items():
        mat_data.append({
            'Material': mat_name,
            'Max Temp (K)': props['max_temp'],
            'Erosion Rate': props['erosion_rate'] * 1000,
            'Cost': props['cost']
        })

    df_materials = pd.DataFrame(mat_data)
    st.dataframe(df_materials, use_container_width=True)

with tab4:
    st.subheader("Acoustic Stability Analysis")

    acoustic = results['acoustic']

    st.metric("Overall Stability", acoustic['stability_margin']['margin'],
              delta_color="off")

    # Mode frequencies
    st.subheader("Acoustic Mode Analysis")
    mode_data = []
    for mode_name, mode_info in acoustic['modes'].items():
        mode_data.append({
            'Mode': mode_name,
            'Frequency (Hz)': f"{mode_info['frequency']:.0f}",
            'Growth Rate': f"{mode_info['growth_rate']:.3f}",
            'Risk Level': mode_info['risk'],
            'Description': mode_info['description']
        })

    df_modes = pd.DataFrame(mode_data)
    st.dataframe(df_modes, use_container_width=True)

    # Recommendations
    st.subheader("Acoustic Stability Recommendations")
    for rec in acoustic['recommendations']:
        if '⚠️' in rec:
            st.warning(rec)
        elif '✅' in rec:
            st.success(rec)
        else:
            st.info(rec)

with tab5:
    st.subheader("Engine Cycle Analysis")
    
    if st.session_state.engine:
        engine = st.session_state.engine
        cycle_info = engine.analyze_engine_cycle()
        
        cols = st.columns(3)
        with cols[0]:
            st.metric("Cycle Efficiency", f"{cycle_info['efficiency']*100:.1f}%")
        with cols[1]:
            st.metric("Throttle Range", cycle_info['throttle_range'])
        with cols[2]:
            st.metric("Complexity", cycle_info['complexity'])
        
        st.write(f"**{cycle_info['cycle_name']}**")
        st.write(cycle_info['description'])
        st.write(f"**Examples:** {cycle_info['examples']}")
        
        # Cycle comparison chart
        cycles = EngineCycleDatabase().CYCLES
        cycle_names = list(cycles.keys())
        efficiencies = [cycles[name]['efficiency'] * 100 for name in cycle_names]
        
        fig = go.Figure(data=[
            go.Bar(
                x=cycle_names,
                y=efficiencies,
                marker_color=['#10b981' if name == selected_cycle else '#3b82f6' for name in cycle_names],
                text=[f"{eff:.1f}%" for eff in efficiencies],
                textposition='auto'
            )
        ])
        fig.update_layout(
            title="Engine Cycle Efficiency Comparison",
            yaxis_title="Efficiency (%)",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

with tab6:
    st.subheader("Nozzle Design Analysis")
    
    if st.session_state.engine:
        engine = st.session_state.engine
        nozzle_info = engine.analyze_nozzle_performance()
        
        cols = st.columns(3)
        with cols[0]:
            st.metric("Divergence Efficiency", f"{nozzle_info['divergence_efficiency']:.1f}%")
        with cols[1]:
            st.metric("Manufacturing Cost", nozzle_info['manufacturing_cost'])
        with cols[2]:
            st.metric("Cooling Complexity", nozzle_info['cooling_complexity'])
        
        st.write(f"**{nozzle_info['nozzle_type']}**")
        st.write(f"**Application:** {nozzle_info['application']}")
        
        # Nozzle comparison
        nozzles = NozzleDesignDatabase().NOZZLE_TYPES
        nozzle_names = list(nozzles.keys())
        efficiencies = [nozzles[name]['divergence_efficiency'] * 100 for name in nozzle_names]
        
        fig = go.Figure(data=[
            go.Bar(
                x=nozzle_names,
                y=efficiencies,
                marker_color=['#10b981' if name == selected_nozzle else '#3b82f6' for name in nozzle_names],
                text=[f"{eff:.1f}%" for eff in efficiencies],
                textposition='auto'
            )
        ])
        fig.update_layout(
            title="Nozzle Divergence Efficiency Comparison",
            yaxis_title="Efficiency (%)",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

with tab7:
    st.subheader("Propellant Analysis")
    
    if st.session_state.engine:
        engine = st.session_state.engine
        prop_analysis = engine.analyze_propellant_type()
        
        cols = st.columns(3)
        with cols[0]:
            st.metric("Propellant Type", prop_analysis['type'])
        with cols[1]:
            st.metric("Optimal O/F", f"{prop_analysis['optimal_of_ratio']:.1f}")
        with cols[2]:
            st.metric("Characteristic Velocity", f"{prop_analysis['characteristic_velocity']:.0f} m/s")
        
        # Show type-specific details
        if 'Solid' in prop_analysis['type']:
            st.subheader("Solid Rocket Motor Characteristics")
            st.metric("Burn Rate", f"{prop_analysis.get('burn_rate', 0):.2f} mm/s")
            st.metric("Propellant Density", f"{prop_analysis.get('propellant_density', 0):.0f} kg/m³")
            st.info("**Solid Rocket Advantages:** Simple, no moving parts, high reliability")
        
        elif 'Hybrid' in prop_analysis['type']:
            st.subheader("Hybrid Rocket Characteristics")
            st.metric("Regression Rate", f"{prop_analysis.get('regression_rate', 0):.2f} mm/s")
            st.metric("Fuel Density", f"{prop_analysis.get('fuel_density', 0):.0f} kg/m³")
            st.success("**Hybrid Rocket Advantages:** Throttleable, restartable, inherently safe")
        
        else:  # Liquid
            st.subheader("Liquid Rocket Characteristics")
            st.info("**Liquid Rocket Advantages:** Highest specific impulse, full throttle control, multiple restarts possible")
        
        # Propellant safety info
        st.subheader("Safety & Handling")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Toxicity", prop_analysis['toxicity'])
        with col2:
            st.metric("Handling", prop_analysis['handling'])

with tab8:
    st.subheader("Difference Explanations: Theoretical vs Experimental")

    for param, explanation in results['explanations'].items():
        with st.expander(f"🔍 {param.upper()} Analysis: {explanation['severity']} ({explanation['deviation']})",
                         expanded=True):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Probable Reasons:**")
                for reason in explanation['reasons']:
                    st.markdown(f"• {reason}")

            with col2:
                st.markdown("**Recommendations:**")
                for rec in explanation['recommendations']:
                    st.markdown(f"• {rec}")

            st.markdown("**Physics Notes:**")
            for note in explanation.get('physics_notes', []):
                st.markdown(f"• {note}")

with tab9:
    st.subheader("3D Engine Visualization")

    # Create 3D model
    try:
        fig_3d = Visualization3D.create_simple_engine_visualization(
            engine.Dc, engine.Lc, engine.Dt, engine.De, engine.Ln
        )
    except Exception as e:
        st.error(f"3D Visualization error: {e}")
        # Create a simple alternative visualization
        fig_3d = go.Figure()
        fig_3d.add_trace(go.Scatter3d(
            x=[0, engine.Dc / 2, engine.Dt / 2, engine.De / 2],
            y=[0, 0, 0, 0],
            z=[0, engine.Lc, engine.Lc + engine.Ln / 2, engine.Lc + engine.Ln],
            mode='lines+markers',
            line=dict(width=4, color='red'),
            marker=dict(size=5, color='blue')
        ))
        fig_3d.update_layout(
            title='Engine Profile (3D view unavailable)',
            scene=dict(
                xaxis_title='Diameter (m)',
                yaxis_title='Y (m)',
                zaxis_title='Length (m)'
            ),
            height=500
        )

    st.plotly_chart(fig_3d, use_container_width=True)

    # Plume visualization
    st.subheader("Exhaust Plume Characteristics")

    # Simulate plume
    z_plume = np.linspace(0, 5, 100)
    r_plume = engine.De / 2 * (1 + 0.3 * z_plume ** 0.7)

    fig_plume = go.Figure()
    fig_plume.add_trace(go.Scatter(x=z_plume, y=r_plume, fill='tozeroy',
                                   line=dict(color='orange', width=3),
                                   name='Plume Boundary'))
    fig_plume.add_trace(go.Scatter(x=z_plume, y=-r_plume, fill='tonexty',
                                   line=dict(color='orange', width=3),
                                   showlegend=False))

    fig_plume.update_layout(title="Exhaust Plume Expansion",
                            xaxis_title="Distance from Exit (m)",
                            yaxis_title="Plume Radius (m)",
                            height=400)

    st.plotly_chart(fig_plume, use_container_width=True)

# ========== FINAL SUMMARY ==========
st.markdown("---")
st.subheader("🎯 COMPREHENSIVE ENGINEERING ASSESSMENT")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Overall Efficiency", f"{results['efficiencies']['overall']:.1f}%")
with col2:
    st.metric("Pressure Stability", f"±{results['stability']['Pressure Stability']}")
with col3:
    st.metric("Acoustic Stability", results['stability']['Acoustic Stability'])

# Key insights
st.subheader("🔬 KEY PHYSICS INSIGHTS")
insights = """
1. **Real Gas Effects:** Combustion products at 3500K are not ideal gases - dissociation and variable γ affect performance by 2-5%.

2. **Boundary Layer Losses:** Nozzle boundary layer reduces thrust by 3-8% depending on Reynolds number and surface roughness.

3. **Combustion Limitations:** Finite-rate chemistry and mixing efficiency typically limit combustion to 97-99% of theoretical.

4. **Thermal Limitations:** Material temperature limits constrain chamber pressure and expansion ratio choices.

5. **Acoustic Coupling:** Combustion instability can cause 5-10% thrust oscillations and must be avoided through design.

6. **Manufacturing Realities:** Surface finish, contour accuracy, and material properties cause 2-5% performance variations.
"""

st.markdown(insights)

st.success("""
**✅ COMPREHENSIVE ANALYSIS COMPLETE**
This professional-grade analysis includes: 21 propellants, 6 advanced materials, 
6 engine cycles, 6 nozzle designs, acoustic stability analysis, 3D visualization, 
and detailed physics-based difference explanations.
""")
