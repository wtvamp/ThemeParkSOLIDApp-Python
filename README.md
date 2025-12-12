# ThemeParkSOLIDApp-Python

A Python training repository demonstrating SOLID principles through a theme park management system. Each branch builds upon the previous one, progressively refactoring the code to follow SOLID design principles.

## Overview

This repo starts with a monolithic `ThemePark` class that violates multiple SOLID principles, then refactors it step-by-step across five branches—one for each SOLID principle.

## Branches

### `main` - Baseline (Anti-Pattern)

The starting point with a single `ThemePark` class that:
- Has 20+ properties for rides and restaurants (hardcoded to exactly 3 of each)
- Handles all responsibilities: data storage, calculations, and printing
- Cannot be extended without modification
- Violates all SOLID principles

**Files:**
- `theme_park.py` - Monolithic class (~77 lines)
- `main.py` - Usage example

---

### `feature/step1-single-responsibility-principle` - SRP

**Principle:** A class should have only one reason to change.

**Changes:**
- Extract `ThemeParkRide` class with its own `name`, `speed`, and `ride_details()` method
- Extract `Restaurant` class with its own `name`, `income`, `loss`, and `restaurant_details()` method
- `ThemePark` now holds `List[ThemeParkRide]` and `List[Restaurant]`

**Key Teaching Point:** Each class now has one responsibility—rides handle ride data, restaurants handle restaurant data, and the park handles park operations.

**New Files:**
- `rides/theme_park_ride.py`
- `restaurants/restaurant.py`

---

### `feature/step2-open-closed-principle` - OCP

**Principle:** Software entities should be open for extension but closed for modification.

**Changes:**
- Make `ThemeParkRide` and `Restaurant` abstract base classes using Python's `ABC`
- Add abstract `extra_details()` method for type-specific information
- Create specialized ride types:
  - `DarkRide` - with scariness rating
  - `SpinningRide` - with spinning degree and speed
- Create specialized restaurant types:
  - `SpaceRestaurant` - themed as miles from Earth
  - `UnderseaRestaurant` - themed as miles under the sea

**Key Teaching Point:** New ride or restaurant types can be added without modifying existing base classes.

**New Files:**
- `rides/dark_ride.py`
- `rides/spinning_ride.py`
- `restaurants/space_restaurant.py`
- `restaurants/undersea_restaurant.py`

---

### `feature/step3-liskov-substitution-principle` - LSP

**Principle:** Objects of a superclass should be replaceable with objects of its subclasses without breaking the application.

**Changes:**
- Add `BrokenRide` subclass that inherits from `ThemeParkRide`
- `BrokenRide` passes `speed=0` to base constructor
- Provides meaningful `extra_details()` override

**Key Teaching Point:** A `BrokenRide` can substitute anywhere a `ThemeParkRide` is expected without breaking the program. The comment in the code shows what NOT to do—setting `total_speed = None` would violate LSP by breaking the base class contract.

**New Files:**
- `rides/broken_ride.py`

---

### `feature/step4-interface-segregation-principle` - ISP

**Principle:** Clients should not be forced to depend on interfaces they do not use.

**Changes:**
- Create separate interfaces in `interfaces.py`:
  - `IThemeParkRide` - just `ride_details()`
  - `IExtraDetails` - just `extra_details()`
  - `ISpinningEngine` - `start()` and `stop()` methods
- `SpinningRide` implements `IExtraDetails` + `ISpinningEngine`
- `DarkRide` and `BrokenRide` implement only `IExtraDetails`
- `ThemePark` uses `isinstance()` checks to call interface-specific methods

**Key Teaching Point:** Classes only implement interfaces they need. A `BrokenRide` doesn't need `start()`/`stop()` methods it can't use.

**New Files:**
- `rides/interfaces.py`

---

### `feature/step5-dependency-inversion-principle` - DIP

**Principle:** High-level modules should not depend on low-level modules. Both should depend on abstractions.

**Changes:**
- `ThemePark` constructor now takes `List[IThemeParkRide]` as dependency injection
- Create `SpinningEngine` and `SpinningEngineSuperFast` implementations of `ISpinningEngine`
- `SpinningRide` receives `ISpinningEngine` via constructor injection
- Rides are created externally and injected into `ThemePark`

**Key Teaching Point:** High-level modules (`ThemePark`) depend on abstractions (`IThemeParkRide`), not concrete types. Different engine implementations can be swapped at runtime.

**New Files:**
- `rides/spinning_engine.py`
- `rides/spinning_engine_super_fast.py`

---

## Final Structure (Step 5)

```
ThemeParkSOLIDApp-Python/
├── README.md
├── main.py
├── theme_park.py
├── rides/
│   ├── __init__.py
│   ├── interfaces.py          # IThemeParkRide, IExtraDetails, ISpinningEngine
│   ├── theme_park_ride.py     # Base class
│   ├── dark_ride.py           # Implements IExtraDetails
│   ├── spinning_ride.py       # Implements IExtraDetails, uses ISpinningEngine
│   ├── broken_ride.py         # Implements IExtraDetails
│   ├── spinning_engine.py     # Implements ISpinningEngine
│   └── spinning_engine_super_fast.py  # Implements ISpinningEngine
└── restaurants/
    ├── __init__.py
    ├── restaurant.py          # Abstract base class
    ├── space_restaurant.py    # Concrete implementation
    └── undersea_restaurant.py # Concrete implementation
```

## Usage

```bash
# Clone the repo
git clone <repo-url>
cd ThemeParkSOLIDApp-Python

# Run the baseline
git checkout main
python main.py

# Explore each SOLID principle
git checkout feature/step1-single-responsibility-principle
python main.py

git checkout feature/step2-open-closed-principle
python main.py

# ... and so on for each step
```

## SOLID Principles Summary

| Letter | Principle | Description |
|--------|-----------|-------------|
| **S** | Single Responsibility | A class should have only one reason to change |
| **O** | Open/Closed | Open for extension, closed for modification |
| **L** | Liskov Substitution | Subtypes must be substitutable for their base types |
| **I** | Interface Segregation | Many specific interfaces are better than one general interface |
| **D** | Dependency Inversion | Depend on abstractions, not concretions |

## Requirements

- Python 3.7+

## Related

This is a Python port of the C# training repository [ThemeParkSOLIDApp](../ThemeParkSOLIDApp).
