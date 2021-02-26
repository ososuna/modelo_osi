# Convert a string to hexadecimal
def string_to_hex(cadena):
  # Create bytearray
  cadena_byte_array = bytearray(cadena, "utf8")
  byte_list = []

  for byte in cadena_byte_array:
      # Convert to binary
      binary_representation = hex(byte)
      # Add to list
      byte_list.append(binary_representation)
  
  return byte_list