python early:
    characters = {}  # Global dictionary to store character objects

    def parse_character(abrev, lexer):
        """
        Parse the character abbreviation and dialogue text from the script.
        """
        dialogue = lexer.rest()  # Parse the rest as dialogue
        return abrev, dialogue  # Return both abbreviation and dialogue

    def execute_character(parsed_object):
        """
        Execute the parsed character statement.
        """
        abrev, dialogue = parsed_object

        # Resolve the character from the dictionary
        char_obj = characters.get(abrev, None)
        
        if not char_obj:
            raise Exception(f"Character '{abrev}' is not defined.")

        # Use the character's .c property to say the dialogue
        return renpy.exports.say(char_obj.c, dialogue)

    # Register a custom statement for a specific character (example: 'jes')
    renpy.register_statement(
        name="jes",
        parse=lambda lexer: parse_character("jes", lexer),  # Corrected parse function
        execute=execute_character,
        block=False,  # No block associated with this statement
    )
    renpy.register_statement(
        name="sof",
        parse=lambda lexer: parse_character("sof", lexer),  # Corrected parse function
        execute=execute_character,
        block=False,  # No block associated with this statement
    )
