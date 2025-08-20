# Complete Superhero Academy: Python Parameters Training! 🦸‍♀️

## 1. Basic Powers (Simple Parameters) 🎯
def superhero_greeting(hero_name):
    print(f"I am {hero_name}, here to save the day!")

superhero_greeting("Captain Python")  # Basic way

## 2. Power Combinations (Multiple Parameters) ⚡
def hero_power_move(hero_name, power):
    print(f"{hero_name} uses {power}!")

# Regular way
hero_power_move("Data Woman", "code blast")

# Keyword Arguments way (more readable!)
hero_power_move(hero_name="Data Woman", power="code blast")
hero_power_move(power="code blast", hero_name="Data Woman")  # Order doesn't matter!

## 3. Hero Equipment (Default Parameters) 🦹
def equip_hero(name, weapon="laptop", costume="cape", mask=True):
    print(f"{name} is equipped with a {weapon}, wearing a {costume}")
    if mask:
        print("And has a cool mask! 😎")

# Different ways to call the same function:
equip_hero("PyGirl")  # Using defaults
equip_hero("CodeMan", "mechanical keyboard")  # Positional argument
equip_hero(
    name="Bug Zapper",
    costume="debug suit",
    weapon="bug spray",
    mask=False
)  # Keyword arguments
equip_hero("Binary Boss", mask=False, weapon="quantum computer")  # Mixed


## 4. Team Assembly (*args - Variable Positional Arguments) 💥
def form_hero_team(team_name, *members):
    print(f"\nTeam {team_name} consists of:")
    for member in members:
        print(f"- {member}")

# Add any number of team members
form_hero_team("Code Warriors", "PyGirl", "JavaMan", "RustRanger")
form_hero_team("Bug Busters", "Debug Duck")  # Works with just one too!

## 5. Hero Stats (**kwargs - Variable Keyword Arguments) 🎭
def create_hero_profile(**stats):
    print("\nHero Profile:")
    for stat, value in stats.items():
        print(f"{stat}: {value}")

# Add any stats you want
create_hero_profile(
    name="The Programmer",
    speed=80,
    coding_power=9000,
    coffee_needed=True
)

## 6. The Ultimate Hero Creator (Combining Everything!) 🏆
# def ultimate_hero_creator(
#     name,                   # Required parameter
#     main_power,            # Required parameter
#     backup_power="none",   # Default parameter
#     *special_moves,        # Variable positional arguments
#     **characteristics      # Variable keyword arguments
# ):
#     print(f"\n🦸 Creating Superhero: {name}")
#     print(f"Main Power: {main_power}")
#     print(f"Backup Power: {backup_power}")
    
#     if special_moves:
#         print("\nSpecial Moves:")
#         for move in special_moves:
#             print(f"- {move}")
    
#     if characteristics:
#         print("\nCharacteristics:")
#         for trait, value in characteristics.items():
#             print(f"{trait}: {value}")

# # Let's create an awesome hero!
# ultimate_hero_creator(
#     "Professor Python",        # Required positional
#     main_power="Code Magic",  # Keyword argument
#     backup_power="Coffee Boost",  # Keyword argument for default parameter
#     "Syntax Strike",          # *args
#     "Exception Handling",     # *args
#     "Bug Blast",             # *args
#     base="Silicon Valley",    # **kwargs
#     weakness="semicolons",    # **kwargs
#     coding_level="expert"     # **kwargs
# )

# ## Quick Reference Guide 📝
# 1. **Regular Parameters**: Basic required inputs
#    ```python
#    def hero(name, power)
#    ```

# 2. **Keyword Arguments**: Name-value pairs when calling
#    ```python
#    hero(name="PyGirl", power="coding")
#    ```

# 3. **Default Parameters**: Optional with fallback values
#    ```python
#    def hero(name, power="coding")
#    ```

# 4. **Args**: Variable number of positional arguments
#    ```python
#    def hero(*powers)  # powers becomes a tuple
#    ```

# 5. **Kwargs**: Variable number of keyword arguments
#    ```python
#    def hero(**traits)  # traits becomes a dictionary
#    ```
