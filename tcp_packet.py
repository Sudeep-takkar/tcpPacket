source_Packet = hex(int('6327'))
dest_Packet = format(8056, 'x')

seq_Numbr = '00000000'
ack_Numbr = '00000000'

data_Offset = '51020010'

print(source_Packet + dest_Packet + seq_Numbr + ack_Numbr + data_Offset)