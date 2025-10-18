# Planet objects with their name, distance from Lumoria, and size
lumoria_planets = [
    { "name": "Mercuria", "distance": 0.4, "size": 4879 },
    { "name": "Earthia", "distance": 1, "size": 12742 },
    { "name": "Venusia", "distance": 0.7, "size": 12104 },
    { "name": "Marsia", "distance": 1.5, "size": 6779 }
]

def get_shadow_count(planets, current_index):
    """
    Calculate how many planets cast a shadow on the current planet.
    
    This is a simplified model that assumes a planet casts a shadow if:
    1. It's closer to Lumoria (earlier in the sorted array)
    2. It's larger than the current planet
    
    Args:
        planets: List of planets sorted by distance from Lumoria
        current_index: Index of the planet we're checking
        
    Returns:
        Number of planets casting shadows on the current planet
    """
    return len([
        planet for planet in planets[:current_index] 
        if planet["size"] > planets[current_index]["size"]
    ])

def get_light_intensity(i, shadow_count):
    """
    Determine the light intensity based on position and shadow count.
    
    Args:
        i: Index of the planet in the sorted array
        shadow_count: Number of planets casting shadows
        
    Returns:
        String describing the light intensity
    """
    if i == 0:
        return 'Full'  # First planet always gets full light
    if shadow_count == 0:
        return 'Full'  # No shadows
    if shadow_count == 1:
        return 'Partial'  # One shadow usually means partial light
    return 'None (Multiple Shadows)'  # Multiple shadows block light completely

def calculate_light_intensity(planets):
    """
    Calculate the light intensity for each planet in the system.
    
    Args:
        planets: List of planets sorted by distance
        
    Returns:
        List of dictionaries with planet name and light intensity
    """
    return [
        {
            "name": planet["name"], 
            "light": get_light_intensity(i, get_shadow_count(planets, i))
        } 
        for i, planet in enumerate(planets)
    ]

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
    
    # Calculate light intensity
    results = calculate_light_intensity(sorted_planets)
    
    # Display the results
    display_results(results)
    
    return results

if __name__ == "__main__":
    main()