source_Packet = hex(int('0864'))
dest_Packet = format(8070, 'x')

seq_Numbr = '00000000'
ack_Numbr = '00000000'

data_Offset = '51020010'

print(source_Packet + dest_Packet + seq_Numbr + ack_Numbr + data_Offset)