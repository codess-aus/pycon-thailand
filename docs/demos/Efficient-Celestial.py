# Planet objects with their name, distance from Lumoria, and size
lumoria_planets = [
    { "name": "Mercuria", "distance": 0.4, "size": 4879 },
    { "name": "Earthia", "distance": 1, "size": 12742 },
    { "name": "Venusia", "distance": 0.7, "size": 12104 },
    { "name": "Marsia", "distance": 1.5, "size": 6779 }
]

def get_shadow_count(planets, current_index):
    """Calculate how many planets cast a shadow on the current planet."""
    # Early optimization: First planet always has 0 shadows
    if current_index == 0:
        return 0
        
    # Efficient implementation using generator expression instead of list comprehension
    return sum(1 for i in range(current_index) if planets[i]["size"] > planets[current_index]["size"])

def get_light_intensity(i, shadow_count):
    """Determine light intensity based on position and shadow count."""
    if i == 0: 
        return 'Full'  # First planet always gets full light
    if shadow_count == 0: 
        return 'Full'  # Corrected: No shadows means full light
    if shadow_count == 1: 
        return 'None'  # One shadow blocks light
    if shadow_count > 1: 
        return 'None (Multiple Shadows)'  # Multiple shadows
    return 'Partial'  # This is now unreachable but kept for completeness

def calculate_light_intensity(planets):
    """Calculate light intensity for all planets."""
    result = []
    for i, planet in enumerate(planets):
        shadow_count = get_shadow_count(planets, i)
        light = get_light_intensity(i, shadow_count)
        result.append({"name": planet["name"], "light": light})
    return result

def display_results(intensity_data):
    """Format and display the results in a readable way."""
    print("Lumoria Planetary System - Light Analysis")
    print("-" * 45)
    for planet in intensity_data:
        print(f"{planet['name']}: {planet['light']} light")
    print("-" * 45)

def main():
    """Run the Lumoria planetary system simulation."""
    # Sort the array of planets by distance
    sorted_planets = sorted(lumoria_planets, key=lambda planet: planet["distance"])
    
    # Calculate and display light intensity
    results = calculate_light_intensity(sorted_planets)
    display_results(results)
    
    return results

if __name__ == "__main__":
    main()