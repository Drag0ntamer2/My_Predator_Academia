init -9998 python:
    def difficultyDamage(difficulty):
        """Determines the base damage multiplier based on difficulty."""
        damage_values = {1: 4, 2: 3, 3: 2}  # Easy, Medium, Hard
        return damage_values.get(difficulty, 2)  # Default to Medium if difficulty is invalid

    def disOverflow(overflow, compression, constitution):
        return (overflow + compression) / constitution


    def applyDis(dis, damage):
        """
        Adjusts the damage effectiveness based on the disorientation level.
        Parameters:
            dis: The current disorientation level (0-5).
            damage: The original damage value.
        Returns:
            Adjusted damage after applying disorientation effects.
        """
        if dis <= 0:
            return damage  # No disorientation, no adjustment

        roll = renpy.random.randint(1, 20)

        # Special cases for extreme disorientation or critical rolls
        if dis > 3:
            if roll == 1:
                return 0  # Complete failure due to high disorientation
            elif roll == 20:
                return damage  # Full effectiveness on a critical success

        # Calculate damage reduction based on disorientation
        reduction_factor = dis / 5  # Scale disorientation to a 0-1 factor
        roll_modifier = (20 - roll) / 20  # Higher rolls mean less reduction
        adjustment = reduction_factor * roll_modifier  # Combine factors

        # Adjust damage based on calculated reduction
        adjusted_damage = damage * (1 - adjustment)
        return max(0, adjusted_damage)  # Ensure damage is not negative