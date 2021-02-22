# Convert a string to binary
def string_to_bin(cadena):
  # Create bytearray
  cadena_byte_array = bytearray(cadena, "utf8")
  byte_list = []

  for byte in cadena_byte_array:
      # Convert to binary
      binary_representation = bin(byte)
      # Add to list
      byte_list.append(binary_representation)
  
  return byte_list