def model(bits):
    sequence = "1011"
    # Initialize count and start to 0
    count = 0
    start = 0
    bit_positions = []
    # Search through the string till
    # we reach the end of it
    while start < len(bits):

        # Check if a substring is present from
        # 'start' position till the end
        pos = bits.find(sequence, start)

        if pos != -1:
            # If a substring is present, move 'start' to
            # the next position from start of the substring
            start = pos + 1
            if((pos + 4) < len(bits)):
                bit_positions.append((pos + 4))
            # Increment the count
            count += 1
        else:
            # If no further substring is present
            break
    # return the value of count
    return count, bit_positions